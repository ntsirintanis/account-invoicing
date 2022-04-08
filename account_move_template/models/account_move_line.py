from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    account_template_id = fields.Many2one("account.move.template")
