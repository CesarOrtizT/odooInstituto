from odoo import models, fields, api
from odoo.exceptions import ValidationError

class grupo(models.Model):
    _name = 'instituto.grupo'
    _descripcion = 'instituto.grupo'

    name = fields.Char(string="Grupo", required=True) #Añadir una restricción para que solo se añada 
    #una letra al campo

    tutor = fields.Many2one("instituto.profesor", string="Tutor")

    anio = fields.Integer(string="Año", required=True)

    estudiantes = fields.Many2many("instituto.estudiante", string="Estudiantes")

    curso = fields.Many2one("instituto.curso", string="Curso")


    @api.constrains('name')
    def comprobarDato(self):
        for record in self:
            if (record.name and len(record.name) > 1 ):
                    raise ValidationError("¡El grupo no puede contener más de una letra como identificador!")
