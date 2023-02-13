from odoo import models, fields, api

class SaleOrderLineKSC(models.Model):
    _name = 'sale.order.line.ksc'
    _description = 'Sale Order Line KSC'

    order_id = fields.Many2one('sale.order.ksc', string='Order No', required=True)
    product = fields.Many2one('product.ksc', string='Product', required=True)
    name = fields.Text(string='Description', required=True)
    quantity = fields.Float(string='Quantity', digits=(6,2), required=True)
    unit_price = fields.Float(string='Unit Price', digits=(6,2), required=True)
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='draft', string='State')
    uom_id = fields.Many2one('product.uom.ksc', string='Unit of Measure', required=True)
