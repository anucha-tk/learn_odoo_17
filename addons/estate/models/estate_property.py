from dateutil.relativedelta import relativedelta
from odoo import api, fields, models


class EstateProperty(models.Model):
    # Private attribute
    _name = "estate.property"
    _description = "Real Estate Property"
    _order = "id desc"
    _sql_constraints = [
        (
            "check_expected_price",
            "CHECK(expected_price > 0)",
            "The expected price must be strictly positive",
        ),
        (
            "check_selling_price",
            "CHECK(selling_price >= 0)",
            "The offer price must be positive",
        ),
    ]

    # Default Method
    def _default_date_availability(self):
        return fields.Date.context_today(self) + relativedelta(month=3)

    # Field Declaration
    ## Basic
    name = fields.Char("Name", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Postcode")
    date_availability = fields.Date(
        "Availability Form",
        default=lambda self: self._default_date_availability(),
        copy=False,
    )
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer("Bedroom", default=2)
    living_area = fields.Integer("Living Area (sqm)")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area")
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[
            ("N", "North"),
            ("S", "South"),
            ("E", "East"),
            ("W", "West"),
        ],
    )
    active = fields.Boolean("Active", default=True)

    # Special
    state = fields.Selection(
        string="Status",
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        required=True,
        copy=False,
        default="new",
    )

    # Relational
    property_type_id = fields.Many2one(
        "estate.property.type", string="Property Type"
    )
    user_id = fields.Many2one(
        "res.users", string="Salesman", default=lambda self: self.env.user
    )
    buyer_id = fields.Many2one(
        "res.partner", string="Buyer", readonly=True, copy=False
    )
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many(
        "estate.property.offer",
        "property_id",
        string="Offers",
    )

    # Compute
    total_area = fields.Integer(
        compute="_compute_total_area",
        string="Total Area (sqm)",
        help="Total area computed by summing the living area and the garden area",
    )

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for prop in self:
            prop.total_area = prop.living_area + prop.garden_area
