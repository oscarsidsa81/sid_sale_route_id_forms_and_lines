{
    'name': 'sid_sale_route_id_forms_and_lines',
    'version': '1.0',
    'category': 'Sales',
    'license': 'AGPL-3',
    'summary': 'Campos en vista tree y form para visualizar las líneas de factura por línea en form y line',
    'description': 'Campos en vista tree y form para visualizar las líneas de factura por línea en form y line',
    'author': 'oscarsidsa81',
    'depends': ['base','crm','sale_crm','sale_management','stock','oct_confrm_access_sale_order','oct_sale_order_by_line'],
    'data': [
        'views/sid_sale_route_id_forms_and_lines.xml'
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
}