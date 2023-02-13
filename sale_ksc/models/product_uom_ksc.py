from odoo import models, fields

class ProductUomKsc(models.Model):
    _name = "product.uom.ksc"
    _description = "Product UOM KSC"

    name = fields.Char(string="Name", required=True)
    category_id = fields.Many2one(
        comodel_name="product.uom.category.ksc", string="UOM Category")