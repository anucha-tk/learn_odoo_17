# -*- coding: utf-8 -*-
from odoo import fields, models


class Student(models.Model):
    # table name
    _name = "wb.student"
    _description = "Student"

    name = fields.Char("name")
