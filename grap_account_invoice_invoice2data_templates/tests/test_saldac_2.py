# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import datetime

from .test_module import TestModule


class TestSaldac(TestModule):
    def test_saldac_2_01(self):
        self._test_supplier_template(
            "saldac__2024-07-15__LUC__FA243352.pdf",
            line_qty=8,
            expected_values={
                "issuer": "Saldac",
                "date": datetime(day=15, month=7, year=2024),
                "date_due": datetime(day=22, month=7, year=2024),
                "invoice_number": "FA243352",
                "amount_untaxed": 711.27,
                "amount": 750.39,
            },
            expected_lines=[
                {
                    "product_code": "CAFEM1KG",
                    "product_name": "Café moulu bio. 1 kg",
                    "vat_code": "5.5",
                    "quantity": 9.0,
                    "price_unit": 13.75,
                    "discount": 2.0,
                    "price_subtotal": 121.28,
                }
            ],
        )
