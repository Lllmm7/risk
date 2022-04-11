from odoo import models,fields,api,_

from odoo.exceptions import ValidationError
from random import *




class RisksConfig(models.Model):
    _name="risk.config"
    _description="risk configuration"
    _inherit = ['risk.disaster','risk.action']


     #---------------------------
     #----------------fields-----
     #-------------------------









class RisksType(models.Model):
    _name="risk.type"
    _description="risk configuration"

    risk_name = fields.Many2one("risk.disaster",string="risk name")
    risk_type = fields.Selection([('naturels', 'Naturels'), ('sanitaire', 'Santaire')
                                     , ('professionnels', 'Professionnels'), ('psychosociaux', 'Psychosociaux')
                                     , ('technologiques', 'Technologiques'),
                                  ('numériques', 'Numériques'), ('financier', 'Financier'),
                                  ('geographiques', 'Geographiques'), ('géopolitique', 'Géopolitiques'),
                                  ('cimatique', 'climatique')], string="risk type")





