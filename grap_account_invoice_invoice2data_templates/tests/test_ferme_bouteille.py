# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import datetime

from .test_module import TestModule


class TestFermeBouteille(TestModule):
    def test_ferme_bouteille(self):
        self._test_supplier_template(
            "ferme-bouteille__2024-02-01__LUC__FA2402-0381.pdf",
            line_qty=4,
            expected_values={
                "issuer": "Ferme Bouteille (GAEC)",
                "date": datetime(day=29, month=2, year=2024),
                "date_due": datetime(day=1, month=3, year=2024),
                "invoice_number": "FA2402-0381",
                "amount_untaxed": 167.60,
                "amount": 176.82,
            },
            expected_lines=[
                {
                    "product_code": "FA-ble_T80-5",
                    "product_name": "Farine de ble T80 5kg",
                    "vat_code": "5.5",
                    "quantity": 4.0,
                    "price_unit": 8.0,
                    "price_subtotal": 32.0,
                },
            ],
        )
