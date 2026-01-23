# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    # Ensure we have date fields for timeline/gantt view
    date_start = fields.Datetime(
        string='Start Date',
        default=fields.Datetime.now,
        tracking=True,
    )
    date_end = fields.Datetime(
        string='End Date',
        tracking=True,
    )
    
    @api.onchange('date_end')
    def _onchange_date_end(self):
        """Sync date_deadline with date_end"""
        if self.date_end:
            self.date_deadline = fields.Datetime.to_datetime(self.date_end).date()
    
    @api.model_create_multi
    def create(self, vals_list):
        """Ensure date_deadline is synced on create"""
        for vals in vals_list:
            if 'date_end' in vals and not vals.get('date_deadline'):
                deadline = fields.Datetime.to_datetime(vals['date_end']).date()
                vals['date_deadline'] = deadline
        return super(ProjectTask, self).create(vals_list)

    def write(self, vals):
        """Sync date_deadline on write if date_end changes"""
        if 'date_end' in vals and not vals.get('date_deadline'):
            deadline = fields.Datetime.to_datetime(vals['date_end']).date()
            vals['date_deadline'] = deadline
        return super(ProjectTask, self).write(vals)
