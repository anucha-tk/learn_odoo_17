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
    student_fees = fields.Float("Student Fees", default=3.2)
    discount_fees = fields.Float("Discount Fees")
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

    # compute field by default not store to database
    # if you want store use store=True
    final_fees = fields.Float(
        compute="_compute_final_fees",
        string="Final Fees",
        store=True,
    )

    # This ensures Odoo recalculates final_fees whenever student_fees or discount_fees changes.
    @api.depends("student_fees", "discount_fees")
    def _compute_final_fees(self):
        for record in self:
            record.final_fees = record.student_fees - record.discount_fees

    # image upload by binary
    binary = fields.Binary("binary")
    # store file name
    binary_filename = fields.Char(string="Filename")
