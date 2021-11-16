from odoo import fields, api, models


class ProductTemplate(models.Model):
    _inherit = 'stock_inventory_line'
    arabic_name = fields.Char('Arabic Name')


