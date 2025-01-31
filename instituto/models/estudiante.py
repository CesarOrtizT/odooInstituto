from odoo import models, fields,api

class estudiante(models.Model):
    _name = 'instituto.estudiante'
    _description = 'instituto.estudiante'

    name = fields.Char(string="Dni", required=True)

    nombre = fields.Char(string="Nombre", required = True)
    
    apellido = fields.Char(string="Apellido", required = True)
    
    fechaNac = fields.Date(string="Fecha nacimiento", required = True)
    
    direccion = fields.Char(string="Dirección", required = True)
    
    telefono = fields.Char(string="Teléfono", required = True)
    
    foto = fields.Image(string="Imagen", compute="_compute_foto") 
    
    fotoAlumno = fields.Char(string="Image URL")

    email = fields.Char(string="Email")
    
    asignatura = fields.Many2many("instituto.asignatura", string="Asignaturas")
    
    calificaciones = fields.One2many("instituto.calificacion", "estudiantes", string="Calificaciones")

    grupo = fields.Many2one("instituto.grupo", string="Grupo")

    curso = fields.Many2one("instituto.curso", string="Curso")


    @api.depends('fotoAlumno')
    def _compute_foto(self):
        for record in self:
            record.foto = True if record.fotoAlumno else False