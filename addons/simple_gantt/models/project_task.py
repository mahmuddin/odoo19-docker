# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    # Ensure we have date fields for timeline/gantt view
    planned_date_start = fields.Datetime(
        string='Start Date',
        default=fields.Datetime.now,
        tracking=True,
    )
    planned_date_end = fields.Datetime(
        string='End Date',
        tracking=True,
    )
    
    @api.onchange('planned_date_end')
    def _onchange_planned_date_end(self):
        """Sync date_deadline with planned_date_end"""
        if self.planned_date_end:
            self.date_deadline = fields.Datetime.to_datetime(self.planned_date_end).date()
    
    @api.model_create_multi
    def create(self, vals_list):
        """Ensure date_deadline is synced on create"""
        for vals in vals_list:
            if 'planned_date_end' in vals and not vals.get('date_deadline'):
                deadline = fields.Datetime.to_datetime(vals['planned_date_end']).date()
                vals['date_deadline'] = deadline
        return super(ProjectTask, self).create(vals_list)

    def write(self, vals):
        """Sync date_deadline on write if planned_date_end changes"""
        if 'planned_date_end' in vals and not vals.get('date_deadline'):
            deadline = fields.Datetime.to_datetime(vals['planned_date_end']).date()
            vals['date_deadline'] = deadline
        return super(ProjectTask, self).write(vals)
