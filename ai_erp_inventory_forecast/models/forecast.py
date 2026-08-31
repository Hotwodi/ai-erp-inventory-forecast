from odoo import models, fields


class InventoryForecast(models.Model):
    _name = 'ai.erp.inventory.forecast'
    _description = 'AI Inventory Forecast'
    _order = 'sequence, id'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
    note = fields.Text(string='Notes')
