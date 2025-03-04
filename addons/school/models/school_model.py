from odoo import fields, models


class School(models.Model):
    _name = "wb.school"
    _description = "School"

    name = fields.Char("name")
