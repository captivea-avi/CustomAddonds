from odoo import models, fields, api

class SaleOrderKSC(models.Model):
    _name = 'sale.order.ksc'
    _description = 'Sale Order KSC'

    name = fields.Char(string='Order No', required=True)
    customer = fields.Many2one(comodel_name='res.partner.ksc', string='Customer', required=True, domain=[('parent_id', '=', False)])
    invoice_customer = fields.Many2one(comodel_name='res.partner.ksc', string='Invoice Customer', required=True, domain=[('address_type', '=', 'invoice')])
    shipping_customer = fields.Many2one(comodel_name='res.partner.ksc', string='Shipping Customer', required=True, domain=[('address_type', '=', 'shipping')])
    sale_order_date = fields.Date(string='Sale Order Date')
    order_line = fields.One2many(comodel_name='sale.order.line.ksc', inverse_name='order_id', string='Order Line')
    salesperson = fields.Many2one(comodel_name='res.users', string='Salesperson')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string='State', default='draft')

    # @api.onchange('customer_id')
    # def _onchange_customer_id(self):
    #     self.invoice_customer_id = False
    #     self.shipping_customer_id = False
    #
    # def action_confirm(self):
    #     self.state = 'confirmed'
    #
    # def action_done(self):
    #     self.state = 'done'
    #
    # def action_cancel(self):
    #     self.state = 'cancelled'
    #
    # def action_draft(self):
    #     self.state = 'draft'
