from odoo import models, fields

class KscProduct(models.Model):
    _name = 'product.ksc'
    _description = 'KSC Product'

    name = fields.Char(string='Name', required=True)
    sku = fields.Char(string='SKU', required=True)
    weight = fields.Float(string='Weight', digits=(2, 2))
    length = fields.Float(string='Length', digits=(2, 2))
    volume = fields.Float(string='Volume', digits=(2, 2))
    width = fields.Float(string='Width', digits=(2, 2))
    barcode = fields.Char(string='Barcode')
    product_type = fields.Selection([
        ('storable', 'Storable'),
        ('consumable', 'Consumable'),
        ('service', 'Service')
    ], string='Product Type')
    sale_price = fields.Float(string='Sale Price', default=1.00, digits=(2, 2))
    cost_price = fields.Float(string='Cost Price', default=1.00, digits=(2, 2))
    category_id = fields.Many2one(comodel_name='product.category.ksc', string='Product Category')
    uom_id = fields.Many2one(comodel_name='product.uom.ksc', string='UOM')

