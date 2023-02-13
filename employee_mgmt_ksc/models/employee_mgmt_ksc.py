from odoo import models, fields, api


class EmployeeDepartmentKsc(models.Model):
    _name = 'employee.department.ksc'
    _description = 'Employee Department'

    department_name = fields.Char(string='Department Name' , required=True)
    employees = fields.One2many(comodel_name='employee.ksc', inverse_name='department_id', string='Employees')
    department_manager = fields.Many2one(comodel_name='res.users', string='Department Manager')



class EmployeeDepartmentShiftKsc(models.Model):
    _name = 'employee.department.shift.ksc'
    _description = 'Employee Department Shift'
    _rec_name = 'shift'


    shift = fields.Selection([('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening'), ('night', 'Night')], string='Shift')
    employee_ids = fields.One2many(comodel_name='employee.ksc', inverse_name='shift_id')


class EmployeeKsc(models.Model):
    _name = 'employee.ksc'
    _description = 'Employee'


    name = fields.Char(string='Name of the Employee', required=True)
    department_id = fields.Many2one(comodel_name='employee.department.ksc', string='Department Name of the Employee',
                                    required=True)
    shift_id = fields.Many2one(comodel_name='employee.department.shift.ksc', string='Shift', required=True)
    job_position = fields.Char(string='Job Position of Employee')
    salary = fields.Float(string='Salary', digits=(6, 2))
    hire_date = fields.Date(string='Hire Date')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('transgender', 'Transgender')], string='Gender')
    job_type = fields.Selection([('permanent', 'Permanent'), ('ad_hoc', 'Ad Hoc')], string='Job Type')
    is_manager = fields.Boolean(string='Is Manager')
    manager_id = fields.Many2one(comodel_name='employee.ksc', string='Manager', readonly=True)
    related_user = fields.Many2one(comodel_name='res.users', string='Related User')
    employee_ids = fields.One2many(comodel_name='employee.ksc', inverse_name='manager_id', string='Employee IDs',
                                   readonly=True)
    increment_percentage = fields.Float(string='Increment Percentage', digits=(2, 2), groups='employee.group_employee')

