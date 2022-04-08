from odoo import fields, models


class AccountMoveAuto(models.Model):
    _name = "account.move.auto"
    _description = "template for account move lines per product"

    name = fields.Char(required=True)
    product_tmpl_ids = fields.One2many(
        comodel_name="product.template",
        inverse_name="account_auto_id",
        string="Products",
        help="""something something""",
    )
    line_ids = fields.One2many(
        comodel_name="account.move.line",
        inverse_name="account_auto_id",
        string="Lines",
        help="""something something""",
    )
