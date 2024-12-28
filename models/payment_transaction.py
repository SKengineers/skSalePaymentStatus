# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    @api.model_create_multi
    def create(self, values_list):
        res = super(PaymentTransaction, self).create(values_list)
        for rec in res:
            for sale in rec.sale_order_ids:
                sale.payment_provider_id = rec.provider_id and rec.provider_id.id or False,
                sale.payment_transaction_id = rec.id
        return res