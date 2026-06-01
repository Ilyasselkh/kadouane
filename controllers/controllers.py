# -*- coding: utf-8 -*-
# from odoo import http


# class Kadouane(http.Controller):
#     @http.route('/kadouane/kadouane', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kadouane/kadouane/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kadouane.listing', {
#             'root': '/kadouane/kadouane',
#             'objects': http.request.env['kadouane.kadouane'].search([]),
#         })

#     @http.route('/kadouane/kadouane/objects/<model("kadouane.kadouane"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kadouane.object', {
#             'object': obj
#         })
