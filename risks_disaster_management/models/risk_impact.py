from odoo import models,fields,api,_
from datetime import date
from odoo.exceptions import ValidationError


class RisksDisaterImpacts(models.Model):
    _name = "risk.impact"
    _description = "risk information"
    _inherit ="risk.disaster"



    # ----------------------------------------
    # filelds--------------------------------
    # ---------------------------------------
    victim_employee = fields.Many2one("hr.employee",string="victim employee")
    risk = fields.Many2one("risk.disaster","requested risk")
    description_effect = fields.Text(string='Impact Description')
    risk_impact_ids  = fields.One2many("risk.disaster", "risk_id", string=" impact refers to risk ID  ")
    impact_description = fields.Text(string="impact description")
    impact_status = fields.Selection([('draft','Draft'),('closed','Closed')],string='impact status')
    impact_Category = fields.Selection([('naturels','Naturels'),('sanitaire','Santaire')
            ,('professionnels','Professionnels'),('psychosociaux','Psychosociaux')
            ,('technologiques','Technologiques'),
         ('numériques','Numériques'),('financier','Financier'),
         ('geographiques','Geographiques'),('géopolitique','Géopolitiques'),
         ('cimatique','climatique')],string="impact category")
    impact_degree = fields.Selection([('Severe','severe'),('Significant','significant'),('Moderate','moderate'),('Minor','minor'),('Minimal','minimal')],string='impact degree')
    heath_safety = fields.Selection([('catostrophic','likely daths and many with seriuos injuries'),
    ('very critical','possibly deaths and many with serious injuries and/or grave diseases')
    ,('critical','some with serius injuries and/or grave diseases'),
    ('dangerous','few with minor injuries and/or diseases'),
    ('not dangerous','minimal or no harm to person')],string="Health and safety human being")

    monetory_values = fields.Selection([('catostrophic','Economic loss >60 million EUR'),
    ('very critical','Economic loss 12_60 million EUR'),('critical','Economic loss 1_12 million EUR'),
    ('dangerous','Economic loss 10000_1 million EUR'),('not dangerous','Economic loss<10000 EUR')],string="Monetory values/Economic issue")
    environment_impact = fields.Selection([
    ('catostrophic','Large uncontrolled release/Regional impact with repartive effort>10 years'),
    ('very critical','Large release/Local impact with repartive effort 3_10 years'),
    ('critical','Significant release/Repartive effort 1_3 years'),
    ('dangerous','Small release/Detectable damage with repartive effort>1 year'),
    ('not dangerous','Minor release/No detectable damage')],string="Environmental Impact")
    organization_impact = fields.Selection([
    ('catostrophic','Internation media attention./Public inquiry/Organization must close down'),
    ('very critical','Internation media attention/Public inquiry/High impact on organization'),
    ('critical','National media attention/Public inquiry/Moderate impact on organization'),
    ('dangerous','Possible local media attention/Possible public inquiry/Low impact on organization'),
    ('not dangerous','Just organizational attention/Just limited impact on organization')],string="Organization Reputation")

    # impact_rating = fields.Selection([('not dangerous','Low'),('dangerous','Low/Medium'),('critical','Medium'),('very critical','Medium/High'),('catostrophic','High')],string="risk rating")
    # impact_score =
    risk_probability = fields.Selection([('not dangerous','rare'),('dangerous','unlikely'),('critical','likely'),('very critical','very likely')],string="probability")
    risk_impact_level = fields.Integer(string="risk likelihood",required="true")
    risk_rating = fields.Integer(string="risk rating",required="true")
    risk_score = fields.Integer(string="risk score",compute="calcul_risk_score",required="true")
    risk_score_state = fields.Char(string="risk state",compute="score_risk_state")
    image=fields.Image(string="score")

    #-----------------------
    #-------methods---------
    #----------------------

    @api.constrains('risk_impact_level')
    def _check_risk_like_hold(self):

        for rec in self:
            if rec.risk_impact_level > 5:
                raise ValidationError(_('risk likehold is out of range,maximum level is 5'))


    @api.constrains('risk_rating')
    def _check_risk_rating(self):

        for rec in self:
            if rec.risk_rating > 5:
                raise ValidationError(_('risk rating is out of range,maximum level is 5'))


    @api.depends('risk_impact_level','risk_rating')
    def calcul_risk_score(self):
        for rec in self:
            rec.risk_score = rec.risk_rating * rec.risk_impact_level
        return rec.risk_score


    @api.depends('risk_score')
    def score_risk_state(self):
        for rec in self:
            if rec.risk_score in range(6):
                rec.risk_score_state = "Low"
            elif rec.risk_score in range(5,17):
                rec.risk_score_state = "Medium"
            else:
                rec.risk_score_state ="High"
        return rec.risk_score_state






