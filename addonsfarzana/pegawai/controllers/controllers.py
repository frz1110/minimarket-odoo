# -*- coding: utf-8 -*-
# from odoo import http


# class Pegawai(http.Controller):
#     @http.route('/pegawai/pegawai', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pegawai/pegawai/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pegawai.listing', {
#             'root': '/pegawai/pegawai',
#             'objects': http.request.env['pegawai.pegawai'].search([]),
#         })

#     @http.route('/pegawai/pegawai/objects/<model("pegawai.pegawai"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pegawai.object', {
#             'object': obj
#         })
