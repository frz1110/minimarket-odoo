from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Penjualan(models.Model):
    _name="farzanamart.penjualan"
    _description= "penjualan"

    name = fields.Char(string='No. Nota')
    nama_pembeli = fields.Char(string='Nama Pembeli')
    tgl_penjualan = fields.Datetime(
        string='Tanggal Transaksi',
        default=fields.Datetime.now())
    total_bayar = fields.Integer(
        string='Total Pembayaran',
        compute='_compute_totalbayar')
    detailpenjualan_ids = fields.One2many(
        comodel_name='farzanamart.detailpenjualan',
        inverse_name='penjualan_id',
        string='Detail Penjualan')

    state = fields.Selection(
        string='Status',
        selection=[('draft', 'Draft'),
                   ('confirm', 'Confirm'),
                   ('done', 'Done'),
                   ('cancelled', 'Cancelled'),
                   ],
        required=True, readonly=True, default='draft')

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        self.write({'state': 'draft'})

    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for line in self:
            result = sum(self.env['farzanamart.detailpenjualan'].search(
                [('penjualan_id', '=', line.id)]).mapped('subtotal'))
            line.total_bayar = result

    def unlink(self):
        if self.filtered(lambda line: line.state != 'draft'):
            raise ValidationError("Tdak dapat menghapus jika status BUKAN DRAFT")
        else:
            if self.detailpenjualan_ids:
                penjualan = []
                for line in self:
                    penjualan = self.env['farzanamart.detailpenjualan'].search(
                        [('penjualan_id', '=', line.id)])
                    print(penjualan)

                for ob in penjualan:
                    print(ob.barang_id.name + ' ' + str(ob.qty))
                    ob.barang_id.stok += ob.qty
            return super(Penjualan, self).unlink()

    _sql_constraints = [
        ('no_nota_unik', 'unique (name)', 'Nomor Nota tidak boleh sama !!!')
    ]
    

class DetailPenjualan(models.Model):
    _name="farzanamart.detailpenjualan"
    _description= "Detail penjualan"

    name = fields.Char(string='Nama')
    penjualan_id = fields.Many2one(
        comodel_name='farzanamart.penjualan',
        string='Detail Penjualan')
    barang_id = fields.Many2one(
        comodel_name='farzanamart.barang',
        string='List Barang')
    harga_satuan = fields.Integer(
        string='Harga Satuan')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')

    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.qty*record.harga_satuan

    @api.onchange('barang_id')
    def _onchange_barang_id(self):
        self.harga_satuan = self.barang_id.harga_jual


    @api.model
    def create(self, vals):
        record = super(DetailPenjualan, self).create(vals)
        if record.qty:
            self.env['farzanamart.barang'].search([('id','=',record.barang_id.id)]).write({'stok':record.barang_id.stok-record.qty})
        return record

    def write(self, vals):
        qty_sebelum = self.qty
        super(DetailPenjualan, self).write(vals)
        self.env['farzanamart.barang'].search([('id','=',self.barang_id.id)]).write({'stok':self.barang_id.stok+(qty_sebelum-self.qty)})

    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty<1:
                raise ValidationError(f'Mau beli {rec.barang_id.name} berapa?')
            elif rec.barang_id.stok < rec.qty:
                raise ValidationError(f'Stok {rec.barang_id.name} tidak cukup')

  