{
    'name': 'Customize Product',
    'version': '1.0',
    'category': 'Product',
    'summary': 'expands on the fundamental Odoo features for product customisation',
    'description': """
    expands the fields and features available in Odoo product templates.
    """,
    'author': 'Majemite James',
    'depends': ['base', 'product'],
    'data': [
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': True,
}
