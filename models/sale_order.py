# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    payment_provider_id = fields.Many2one('payment.provider', string='Payment Acquirer')
    payment_transaction_id = fields.Many2one('payment.transaction', string='Payment Transaction')
    count_transaction = fields.Integer(string='Count Transaction', compute='compute_count_transaction', store=True)
    payment_status = fields.Selection(related='payment_transaction_id.state', store=True, string='Payment Status')

    @api.depends('payment_transaction_id')
    def compute_count_transaction(self):
        for rec in self:
            rec.count_transaction = len(rec.payment_transaction_id)

    def action_view_transaction(self):
        action = {
            'name': _('Payment Transaction'),
            'type': 'ir.actions.act_window',
            'res_model': 'payment.transaction',
            'target': 'current',
        }
        payment_transaction_id = self.payment_transaction_id.ids
        if len(payment_transaction_id) == 1:
            action['res_id'] = payment_transaction_id[0]
            action['view_mode'] = 'form'
        else:
            action['view_mode'] = 'tree,form'
            action['domain'] = [('id', 'in', payment_transaction_id)]
        return action