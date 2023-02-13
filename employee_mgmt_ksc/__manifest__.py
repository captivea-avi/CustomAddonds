{
    'name': 'Employee Department Ksc',
    'version': '1.6',
    'category': 'Employee Department',
    'author': 'Avi Prajapati',
    'sequence': -100,
    'summary': 'Employee Department',
    'description': "This Is Employee Department",
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "views/employee_department_ksc.xml",
        "views/employee_department_shift_ksc.xml",
        "views/employee_Ksc.xml",
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}