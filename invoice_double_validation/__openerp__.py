# -*- encoding: utf-8 -*-
############################################################################
#    Module Writen For Odoo, Open Source Management Solution
#
#    Copyright (c) 2011 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
#    coded by: hugo@vauxoo.com
#    planned by: Nhomar Hernandez <nhomar@vauxoo.com>
############################################################################

{
    'name': 'Double validation in account_invoice',
    'version': '1.6',
    'author': 'Vauxoo',
    'category': '',
    'depends': [
        'account',
    ],
    'demo': [],
    'website': 'https://www.vauxoo.com',
    'data': [
        'security/two_validations_security.xml',
        'views/two_validations_invoice_view.xml',
    ],
    'test': [],
    'installable': True,
    'auto_install': False,
    'images': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
