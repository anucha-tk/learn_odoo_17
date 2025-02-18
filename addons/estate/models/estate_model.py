from odoo import fields, models


class EstateModel(models.Model):
    _name = "app.estate"
    _description = "test estate description"

    name = fields.Char("Name", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Postcode")
    date_availability = fields.Date("Date Availability")
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price")
    bedrooms = fields.Integer("Bedroom")
    living_area = fields.Integer("Living Area")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area")
    garden_orientation = fields.Selection(
        string="Type",
        selection=[
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ],
    )
