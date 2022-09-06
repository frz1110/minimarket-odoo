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
