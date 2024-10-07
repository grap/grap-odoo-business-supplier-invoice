# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import datetime

from .test_module import TestModule


class TestRelaisVert(TestModule):
    def test_relais_vert_3_01(self):
        self._test_supplier_template(
            "relais-vert__2024-07-26__CLO__AC10407220.pdf",
            line_qty=13,
            expected_values={
                "issuer": "Relais Vert",
                "version": 3,
                "date": datetime(day=26, month=7, year=2024),
                "invoice_number": "AC10407220",
                "amount_untaxed": 105.38,
                "amount": 111.18,
            },
            expected_lines=[
                {
                    "product_code": "16887",
                    "product_name": "BOUCHEES MOZZARELLA ET TOMATES (6X30G) CARTE NATURE",
                    "vat_code": "1",
                    "quantity": 2.0,
                    "price_unit": 2.83,
                    "price_subtotal": 5.66,
                }
            ],
        )
