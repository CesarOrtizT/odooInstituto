from odoo import models, fields, api
from odoo.exceptions import ValidationError

class curso(models.Model):
    _name = 'instituto.curso'
    _description = 'Curso'
    
    name = fields.Integer(string="Número del curso", required = True)

    grupos = fields.Many2many("instituto.grupo", string="Grupos")
     
    
    @api.constrains('name')
    def _check_name(self):
        for record in self:
            for grupo in record.grupos:
                if (grupo.curso != record.name):
                    raise ValidationError("No puede ser el número del curso distinto al del grupo.")