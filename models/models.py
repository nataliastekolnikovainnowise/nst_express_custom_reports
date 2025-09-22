# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class nst_delivery_express(models.Model):
#     _name = 'nst_delivery_express.nst_delivery_express'
#     _description = 'nst_delivery_express.nst_delivery_express'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

