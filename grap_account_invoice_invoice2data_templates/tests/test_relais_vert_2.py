# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import datetime

from .test_module import TestModule


class TestRelaisVert(TestModule):
    def test_relais_vert_2_01(self):
        self._test_supplier_template(
            "relais-vert__2023-12-11__LUC__FC11890790.pdf",
            line_qty=76,
            expected_values={
                "issuer": "Relais Vert",
                "version": 2,
                "date": datetime(day=11, month=12, year=2023),
                "invoice_number": "FC11890790",
                "amount_untaxed": 1825.81,
                "amount": 1945.11,
                "amount_extra_parafiscal_tax_interfel_200": 1.11,
            },
            expected_lines=[
                {
                    "product_code": "15461",
                    "product_name": "TARTARE D'ALGUES CLASSIQUE (1KG) BORD A",
                    "vat_code": "1",
                    "quantity": 1.0,
                    "price_unit": 23.09,
                    "price_subtotal": 23.09,
                }
            ],
        )

    def test_relais_vert_2_02(self):
        self._test_supplier_template(
            "relais-vert__2024-07-15__BES__FC12014253.pdf",
            line_qty=27,
            expected_values={
                "issuer": "Relais Vert",
                "version": 2,
                "date": datetime(day=15, month=7, year=2024),
                "invoice_number": "FC12014253",
                "amount_untaxed": 512.92,
                "amount": 543.76,
                "amount_extra_parafiscal_tax_interfel_200": 0.11,
                "amount_extra_shipping_costs_200": 16.0,
            },
            expected_lines=[
                {
                    "product_code": "13131",
                    "product_name": "PARMESAN REGGIANO DOP 20 MOIS VRAC LAIT",
                    "vat_code": "1",
                    "quantity": 1.696,
                    "price_unit": 23.66,
                    "price_subtotal": 40.13,
                }
            ],
        )

    def test_relais_vert_2_03(self):
        self._test_supplier_template(
            "relais-vert__2024-07-16__BSG__FC12014853.pdf",
            line_qty=88,
            expected_values={
                "issuer": "Relais Vert",
                "version": 2,
                "date": datetime(day=16, month=7, year=2024),
                "invoice_number": "FC12014853",
                "amount_untaxed": 3318.56,
                "amount": 3507.16,
                "amount_extra_parafiscal_tax_interfel_200": 3.20,
            },
            expected_lines=[
                {
                    "product_code": "28444",
                    "product_name": "LEVURE MALTEE PAILLETTE (3KG) MARKAL",
                    "vat_code": "1",
                    "quantity": 3.0,
                    "price_unit": 34.51,
                    "price_subtotal": 103.53,
                }
            ],
        )

    def test_relais_vert_2_04(self):
        self._test_supplier_template(
            "relais-vert__2024-10-08__3PP__FC12061180.pdf",
            line_qty=86,
            expected_values={
                "issuer": "Relais Vert",
                "version": 2,
                "date": datetime(day=8, month=10, year=2024),
                "invoice_number": "FC12061180",
                "amount_untaxed": 1645.37,
                "amount": 1755.83,
                "amount_extra_parafiscal_tax_interfel_200": 0.79,
            },
            expected_lines=[
                {
                    "product_code": "CHFLRORE",
                    "product_name": "CHOU FLEUR ROMANESCO X 8 CONV CAT II",
                    "vat_code": "1",
                    "quantity": 1.0,
                    "price_unit": 25.73,
                    "price_subtotal": 25.73,
                }
            ],
        )

    def test_relais_vert_2_05(self):
        self._test_supplier_template(
            "relais-vert__2025-03-25__3PP__FC12162859.pdf",
            line_qty=59,
            expected_values={
                "issuer": "Relais Vert",
                "version": 2,
                "date": datetime(day=25, month=3, year=2025),
                "invoice_number": "FC12162859",
                "amount_untaxed": 1187.89,
                "amount": 1262.29,
                "amount_extra_parafiscal_tax_interfel_200": 0.76,
            },
            expected_lines=[
                {
                    "product_code": "29900",
                    "product_name": "PAPIER D'ARMENIE TRADITION PAV (12",
                    "vat_code": "6",
                    "quantity": 1.0,
                    "price_unit": 22.39,
                    "price_subtotal": 22.39,
                }
            ],
        )
