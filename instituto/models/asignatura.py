# -*- coding: utf-8 -*-

from odoo import models, fields, api


class asignatura(models.Model):
     _name = 'instituto.asignatura'
     _description = 'instituto.asignatura'

     name = fields.Char(string = "Nombre", required = True)
     # grupo = fields.Many2one()
     curso = fields.Many2one("instituto.curso", string="Curso", required=True)
     estudiantes = fields.Many2many("instituto.estudiante", string="Estudiante", required=True)
     
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
