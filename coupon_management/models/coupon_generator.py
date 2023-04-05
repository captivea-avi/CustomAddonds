from odoo import fields,models,api, exceptions

class CouponGenerator(models.Model):
    _name = 'coupon.generator'
    _description = 'Coupon Generator'

    name = fields.Char(string='Coupon Name')
    number_of_coupons = fields.Integer(string='Number of Coupons')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date', required=True)
    customer_ids = fields.Many2many('res.partner', string='Customers')
    coupon_ids = fields.One2many('coupon.master', 'coupon_id', string='Coupon Lines')
    total_value = fields.Monetary(string='Total_value', compute='_compute_total_value',
                                  currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', required=True,
                                  default=lambda self: self._default_currency_id())

    @api.depends('coupon_ids')
    def _compute_total_value(self):
        for coupon in self:
            coupon.total_value = sum(coupon.coupon_ids.mapped('value'))

    def action_generate_coupon_lines(self):
       pass

    def _default_currency_id(self):
        return self.env.user.company_id.currency_id




