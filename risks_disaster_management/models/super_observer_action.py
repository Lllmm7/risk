import re

from odoo import models,fields,api,_
from odoo import exceptions

from odoo15.odoo.exceptions import ValidationError


class SuperObserverAction(models.Model):
    _name = "observer.action"
    _description = "super observer  Actions"



    #------------------------------------
    #fields------------------------------
    #------------------------------------
    presence_status = fields.Selection([('Left','left'),('Present','present')],string="prsence status")
    observer_available = fields.Selection([('Available','available'),('Unvailable','unvailable')])
    image_1920 = fields.Image(readonly=False, store=True)
    observer_street = fields.Char("street")
    observer_city = fields.Char("City")
    observer_street_number = fields.Integer("street number")
    observer_name = fields.Char(string="superobserver name")
    observer_job = fields.Many2one("hr.job",string="job")
    observer_phone = fields.Char(string="phone number")
    observer_email = fields.Char(string="email")
    observer_action = fields.Many2one("risk.action",string="select/create action")
    risk_description = fields.Text("risk description")
    observer_risk = fields.Many2one("risk.disaster",string="requested risk")
    observer_status = fields.Selection([('Accept','accept'),('Transfer to','transfer to')])
    observer_risk_information = fields.Text(string="actual information")
    availibility_status = fields.Selection([('Available','available'),('Unvailable','unvailable')])
    crisis_information = fields.Text("send crisis information")
    observer_category = fields.Selection([('External','external'),('Internal','internal')])
    apropriate_employee = fields.Many2one("hr.employee","transfer to")
    crisis_status = fields.Selection([('Draft','draft'),('Inprogress','inprogress'),('Closed','closed')],string="risk status")
    mission_status = fields.Selection([('Failed','failed'),('Sucess','sucess')])
    mission_type = fields.Selection([('People', 'people'), ('Facilities', 'facilities')
                                           , ('Systems', 'systems'), ('Equipment', 'equipment')
                                            , ('Materials', 'materials'),
                                         ('Supplies', 'supplies'),
                                         ('Funding', 'funding'), ('Information', 'information'),
                                         ('Public Emergency Service', 'public emergency service'),
                                         ('Logistics', 'logistics'),
                                         ('Communications And Warning Technologies',
                                          'Communications and warning technologies'),
                                         ('Fire protection and life safety systems',
                                          'fire protection and life safety systems'),
                                         ('Pollution control systems', 'pollution control systems'),
                                         ('Information about the threats or hazards',
                                          'information about the threats or hazards'),
                                         ('Special expertise', 'special expertise')])
    external_res = fields.Many2one("res.partner",string="transfer to external Ressource")


    def set_state_draft(self):
        if self.crisis_status == 'closed':
            self.crisis_status = 'draft'



    def set_state_inprogress(self):
        if self.crisis_status=='draft':
            self.crisis_status='inprogress'

    def set_state_closed(self):
        if self.crisis_status == "inprogress":
            self.crisis_status = "closed"



    @api.constrains('observer_email')
    def validate_mail(self):
        for rec in self:
            if rec.observer_email:
                match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                                 rec.observer_email)
                if match == None:
                    raise ValidationError('Not a valid E-mail')

    # def show_notification(self):
    #     notification = {
    #     'type': 'ir.actions.client',
    #     'tag': 'display_notification',
    #     'params': {
    #         'title': ('Your Custom Title'),
    #         'message': 'as a i accept to do the mission'+" "+str(self.action_name),
    #         'type': 'success',  # types: success,warning,danger,info
    #         'sticky': True,  # True/False will display for few seconds if false
    #     },
    # }
    #     return notification






























