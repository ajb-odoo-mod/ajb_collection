####################################################################### 
# Copyright (C) 2015 Romeo Abulencia # 
# Author: romeo abulencia <romeo.abulencia@gmail.com> 
# Maintainer: romeo abulencia <romeo.abulencia@gmail.com> # 
# This program is free software: you can redistribute it and/or modify 
# it under the terms of the GNU General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version. # 
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details. # 
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see <http://www.gnu.org/licenses/>. 
#######################################################################
import csv,json
#load file 
csv_file = open('Items.csv','r')
reader = csv.reader(csv_file)
current_customer_row=[]

column_headers=[]
target_data=[]

# Open Sales invoice importer
for row in reader:
    if row and row[0] == "Type":
        column_headers=row
    else:
        for h_count,header in enumerate(column_headers):
            if row[h_count]:
                current_customer_row.append((header,row[h_count]))
        if current_customer_row:
            target_data.append(dict(current_customer_row))
            current_customer_row=[]

for y in column_headers:
# for y in ['Telephone 2']:
    target_data_type=y
    data_values=[]
    for x in target_data:
        if target_data_type in x:
            if x[target_data_type] not in data_values:
                data_values.append(x[target_data_type])
                
    print 'target_data_type',target_data_type        
    print 'data_values',data_values
    
simple_data_export=
{'Sales Description': 'description_sale',
 'Foreign Cost 1': 'foreign_cost1',
 'Revenue/Income': 'revenue',
 'Foreign Cost 2': 'foreign_cost2',
 'Commodity code': 'commodity_code',
 'Unit Cost': 'standard_price',
 'Unit Price': 'list_price',
 'Number of units per box': 'units_per_box',
 'Price Impact': 'price_impact',
 'Minimum Order Quantity': 'minimum_order_quantity',
 'Supplier Part number/Code': 'supplier_part_number',
 'Barcode': 'ean13',
 'Print as single line (sales)': 'sales_single_line_print',
 'Re-order level': 'reorder_level',
#  'Serial Number': 'ean13?',
 'Shortfall': 'shortfall',
 'Amounts as percentage': 'amount_percentage',
 'Matrix Parent': 'matrix_parent',
 'On Purchase Orders': 'incoming_qty',
 'Average Lead Time': 'sale_delay',
 'Foreign Price 1': 'foreign_price1',
 'Foreign Price 2': 'foreign_price2',
 'Print as single line (purchasing)': 'purchasing_single_line_print',
 'Cart Mapping': 'cart_mapping',
 'Minimum Order Value': 'minimum_order_value',
 'Supplier Description': 'supplier_description',
 'On Sales Orders (Not Allocated)': 'qty_unallocated',
 'Item Code': 'default_code',
 'Is Matrix': 'matrix_ok',
 'Default Order Type': 'default_order_type',
 'Average Cost': 'average_price',
 'Shipping Instructions': 'shipping_notes',
 'Free Stock': 'qty_free',
 'On Hand': 'qty_available',
 'On Sales Orders (Allocated)': 'qty_allocated'}



    
function_needed_data={
'Item is Drop Shipped': 'drop_shipped', 
 'Category 2': 'category_line_ids', 
 'Category 3': 'category_line_ids', 
 'Category 1': 'category_line_ids', 
 'Asset': 'asset_id', 
 'Category 4': 'category_line_ids', 
 'Item is Sold': 'sale_ok', 
 'Type': 'type', 
 'Item is Purchased': 'purchase_ok', 
 'Pays Commission': 'pay_commission', 
 'Weigh Before Shipping': 'pack_separately', 
 'Attribute 3': 'attribute_line_ids', 
 'Attribute 2': 'attribute_line_ids', 
 'Attribute 1': 'attribute_line_ids', 
 'Attribute 6': 'attribute_line_ids', 
 'Attribute 5': 'attribute_line_ids', 
 'Attribute 4': 'attribute_line_ids', 
 'Dimension Units': 'volume', 
 'Purchase Units': 'uom_po_id', 
 'Item Class': 'item_class_id', 
 'Item is active?': 'active', 
 'Expense': 'expense_id', 
 'Available in Portal Cart': 'portal_cart', 
 'Weight': 'weight', 
 'Pack Separately': 'pack_seperately', 
 'Sales Units': 'uom_id', 
 'Image 1': 'image_ids', 
 'Image 2': 'image_ids', 
 'Image 3': 'image_ids', 
 'Image 4': 'image_ids', 
 'Use on Purchase Documents': 'use_on_purchase_document'
 }


# print 'column_headers'
# for x in column_headers: print x
# print json.dumps(target_data, sort_keys=True, indent=2)

#value orm write organizer
for data_count,datum in enumerate(target_data):
    orm_write_data={}
#     print 'datum',datum
    #HANDLES SIMPLE DATA EXPORT
    for datum_data_type in datum:
        if datum_data_type in simple_data_export:
            orm_write_data[simple_data_export[datum_data_type]]=datum[datum_data_type]

    #HANDLES DATA REQUIRING FUNCTIONS        