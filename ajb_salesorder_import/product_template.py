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
            'name':fields.char('Images', size=64, required=False, readonly=False),
            'image':fields.binary('Image', filters=None), 
                    }    
    
class product_expense(osv.Model):
    _name="product.expense"
    _columns = {
            'name':fields.char('Name', size=64, required=False, readonly=False),
                    }    

class product_asset(osv.Model):
    _name="product.asset"
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
              'asset_id':fields.many2one('product.asset','Asset'),
              
              'sales_single_line_print':fields.char('Print as single line (sales)',size=64),
              'purchasing_single_line_print':fields.char('Print as single line (purchasing)',size=64),
              'matrix_parent':fields.char('Matrix Parent',size=64),
              'matrix_ok':fields.boolean('Is matrix'),
              'commodity_code':fields.char('Commodity Code',size=64),
              'amount_percentage':fields.char('Ammounts as percentage',size=64),
              'foreign_price1':fields.float('Foreign Price 1',digits=(16,2)),
              'foreign_price2':fields.float('Foreign Price 2',digits=(16,2)),
              'pay_commission':fields.boolean('Pays Commission'),
              'foreign_cost1':fields.float('Foreign Cost 1',digits=(16,2)),
              'foreign_cost2':fields.float('Foreign Cost 2',digits=(16,2)),
              'qty_allocated':fields.integer('On Sales Orders (Allocated)'),
              'qty_free':fields.integer('Free Stock'),
              'qty_unallocated':fields.integer('On Sales Orders (Not Allocated)'),
              'shortfall':fields.float('Shortfall',digits=(16,2)),
              'supplier_part_number':fields.char('Supplier Part number/Code'),
              'supplier_description':fields.char('Supplier Description'),
              'use_on_purchase_document':fields.char('Use on Purchase Documents',size=64),
              'default_order_type':fields.char('Default Order Type',size=64),
              'reorder_level':fields.integer('Re-order Level'),
              'minimum_order_value':fields.float('Minimum Order Value',digits=(16,2)),
              'minimum_order_quantity':fields.integer('Minimum Order Quantity'),
              'drop_shipped':fields.boolean('Item is Drop Shipped'),
              'pack_seperately':fields.boolean('Pack Separately'),
              'weigh_before_shipping':fields.boolean('Weigh Before Shipping'),
              'units_per_box':fields.integer('Number of units per box'),
              'shipping_notes':fields.char('Shipping Instructions',size=64),
              'revenue':fields.char('Revenue/Income',size=64),
              'portal_cart':fields.boolean('Available in Portal Cart'),
              'cart_mapping':fields.char('Cart Mapping',size=64),
              'price_impact':fields.char('Price Impact',size=64),
                          
              }
    