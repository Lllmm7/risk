from odoo import models,fields,api,_

from odoo.exceptions import ValidationError


class RisksDisasterCauses(models.Model):

    _name = "risk.cause"
    _description = "risk causes"
    # _inherit = "risk.disaster"





    #----------------------------------------
    #filelds--------------------------------
    #---------------------------------------

    risk_cause_id = fields.Many2one("risk.disaster",string="causes refers to risk",required=True)
    risk_causes = fields.Text(string="Cause Description",default="cause description")#relier au risk
    risk_cause_source = fields.Selection([('external','External'),('internal','Internal')],string="Cause source")
    cause_category = fields.Selection([('naturels','Naturels'),('sanitaire','Santaire'),('professionnels','Professionnels'),('psychosociaux','Psychosociaux'),('technologiques','Technologiques'),('numériques','Numériques'),('financier','Financier'),('geographiques','Geographiques'),('géopolitique','Géopolitiques'),('cimatique','climatique')])
    risk_responsible_ids = fields.Many2many("hr.employee",string="responsible(s)")
    risk_responsible_category = fields.Selection([('external','External'),('internal','Internal')],string="Responsible  Category")
    cause_name = fields.Char("Cause Name")
    cause_location = fields.Many2one("hr.work.location",string="cause location")
    image_1920 = fields.Image(readonly=False, store=True)




    #------------------------------
    #methods-----------------------
    #------------------------------

    # @api.constrains("cause_category")
    # def _check_cause_categeory(self):
    #     """check cause category"""
    #     types = ["Naturels", "Sanitaire", "Professionnels", "Psychosociaux", "Technologiques", "Numériques"
    #         , "Financiers", "Géographiques", "Géopolitiques", "Climatiques", "external risk"]
    #
    #     for rec in self:
    #         for i in range(len(types)):
    #
    #            if rec.cause_category not in types :
    #                raise ValidationError (_("cause category invalid field"))







