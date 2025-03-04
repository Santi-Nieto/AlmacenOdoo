# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Modelo de Producto
class AlmacenProducto(models.Model):
    _name = 'almacen.producto'
    _description = 'Productos'
    _rec_name = 'producto'

    producto = fields.Char(required=True)
    codigo_barras = fields.Image(max_width= 200)
    estado = fields.Selection(selection=[
            ('activo', 'Activo'),
            ('inactivo', 'Inactivo')
            
        ],
        string="Estado",
        default='activo',
    )
    stock = fields.Integer()
    pedir = fields.Boolean(compute="_stock", store=True)

    almacen = fields.Many2many('almacen.almacen')


    #Este computo depende de la variable stock
    @api.depends('stock')
	#Funcion para calcular el valor de stock
    def _stock(self):
    	#Para cada registro
        for record in self:
        	#Si la stock es menor que 5, se considera poco stock y marca el booleano pedir
            if record.stock<5:
                record.pedir = True
            else:
            	record.pedir = False


    


