from odoo import models, fields, api

class profesor(models.Model):
    _name = 'instituto.profesor'
    _description = 'Profesor'
    
    name = fields.Char(string = "DNI", required = True)
    
    nombre = fields.Char(string = "Nombre", required = True)
    
    apellido = fields.Char(string = "Apellido", required = True)
    
    fechaNac = fields.Date(string = "Fecha de nacimiento", required = True)
    
    direccion = fields.Char(string = "Dirección", required = True)
    
    telefono = fields.Char(string = "Teléfono", required = True)
    
    # Hacer un widget para que la imagen se muestre en el formulario
    
    fotoProfesor = fields.Char(string="Image URL")

    foto = fields.Boolean(string="Is Image URL Set", compute="_compute_foto")
      
    especialidad = fields.Char(string = "Especialidad", required = True)

# Añadido un comentario random
    @api.depends('fotoProfesor')
    def _compute_foto(self):
        for record in self:
            record.foto = True if record.fotoProfesor else False
    