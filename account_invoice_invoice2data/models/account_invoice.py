# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import _, api, fields, models


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    invoice2data_template_id = fields.Many2one(
        comodel_name="account.invoice2data.template",
        help="Invoice2data template Used to analyse" " the supplier invoice",
    )

    invoice2data_state = fields.Selection(
        compute="_compute_invoice2data_info",
        selection=[
            ("not_applicable", "Not Applicable"),
            ("available", "Available"),
            ("disabled", "Disabled"),
            ("not_found", "Not Found"),
            ("no_vat", "Vat Number Not Set"),
        ],
        help="* Not Applicable:"
        " the invoice state of the invoice doesn't allow pdf import\n"
        " * Available:"
        " The supplier invoice can be analyzed\n"
        " * Disabled: "
        " The analysis is temporarily disabled\n"
        " * Not Found:"
        " The supplier invoice can not be analyzed\n"
        " * No VAT:"
        " The supplier doesn't have VAT defined. Unable to"
        " know if the invoice can be analyzed.",
    )

    invoice2data_message = fields.Text(
        compute="_compute_invoice2data_info",
    )

    @api.depends("partner_id.vat", "state")
    def _compute_invoice2data_info(self):
        for invoice in self.filtered(lambda x: x.state == "draft" and x.partner_id):
            current_vat = (invoice.partner_id.vat or "").replace(" ", "")
            if current_vat:
                templates = (
                    self.env["account.invoice2data.template"]
                    .with_context(active_test=False)
                    .search(
                        [("vat", "=", current_vat)],
                    )
                )
                if any(templates.mapped("active")):
                    invoice.invoice2data_state = "available"
                    invoice.invoice2data_message = (
                        _(
                            "The supplier's electronic invoice analysis"
                            " is available to Supplier %s."
                        )
                        % templates[0].name
                    )
                elif templates:
                    invoice.invoice2data_state = "disabled"
                    invoice.invoice2data_message = (
                        _(
                            "The supplier's electronic invoice analysis"
                            " is temporarily unavailable to Supplier %s."
                        )
                        % templates[0].name
                    )
                else:
                    invoice.invoice2data_state = "not_found"
            else:
                invoice.invoice2data_state = "no_vat"
                invoice.invoice2data_message = _(
                    "Please enter your supplier's VAT number,"
                    " to know if the supplier's electronic invoice"
                    " analysis is available."
                )

        for invoice in self.filtered(lambda x: x.state != "draft"):
            invoice.invoice2data_state = "not_applicable"
            invoice.invoice2data_message = False
