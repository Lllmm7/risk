from odoo import models,fields,api,_
from datetime import date, datetime
from odoo.exceptions import ValidationError

import _strptime




class RisksDisasterActions(models.Model):
    _name = "risk.action"
    _description = "risk Actions"


    #----------------------------------------
    #filelds--------------------------------
    #---------------------------------------
    risk_ids = fields.One2many(comodel_name="risk.disaster", inverse_name="risk_id"
    )
    risk_count=fields.Integer(compute="_compute_risk_count",string="risk count")
    useraction_id = fields.Many2one("res.users")
    action_id = fields.Many2one("risk.disaster",string="action_id",required=True)
    risk_owner = fields.Char(string="Owner",required=True)
    progress_action = fields.Float(string="action progress" ,default="20" )
    # action_category = fields.Char(string="Category action")
    action_source = fields.Selection([('external','External'),('internal','Internal')],string="Action source ",required=True)
    action_success = fields.Float(string="Sucess Pourcentage",default="20")
    action_description = fields.Text(string="description",required=True)
    action_status = fields.Selection([('draft','Draft'),('inprogress','Inprogress'),('closed','Closed')],string='action status',required=True)
    risk_owner = fields.Many2many("hr.employee",string="owner(s)",required=True)
    action_name = fields.Char(string="Action Name",required=True)
    # action_risk_name = fields.Char("risk name",compute="get_risk_name")
    action_risk = fields.Many2one("risk.disaster")
    action_category = fields.Selection([('naturels','Naturels'),('sanitaire','Santaire')
            ,('professionnels','Professionnels'),('psychosociaux','Psychosociaux')
            ,('technologiques','Technologiques'),
         ('numériques','Numériques'),('financier','Financier'),
         ('geographiques','Geographiques'),('géopolitique','Géopolitiques'),
         ('cimatique','climatique')],required=True)
    action_cause = fields.Many2many("risk.cause",required=True)
    action_start_date = fields.Date(string="action start datetime",required=True)
    action_end_date = fields.Date(string="action end Date",required=True)
    department_id = fields.Many2one("hr.department",required=True)
    # duration_date =  fields.Integer(string="action duration",compute="_duration_action",store=True)
    select_mission_int = fields.Char("select mission to external Ressource")
    select_mission_ext = fields.Char("select mission to internal Ressource")
    location = fields.Many2one("hr.work.location",required=True)
    emergency_degree=fields.Selection([('need for resuscitation','need for resuscitation'),('emergency','emergency'),('urgent','urgent'),('semi-urgent','semi-urgent'),('non-urgent','non-urgent')],string="emergency_level")
    ext_res_category = fields.Selection([('People', 'people'), ('Facilities', 'facilities')
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
                                         ('Special expertise', 'special expertise')],
                                        string="external ressource category")
    risk_status = fields.Selection([('draft','Draft'),('inprogress','Inprogress'),('closed','Closed')],string="risk status")
    availibilty=fields.Boolean("availibilty")
    employee_mission_available=fields.Boolean("CMS avalaiblity",compute="_check_availability")
    action_result = fields.Selection([('sucess','sucess'),('failed','failed')],string="action result")




#---------------------------------------------------
#methods--------------------------------------------
#---------------------------------------------------


    def set_state_draft(self):

        return self.write({'action_status': 'draft'})

    def set_state_inprogress(self):
        return self.write({'action_status': 'inprogress'})

    def set_state_closed(self):
        return self.write({'action_status': 'closed'})

    def set_state_risk_draft(self):

        return self.write({'risk_status': 'draft'})

    def set_state_risk_inprogress(self):
        return self.write({'risk_status': 'inprogress'})

    def set_state_risk_closed(self):
        return self.write({'risk_status': 'closed'})


    def test_url(self):
        if self.id:
            return {
                'type': 'ir.actions.act_url',
                'url': 'https://www.google.com/maps/@36.8712709,10.305536,14z=%s' % (self.id),
                'target': 'new',
            }



    def test_url_cantact(self):
        if self.id:
            return {
                'type': 'ir.actions.act_url',
                'url': 'http://0.0.0.0:8015/web#cids=1&menu_id=111&action=139&model=res.partner&view_type=list=%s' % (self.id),
                'target': 'new',
            }









    @api.depends("action_start_date", "action_end_date")
    def _check_date(self):
        for rec in self:
            if rec.action_start_date > rec.action_end_date:
                raise ValidationError(_('invalid field,End Date Must be greater Than Start Date...'))

    def _compute_risk_count(self):
        for risk in self:
            risk.risk_count = len(risk.risk_ids)
            print(risk.risk_count)






