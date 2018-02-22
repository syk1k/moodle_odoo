# -*- coding: utf-8 -*-
{
    'name': "Moodle",

    'summary': """
        Module that allows connection to Moodle from Odoo v11.
        """,

    'description': """
        This module makes Moodle management possible from Odoo v11 and easier.
    """,

    'author': "Kalamar",
    'website': "http://www.kalamar.tg",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',
    'application':True,
    'installable':True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/moodle_class.xml',
        'views/moodle_menus.xml',
        'views/wizard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}