# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from datetime import datetime

from .test_module import TestModule


class TestRelaisVert(TestModule):
    def test_relais_vert(self):
        self._test_supplier_template(
            "relais-vert__2023-02-06__FC11716389.pdf",
            line_qty=6,
            expected_values={
                "issuer": "Relais Vert",
                "date": datetime(day=6, month=2, year=2023),
                "invoice_number": "FC11716389",
                "amount_untaxed": 120.90,
                "amount": 127.66,
                "amount_extra_parafiscal_tax_interfel_200": 0.25,
            },
            expected_lines=[
                {
                    "product_code": "KIJAIT",
                    "product_name": "KIWI JAUNE VRAC CAT II",
                    "vat_code": "1",
                    "quantity": 10.0,
                    "price_unit": 3.73,
                    "price_subtotal": 37.30,
                }
            ],
        )
