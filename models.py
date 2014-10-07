# -*- coding: utf-8 -*-

from openerp import models, fields, api


class link(models.Model):
    _name = 'link.link'
    _rec_name = 'title'

    url = fields.Text(string='URL')
    title = fields.Char(string='Title', size=140)
    remark = fields.Char(string='Remark', size=140)
    is_public = fields.Boolean(string='public', help='public for all the users')
