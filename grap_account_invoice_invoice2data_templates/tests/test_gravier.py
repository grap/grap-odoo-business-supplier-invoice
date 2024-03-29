# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import datetime

from .test_module import TestModule


class TestGravier(TestModule):
    def test_gravier_01(self):
        self._test_supplier_template(
            "gravier__2022-11-16__ECS__FA1375938.pdf",
            line_qty=4,
            expected_values={
                "issuer": "Gravier",
                "date": datetime(day=16, month=11, year=2022),
                "date_due": datetime(day=31, month=12, year=2022),
                "invoice_number": "FA1375938",
                "amount_untaxed": 291.15,
                "amount": 349.38,
            },
            expected_lines=[
                {
                    "product_code": "LE00001402",
                    "product_name": "LIQUIDE VAISSELLE MAIN ULTRA DEGRAISSANT 5L",
                    "vat_code": "20",
                    "quantity": 4.0,
                    "price_unit": 14.19,
                    "discount": 20.0,
                    "price_subtotal": 45.41,
                }
            ],
        )

    def test_gravier_02(self):
        self._test_supplier_template(
            "gravier__2024-02-14__BSG__FA1387616.pdf",
            line_qty=4,
            expected_values={
                "issuer": "Gravier",
                "date": datetime(day=14, month=2, year=2024),
                "date_due": datetime(day=31, month=3, year=2024),
                "invoice_number": "FA1387616",
                "amount_untaxed": 198.01,
                "amount": 237.61,
            },
            expected_lines=[
                {
                    "product_code": "ASE0003600",
                    "product_name": "LIQUIDE VAISSELLE CONCENTRE 1L",
                    "vat_code": "20",
                    "quantity": 24.0,
                    "price_unit": 1.89,
                    "discount": 10.0,
                    "price_subtotal": 40.82,
                }
            ],
        )
