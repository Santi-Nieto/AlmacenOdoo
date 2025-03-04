# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Modelo de Autor
class AlmacenCargo(models.Model):
    _name = 'almacen.cargo'
    _description = 'Trabajadores Almacenes del Condado S.L'
    _rec_name = 'cargo'

    cargo = fields.Selection(selection=[
            ('reponedor', 'Reponedor/a'),
            ('cajero', 'Cajero/a'),
            ('limpiador', 'Limpiador/a'),
            ('gerente', 'Gerente'),
            ('repartidor', 'Repartidor/a')
        ],
        string="Cargo",
        default='reponedor',
        required= True
    )

    salario = fields.Float(compute="_compute_salario", store=True)

    almacen = fields.Many2one('almacen.almacen', string="Almacen")

    trabajador = fields.One2many('almacen.trabajador', 'cargo', string="Trabajador")

    #Este computo depende de la variable cargo
    @api.depends('cargo')
    def _compute_salario(self):
        salario_dict = {
            'reponedor': 1200.0,
            'cajero': 1500.0,
            'limpiador': 1100.0,
            'gerente': 2500.0,
            'repartidor': 1400.0
        }
        for record in self:
            record.salario = salario_dict.get(record.cargo, 0.0)
    

    

    