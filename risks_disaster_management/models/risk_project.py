from odoo import models,fields,api,_

class RiskProject(models.Model):

    _name="risk.project"
    description="risk project incident"


    #----------------------
    #------fields---------

    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High')
    ], readonly=True, string="Priority")
    image = fields.Binary(string="incident image")
    incident_name = fields.Char(string="risk incident")
    incident_project = fields.Many2one("project.project",string="project")
    incident_description = fields.Text(string="incident description")
    assigned_to = fields.Many2one("hr.employee",string="assigned to")
    incident_stage = fields.Selection([('draft','Draft'),('inprogress','Inprogress'),('closed','Closed')])
    #--------------------------------------------------------
    #-------------------method-------------------------------
    #--------------------------------------------------------

    def set_inprogress(self):
        if self.incident_stage == 'draft':
            self.incident_stage = 'inprogress'

    def set_draft(self):
        if self.incident_stage == 'closed':
            self.incident_stage = 'draft'

    def set_closed(self):
        if self.incident_stage == "inprogress":
            self.incident_stage = "closed"


class ProjectTaskInherit(models.Model):
    _inherit="project.task"

    incident_name = fields.Char(string="risk incident")
    incident_project = fields.Many2one("project.project", string="project")
    incident_description = fields.Text(string="incident description")
    assigned_to = fields.Many2one("hr.employee", string="assigned to")
    incident_stage = fields.Selection([('draft', 'Draft'), ('inprogress', 'Inprogress'), ('closed', 'Closed')])





