from odoo import fields, models


class EstatePropertyTag(models.Model):
    # Private Attrs
    _name = "estate.property.tag"
    _description = "Real Estate Property Tag"
    _order = "name"
    _sql_constraints = [
        ("name_unique", "UNIQUE(name)", "The name must be unique"),
    ]

    # Field Declaration
    name = fields.Char("Name", required=True)
    color = fields.Integer("Color Index")
