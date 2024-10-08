# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import datetime

from .test_module import TestModule


class TestSaldac(TestModule):
    def test_saldac_3_01(self):
        self._test_supplier_template(
            "saldac__2024-08-20__LUC__FA243718.pdf",
            line_qty=4,
            expected_values={
                "issuer": "Saldac",
                "version": 3,
                "date": datetime(day=20, month=8, year=2024),
                "date_due": datetime(day=27, month=8, year=2024),
                "invoice_number": "FA243718",
                "amount_untaxed": 437.32,
                "amount": 461.37,
            },
            expected_lines=[
                {
                    "product_code": "CAFEM1KG",
                    "product_name": "Café moulu bio. El Palomar - Pérou 1 kg. *SPP",
                    "vat_code": "5.5",
                    "quantity": 18.0,
                    "price_unit": 13.75,
                    "discount": 2.0,
                    "price_subtotal": 242.55,
                }
            ],
        )

    def test_saldac_3_02(self):
        self._test_supplier_template(
            "saldac__2024-09-24__LUC_FA244308.pdf",
            line_qty=8,
            expected_values={
                "issuer": "Saldac",
                "version": 3,
                "date": datetime(day=24, month=9, year=2024),
                "date_due": datetime(day=1, month=10, year=2024),
                "invoice_number": "FA244308",
                "amount_untaxed": 909.17,
                "amount": 959.17,
            },
            expected_lines=[
                {
                    "product_code": "NOIXAMA2KG",
                    "product_name": "Noix Amazonie grillée bio. Pérou. sac de 2 kg",
                    "vat_code": "5.5",
                    "quantity": 1.0,
                    "price_unit": 45.2,
                    "discount": 2.0,
                    "price_subtotal": 44.3,
                }
            ],
        )
