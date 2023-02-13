{
    'name': 'Sale Ksc1',
    'version': '1.6',
    'category': 'Sale',
    'author': 'Avi Prajapati',
    'sequence': -100,
    'summary': 'This Is Sale Ksc',
    'description': "Sale Sale Sale",
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "views/product_category_ksc.xml",
        "views/product_ksc.xml",
        "views/product_uom_category_ksc.xml",
        "views/product_uom_ksc.xml",
        "views/res_partner_ksc.xml",
        "views/sale_order_ksc.xml",
        "views/sale_order_line_ksc.xml",
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}