from odoo.tests.common import TransactionCase

class TestProductTemplate(TransactionCase):

    def test_additional_barcode_unique(self):
        product_template = self.env['product.template'].create({
            'name': 'Test Product',
            'additional_barcode': '1234567890'
        })
        with self.assertRaises(ValidationError):
            self.env['product.template'].create({
                'name': 'Test Product 2',
                'additional_barcode': '1234567890'
            })
