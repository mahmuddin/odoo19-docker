{
    "name": "Project Subtask JS Fix",
    "version": "19.0.1.0.0",
    "summary": "Workaround to avoid SubtaskListRenderer 'dirty' JS error",
    "description": """
Project Subtask JS Fix
======================

Small technical module that patches the SubtaskListRenderer used on the
Project task Sub-tasks tab. It wraps the onCellKeydownEditMode method in a
try/except to ignore the specific 'reading \\'dirty\\'' TypeError that occurs
when creating/editing subtasks inline.

This is a *temporary* workaround until the upstream bug is fixed.
""",
    "author": "Mahmuddin / ChatGPT",
    "website": "https://localhost",
    "license": "LGPL-3",
    "category": "Project",
    "depends": ["project"],
    "data": [],
    "assets": {
        "web.assets_backend": [
            "project_subtask_fix/static/src/js/subtask_fix.js",
        ],
    },
    "installable": True,
    "application": False,
}

