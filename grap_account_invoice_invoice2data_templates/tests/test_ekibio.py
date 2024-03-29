# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import datetime

from .test_module import TestModule


class TestEkibio(TestModule):
    def test_ekibio_01(self):
        self._test_supplier_template(
            "ekibio__2023-02-02__EPV__791601.pdf",
            line_qty=35,
            expected_values={
                "issuer": "Ekibio",
                "date": datetime(day=2, month=2, year=2023),
                "date_due": datetime(day=4, month=3, year=2023),
                "invoice_number": "791601",
                "amount_untaxed": 965.60,
                "amount": 1020.81,
            },
            expected_lines=[
                {
                    "product_code": "005844",
                    "product_name": "PROTEGE SLIP 24u",
                    "vat_code": "1",
                    "quantity": 12.0,
                    "price_unit": 2.780,
                    "price_subtotal": 33.36,
                }
            ],
        )

    def test_ekibio_02(self):
        self._test_supplier_template(
            "ekibio__2023-02-07__GAE__792437.pdf",
            line_qty=18,
            expected_values={
                "issuer": "Ekibio",
                "date": datetime(day=7, month=2, year=2023),
                "date_due": datetime(day=9, month=3, year=2023),
                "invoice_number": "792437",
                "amount_untaxed": 625.55,
                "amount": 671.37,
            },
            expected_lines=[
                {
                    "product_code": "010118",
                    "product_name": "COUSCOUS DEMI COMPLET FILIERE FRANCE 5KG",
                    "vat_code": "1",
                    "quantity": 10.0,
                    "price_unit": 2.56,
                    "price_subtotal": 25.60,
                }
            ],
        )

    def test_ekibio_03(self):
        self._test_supplier_template(
            "ekibio__2023-02-17__ACR__794596.pdf",
            line_qty=11,
            expected_values={
                "issuer": "Ekibio",
                "date": datetime(day=17, month=2, year=2023),
                "date_due": datetime(day=19, month=3, year=2023),
                "invoice_number": "794596",
                "amount_untaxed": 822.07,
                "amount": 941.97,
            },
            expected_lines=[
                {
                    "product_code": "004951",
                    "product_name": "GALETTE MAIS 120G",
                    "vat_code": "1",
                    "quantity": 12.0,
                    "price_unit": 1.22,
                    "price_subtotal": 14.64,
                }
            ],
        )

    def test_ekibio_04(self):
        self._test_supplier_template(
            "ekibio__2023-04-13__3PP__804686.pdf",
            line_qty=57,
            expected_values={
                "issuer": "Ekibio",
                "date": datetime(day=13, month=4, year=2023),
                "date_due": datetime(day=13, month=5, year=2023),
                "invoice_number": "804686",
                "amount_untaxed": 1738.17,
                "amount": 1898.72,
            },
            expected_lines=[
                {
                    "product_code": "007308",
                    "product_name": "DOUBLE CONCENTRE DE TOMATES 200G",
                    "vat_code": "1",
                    "quantity": 12.0,
                    "price_unit": 1.84,
                    "price_subtotal": 22.08,
                },
                {
                    "product_code": "007426",
                    "product_name": "TOMATES PELEES ENTIERES 400G",
                    "vat_code": "1",
                    "quantity": 12.0,
                    "price_unit": 1.18,
                    "price_subtotal": 14.16,
                },
            ],
        )

    def test_ekibio_05(self):
        self._test_supplier_template(
            "ekibio__2024-02-07__BSG__863788.pdf",
            line_qty=21,
            expected_values={
                "issuer": "Ekibio",
                "date": datetime(day=7, month=2, year=2024),
                "date_due": datetime(day=8, month=3, year=2024),
                "invoice_number": "863788",
                "amount_untaxed": 552.28,
                "amount": 573.92,
            },
            expected_lines=[
                {
                    "product_code": "009209",
                    "product_name": "BIS SABLES CEREALES MUESLI ET FRUITS 200G",
                    "vat_code": "1",
                    "quantity": 12.0,
                    "price_unit": 1.71,
                    "price_subtotal": 20.52,
                },
            ],
        )
