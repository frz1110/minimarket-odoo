from odoo import models, fields, api


class BarangDatang(models.TransientModel):
     _name = 'farzanamart.barangdatang'

     barang_id = fields.Many2one(comodel_name='farzanamart.barang', string='Nama Barang')
     jumlah = fields.Integer(string='Jumlah')

     def button_barang_datang(self):
        pass