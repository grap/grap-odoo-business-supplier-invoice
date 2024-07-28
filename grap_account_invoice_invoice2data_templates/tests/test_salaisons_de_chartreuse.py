# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import datetime

from .test_module import TestModule


class TestSalaisonsDeChartreuse(TestModule):
    def test_salaisons_de_chartreuse_01(self):
        self._test_supplier_template(
            "salaisons-de-chartreuse__2024-02-08__LUC__F2402-02087.pdf",
            line_qty=3,
            expected_values={
                "issuer": "Les Salaisons de Chartreuse",
                "date": datetime(day=8, month=2, year=2024),
                "invoice_number": "F2402-02087",
                "amount_untaxed": 148.90,
                "amount": 157.09,
            },
            expected_lines=[
                {
                    "product_code": "LS4004",
                    "product_name": "SAUCISSON SEC DE PORC BIO",
                    "vat_code": "5.5%",
                    "quantity": 15.00,
                    "price_unit": 5.30,
                    "price_subtotal": 79.50,
                }
            ],
        )
