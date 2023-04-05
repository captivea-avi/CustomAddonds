# -*- coding: utf-8 -*-
{
    "name": "coupon management",
    "version": "1.0.0",
    'author': "Avi Prajapati",
    "category": "",
    'summary': '',
    'sequence': -100,
    "description": """ 
    """,
    "price": 000,
    "currency": 'EUR',
    "depends": ['base'],
    "data": ["security/ir.model.access.csv",
             "reports/coupon_generator_report.xml",
             "reports/coupon_generator_report_template.xml",
             "views/coupon_generator.xml",
             "views/coupon_master.xml",

            ],
    "auto_install": False,
    "installable": True,
    "application": True,
    "license": 'LGPL-3',
}
