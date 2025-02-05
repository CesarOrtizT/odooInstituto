from odoo import models, fields

class calificacion(models.Model):
    _name = 'instituto.calificacion'
    _descripcion = 'instituto.calificacion'

    name = fields.Float(string="Nota", required=True)

    estudiantes = fields.Many2one("instituto.estudiante", string="Estudiante", required=True)

    asignatura = fields.Many2one("instituto.asignatura", string="Asignatura", required=True)


### COMPROBAR QUE NO HAY DOS CALIFICACIONES CON EL MISMO ESTUDIANTE Y ASIGNATURA

### SI SE SELECCIONA ESTUDIANTE QUE SÓLO PUEDAN SALIR SUS ASIGNATURAS

### SI SE SELECCIONA UNA ASIGNATURA QUE SÓLO SALGAN SUS ESTUDIANTES