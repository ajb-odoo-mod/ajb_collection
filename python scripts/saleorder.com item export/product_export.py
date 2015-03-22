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
    
function_needed_data="""
function_needed_data=
Type,type
Item is active?,active
Item is Sold,sale_ok
Item is Purchased,purchase_ok
Sales Units,uom_id
Pays Commission,pay_commission
Purchase Units,uom_po_id
Use on Purchase Documents,use_on_purchase_document
Category 1,category_line_ids
Category 2,category_line_ids
Category 3,category_line_ids
Category 4,category_line_ids
Attribute 1,attribute_line_ids
Attribute 2,attribute_line_ids
Attribute 3,attribute_line_ids
Attribute 4,attribute_line_ids
Attribute 5,attribute_line_ids
Attribute 6,attribute_line_ids
Item Class,item_class_id
Image 1,image_ids
Image 2,image_ids
Image 3,image_ids
Image 4,image_ids
Item is Drop Shipped,drop_shipped
Pack Separately,pack_seperately
Weigh Before Shipping,pack_separately
Dimension Units,volume
Weight,weight
Asset,asset_id
Expense,expense_id
Available in Portal Cart
"""

# print 'column_headers'
# for x in column_headers: print x
# print json.dumps(target_data, sort_keys=True, indent=2)