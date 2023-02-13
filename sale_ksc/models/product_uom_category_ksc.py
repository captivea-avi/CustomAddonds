from odoo import models, fields

class ProductUomCategoryKsc(models.Model):
    _name = 'product.uom.category.ksc'

    name = fields.Char(string="Name", required=True)
    uom_ids = fields.One2many('product.uom.ksc', 'category_id', string="Units of Measure")