from odoo import api, models, _
from odoo.exceptions import UserError, ValidationError


class ProjectTask(models.Model):
    _inherit = "project.task"



    @api.model
    def create(self, values):

        stage_id = self.env['project.task.type'].browse(values['stage_id'])

        # Check if the current user has access to change task to closed stage
        if stage_id.is_closed:
            if not self.env.user.has_group('hasanin_right_access.can_move_to_closed_stages'):
                raise UserError(_("You are not allowed to change task to closed stage !!"))

        # Check if the current user has access to change task stage.
        if not stage_id.is_closed:
            if not self.env.user.has_group('hasanin_right_access.can_move_btw_stages'):
                raise UserError(_("You are not allowed to change task stage !!"))

        return super(ProjectTask, self).create(values)

    def write(self, values):

        stage_id = False
        if values.get('stage_id'):
            stage_id = self.env['project.task.type'].browse(values['stage_id'])
        else:
            return super(ProjectTask, self).write(values)

        # Check if the current user has access to change task to closed stage
        if stage_id.is_closed:
            if not self.env.user.has_group('hasanin_right_access.can_move_to_closed_stages'):
                raise UserError(_("You are not allowed to change task to closed stage !!"))

        # Check if the current user has access to change task stage.
        if not stage_id.is_closed:
            if not self.env.user.has_group('hasanin_right_access.can_move_btw_stages'):
                raise UserError(_("You are not allowed to change task stage !!"))

        return super(ProjectTask, self).write(values)