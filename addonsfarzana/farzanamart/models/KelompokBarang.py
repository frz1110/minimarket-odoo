from odoo import api, fields, models


class KelompokBarang(models.Model):
    _name = 'farzanamart.kelompokbarang'
    _description = 'New Description'

    name = fields.Selection([
        ('makanan basah', 'Makanan Basah'),
        ('makanan kering', 'Makanan Kering'),
        ('minuman', 'Minuman')
        ], string="Nama Kelompok"
    )

    kode_kelompok = fields.Char(string='Kode Kelompok Barang')
    kode_rak = fields.Char(string='Kode Rak')
    barang_id = fields.One2many(comodel_name='farzanamart.barang', inverse_name="kelompokbarang_id", string="Barang")
    jml_item = fields.Char(compute='_compute_jml_item', string='Jml Item')
    daftar = fields.Char(string='Daftar Barang')

    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if self.name == 'makanan basah':
            self.kode_kelompok = 'MAK01'
        elif self.name == 'makanan kering':
            self.kode_kelompok = 'MAK02'
        elif self.name == 'minuman':
            self.kode_kelompok = 'MIN01'

    @api.depends('barang_id')
    def _compute_jml_item(self):
        for record in self:
            daftar_barang = self.env['farzanamart.barang'].search([('kelompokbarang_id', '=', record.id)]).mapped('name')
            record.jml_item = len(daftar_barang)
            record.daftar = daftar_barang
    
    

