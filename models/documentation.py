# -*- coding: utf-8 -*-

from odoo import fields, models


class KadouaneDocumentation(models.Model):
    _name = 'kadouane.documentation'
    _description = 'Documentation'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    name = fields.Char(string="Description", required=True, tracking=True)
    file = fields.Binary(string="Fichier", attachment=True)
    file_filename = fields.Char(string="Nom du fichier")
    link = fields.Char(string="Lien", tracking=True)
    active = fields.Boolean(default=True)
