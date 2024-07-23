# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import datetime

from .test_module import TestModule


class TestCds(TestModule):
    def test_cds_01(self):
        self._test_supplier_template(
            "cds__2023-01-30__ACR__37136.pdf",
            line_qty=4,
            expected_values={
                "issuer": "CDS",
                "date": datetime(day=30, month=1, year=2023),
                "invoice_number": "37136",
                "amount_untaxed": 694.46,
                "amount": 833.35,
            },
            expected_lines=[
                {
                    "product_code": "63JE001BV",
                    "product_name": "DESINFECTANT SANS RINCAGE 5L Colis de 4",
                    "vat_code": "1",
                    "quantity": 3,
                    "quantity2": 4,
                    "price_unit": 33.08,
                    "price_subtotal": 397.08,
                },
                {
                    "product_code": "24JE003BV",
                    "product_name": "SAVON NOIR 20KG",
                    "vat_code": "1",
                    "quantity": 2,
                    "price_unit": 73.93,
                    "price_subtotal": 147.86,
                },
            ],
        )

    def test_cds_02(self):
        self._test_supplier_template(
            "cds__2024-07-15__CRB__43181.pdf",
            line_qty=8,
            expected_values={
                "issuer": "CDS",
                "date": datetime(day=15, month=7, year=2024),
                "invoice_number": "43181",
                "amount_untaxed": 939.04,
                "amount": 1126.85,
            },
            expected_lines=[
                {
                    "product_code": "25JE003BV",
                    "product_name": "LESSIVE HYPO 20KG",
                    "vat_code": "1",
                    "quantity": 1,
                    "price_unit": 47.55,
                    "price_subtotal": 47.55,
                },
                {
                    "product_code": "20JE003BV_3+1_P",
                    "product_name": "LESSIVE FLEUR A SAVON 2 EN 1 - 20KG 3+1",
                    "vat_code": "1",
                    "quantity": 1,
                    "quantity2": 3,
                    "price_unit": 56.85,
                    "price_subtotal": 170.55,
                },
            ],
        )
