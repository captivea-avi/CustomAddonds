from odoo import fields,models,api,exceptions

class CouponMaster(models.Model):

    _name = 'coupon.master'
    _description = 'Coupon Master'

    name = fields.Char(string='Coupon Code',size=8,required=1)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    value = fields.Monetary(string='Value')
    coupon_id = fields.Many2one('coupon.generator')
    generator_id = fields.Many2one('coupon.generator', string='Coupon Generator')
    currency_id = fields.Many2one('res.currency',defualt='get_default_currency')

    sql_constraints = [
        ('unique_name', 'unique(name)', 'Coupon code must be unique!')
    ]





