from odoo import models, fields

class ResPartnerKsc(models.Model):
    _name = 'res.partner.ksc'
    _description = 'Res Partner KSC'

    name = fields.Char(string='Name', required=True)
    street1 = fields.Char(string='Street 1')
    street2 = fields.Char(string='Street 2')
    country_id = fields.Many2one('res.country.ksc', string='Country')
    state_id = fields.Many2one('res.state.ksc', string='State')
    city_id = fields.Many2one('res.city.ksc', string='City')
    zip = fields.Char(string='Zip Code')
    email = fields.Char(string='Email')
    mobile = fields.Char(string='Mobile')
    phone = fields.Char(string='Phone')
    photo = fields.Binary(string='Photo')
    website = fields.Char(string='Website')
    active = fields.Boolean(string='Active', default=True)
    parent_id = fields.Many2one('res.partner.ksc', string='Parent Partner')
    child_ids = fields.One2many('res.partner.ksc', 'parent_id', string='Child Partners')
    address_type = fields.Selection([
        ('invoice', 'Invoice'),
        ('shipping', 'Shipping'),
        ('contact', 'Contact')
    ], string='Address Type')

