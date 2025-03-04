# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


# Modelo de Libro
class AlmacenAlmacen(models.Model):
    _name = 'almacen.almacen'
    _description = 'Almacenes de Almacenes del Condado'
    _rec_name = 'nombre'
    
    nombre = fields.Char()

    activo = fields.Boolean(default=True)

    ciudad = fields.Char()

    fecha = fields.Date(string="Fecha de Creacion")

    cargo = fields.One2many('almacen.cargo', 'almacen', string="Cargo")

    producto = fields.Many2many('almacen.producto')


    @api.constrains('fecha')
    def _check_fechas(self):
        hoy = date.today()
        for record in self:
            if record.fecha and record.fecha > hoy:
                raise ValidationError("La fecha no puede ser posterior a la de hoy")
  
