# Copyright (C) 2023 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging
import os
from pathlib import Path

import invoice2data
from cryptography.fernet import Fernet

from odoo import tools
from odoo.tests.common import TransactionCase

_logger = logging.getLogger(__name__)


class TestModule(TransactionCase):
    def setUp(self):
        super().setUp()

        # Load Templates
        self.local_templates_dir = str(
            Path(os.path.realpath(__file__)).parent.parent / "templates"
        )

        self.templates = invoice2data.extract.loader.read_templates(
            self.local_templates_dir
        )
        self.pdf_folder_path = Path(os.path.realpath(__file__)).parent / "invoices"

        self.invoice2data_key = tools.config.get("invoice2data_key", False)
        if not self.invoice2data_key:
            self.invoice2data_key = os.environ["INVOICE2DATA_KEY"]
        self.invoice2data_key = self.invoice2data_key and self.invoice2data_key.encode(
            "utf-8"
        )

    def _get_invoice_path(self, invoice_file_name):
        invoice_path = self.pdf_folder_path / invoice_file_name
        invoice_path_encrypted = self.pdf_folder_path / (
            invoice_file_name + ".encrypted"
        )
        if invoice_path.exists() and invoice_path_encrypted.exists():
            return invoice_path

        elif not invoice_path.exists() and not invoice_path_encrypted.exists():
            raise Exception("%s file doesn't exist" % invoice_path)

        fernet = Fernet(self.invoice2data_key)
        if invoice_path.exists() and not invoice_path_encrypted.exists():
            # we encrypt the pdf to put it on the CI
            with open(invoice_path, "rb") as file:
                file_data = file.read()
                encrypted_data = fernet.encrypt(file_data)
            with open(invoice_path_encrypted, "wb") as file:
                file.write(encrypted_data)

        elif not invoice_path.exists() and invoice_path_encrypted.exists():
            # we decrypt the pdf to extract the data
            with open(invoice_path_encrypted, "rb") as file:
                file_data = file.read()
                decrypted_data = fernet.decrypt(file_data)
            with open(invoice_path, "wb") as file:
                file.write(decrypted_data)

        return invoice_path

    def _test_supplier_template(
        self,
        invoice_file_name,
        line_qty,
        expected_values,
        expected_lines,
    ):
        invoice_path = self._get_invoice_path(invoice_file_name)
        result = invoice2data.main.extract_data(
            str(invoice_path), templates=self.templates
        )

        for key, expected_value in expected_values.items():
            self.assertEqual(result[key], expected_value)

        for expected_line in expected_lines:
            line_found = False
            for real_line in result["lines"]:
                line_found = line_found or all(
                    [
                        real_line.get(key, False) == expected_line[key]
                        for key in expected_line.keys()
                    ]
                )

            self.assertTrue(
                line_found,
                "The following data has not been found %s\n"
                "===========\n"
                "%s"
                "===========\n" % (str(expected_line), str(result)),
            )
