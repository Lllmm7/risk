from odoo import models,fields,api,_
from datetime import datetime
from odoo.exceptions import ValidationError


class RisksDisaterMiltigation(models.Model):
    _name = "risk.miltigation"
    _description = "miltigation risk informations"