from odoo import models, fields

class Property(models.Model):
    _name = "estate.property"
    _description = "This is a real estate property model"

    name = fields.Char()