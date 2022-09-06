from odoo import api, fields, models

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

    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for line in self:
            result = sum(self.env['farzanamart.detailpenjualan'].search(
                [('penjualan_id', '=', line.id)]).mapped('subtotal'))
            line.total_bayar = result


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