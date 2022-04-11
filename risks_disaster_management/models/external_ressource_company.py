from odoo import models,fields,api,_
from datetime import date, datetime
from odoo.exceptions import ValidationError

class CantactCompanyAction(models.Model):
    # _name = "company.cantact"
    _description = "select an external ressource"
    _inherit = "res.partner"

    action_id = fields.Many2one("risk.action",string="submit action")
    available=fields.Boolean("available?")


    def test_url_cantact_company(self):
        if self.id:
            return {
                'type': 'ir.actions.act_url',
                'url': 'http://0.0.0.0:8015/web#id=3&cids=1&menu_id=701&action=1160&model=risk.action&view_type=form=26=%s' % (
                    self.id),
                'target': 'new',
            }

    def test_url_cantact_company_action(self):
        if self.id:
            return {
                'type': 'ir.actions.act_url',
                'url': 'http://0.0.0.0:8015/web#id=3&cids=1&menu_id=701&action=1160&active_id=10&model=risk.action&view_type=form=11=%s' % (
                    self.id),
                'target': 'new',
            }
