# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import datetime

from .test_module import TestModule


class TestBrasserieStephanoise(TestModule):
    def test_brasserie_stephanoise_01(self):
        self._test_supplier_template(
            "brasserie-stephanoise__2024-05-30__ACR__2024-05-0458.pdf",
            line_qty=4,
            expected_values={
                "issuer": "La Brasserie Stéphanoise",
                "date": datetime(day=30, month=5, year=2024),
                "date_due": datetime(day=29, month=6, year=2024),
                "invoice_number": "2024-05-0458",
                "amount_untaxed": 198.84,
                "amount": 238.61,
            },
            expected_lines=[
                {
                    "product_name": 'La Manu Blonde "Hoppy Blond Ale"'
                    " Bio 5.5 % Carton de 12 bouteilles de 75cl",
                    "vat_code": "20.0",
                    "quantity": 2,
                    "price_unit": 39.12,
                    "price_subtotal": 78.24,
                }
            ],
        )
