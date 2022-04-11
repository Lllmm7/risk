from odoo import models,fields,api,_
from datetime import date, datetime
from odoo.exceptions import ValidationError


class ExternalRessource(models.Model):
    _name = "external.ressource"
    _description = "select an external ressource"
    _inherit = "risk.disaster"


    #-----------------------------------
    #fields-----------------------------
    #-----------------------------------

    ext_res_name_id = fields.Many2one("risk.disaster")
    ext_res_name = fields.Char(string="external ressource")
    ext_res_category = fields.Selection([('People','people'),('Facilities','facilities')
            ,('Systems','systems'),('Equipment','equipment')
            ,('Materials','materials'),
         ('Supplies','supplies'),
         ('Funding','funding'),('Information','information'),
         ('Public Emergency Service','public emergency service'),('Logistics','logistics'),
        ('Communications And Warning Technologies','Communications and warning technologies'),
        ('Fire protection and life safety systems','fire protection and life safety systems'),
        ('Pollution control systems','pollution control systems'),
        ('Information about the threats or hazards','information about the threats or hazards'),
        ('Special expertise','special expertise')],string="external ressource category")

    # ext_res_category = fields.Many2one(string="risk.disaster")
    description  = fields.Text(string="descripe necessity")
    text_sms = fields.Char(string="phone camapny")
    text_sms_cordinator = fields.Char(string="ressource phone")
    location_campany_street =  fields.Char(string="street location")
    location_campany_street_number = fields.Char(string="street location number")
    location_campany_city = fields.Char(string="City")
    resource_phone = fields.Char(string="phone campany")
    ext_res_ref = fields.Many2one("risk.disaster")
    company_name = fields.Char("company name")
    availabilty = fields.Boolean('acitve')
    campany_phone = fields.Char("phone company")
    #------for very dangerous cases(natural disaster)
    #1 descripe risk and select category

    emergency_center_name = fields.Char("emergency")
    emergency_center_department = fields.Char("emergency category")
    emergency_degree = fields.Selection([('need for resuscitation','need for resuscitation'),('emergency','emergency'),('urgent','urgent'),('semi-urgent','semi-urgent'),('non-urgent','non-urgent')])
    # emergency_center_category = fields.Selection([])
    # emergency_center_cantact = fields.Text()
    # emergency_action_status=fields.Selection()
    #







