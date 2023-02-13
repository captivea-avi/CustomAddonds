from odoo import models, fields

class ProductCategoryKSC(models.Model):
    _name = 'product.category.ksc'
    _description = 'Product Category KSC'

    name = fields.Char(string='Name', required=True)
    parent_id = fields.Many2one('product.category.ksc', string='Parent Category')

