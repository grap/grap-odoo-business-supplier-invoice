# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from .test_abstract import TestAbstract


class TestModule(TestAbstract):
    def setUp(self):
        super().setUp()
        self.env.user.company_id = self.env.ref(
            "account_invoice_invoice2data.invoice2data_company"
        )
        self.partner_demo = self.env.ref(
            "grap_account_invoice_invoice2data_self_import.partner_demo"
        )
        self.invoice_demo = self.env.ref(
            "grap_account_invoice_invoice2data_self_import.invoice_demo"
        )
        self.main_company = self.env.ref("base.main_company")

        self.odoo_fermente_template = self.env["account.invoice2data.template"].search(
            [("file_name", "=", "odoo_fermente.yml")]
        )

    def test_message_on_invoice_form(self):

        self.assertEqual(
            len(self.odoo_fermente_template),
            1,
            "The Odoo Fermente template is not found in the template dir %s"
            % self.local_templates_dir,
        )

        self.invoice_demo.partner_id.vat = False
        self.assertEqual(self.invoice_demo.invoice2data_state, "no_vat")
        self.invoice_demo.partner_id.vat = "FR17345184428"
        self.assertEqual(self.invoice_demo.invoice2data_state, "not_found")

        self.main_company.vat = "FR17345184428"
        # Force recompute, because the compute doesn't depends on vat company
        self.invoice_demo._compute_invoice2data_info()
        self.assertEqual(self.invoice_demo.invoice2data_state, "available")

        self.odoo_fermente_template.active = False
        # Force recompute, because the compute doesn't depends on invoice2data state
        self.invoice_demo._compute_invoice2data_info()
        self.assertEqual(self.invoice_demo.invoice2data_state, "disabled")
