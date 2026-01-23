# -*- coding: utf-8 -*-
{
    'name': 'Simple Timeline View (Calendar-based)',
    'version': '19.0.1.0.0',
    'category': 'Project',
    'summary': 'Add Timeline view for Projects and Tasks using Calendar in Odoo 19 Community',
    'description': """
        Simple Timeline View Module (Community Edition)
        ================================================
        This module adds timeline visualization for project tasks in Odoo 19 Community Edition.
        
        ⚠️ Note: True Gantt view is an Enterprise-only feature. This module provides
        a timeline alternative using the Community-available Calendar view.
        
        Features:
        ---------
        * Enhanced Calendar view for project tasks with timeline feel
        * Visual representation of task start and end dates
        * Color-coded by project
        * Graph view for task analysis
        * Works with Odoo 19 Community Edition (no Enterprise required)
        
        Usage:
        ------
        Go to Project > Tasks and click on the Calendar icon to see the timeline view.
    """,
    'author': 'Mahmuddin',
    'website': '',
    'license': 'LGPL-3',
    'depends': ['project', 'web'],
    'data': [
        'views/project_task_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'simple_gantt/static/src/css/timeline_view.css',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
