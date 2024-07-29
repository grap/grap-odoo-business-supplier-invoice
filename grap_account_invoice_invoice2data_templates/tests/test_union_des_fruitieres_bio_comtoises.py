# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import datetime

from .test_module import TestModule


class TestUnionDesFruitieresBioComtoises(TestModule):
    def test_union_des_fruitieres_bio_comtoises_01(self):
        self._test_supplier_template(
            "union-des-fruitieres-bio-comtoises__2024-05-27__LUC__FC20052825.pdf",
            line_qty=3,
            expected_values={
                "issuer": "Union des Fruitières Bio-Comtoises (UFBC)",
                "date": datetime(day=27, month=5, year=2024),
                "date_due": datetime(day=26, month=6, year=2024),
                "invoice_number": "FC20052825",
                "amount_untaxed": 638.97,
                "amount": 674.11,
            },
            expected_lines=[
                {
                    "product_code": "CJOUS231108",
                    "product_name": "Comté AOP jeune nov 23 Oussieres 1/ 8 meule",
                    "vat_code": "5.50",
                    "quantity": 17.78,
                    "price_unit": 14.67,
                    "price_subtotal": 260.83,
                }
            ],
        )

    def test_union_des_fruitieres_bio_comtoises_02(self):
        self._test_supplier_template(
            "union-des-fruitieres-bio-comtoises__2024-06-17__HAL__FC20052955.pdf",
            line_qty=1,
            expected_values={
                "issuer": "Union des Fruitières Bio-Comtoises (UFBC)",
                "date": datetime(day=17, month=6, year=2024),
                "date_due": datetime(day=17, month=7, year=2024),
                "invoice_number": "FC20052955",
                "amount_untaxed": 147.67,
                "amount": 155.79,
            },
            expected_lines=[
                {
                    "product_code": "CJLAV231104",
                    "product_name": "Comté AOP jeune nov 23 Lavigny 1/ 4 meule",
                    "vat_code": "5.50",
                    "quantity": 10.205,
                    "price_unit": 14.47,
                    "price_subtotal": 147.67,
                }
            ],
        )
