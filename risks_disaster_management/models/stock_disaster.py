from odoo import models,fields,api,_
from datetime import date
from odoo.exceptions import ValidationError


class StockDisaster(models.Model):
    _inherit = "stock.picking"

    problem_exist = fields.Boolean(string="risk exist")
    stock_disaster = fields.Many2one("risk.disaster",string="risk reference")



