from odoo import models, api, fields
from odoo.exceptions import ValidationError
import requests
class RiskActivity(models.Model):
     _inherit = "mail.activity"
     _name = "risk.activity"

     activity_degree = fields.Integer("activity degree")
