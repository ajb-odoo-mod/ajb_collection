import json

a="""Type,customer,call_function
Customer Name,name
Ref #,salesorder_ref
Owner,user_id,call_function
Currency
First Name,first_name
Address Line 1,street
Town/City,city
State/Province,state_id,call_function
Country,country_id,call_function
Post/Zip code,zip
Contact Type
Telephone 1,phone
E-mail,email
Is Active,active,call_function
Customer since,customer_since_date
Enable login,login
Login ID
Password
Terms,comment
Price List,property_product_pricelist,call_function
Ship via,property_delivery_carrier,call_function
Payment Processor
Class 1,class_1
Class 2,class_2
Class 3,class_3
Balance,balance
Address Line 2,street2
Price Level
Map (www link)
Telephone 2,phone2
Last Name,last_name
Gender,gender
Mobile,mobile
County,country_id,call_function
Assistant,assistant_name
Assistant Phone,assistant_phone
Fax,fax
Website,website
Enable Portal Shopping Cart
Title,title,call_function
Job Title,job_title_id,call_function"""

disregarded_data=[]
function_needed_data=[]
simple_data_export=[]

for x in a.split('\n'):
	tmp = x.split(',')
	if len(tmp) == 1:
		disregarded_data.append(x)
	elif len(tmp)==3 and tmp[2] == 'call_function':
		function_needed_data.append([tmp[0],tmp[1]])
	else:
		simple_data_export.append(tmp)


print 'disregarded_data',json.dumps(disregarded_data, sort_keys=True, indent=2)
print 'function_needed_data',json.dumps(function_needed_data, sort_keys=True, indent=2)
print 'simple_data_export',json.dumps(simple_data_export, sort_keys=True, indent=2)
