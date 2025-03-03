from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"
    _order = "sequence, name"
    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique")
    ]

    # Field Declaration
    ## Basic
    name = fields.Char("name", required=True)
    sequence = fields.Integer("Sequence", default=10)

    # Relational (for inline view)
    property_ids = fields.One2many(
        "estate.property", "property_type_id", string="Properties"
    )

    # Computed (for stat button)
    offer_count = fields.Integer(
        compute="_compute_offer_count", string="Offer Count"
    )

    # TODO: make _compute_offer_count
    def _compute_offer_count(self):
        return

    # TODO: make action_view_offers
    def action_view_offers(self):
        return
