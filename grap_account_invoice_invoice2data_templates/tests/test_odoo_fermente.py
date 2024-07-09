# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import datetime

from .test_module import TestModule


class TestOdooFerement(TestModule):
    def test_odoo_fermente_01(self):
        self._test_supplier_template(
            "odoo_fermente__2024-07-09__3PP__VT-24-0382.pdf",
            line_qty=6,
            expected_values={
                "issuer": "Activités du réseau",
                "date": datetime(day=9, month=7, year=2024),
                "date_due": datetime(day=30, month=8, year=2024),
                "invoice_number": "VT/24/0382",
                "amount_untaxed": 108.96,
                "amount": 130.75,
            },
            expected_lines=[
                {
                    "product_code": "VIN-000227",
                    "product_name": "Côtes du Rhône - 75 cl - Château de Montfrin",
                    "vat_code": "20.0",
                    "quantity": 6.00,
                    "price_unit": 4.8,
                    "discount": 10.0,
                    "price_subtotal": 25.92,
                }
            ],
        )
