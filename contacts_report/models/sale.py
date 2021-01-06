from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order'

    product_id = fields.Many2one('product.product', string='Product')
    qty = fields.Integer(string='Quantity', default=1)

    @api.onchange('product_id')
    def onchange_product_qty(self):
        flag = False
        for rec in self:
            if rec.product_id:
                if not rec.order_line:
                    print("\n\n\n----111111111111111=====")
                    rec.write({
                        'order_line': [
                            (0, 0, {
                                'product_id': rec.product_id.id,
                                'product_uom_qty': rec.qty
                            }
                            ),
                        ]
                    })
                else:
                    for sol in rec.order_line:
                        if sol.product_id.id == rec.product_id.id:
                            print("\n\n\n----ifififififif=====")
                            sol.product_uom_qty += rec.qty
                            flag = True

                    if flag is not True:
                        rec.write({
                            'order_line': [
                                (0, 0, {
                                    'product_id': rec.product_id.id,
                                    'product_uom_qty': rec.qty
                                }
                                ),
                            ]
                        })
