# -*- coding: utf-8 -*-

from odoo import models, fields, api
from . import almacen_cargo

# Modelo de Autor
class AlmacenTrabajador(models.Model):
    _name = 'almacen.trabajador'
    _description = 'Trabajadores Almacenes del Condado S.L'
    _rec_name = 'nombre'

    nombre = fields.Char(required=True)
    apellidos = fields.Char()
    dni = fields.Char()
    telefono = fields.Char()
    email = fields.Char()


    cargo = fields.Many2one('almacen.cargo', string="Cargo", readonly=True)


    salario = fields.Float(compute="_compute_salario", store=True)

    
    @api.depends('cargo.salario')
    def _compute_salario(self):
        for record in self:
            if record.cargo:
                record.salario = record.cargo.salario  # Obtener salario desde el cargo
            else:
                record.salario = 0.0  # Si no tiene cargo asignado



    