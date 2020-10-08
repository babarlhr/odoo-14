#from stdnum.mx.rfc import _get_date

from odoo import models, fields, api
import datetime
from odoo.tools.translate import _


class CustomStockProductionLot(models.Model):
    _inherit = "stock.production.lot"

    lot_name = fields.Char(string='Lot No.',  help="Lot Number")
    expiration_date = fields.Date()
    import_ref = fields.Char(string='Import Ref.')

class CustomStockPackOperation(models.Model):
    _inherit = "stock.move.line"

    lot_name = fields.Char(string='Lot No.', help="Lot Number")
    expiration_date=fields.Date()