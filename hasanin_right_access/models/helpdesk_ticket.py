from odoo import api, models, _
from odoo.exceptions import UserError, ValidationError
from odoo import tools


class IrActionsInherit(models.Model):
    _inherit = 'ir.actions.actions'

    @api.model
    @tools.ormcache('frozenset(self.env.user.groups_id.ids)', 'model_name')
    def get_bindings(self, model_name):
        result = super(IrActionsInherit, self).get_bindings(model_name)
        actions = result.get('action')
        for action in actions:
            if action.get('name') == 'Generate Pricelist':
                actions.remove(action)
                result.update({'action': actions})
        return result


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    @api.model
    def create(self, values):
        if values.get('stage_id', False) and values['stage_id'] is int:
            stage_id = self.env['helpdesk.stage'].browse(values['stage_id'])

            # Check if the current user has access to change ticket to closed stage
            if stage_id.is_close:
                if not self.env.user.has_group('hasanin_right_access.can_move_to_closed_helpdesk_stages'):
                    raise UserError(_("You are not allowed to change ticket to closed stage !!"))

        return super(HelpdeskTicket, self).create(values)

    def write(self, values):

        stage_id = False
        if values.get('stage_id'):
            stage_id = self.env['helpdesk.stage'].browse(values['stage_id'])
        else:
            return super(HelpdeskTicket, self).write(values)

        # Check if the current user has access to change ticket to closed stage
        if stage_id.is_close:
            if not self.env.user.has_group('hasanin_right_access.can_move_to_closed_helpdesk_stages'):
                raise UserError(_("You are not allowed to change ticket to closed stage !!"))

        # Check if the current user has access to change ticket stage.
        if not stage_id.is_close:
            if not self.env.user.has_group('hasanin_right_access.can_move_btw_helpdesk_stages'):
                raise UserError(_("You are not allowed to change ticket stage !!"))

        return super(HelpdeskTicket, self).write(values)
