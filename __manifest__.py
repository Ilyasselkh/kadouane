# -*- coding: utf-8 -*-
{
    'name': "KAdouane",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','web'],

    # always loaded
    'data': [
    'security/security.xml',
    'security/ir.model.access.csv',

    'views/views.xml',
    'views/viewssupp.xml',
    'views/client.xml',
    'views/documentation.xml',
    'views/calendarexp.xml',
    'views/calendarImp.xml',
    'views/templates.xml',

    'data/kadouanesequ.xml',

    'reports/report.xml',
    'reports/order_transit.xml',
    'reports/order_transport.xml',
    'reports/order_transit_import.xml',
],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'kadouane/static/src/js/kadouane_calendar_drag.js',
            'kadouane/static/src/scss/kadouane_calendar.scss',
        ],
    },
}
