from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    # Старое поле экспресс-доставки
    is_express = fields.Boolean(string="Express Delivery (old)", default=False)

    # Новое поле для печатной формы
    express_delivery = fields.Boolean(string="Express Delivery", default=False)

    # Оставляем только новое поле Express Picking (вычисляемое имя)
    express_picking_name = fields.Char(
        string="Express Picking (name)",
        compute="_compute_express_picking_name",
        store=False,
        help="Name of the express picking if created"
    )

    # Новое поле — ссылка на picking (для отчёта)
    express_picking_id = fields.Many2one(
        "stock.picking",
        string="Express Picking",
        help="Linked express picking if created"
    )
    
    @api.depends('is_express', 'order_id.picking_ids', 'order_id.picking_ids.name')
    def _compute_express_picking_name(self):
        """Вычисляет имя экспресс picking'а для строки заказа"""
        for line in self:
            if not line.is_express:
                line.express_picking_name = ""
                continue
            
            # Ищем express picking для данного заказа
            express_pickings = line.order_id.picking_ids.filtered(
                lambda p: "(Express)" in (p.origin or "") and p.state not in ['cancel']
            )
            if express_pickings:
                line.express_picking_name = express_pickings[0].name
            else:
                line.express_picking_name = ""


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # Поле для фильтрации заказов с экспресс-линиями
    has_express_lines = fields.Boolean(
        string="Has Express Lines",
        compute="_compute_has_express_lines",
        store=False
    )

    def _compute_has_express_lines(self):
        for order in self:
            order.has_express_lines = any(line.express_delivery for line in order.order_line)
