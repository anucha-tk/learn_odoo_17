from odoo import fields, models


class School(models.Model):
    _name = "wb.school"
    _description = "School"

    school_image = fields.Image("School Image", max_width=50, max_height=50)
    name = fields.Char("Name")
    student_ids = fields.One2many("wb.student", "school_id", string="Students")
    # on form you can write database relate field by selection dynamic model
    ref_field_id = fields.Reference(
        selection=[
            ("wb.hobby", "Hobby"),
            ("wb.student", "Student"),
            ("wb.school", "School"),
        ]
    )
    # related
    ## make root relate field
    res_user_id = fields.Many2one("res.users", string="Res User")
    ## add readonly field relate on `res_user_id` for show information data
    res_user_email_id = fields.Char(
        string="Res User Email",
        related="res_user_id.email",
    )
