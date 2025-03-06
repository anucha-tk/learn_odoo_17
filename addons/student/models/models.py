# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Student(models.Model):
    # table name
    _name = "wb.student"
    _description = "Student"

    @api.model
    def _get_vip_list(self):
        return [
            ("a", "1"),
            ("b", "2"),
            ("c", "3"),
        ]

    name = fields.Char("Name")
    student_name = fields.Char(
        "Student Name",
    )
    address = fields.Text("Address")
    address_html = fields.Html("Address Html")
    is_paid = fields.Boolean(
        "Is Paid",
        help="this field is for this student paid or not the full fees!",
    )
    gender = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
        ],
        string="gender",
        required=True,
    )
    vip_gender = fields.Selection(_get_vip_list)
    roll_number = fields.Integer("Roll Number")
    school_id = fields.Many2one("wb.school", string="School")
    hobby_list_ids = fields.Many2many(
        "wb.hobby",
        string="Hobbies",
        help="Select hobby list for this student!",
    )
