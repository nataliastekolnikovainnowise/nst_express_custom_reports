{
    "name": "NST Express Custom Reports",
    "version": "1.0",
    "author": "Natalia Stekolnikova",
    "website": "https://github.com/nataliastekolnikovainnowise/nst-sale-express-delivery",
    "category": "Sales",
    "summary": "Custom and extended reports for Sale Orders with Express Delivery",
    "depends": ["sale", "stock", "sale_management"],
    "data": [
        "views/sale_order_views.xml",
        "views/ir_actions_demo.xml",
        "reports/sale_express_report.xml",  # <- НОВЫЙ ФАЙЛ
        # УДАЛИТЕ эти две строки:
        # "reports/sale_report_data.xml",
        # "reports/sale_report_templates.xml",
        "reports/sale_report_payment.xml",
        "reports/invoice_report.xml",
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
