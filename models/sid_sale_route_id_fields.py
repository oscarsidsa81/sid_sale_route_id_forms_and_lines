# -*- coding: utf-8 -*-
from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    route_block_oos = fields.Boolean(
        string='Ruta: no vender sin stock',
        related='route_id.do_not_sell_out_of_stock',
        store=True,  # necesario para poder filtrar/usar con decos sin problemas
        readonly=True,
        help="Campo relacionado con do_not_sell_out_of_stock que tiene como objetivo ver si es ubicación de stock o no",
    )
