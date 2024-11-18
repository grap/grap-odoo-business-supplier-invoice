# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import datetime

from .test_module import TestModule


class TestEcodis(TestModule):
    def test_ecodis_2_01(self):
        self._test_supplier_template(
            "ecodis__2023-12-22__HAL__371068.pdf",
            line_qty=13,
            expected_values={
                "issuer": "Ecodis",
                "version": 2,
                "date": datetime(day=22, month=12, year=2023),
                "date_due": datetime(day=22, month=1, year=2024),
                "invoice_number": "371068",
                "amount_untaxed": 440.00,
                "amount": 528.00,
            },
            expected_lines=[
                {
                    "product_code": "DO033",
                    "product_name": "Lot de 2 éponges grattantes écologiques",
                    "vat_code": "20.00",
                    "quantity": 2,
                    "quantity2": 24,
                    "price_unit": 1.15,
                    "discount": 0.0,
                    "price_subtotal": 55.20,
                }
            ],
        )

    def test_ecodis_2_02(self):
        self._test_supplier_template(
            "ecodis__2024-05-21__HAL__379385.pdf",
            line_qty=18,
            expected_values={
                "issuer": "Ecodis",
                "version": 2,
                "date": datetime(day=21, month=5, year=2024),
                "date_due": datetime(day=21, month=6, year=2024),
                "invoice_number": "379385",
                "amount_untaxed": 385.24,
                "amount": 453.96,
            },
            expected_lines=[
                {
                    "product_code": "DO033",
                    "product_name": "Lot de 2 éponges grattantes écologiques",
                    "vat_code": "20.00",
                    "quantity": 1,
                    "quantity2": 24,
                    "price_unit": 1.15,
                    "discount": 3.0,
                    "price_subtotal": 26.78,
                },
                {
                    "product_code": "AE052",
                    "product_name": "30 pansements coton bio",
                    "vat_code": "20.00",
                    "quantity": 1,
                    "quantity2": 12,
                    "price_unit": 1.95,
                    "discount": 2.5,
                    "price_subtotal": 22.81,
                },
            ],
        )

    def test_ecodis_2_03(self):
        self._test_supplier_template(
            "ecodis__2024-07-22__CRB__382976.pdf",
            line_qty=13,
            expected_values={
                "issuer": "Ecodis",
                "version": 2,
                "date": datetime(day=19, month=7, year=2024),
                "date_due": datetime(day=19, month=8, year=2024),
                "invoice_number": "382976",
                "amount_untaxed": 396.60,
                "amount": 468.29,
            },
            expected_lines=[
                {
                    "product_code": "AE445",
                    "product_name": "Tube compte-gouttes 15 ml",
                    "vat_code": "20.00",
                    "quantity": 1,
                    "quantity2": 5,
                    "price_unit": 1.95,
                    "discount": 2.5,
                    "price_subtotal": 9.51,
                },
            ],
        )

    def test_ecodis_2_04(self):
        self._test_supplier_template(
            "ecodis__2024-10-10__CHE__387499.pdf",
            line_qty=19,
            expected_values={
                "issuer": "Ecodis",
                "version": 2,
                "date": datetime(day=10, month=10, year=2024),
                "date_due": datetime(day=10, month=11, year=2024),
                "invoice_number": "387499",
                "amount_untaxed": 558.29,
                "amount": 663.79,
            },
            expected_lines=[
                {
                    "product_code": "AE638",
                    "product_name": "Recharges vrac souple pour brosse à dents",
                    "vat_code": "20.00",
                    "quantity": 2,
                    "quantity2": 20,
                    "price_unit": 0.67,
                    "discount": 2.5,
                    "price_subtotal": 26.12,
                },
            ],
        )
