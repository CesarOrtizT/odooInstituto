# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


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



     @api.constrains('hora_inicio', 'hora_fin')
     def _check_horario(self):
        for record in self:
            if record.hora_inicio >= record.hora_fin:
                raise ValidationError("La hora de inicio debe ser menor que la hora de fin.")
            


     @api.constrains('dia_semana', 'hora_inicio', 'hora_fin', 'asignatura')
     def _check_superposicion(self):
          for record in self:
               conflicto = self.env['instituto.horario'].search([
                    ('id', '!=', record.id),
                    ('dia_semana', '=', record.dia_semana),
                    ('asignatura', '=', record.asignatura.id),
                    ('hora_inicio', '<', record.hora_fin),
                    ('hora_fin', '>', record.hora_inicio),
               ])
          if conflicto:
            raise ValidationError("El horario se solapa con otra asignatura en el mismo día.")
          
     @api.depends('asignatura', 'dia_semana', 'hora_inicio','hora_fin')
     def _compute_name(self):
          for record in self:
               if record.asignatura and record.dia_semana:
                    dia_dict = dict(record._fields['dia_semana'].selection)
                    dia_nombre = dia_dict.get(record.dia_semana, "Desconocido")
                    record.name = f"{record.asignatura.name} - {dia_nombre} ({record.hora_inicio}) - ({record.hora_fin})"
               else:
                    record.name = "Nombre no disponible"
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
