#######################################################################
# AJB product template modifications
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
from openerp.osv import osv, fields


class product_category_line(osv.Model):
    _name="product.category.line"
    _columns = {
            'name':fields.char('Category', size=64, required=False, readonly=False),
            'type': fields.integer('Type number'), 
                    }
    
class product_item_class(osv.Model):
    _name="product.item.class"
    _columns = {
            'name':fields.char('Name', size=64, required=False, readonly=False),
                    }    
class product_images(osv.Model):
    _name="product.images"
    _columns = {
            'product_id':fields.many2one('product.template', 'Product', required=True),
            'priority':fields.integer('Priority'), 
            'name':fields.char('Name', size=64, required=False, readonly=False),
            'image':fields.binary('Image', filters=None), 
                    }    
    
class product_expense(osv.Model):
    _name="product.expense"
    _columns = {
            'name':fields.char('Name', size=64, required=False, readonly=False),
                    }    
    
#Product Template Inheritance
class product_template(osv.Model):
    _inherit="product.template"
    _name="product.template"
    _columns={
              'category_line_ids':fields.many2many('product.category.line', 'product_category_line_rel','product_id','category_id', 'Product Category'), 
              'item_class_id':fields.many2one('product.item.class', 'Product Class', required=False), 
              'image_ids':fields.one2many('product.images', 'product_id', 'Images', required=False),
              'expense_id':fields.many2one('product.expense', 'Expense', required=False),               
              }
    