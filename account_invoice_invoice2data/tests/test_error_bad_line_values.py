# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import base64

from .test_module import TestModule


class TestErrorBadLineValues(TestModule):
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
            "brasserie-teddy-beer__2222-12-01__FA2212-3445__error__bad-line-values.pdf"
        )
        invoice_file = open(str(self._get_invoice_path(self.invoice_name)), "rb")
        self.base64_data = base64.b64encode(invoice_file.read())

        self.template_teddy_beer = self.env["account.invoice2data.template"].search(
            [("vat", "=", "FR31832431373")]
        )[0]

        self.tranquille75_invoice_line = (
            self.invoice_teddy_beer.invoice_line_ids.filtered(
                lambda x: "tranquille75" in x.name
            )
        )
        self.miel75_invoice_line = self.invoice_teddy_beer.invoice_line_ids.filtered(
            lambda x: "miel75" in x.name
        )

    def test_full_workflow_error_bad_line_values(self):
        # unlink previous attachment to make the test idempotens
        self._get_attachments(self.invoice_teddy_beer).unlink()
        self.partner_teddy_beer.vat = False

        self.assertEqual(self.template_teddy_beer.invoice_qty, 0)
        self.assertEqual(self.template_teddy_beer.invoice_line_qty, 0)

        def _import_invoice(self):
            wizard = self.Wizard.create(
                {
                    "invoice_file": self.base64_data,
                    "invoice_filename": self.invoice_name,
                    "invoice_id": self.invoice_teddy_beer.id,
                    "partner_id": self.invoice_teddy_beer.partner_id.id,
                }
            )
            wizard.import_invoice()
            return wizard

        # ###########################################
        # Part 1 : Import Invoice and ignore bad line
        # ###########################################
        wizard = _import_invoice(self)

        self.assertEqual(wizard.state, "line_differences")
        tranquille75_line = wizard.line_ids.filtered(
            lambda x: x.pdf_product_code == "tranquille75"
        )
        miel75_line = wizard.line_ids.filtered(lambda x: x.pdf_product_code == "miel75")

        self.assertNotAlmostEqual(
            self.tranquille75_invoice_line.price_unit, tranquille75_line.pdf_price_unit
        )
        self.assertNotAlmostEqual(
            self.miel75_invoice_line.price_unit, miel75_line.pdf_price_unit
        )

        self.assertTrue(tranquille75_line.pdf_has_bad_line_value)
        self.assertFalse(miel75_line.pdf_has_bad_line_value)

        tranquille75_line.apply_change = False

        wizard.apply_changes()

        # ignore wizard tranquille75 line should not update the according invoice line
        self.assertNotAlmostEqual(
            self.tranquille75_invoice_line.price_unit,
            tranquille75_line.pdf_price_unit,
            2,
        )
        self.assertAlmostEqual(
            self.miel75_invoice_line.price_unit, miel75_line.pdf_price_unit, 2
        )

        # #####################################################
        # Part 2 : Import Invoice and apply changes on bad line
        # #####################################################
        wizard = _import_invoice(self)
        self.assertEqual(wizard.state, "line_differences")

        tranquille75_line = wizard.line_ids.filtered(
            lambda x: x.pdf_product_code == "tranquille75"
        )
        miel75_line = wizard.line_ids.filtered(lambda x: x.pdf_product_code == "miel75")

        self.assertNotAlmostEqual(
            self.tranquille75_invoice_line.price_unit,
            tranquille75_line.pdf_price_unit,
            2,
        )
        self.assertAlmostEqual(
            self.miel75_invoice_line.price_unit, miel75_line.pdf_price_unit, 2
        )

        self.assertTrue(tranquille75_line.pdf_has_bad_line_value)
        self.assertFalse(miel75_line.pdf_has_bad_line_value)

        wizard.apply_changes()

        # Don't ignore wizard tranquille75 line should update the according invoice line
        self.assertAlmostEqual(
            self.tranquille75_invoice_line.price_unit,
            tranquille75_line.pdf_price_unit,
            2,
        )
        self.assertAlmostEqual(
            self.miel75_invoice_line.price_unit, miel75_line.pdf_price_unit, 2
        )
