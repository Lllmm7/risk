import self as self
from odoo import models,fields,api,_
import re

from datetime import datetime


from odoo.exceptions import ValidationError


class RisksDisaterInformations(models.Model):
    _name = "risk.disaster"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "risk information"
    _rec_name ='risk_name'
    # _rec_id = "risk_id"


    #----------------------------------------
    #filelds--------------------------------
    #---------------------------------------

    risk_id = fields.Many2one('risk.action',string='Risk ID')
    risk_name = fields.Char(string="Risk Name",required=True)
    risk_status = fields.Selection([('draft','Draft'),('inprogress','Inprogress'),('closed','Closed')],string="Risk Status",default="draft")
    risk_category = fields. Selection(
        [('naturels','Naturels'),('sanitaire','Santaire')
            ,('professionnels','Professionnels'),('psychosociaux','Psychosociaux')
            ,('technologiques','Technologiques'),
         ('numériques','Numériques'),('financier','Financier'),
         ('geographiques','Geographiques'),('géopolitique','Géopolitiques'),
         ('cimatique','climatique')]
        ,help="Risk Category: The type of risk in terms of the project's or business' chosen categories (e.g. Schedule, quality, legal etc.)",string="Risk Type")
    risk_description = fields.Char(string='Risk Description', help="Short description of the Risk.",required=True)
    risk_start_datetime = fields.Datetime(string="StartDateTime",help="Date of the Risk registered. Auto populated.")
    location = fields.Many2one("hr.work.location",string='department Location')
    department = fields.Many2one("hr.department",string="Department")
    risk_source = fields.Selection([('external','External'),('internal','Internal')],string="Risk source")
    risk_end_datetime = fields.Datetime(string="EndDateTime")
    # risk_probability = fields.Float(string="Probability",store=True,compute="_calcul_prob")
    priority_level = fields.Integer(string="priority level",default="0",required=True)
    users_res = fields.Many2one("res.users",string="relared users")
    risk_Owner = fields.Char(string="Owner")
    campany_name = fields.Many2one("res.company",string="campany name")
    company_id = fields.Many2one("res.partner")
    witness_name = fields.Char("witness name",required=True)
    witness_job = fields.Many2one("hr.job",required=True)
    witness_category = fields.Selection([('external','External'),('internal','Internal')])
    witness_phone = fields.Char("mobile phone",required=True)
    Witness_email = fields.Char("Email")
    witness_location = fields.Char("submit your geographical Location ",required=True)
    witness_street = fields.Char("street",required=True)
    witness_city = fields.Char("City",required=True)
    Witness_country = fields.Char("Contry",required=True)
    witness_street_number = fields.Integer("street number")
    image_1920 = fields.Image(readonly=False, store=True, copy=False)
    risk_latitude = fields.Float(string="Geo Latitude", digits=(10, 7))
    risk_longitude = fields.Float(string="Geo Longitude", digits=(10, 7))
    risk_street = fields.Char(string="street name")
    risk_city = fields.Char(string="city name")
    risk_country_state = fields.Many2one("res.county.state", string="state")
    risk_country = fields.Many2one("res.country", string="country")
    risk_street_number = fields.Integer(string="street number",default=0)
    count=fields.Integer(string="somme",compute="create")
    risk_cause=fields.Text("Cause Description")
    code = fields.Char("code")
    risk_request=fields.Selection([('avoid','avoid'),('refuse','refuse')],string="risk_request")
    # risk_duration = fields.Integer(compute="_calcule_risk_duration" , string="days duration")
    probability = fields.Float(string="risk probability",compute="calcul_prob",store=True)
    risk_count = fields.Integer(string="risk_count",compute="count_risk")



    # ----------------------------------------
    # risks methods--------------------------------
    # ---------------------------------------



    def set_state_draft(self):
        return self.write({'risk_status': 'draft'})

    def set_state_inprogress(self):
        return self.write({'risk_status': 'inprogress'})

    def set_state_closed(self):
        return self.write({'risk_status': 'closed'})


    def your_custom_function(self):

        if self.risk_name:
            notification = {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Your Custom Title'),
                'message': 'Your Custom Message',

            }
        }
        return notification

    def test_url(self):
        if self.id:
            return {
                'type': 'ir.actions.act_url',
                'url': 'http://0.0.0.0:8015/web/login=%s' % (self.id),
                'target': 'new',
            }

    @api.constrains('risk_start_datetime', 'risk_end_datetime')
    def _check_date_time(self):
        for rec in self:
            if rec.risk_end_datetime < rec.risk_start_datetime:
                raise ValidationError(_('invalid field,End Date Must be greater Than Start Date...'))


    @api.constrains('Witness_email')
    def validate_mail(self):
        for rec in self:
         if rec.Witness_email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', rec.Witness_email)
            if match == None:
                raise ValidationError('Not a valid E-mail')


    @api.constrains('priority_level')
    def _check_level_priority(self):
        """check priority level"""
        for rec in self:
            if rec.priority_level > 5 :
                raise ValidationError(_('priority level is out of range,maximum level is 5'))



    @api.model
    def create(self, vals):
        risk = super(RisksDisaterInformations, self).create(vals)
        if risk:
            users = self.env.ref("risks_disaster_management.group_risk_cordinator").users
            print('users', users)
            for user in users:
                 risk.activity_schedule("risk_disaster.mail_activity_risk", user_id=user.id)

        return risk


    def count_risk(self):
        for rec in self:

            rec.risk_count = self.env['risk.disaster'].search_count([('risk_name', '!=' ,'""' )])
            print("riskcount", rec.risk_count)

    # @api.depends('risk_count','risk_category')
    def calcul_prob(self):


            for rec in self:
                rec.nb = 0
                rec.prob = 0
                if rec.risk_category == "Naturels":
                    rec.nb = rec.nb + 1
                    prob = float(rec.nb/rec.risk_count)

                # elif rec.risk_category=="Santaire":
                #     nb=nb+1
                #     prob = float(nb / rec.risk_count)
                # elif rec.risk_category=="Professionnels":
                #     nb=nb+1
                #     prob =float( nb / rec.risk_count)
                # elif rec.risk_category=="Psychosociaux":
                #     nb=nb+1
                #     prob = float(nb / rec.risk_count)
                # elif rec.risk_category=="Technologiques":
                #     nb=nb+1
                #     prob =float( nb / rec.risk_count)
                # elif rec.risk_category=="Numériques":
                #     nb=nb+1
                #     prob = float(nb / rec.risk_count)
                # elif rec.risk_category == "Financier":
                #     nb = nb + 1
                #     prob = float(nb / rec.risk_count)
                # elif rec.risk_category=="Geographiques":
                #     nb=nb+1
                #     prob = float(nb / rec.risk_count)
                # elif rec.risk_category=="Géopolitiques":
                #     nb=nb+1
                #     prob = float(nb / rec.risk_count)
                # elif rec.risk_category == "climatique":
                #     nb = nb + 1
                #     prob = float(nb / rec.risk_count)
            rec.probability = prob

            return rec.probability

















    # @api.depends('risk_start_datetime', 'risk_end_datetime')
    # def _calcule_risk_duration(self):
    #
    #     fmt = "%Y-%m-%d %H:%M:%S"
    #     for record in self:
    #         date_debut = record.risk_start_datetime
    #
    #         date_fin = record.risk_end_datetime
    #
    #         d1 = datetime.strptime(str(date_debut), fmt).date()
    #
    #         d2 = datetime.strptime(str(date_fin), fmt).date()
    #
    #         if d2 > d1:
    #             record.risk_duration = (d2 - d1).days
    #         else:
    #             raise ValidationError(_('non valid time '))




























