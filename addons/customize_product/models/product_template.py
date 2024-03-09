from odoo import models, fields, api
from odoo.exceptions import ValidationError
from slugify import slugify

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    slug = fields.Char(string='Slug', compute='_compute_slug', store=True)
    additional_barcode = fields.Char(string='Additional Barcode', unique=True)

    @api.depends('name')
    def _compute_slug(self):
        for record in self:
            record.slug = slugify(record.name)

    @api.constrains('additional_barcode')
    def _check_unique_additional_barcode(self):
        for record in self:
            if self.search_count([('additional_barcode', '=', record.additional_barcode)]) > 1:
                raise ValidationError("Additional barcode must be unique!")
