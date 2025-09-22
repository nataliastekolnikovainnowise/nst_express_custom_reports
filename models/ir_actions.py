from collections import defaultdict
from odoo import models
from odoo.exceptions import MissingError
from odoo.tools.misc import frozendict


class IrActionsActions(models.Model):
    _inherit = 'ir.actions.actions'

    def _get_bindings(self, model_name):
        """Override to sort reports by name instead of ID"""
        cr = self.env.cr
        result = defaultdict(list)
        
        self.env.flush_all()
        cr.execute("""
            SELECT a.id, a.type, a.binding_type, a.name
              FROM ir_actions a
              JOIN ir_model m ON a.binding_model_id = m.id
             WHERE m.model = %s
          ORDER BY a.name, a.id
        """, [model_name])
        
        for action_id, action_model, binding_type, name in cr.fetchall():
            try:
                action = self.env[action_model].sudo().browse(action_id)
                fields = ['name', 'binding_view_types']
                for field in ('groups_id', 'res_model', 'sequence', 'domain'):
                    if field in action._fields:
                        fields.append(field)
                action = action.read(fields)[0]
                if action.get('groups_id'):
                    groups = self.env['res.groups'].browse(action['groups_id'])
                    action['groups_id'] = list(groups._ensure_xml_id().values())
                if 'domain' in action and not action.get('domain'):
                    action.pop('domain')
                result[binding_type].append(frozendict(action))
            except (MissingError):
                continue
        
        return result
