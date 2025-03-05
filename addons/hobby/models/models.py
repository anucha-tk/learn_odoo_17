# -*- coding: utf-8 -*-
from odoo import fields, models


class Hobby(models.Model):
    _name = "wb.hobby"
    _description = "This is student hobbies."

    name = fields.Char("Name")
