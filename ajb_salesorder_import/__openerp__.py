#######################################################################
# AJB salesorder import modifications
# Copyright (C) 2015 Romeo Abulencia #
# Author: romeo abulencia <romeo.abulencia@gmail.com>
# Maintainer: romeo abulencia <romeo.abulencia@gmail.com> #
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. # # This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details. #
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>. 
#######################################################################


{
    'name': 'Salesorder.com Import Modifications',
    'version': '1.0',
    'category': 'Tools',
    'description': """
Sales Module Modification
    """,
    'author': 'Romeo Abulencia',
    'depends': ['base','crm_profiling'],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'res_partner_view.xml',
        'product_template_view.xml',

    ],
    'installable': True,
    'auto_install': False,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
