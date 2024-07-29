# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import datetime

from .test_module import TestModule


class TestManivelle(TestModule):
    def test_manivelle_01(self):
        self._test_supplier_template(
            "manivelle__2024-03-08__LUC__FA00013883.pdf",
            line_qty=4,
            expected_values={
                "issuer": "La Manivelle (Brasserie Artisanale De Die)",
                "date": datetime(day=8, month=3, year=2024),
                "date_due": datetime(day=10, month=4, year=2024),
                "invoice_number": "FA00013883",
                "amount_untaxed": 147.66,
                "amount": 177.19,
            },
            expected_lines=[
                {
                    "product_name": "BIPA bio 6 Bouteilles - 0.75L",
                    "vat_code": "20.00%",
                    "quantity": 2.0,
                    "price_unit": 21.30,
                    "price_subtotal": 42.60,
                }
            ],
        )
