# -*- coding: utf-8 -*-
{
    'name': "SK odoo Sale Order Payment Status",
    'summary': """
        Sale Order Payment Status""",
    'description': """
        Sale Order Payment Status
            """,
    'author': 'Sritharan K',
    'company': 'SK Engineer',
    'maintainer': 'SK Engineer',
    'website': "https://www.skengineer.be",
    'category': 'Sales',
    'version': '17.1',
    'depends': ['base', 'sale', 'payment'],
    'data': [
        'security/ir.model.access.csv',

        'views/sale_order_view.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
    'images': [
        'static/description/status.png'
    ],
}
