# -*- coding: utf-8 -*-
from odoo import api, fields, models

class HrAttendance(models.Model):
    _inherit = "hr.attendance"

    latitude = fields.Float(string='Latitude', default=0, readonly=True)
    longitude = fields.Float("Longitude", default=0, readonly=True)