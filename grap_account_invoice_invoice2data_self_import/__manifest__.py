# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Account Invoice - Self Import Invoice2data Invoices (GRAP)",
    "version": "12.0.1.2.0",
    "category": "Accounting",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business-supplier-invoice",
    "license": "AGPL-3",
    "depends": [
        # OCA
        "account_invoice_default_code_column",
        "account_invoice_uom_column",
        # GRAP
        "grap_account_invoice_invoice2data_templates",
    ],
    "data": ["report/qweb_template_account_invoice.xml"],
    "demo": [
        "demo/res_users.xml",
        "demo/res_partner.xml",
        "demo/account_invoice.xml",
        "demo/product_product.xml",
    ],
    "installable": True,
}
