from odoo import fields, models


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"
    _order = "price desc"

    price = fields.Float("Price", required=True)
    status = fields.Selection(
        [
            ("accepted", "Accepted"),
            ("refused", "Refused"),
        ],
        string="Status",
        copy=False,
        default=False,
    )

    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one(
        "estate.property", string="Property", required=True
    )
