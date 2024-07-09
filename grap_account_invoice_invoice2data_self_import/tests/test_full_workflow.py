# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import os
from datetime import datetime
from pathlib import Path

from odoo.tests import tagged
from odoo.tests.common import HttpCase
from odoo.tools.misc import mute_logger

from odoo.addons.account.tests.account_test_no_chart import TestAccountNoChartCommon
from odoo.addons.account_invoice_invoice2data.tests.test_abstract import (
    TestAbstract as TestAbstractGlobal,
)

from .test_abstract import TestAbstract


@tagged("post_install", "-at_install")
class TestModule(HttpCase, TestAbstract, TestAbstractGlobal, TestAccountNoChartCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.setUpAdditionalAccounts()
        cls.main_company = cls.env.ref("base.main_company")
        cls.demo_product = cls.env.ref(
            "grap_account_invoice_invoice2data_self_import.demo_product"
        )
        cls.AccountInvoice = cls.env["account.invoice"]
        cls.product = cls.env.ref("product.product_product_6")
        cls.report_action = cls.env.ref(
            "account.account_invoices_without_payment"
        ).with_context(force_report_rendering=True, lang="fr_FR")

        # Reconfigure USD because we can not affect EUR
        # to the main_company, due to existing account moves
        cls.env.ref("base.USD").write(
            {
                "position": "after",
                "symbol": "€",
            }
        )
        # Account settings
        cls.main_company.vat = "FR31790058572"
        cls.main_company.country_id.vat_label = "TVA intracommunautaire"
        cls.tax_20 = cls.env["account.tax"].create(
            {
                "name": "Tax 20%",
                "amount": 20.0,
                "description": "20.0%",
                "company_id": cls.main_company.id,
                "type_tax_use": "sale",
            }
        )
        # Load French translation
        with mute_logger("odoo.addons.base.models.ir_translation"):
            cls.env["base.language.install"].create(
                {"lang": "fr_FR", "overwrite": True}
            ).lang_install()
        cls.partner_customer_usd.lang = "fr_FR"

    def test_full_workflow(self):
        # Create an invoice in base.main_company
        # and try to integrate it in invoice2data company
        invoice = self.AccountInvoice.create(
            {
                "name": "",
                "type": "out_invoice",
                "partner_id": self.partner_customer_usd.id,
                "invoice_line_ids": [
                    (
                        0,
                        0,
                        {
                            "name": self.demo_product.name,
                            "product_id": self.demo_product.id,
                            "quantity": 10,
                            "uom_id": self.demo_product.uom_id.id,
                            "price_unit": 100,
                            "account_id": self.account_income.id,
                            "invoice_line_tax_ids": [(4, self.tax_20.id)],
                        },
                    )
                ],
                "account_id": self.account_payable.id,
                "journal_id": self.sale_journal0.id,
                "currency_id": self.main_company.currency_id.id,
            }
        )
        invoice.action_invoice_open()
        res = self.report_action.render_qweb_pdf(invoice.ids)
        f = open(
            Path(os.path.realpath(__file__)).parent / "invoices" / "test_output.pdf",
            "wb",
        )
        f.write(res[0])
        f.close()

        if self.cr.dbname == "odoo":
            # For the time being, there is a trouble with assets
            # Locally, the first time the code is executed, or
            # on CI, the call of web/content/xxx-xxxxxxx/web.report_assets_xxx
            # return a 404
            # so for the time being, we don't test the final analysis
            # In the CI
            return

        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        self._test_supplier_template(
            "test_output.pdf",
            line_qty=1,
            expected_values={
                "issuer": "Activités du réseau",
                "date": today,
                "date_due": today,
                "invoice_number": "SJT0/2024/0001",
                "amount_untaxed": 1000.0,
                "amount": 1200.0,
            },
            expected_lines=[
                {
                    "product_code": "DEF-123456",
                    "product_name": "Demo Product",
                    "vat_code": "20.0",
                    "quantity": 10.00,
                    "price_unit": 100.0,
                    "discount": 0.0,
                    "price_subtotal": 1000.0,
                }
            ],
        )
