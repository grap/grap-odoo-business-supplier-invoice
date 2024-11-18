# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import datetime

from .test_module import TestModule


class TestTAirDeFamille(TestModule):
    def test_t_air_de_famille_01(self):
        self._test_supplier_template(
            "t-air-de-famille__2023-02-01__GAE__FA20230020.pdf",
            line_qty=4,
            expected_values={
                "issuer": "T'air de Famille",
                "date": datetime(day=1, month=2, year=2023),
                "date_due": datetime(day=1, month=2, year=2023),
                "invoice_number": "FA20230020",
                "amount_untaxed": 83.76,
                "amount": 88.37,
            },
            expected_lines=[
                {
                    "product_code": "AR00101",
                    "product_name": "Purée de pomme 1kg x 6",
                    "vat_code": False,
                    "quantity": 1,
                    "price_unit": 20.28,
                    "price_subtotal": 20.28,
                }
            ],
        )

    def test_t_air_de_famille_02(self):
        self._test_supplier_template(
            "t-air-de-famille__2024-10-01__HAL__FA20240526.pdf",
            line_qty=12,
            expected_values={
                "issuer": "T'air de Famille",
                "date": datetime(day=1, month=10, year=2024),
                "date_due": datetime(day=1, month=10, year=2024),
                "invoice_number": "FA20240526",
                "amount_untaxed": 167.10,
                "amount": 176.29,
            },
            expected_lines=[
                {
                    "product_code": "AR00007",
                    "product_name": "purée de pomme cerise 340g x 12",
                    "vat_code": False,
                    "quantity": 0,
                    "price_unit": 19.0,
                    "price_subtotal": 0.0,
                }
            ],
        )
