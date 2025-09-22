{
    "name": "NST Express Custom Reports",
    "version": "1.0",
    "author": "Natalia Stekolnikova",
    "category": "Sales",
    "summary": "Custom and extended reports for Sale Orders with Express Delivery",
    "depends": ["sale", "stock", "sale_management", "nst_delivery_express"],
    "data": [
        "views/sale_order_views.xml",
        "views/ir_actions_demo.xml",
        "reports/invoice_report.xml",
        "reports/sale_report_payment.xml",
        "reports/sale_express_report.xml",
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
