# -*- coding: utf-8 -*-
##############################################################################

#    For Module Support : developerhasanein@gmail.com
#
##############################################################################

{
    'name': 'Hide Delete Button', 
    'version': '14.0.1.0',
    'sequence': 1, 
    'category': 'Tools', 
    'description': 
        """ 
         Hide Duplicate. disable duplicate button , disbale delete
This Odoo application will hide Delete option from the all the records of the odoo. So once this application is installed, nobody can Delete any record of odoo(except some authenticated users)

Delete option will be hidden for all the records of odoo
Only user with Access Delete right can duplicate records

Delete option of odoo
Remove Delete access from the user
Delete option is hidden now

odoo appp Hide delete button from action. hide delete, delete buttton hide, hide delete button, hide delete action, hide delete, delete hide button, hide delete action, action delete hide, disable delete, delete disable, delete hide

    """,
    'summary': 'odoo appp Hide delete button from action. hide delete, delete buttton hide, hide delete button, hide delete action, hide delete, delete hide button, hide delete action, action delete hide, disable delete, delete disable, delete hide',
    'depends': ['web'],
    'data': [
        'security/security.xml',
        'views/assets.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    
    # author and support Details =============#
    'author': 'Hasanein Abusadah',
    'website': 'http://www.https://mt-sys.online/',
    'maintainer': 'MTS',
    'support': 'developerhasanein@gmail.com',
    'price':50.0,
    'currency':'SAR',
    #'live_test_url':'https://youtu.be/A5kEBboAh_k',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
