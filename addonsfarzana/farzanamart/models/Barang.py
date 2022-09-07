# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Barang(models.Model):
     _name = 'farzanamart.barang'
     _description = 'New Description'

     name = fields.Char(string='Nama Barang')
     harga_beli = fields.Integer(string='Harga Modal', required=True)
     harga_jual = fields.Integer(string='Harga Jual', required=True)
     stok = fields.Integer(string='Stok')
     kelompokbarang_id = fields.Many2one(comodel_name='farzanamart.kelompokbarang', string='Kelompok Barang', ondelete='cascade')
     supplier_id = fields.Many2many(comodel_name='farzanamart.supplier', string='Supplier')
     
     