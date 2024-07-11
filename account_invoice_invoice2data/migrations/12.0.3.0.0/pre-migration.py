# Copyright (C) 2024 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    if openupgrade.column_exists(cr, "account_invoice", "message_attachment_count"):
        _logger.info(
            "Guess missing invoice2data_template_id on account_invoice tables..."
        )
        openupgrade.logged_query(
            cr,
            """
            UPDATE account_invoice ai
            SET invoice2data_template_id = template.id
            FROM account_invoice2data_template template,
                res_partner rp
            WHERE ai.partner_id = rp.id
                AND template.vat = rp.sanitized_vat
                AND template.version = 1
                AND ai.message_attachment_count = 1
                AND ai.invoice2data_template_id is null
                AND ai.type in ('in_invoice', 'in_refund');
            """,
        )
    else:
        _logger.warning(
            "Unable to guess missing invoice2data_template_id on account_invoice tables"
            " because 'account_invoice_attachment_count' is not installed."
        )

    # Try to fix the following invoices
    # that have no invoice2data_template_id
    # But that looks to have been analyzed

    # SELECT ai.create_date,
    #     ai.invoice2data_template_id,
    #     ai.message_attachment_count,
    #     rp.sanitized_vat,
    #     rp.name
    # FROM account_invoice ai
    # INNER JOIN res_partner rp
    #     ON ai.partner_id = rp.id
    # WHERE ai.message_attachment_count = 1
    #     AND ai.invoice2data_template_id is null
    #     AND ai.type in ('in_invoice', 'in_refund')
    #     ORDER BY invoice2data_template_id, rp.sanitized_vat;
