# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models


class WizardInvoice2dataImport(models.TransientModel):
    _inherit = "wizard.invoice2data.import"

    def _compute_supplier_name_different(self):
        super()._compute_supplier_name_different()
        for wizard in self:
            # We don't check if it's an intercompany import
            if wizard.pdf_issuer == "Activités du réseau":
                wizard.supplier_name_different = False
