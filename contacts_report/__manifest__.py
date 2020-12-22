# -*- coding: utf-8 -*-
{
    'name': "contact_report",
    'summary': """This Module will create report of selected contacts.""",
    'description': """This Module will create report of selected contacts.""",
    'author': "Aktiv Software",
    'website': "http://www.aktivsoftware.com",
    'category': 'Uncategorized',
    'version': '14.0.1.0.0',
    'depends': ['contacts'],
    'data': [
        # 'security/ir.model.access.csv',
        'reports/reports.xml',
        'reports/contact_detail_report.xml',
    ],
}
