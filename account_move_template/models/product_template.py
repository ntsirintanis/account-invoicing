from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    account_template_id = fields.Many2one("account.move.template")
