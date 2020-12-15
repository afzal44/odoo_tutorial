# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'
    _description = "Wizard: Quick Registration of Attendees to Sessions"

    def _default_sessions(self):
        return self.env['openacademy.session'].browse(self._context.get('active_ids'))

    def _default_session(self):
        return self.env['openacademy.session'].browse(self._context.get('active_id'))

    session_ids = fields.Many2one('openacademy.session',
        string="Session", required=True, default=_default_session)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids

        return {}

