# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Account Invoice - Test for Invoice2data Import (GRAP)",
    "version": "12.0.1.0.3",
    "category": "Accounting",
    "author": "GRAP",
    "website": "https://github.com/grap/grap-odoo-business-supplier-invoice",
    "license": "AGPL-3",
    "depends": ["account_invoice_invoice2data", "l10n_generic_coa"],
    "demo": [
        "demo/account_tax_group.xml",
        "demo/account_tax.xml",
        "demo/product_product.xml",
        "demo/account_invoice.xml",
    ],
    "installable": True,
}
