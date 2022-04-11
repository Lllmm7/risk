from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    message = fields.Char("message")


    def send_msg(self):


            return {
                'type': 'ir.actions.act_url',
                'url': "https://api.whatsapp.com/send?phone=" ,
                'target': 'self',
                'res_id': self.id,
            }