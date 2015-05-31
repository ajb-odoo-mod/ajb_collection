#######################################################################
# AJB Sales module modification
# Copyright (C) 2013 Romeo Abulencia #
# Author: romeo abulencia <romeo.abulencia@gmail.com>
# Maintainer: romeo abulencia <romeo.abulencia@gmail.com> #
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. # # This program is distributed in the hope that it will be useful, # but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details. #
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>. 
#######################################################################


{
    'name': 'Sales Modification',
    'version': '1.0',
    'category': 'Tools',
    'description': """
Sales Module Modification
    """,
    'author': 'Romeo Abulencia',
    'depends': ['sale','warning','account'],
    'demo': [],
    'data': [
        'sale_view.xml',
        'account_invoice_view.xml',

    ],
    'installable': True,
    'auto_install': False,
}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
