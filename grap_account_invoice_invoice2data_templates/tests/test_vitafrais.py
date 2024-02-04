# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import datetime

from .test_module import TestModule


class TestVitafrais(TestModule):
    def test_vitafrais_01(self):
        self._test_supplier_template(
            "vitafrais__2023-02-13__GAE__23013043.pdf",
            line_qty=27,
            expected_values={
                "issuer": "Vitafrais",
                "date": datetime(day=13, month=2, year=2023),
                "date_due": datetime(day=6, month=3, year=2023),
                "invoice_number": "23013043",
                "amount_untaxed": 453.52,
                "amount": 478.73,
                "amount_extra_fuel_surcharge_200": 1.83,
            },
            expected_lines=[
                {
                    "product_code": "9314",
                    "product_name": "Brillat-Savarin affiné 200 g",
                    "vat_code": "5.50",
                    "quantity": 6.0,
                    "price_unit": 5.82,
                    "discount": 8.0,
                    "price_subtotal": 32.13,
                }
            ],
        )

    def test_vitafrais_02(self):
        self._test_supplier_template(
            "vitafrais__2024-01-24_CDC__24006193.pdf",
            line_qty=19,
            expected_values={
                "issuer": "Vitafrais",
                "date": datetime(day=24, month=1, year=2024),
                "date_due": datetime(day=14, month=2, year=2024),
                "invoice_number": "24006193",
                "amount_untaxed": 318.68,
                "amount": 336.32,
                "amount_extra_fuel_surcharge_200": 0.78,
            },
            expected_lines=[
                {
                    "product_code": "13998",
                    "product_name": "Pains au lait 280 g",
                    "vat_code": "5.50",
                    "quantity": 16.0,
                    "price_unit": 2.42,
                    "discount": 8.0,
                    "discount_2": 20.0,
                    "price_subtotal": 28.50,
                }
            ],
        )
