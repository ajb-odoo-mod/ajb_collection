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
import oerplib,psycopg2
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

server = raw_input('Enter server:\n 1: http://188.165.45.213 or localhost') or 'localhost'
if server == '1':
    server = 'cgsyd01.carnacgroup.com'
dbuser='odoo_ajb'
dbpass='odoo_ajb'
port=8069
login_name='programmer@northdown.com.au'
password='Romeo1'
database = raw_input('Enter target database:\n 1: Northdown \n 2: Northdown_staging \n or ajb_live') or 'ajb_live'
if database == '1':
    database = 'Northdown'
    dbuser='bn_openerp'
    dbpass='df124428'
    port = 80
elif database == '2':
    database = 'Northdown_staging'
    dbuser='bn_openerp'
    dbpass='df124428'
    port = 80    
    
    
print 'server',server
print 'database',database
print 'port',port
print 'dbuser',dbuser
print 'dbpass',dbpass
oerp = oerplib.OERP(server=server, database=database, protocol='xmlrpc', port=port) 
conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (server,database,dbuser,dbpass) )

cr = conn.cursor() 
print 'login_name',login_name
print 'password',password
user = oerp.login(user=login_name, passwd=password)
uid = user.id
pool = oerp.get    
    
simple_data_export={
'Sales Description': 'description_sale',
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
 'Default Order Type': 'default_order_type',
 'Average Cost': 'average_price',
 'Shipping Instructions': 'shipping_notes',
 'Free Stock': 'qty_free',
 'On Hand': 'qty_available',
 'On Sales Orders (Allocated)': 'qty_allocated'}


boolean_data=[
 "Item is active?", 
 "Item is Sold", 
 "Item is Purchased", 
 "Is Matrix", 
 "Pays Commission", 
 "Use on Purchase Documents", 
 "Item is Drop Shipped", 
 "Pack Separately", 
 "Weigh Before Shipping", 
 "Available in Portal Cart"
]


    
function_needed_data={
'Item is Drop Shipped': 'drop_shipped', #boolean
 'Category 2': 'category_line_ids', 
 'Category 3': 'category_line_ids', 
 'Category 1': 'category_line_ids', 
 'Asset': 'asset_id', 
 'Category 4': 'category_line_ids', 
 'Item is Sold': 'sale_ok', #boolean
 'Type': 'type', 
 'Item is Purchased': 'purchase_ok',#boolean 
 'Pays Commission': 'pay_commission', #boolean
 'Weigh Before Shipping': 'pack_separately', #boolean
 'Attribute 3': 'attribute_line_ids', 
 'Attribute 2': 'attribute_line_ids', 
 'Attribute 1': 'attribute_line_ids', 
 'Attribute 6': 'attribute_line_ids', 
 'Attribute 5': 'attribute_line_ids', 
 'Attribute 4': 'attribute_line_ids', 
 'Dimension Units': 'volume', 
 'Purchase Units': 'uom_po_id', 
 'Item Class': 'item_class_id', 
 'Item is active?': 'active', #boolean
 'Expense': 'expense_id', 
 'Available in Portal Cart': 'portal_cart', #boolean
 'Weight': 'weight', 
 'Pack Separately': 'pack_seperately', #boolean
 'Sales Units': 'uom_id', 
 'Image 1': 'image_ids', 
 'Image 2': 'image_ids', 
 'Image 3': 'image_ids', 
 'Image 4': 'image_ids', 
 'Is Matrix': 'matrix_ok',#boolean 
 'Use on Purchase Documents': 'use_on_purchase_document'#boolean
 }


# print 'column_headers'
# for x in column_headers: print x
# print json.dumps(target_data, sort_keys=True, indent=2)

#value orm write organizer
for data_count,datum in enumerate(target_data):
    orm_write_data={}
    category_line_ids=[]
    attribute_line_ids=[]
#     print 'datum',datum
    #HANDLES SIMPLE DATA EXPORT
    for datum_data_type in datum:
        if datum_data_type in simple_data_export:
            if datum[datum_data_type] and datum[datum_data_type] not in ['None','0','0.00']:
                orm_write_data[simple_data_export[datum_data_type]]=datum[datum_data_type]

    #HANDLES DATA REQUIRING FUNCTIONS   
        #handles boolean data
        if datum_data_type in boolean_data:
            if datum[datum_data_type] == 'Y':
                orm_write_data[function_needed_data[datum_data_type]]=1
        elif datum_data_type in ['Category 1', 'Category 2', 'Category 3', 'Category 4']:
            #category_line_ids
            #product.category.line
            #name
            #type
            target_type=datum_data_type.split(' ')[1]
            target_name=datum[datum_data_type]
            category_data={'name':target_name,'type':target_type}
            target_category_id=pool('product.category.line').search([('name','=',target_name),('type','=',target_type)])
            if not target_category_id:
                target_category_id = pool('product.category.line').create(category_data)
            if isinstance(target_category_id,list):
                category_line_ids.extend(target_category_id)
            else:
                category_line_ids.append(target_category_id)
                
        elif datum_data_type == 'Asset':
            asset_data={'name':datum[datum_data_type]}
            target_asset_id=pool('product.asset').search([('name','=',datum[datum_data_type])])
            if not target_asset_id:
                target_asset_id=pool('product.asset').create(asset_data)
            if isinstance(target_asset_id,list):
                orm_write_data[function_needed_data[datum_data_type]]=target_asset_id[0]
            else:
                orm_write_data[function_needed_data[datum_data_type]]=target_asset_id
            
        elif datum_data_type=='Type':
            if datum[datum_data_type]=='Stock Item':
                orm_write_data[function_needed_data[datum_data_type]]='product'
                
        elif datum_data_type in ['Attribute 1', 'Attribute 2', 'Attribute 3', 'Attribute 4']:


            #attribute_line_ids
            #product.attribute.line
            #name
            #type
            target_type=datum_data_type.split(' ')[1]
            target_name=datum[datum_data_type]
            attribute_data={'name':target_name,'type':'select'}
            target_attribute_id=pool('product.attribute').search([('name','=',target_name),('type','=',target_type)])
            if not target_attribute_id:
                target_attribute_id = pool('product.attribute').create(attribute_data)
            if isinstance(target_attribute_id,list):
                attribute_line_ids.extend(target_attribute_id)
            else:
                attribute_line_ids.append(target_attribute_id)
                
        elif datum_data_type == 'Dimension Units':
            target_dimension_unit = datum[datum_data_type].lower()
            target_width = int(datum['Width'])
            target_height = int(datum['Height'])
            target_length = int(datum['Length'])
            orm_write_data[function_needed_data[datum_data_type]]=target_width*target_height*target_length*0.01
            
    if attribute_line_ids:
        orm_write_data['attribute_line_ids']=[(6,0,attribute_line_ids)]
    if category_line_ids:
        orm_write_data['category_line_ids']=[(6,0,category_line_ids)]
    print 'orm_write_data',orm_write_data
