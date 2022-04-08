from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    account_auto_id = fields.Many2one("account.move.auto")
