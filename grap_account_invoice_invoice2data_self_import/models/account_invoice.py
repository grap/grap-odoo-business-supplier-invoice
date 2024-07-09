# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    def _compute_invoice2data_info(self):
        super()._compute_invoice2data_info()

        odoo_fermente_template = (
            self.env["account.invoice2data.template"]
            .with_context(active_test=False)
            .search([("file_name", "=", "odoo_fermente.yml")])
        )
        if not odoo_fermente_template:
            return

        vat_companies = (
            self.env["res.company"]
            .with_context(active_test=False)
            .search([])
            .mapped("partner_id.sanitized_vat")
        )

        vat_companies = [x for x in vat_companies if x is not False]

        for invoice in self.filtered(lambda x: x.state == "draft" and x.partner_id):
            if invoice.partner_id.sanitized_vat in vat_companies:
                if odoo_fermente_template.active:
                    invoice.invoice2data_state = "available"
                    invoice.invoice2data_message = _(
                        "The supplier's electronic invoice analysis"
                        " is available for this supplier."
                    )
                else:
                    invoice.invoice2data_state = "disabled"
                    invoice.invoice2data_message = _(
                        "The supplier's electronic invoice analysis"
                        " is temporarily unavailable for this supplier."
                    )
