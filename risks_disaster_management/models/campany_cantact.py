from odoo import models,fields,api,_
from datetime import date, datetime
from odoo.exceptions import ValidationError

class CantactCompany(models.Model):
    # _name = "company.cantact"
    _description = "select an external ressource"
    _inherit = "res.partner"

    def test_url_cantact(self):
        if self.id:
            return {
                'type': 'ir.actions.act_url',
                'url': 'http://0.0.0.0:8015/web#id=3&cids=1&menu_id=701&action=1160&model=risk.action&view_type=form=%s' % (
                    self.id),
                'target': 'new',
            }

    def test_url_employee(self):
        if self.id:
            return {
                'type': 'ir.actions.act_url',
                'url': 'http://0.0.0.0:8015/web#id=3&cids=1&menu_id=701&action=1160&model=risk.action&view_type=form=14=%s' % (
                    self.id),
                'target': 'new',
            }




