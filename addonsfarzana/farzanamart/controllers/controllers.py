# -*- coding: utf-8 -*-
# from odoo import http


# class Farzanamart(http.Controller):
#     @http.route('/farzanamart/farzanamart', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/farzanamart/farzanamart/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('farzanamart.listing', {
#             'root': '/farzanamart/farzanamart',
#             'objects': http.request.env['farzanamart.farzanamart'].search([]),
#         })

#     @http.route('/farzanamart/farzanamart/objects/<model("farzanamart.farzanamart"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('farzanamart.object', {
#             'object': obj
#         })

from odoo import http, models
from odoo.http import request
import json

class Farzanamart(http.Controller):
     @http.route('/farzanamart/get_barang', auth='public', method=['GET'])
     def get_barang(self, **kw):
         barang_data = request.env['farzanamart.barang'].search([])
         isi = []
         for barang in barang_data:
            isi.append({
                "Nama": barang.name,
                "harga_jual":barang.harga_jual,
                "stok":barang.stok,
            })
         return json.dumps(isi)
