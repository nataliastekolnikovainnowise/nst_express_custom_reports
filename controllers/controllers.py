# -*- coding: utf-8 -*-
# from odoo import http


# class NstDeliveryExpress(http.Controller):
#     @http.route('/nst_delivery_express/nst_delivery_express', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nst_delivery_express/nst_delivery_express/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nst_delivery_express.listing', {
#             'root': '/nst_delivery_express/nst_delivery_express',
#             'objects': http.request.env['nst_delivery_express.nst_delivery_express'].search([]),
#         })

#     @http.route('/nst_delivery_express/nst_delivery_express/objects/<model("nst_delivery_express.nst_delivery_express"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nst_delivery_express.object', {
#             'object': obj
#         })

