from odoo import fields, models


class ResUsers(models.Model):
    """docstring for ResUsers."""

    _inherit = "res.users"

    property_ids = fields.One2many(
        "estate.property",
        "user_id",
        string="Properties",
        domain=[("state", "in", ["new", "offer_received"])],
    )
