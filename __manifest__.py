# -*- coding: utf-8 -*-
{
    'name': "Almacenes del Condado S.L",

    'summary': "Almacenes del Condado S.L es una empresa dedicadas a la distribucion de consumible (alimentos, bebidas, productos de limpieza ...)",

    'description': """
Modulo para Almacenes del Condado S.L con varios modulos y facturas
    """,

    'author': "Santi Nieto",
    'website': "https://www.AlmacenesdelCondado.com",
    'application': True,
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
         
        'security/ir.model.access.csv',
        'views/library_views.xml',
        'report/report.xml',

    ]
}

