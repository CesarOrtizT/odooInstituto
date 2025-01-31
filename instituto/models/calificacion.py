from odoo import models, fields

class calificacion(models.Model):
    _name = 'instituto.calificacion'
    _descripcion = 'instituto.calificacion'

    name = fields.Float(string="Nota", required=True)

    estudiantes = fields.Many2one("instituto.estudiante", string="Estudiante", required=True)

    asignatura = fields.Many2one("instituto.asignatura", string="Asignatura", required=True)
