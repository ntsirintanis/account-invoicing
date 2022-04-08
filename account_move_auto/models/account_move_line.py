from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    account_auto_id = fields.Many2one("account.move.auto")
