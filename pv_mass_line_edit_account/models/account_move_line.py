# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    apply_all = fields.Boolean(
        string="Apply to All",
        help="When enabled, changes on this line are propagated to other "
             "lines of the same document that also have this enabled.",
        default=False,
    )

    def write(self, vals):
        """
        Propagate edits made on a line with apply_all=True to sibling lines
        (same move_id) that also have apply_all=True. Avoid recursion via a
        context flag so we don't loop.
        """
        # Already propagating? do the normal write and stop.
        if self.env.context.get("mass_edit_propagation"):
            return super().write(vals)

        # Don't propagate when only toggling the flag itself.
        fields_to_push = {k: v for k, v in vals.items() if k != "apply_all"}
        if not fields_to_push:
            return super().write(vals)

        # Do the normal write first so constraints/computations run on the source.
        res = super(AccountMoveLine, self).write(vals)

        # Push to siblings per record edited.
        for line in self:
            if not line.apply_all or not line.move_id:
                continue

            siblings = self.search([
                ("move_id", "=", line.move_id.id),
                ("id", "!=", line.id),
                ("apply_all", "=", True),
            ])
            if siblings:
                siblings.with_context(mass_edit_propagation=True).write(fields_to_push)

        return res

    @api.onchange("apply_all")
    def _onchange_apply_all(self):
        # no-op; keep here if you later want UI side-effects.
        return
