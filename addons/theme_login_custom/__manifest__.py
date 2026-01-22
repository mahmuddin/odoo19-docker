{
    'name': 'Custom Login Theme (theme_login_custom)',
    'version': '1.0',
    'summary': 'Custom background and welcome message for login page',
    'description': """
        Customizes the Odoo login page with:
        - A custom background
        - A "Welcome to Odoo 19" message
    """,
    'category': 'Theme/Hidden',
    'author': 'Your Name',
    'depends': ['web'],
    'application': True,
    'data': [
        'views/login_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'theme_login_custom/static/src/css/login_custom.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
