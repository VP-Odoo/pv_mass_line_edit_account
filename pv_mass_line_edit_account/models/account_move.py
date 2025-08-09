# -*- coding: utf-8 -*-
from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = "account.move"

    select_all_lines = fields.Boolean(
        string="Select All Journal Items",
        help="Check to select/deselect all lines below",
    )

    @api.onchange('select_all_lines')
    def _onchange_select_all_lines(self):
        for move in self:
            # propagate to all lines
            for line in move.line_ids:
                line.apply_all = move.select_all_lines
