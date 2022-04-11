from odoo import models,fields,api,_
from datetime import date, datetime
from odoo.exceptions import ValidationError

class CantactEmployee(models.Model):
    # _name = "company.cantact"
    _description = "select an external ressource"
    _inherit = "hr.employee"


    hr_available = fields.Boolean(string="employee availibility")



    def test_url_employee(self):
        if self.id:
            return {
                'type': 'ir.actions.act_url',
                'url': 'http://0.0.0.0:8015/web#id=3&cids=1&menu_id=701&action=1160&model=risk.action&view_type=form=14=%s' % (
                    self.id),
                'target': 'new',
            }

