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
 
simple_data_export={}

file=open('/home/romeo/Desktop/Odoo Projects/AJB/python scripts/saleorder.com item export/column checklist.csv','r')
for count,x in enumerate(file.readlines()):
	if count != 0:
		temp=x.split(',')
		if temp[0] not in function_needed_data and temp[1] != 'y':
			if temp[3]:
				simple_data_export[temp[0]]=temp[3]
			elif temp[6]:
				simple_data_export[temp[0]]=temp[6]
			else:
				simple_data_export[temp[0]]=''

print str(simple_data_export).replace(',',',\n')
