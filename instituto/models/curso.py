from odoo import models, fields, api

class curso(models.Model):
    _name = 'instituto.curso'
    _description = 'Curso'
    
    name = fields.Integer(string="Número del curso", required = True)

    grupos = fields.Many2many("instituto.grupo", string="Grupos")