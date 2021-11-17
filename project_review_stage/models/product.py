from odoo import fields, api, models


class helpdeskstage(models.Model):
    _inherit = 'helpdesk.stage'
    Review_stage =  is_closed = fields.Boolean('Review stage', help="Tasks in this stage are considered as Review.")


