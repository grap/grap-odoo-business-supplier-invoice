# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import base64

from .test_module import TestModule


class TestErrorAmountUntaxedDifference(TestModule):
    def setUp(self):
        super().setUp()
        self.AccountInvoice = self.env["account.invoice"]
        self.Wizard = self.env["wizard.invoice2data.import"]
        self.invoice_teddy_beer = self.env.ref(
            "account_invoice_invoice2data.invoice_teddy_beer"
        )
        self.partner_teddy_beer = self.env.ref(
            "account_invoice_invoice2data.partner_teddy_beer"
        )

        # Prepare binary data
        self.invoice_name = (
            "brasserie-teddy-beer__2222-12-01__FA2212-3445"
            "__error__amount-untaxed-difference.pdf"
        )
        invoice_file = open(str(self._get_invoice_path(self.invoice_name)), "rb")
        self.base64_data = base64.b64encode(invoice_file.read())

        self.template_teddy_beer = self.env["account.invoice2data.template"].search(
            [("vat", "=", "FR31832431373")]
        )[0]

    def test_full_workflow_error_amount_untaxed_difference(self):
        # unlink previous attachment to make the test idempotens
        self._get_attachments(self.invoice_teddy_beer).unlink()
        self.partner_teddy_beer.vat = False

        self.assertEqual(self.template_teddy_beer.invoice_qty, 0)
        self.assertEqual(self.template_teddy_beer.invoice_line_qty, 0)

        # #######################
        # Part 1 : Import Invoice
        # #######################

        wizard = self.Wizard.create(
            {
                "invoice_file": self.base64_data,
                "invoice_filename": self.invoice_name,
                "invoice_id": self.invoice_teddy_beer.id,
                "partner_id": self.invoice_teddy_beer.partner_id.id,
            }
        )
        wizard.import_invoice()

        self.assertEqual(wizard.state, "import_amount_untaxed_difference")
