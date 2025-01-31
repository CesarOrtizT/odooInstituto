# -*- coding: utf-8 -*-

from odoo import models, fields, api


class horario(models.Model):
     _name = 'instituto.horario'
     _description = 'instituto.horario'

     name = fields.Char(string = "Nombre", required = True)
     asignatura = fields.Many2one(comodel_name="instituto.asignatura", required = True)
     dia_semana = fields.Selection([
        ('0', 'Lunes'),
        ('1', 'Martes'),
        ('2', 'Miércoles'),
        ('3', 'Jueves'),
        ('4', 'Viernes')
    ], string="Día de la Semana", default='0') #default selecciona un día de la semana válido
     
     hora_inicio = fields.Float(string="Hora de inicio", required = True)
     hora_fin = fields.Float(string="Hora de inicio", required = True)
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
