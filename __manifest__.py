# -*- coding: utf-8 -*-
{
    'name': "Agodoo Sale Order Payment Status",
    'summary': """
        Sale Order Payment Status""",
    'description': """
        Sale Order Payment Status
            """,
    'author': 'Aadhav Group',
    'company': 'Aadhav Group',
    'maintainer': 'Aadhav Group',
    'website': "https://www.aadhavgroup.com/",
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
