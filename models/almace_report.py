# -*- coding: utf-8 -*-

from odoo import models, api

class AlmacenTrabajadorReport(models.AbstractModel):
    _name = 'report.almacen.trabajador_report'
    _description = 'Reporte de Trabajadores'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['almacen.trabajador'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'almacen.trabajador',
            'docs': docs,
        }