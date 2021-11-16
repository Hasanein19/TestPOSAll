from odoo import fields, api, models


class ProductTemplate(models.Model):
    _inherit = 'stock_inventory'
    arabic_name = fields.Char('Arabic Name')


