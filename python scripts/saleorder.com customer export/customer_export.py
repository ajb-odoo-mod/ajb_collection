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
import datetime
import oerplib
import psycopg2
#load file 
csv_file = open('Customers.csv','r')
reader = csv.reader(csv_file)
current_customer_row=[]

column_headers=[]
target_data=[]
used_column_headers=['Type', 'Customer Name', 'Ref #', 'Owner', 'Currency', 'First Name', 'Address Line 1', 'Town/City', 'State/Province', 'Country', 'Post/Zip code', 'Contact Type', 'Telephone 1', 'E-mail', 'Is Active', 'Customer since', 'Enable login', 'Login ID', 'Password', 'Terms', 'Price List', 'Ship via', 'Payment Processor', 'Class 1', 'Class 2', 'Class 3', 'Balance', 'Address Line 2', 'Price Level', 'Map (www link)', 'Telephone 2', 'Last Name', 'Gender', 'Mobile', 'County', 'Assistant', 'Assistant Phone', 'Fax', 'Website', 'Enable Portal Shopping Cart', 'Title', 'Job Title']


disregarded_data = [
  "Currency", 
  "Contact Type", 
  "Login ID", 
  "Password", 
  "Payment Processor", 
  "Price Level", 
  "Map (www link)", 
  "Enable Portal Shopping Cart"
  "County"
]

simple_data_export = {
 "Address Line 1": "street", 
 "Address Line 2": "street2", 
 "Assistant": "assistant_name", 
 "Assistant Phone": "assistant_phone", 
 "Balance": "balance", 
 "Class 1": "class_1", 
 "Class 2": "class_2", 
 "Class 3": "class_3", 
 "Customer Name": "name", 
 "E-mail": "email", 
 "Enable login": "login", 
 "Fax": "fax", 
 "First Name": "first_name", 
 "Last Name": "last_name", 
 "Mobile": "mobile", 
 "Post/Zip code": "zip", 
 "Ref #": "salesorder_ref", 
 "Telephone 1": "phone", 
 "Telephone 2": "phone2", 
 "Terms": "comment", 
 "Town/City": "city", 
 "Website": "website"
}


function_needed_data = {
 "Country": "country_id", 
#  "County": "country_id", 
 "Is Active": "active", 
 "Job Title": "job_title_id", 
 "Owner": "user_id", 
 "Price List": "property_product_pricelist", 
 "Ship via": "property_delivery_carrier", 
 "State/Province": "state_id", 
 "Title": "title", 
 "Type": "customer",
 "Customer since": "customer_since_date", 
 "Gender": "gender", 
 
 
}


# Open Sales invoice importer
for row in reader:
    if row and row[0] == "Type":
        column_headers=row
    else:
        for h_count,header in enumerate(column_headers):
            if header in used_column_headers and row[h_count]:
                current_customer_row.append((header,row[h_count]))
        if current_customer_row:
            target_data.append(dict(current_customer_row))
            current_customer_row=[]

# for count,x in enumerate(column_headers):
#     if x in used_column_headers:
#         print count,x
# print json.dumps(target_data, sort_keys=True, indent=2)
server = raw_input('Enter server:\n 1: http://188.165.45.213 or localhost') or 'localhost'
if server == '1':
    server = 'cgsyd01.carnacgroup.com'
dbuser='odoo_ajb'
dbpass='odoo_ajb'
port=8069
login_name='programmer@northdown.com.au'
password='Romeo1'
database = raw_input('Enter target database:\n 1: Northdown or ajb_live') or 'ajb_live'
if database == '1':
    database = 'Northdown'
    dbuser='bn_openerp'
    dbpass='SFrule7S'
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

#value checker for data type
for y in function_needed_data:
# for y in ['Telephone 2']:
    target_data_type=y
    data_values=[]
    for x in target_data:
        if target_data_type in x:
            if x[target_data_type] not in data_values:
                data_values.append(x[target_data_type])
                
    print 'target_data_type',target_data_type        
    print 'data_values',data_values

#value orm write organizer
for data_count,datum in enumerate(target_data):
    orm_write_data={}
#     print 'datum',datum
    #HANDLES SIMPLE DATA EXPORT
    for datum_data_type in datum:
        if datum_data_type in simple_data_export:
            orm_write_data[simple_data_export[datum_data_type]]=datum[datum_data_type]

    #HANDLES DATA REQUIRING FUNCTIONS
        if datum_data_type == 'Country':
            cr.execute("select id from res_country where name = '%s'" % datum[datum_data_type])
            target_country_id = cr.fetchone()[0]
            orm_write_data['country_id'] = target_country_id
        elif datum_data_type == 'Is Active':
            orm_write_data['active']=1
        elif datum_data_type == 'Job Title':
            cr.execute("select id from res_partner_job_title where name='%s'" % datum[datum_data_type])
            temp_ids = [x[0] for x in cr.fetchall()]
            
            if not temp_ids:
                target_job_title_id=pool('res.partner.job.title').create({'name':datum[datum_data_type]})
            else:
                target_job_title_id =temp_ids[0]
            orm_write_data['job_title_id']=target_job_title_id
        elif datum_data_type=='Owner':

#             cr.execute("select id from res_users where name = '%s'" % datum[datum_data_type] )
            cr.execute("select users.id from res_partner as partner inner join res_users as users on users.partner_id = partner.id where partner.name = '%s'" % datum[datum_data_type] )            
            temp_ids =[x[0] for x in cr.fetchall()]
            if not temp_ids:
                #creates new user
                user_data = pool('res.users').read(uid, ['company_id'])
                comp_id = user_data['company_id'][0]
                new_user_data={'name':datum[datum_data_type],'login':datum['E-mail'],'company_id':comp_id}
                target_user_id = pool('res.users').create(new_user_data)
            else:
                target_user_id = temp_ids[0]

            orm_write_data['user_id']=target_user_id
            
#         elif datum_data_type=='Price List':
#             
# #             Public Pricelist
# #             Sydney, Canberra Metro & Regional VIC Pricelist
# #             Hobart, Launceston, Adelaide, Brisbane, Perth Metro & Regional NSW, SA Pricelist
# #             Regional QLD, TAS, WA Pricelist
#              ['Syd, Ade, Vic', 'Bris, Tas', 'None']
#              [[],
#               
#              ]
# 
#             orm_write_data['property_product_pricelist']

        elif datum_data_type == "Ship via":
            if datum[datum_data_type] or datum[datum_data_type]!='None':
                cr.execute("select id from delivery_carrier where name = '%s'" % datum[datum_data_type])
                temp_ids=[x[0] for x in cr.fetchall()]
                if not temp_ids:
                    cr.execute("select id from product_product where product_tmpl_id = (select id from product_template where name = 'Service')")
                    temp_ids=[x[0] for x in cr.fetchall()]
                    target_service_product_id = temp_ids[0]
                    delivery_carrier_data={'name':datum[datum_data_type],'product_id':target_service_product_id,'partner_id':user.company_id.partner_id.id}
                    target_delivery_carrier_id=pool('delivery.carrier').create(delivery_carrier_data)
                else:
                    target_delivery_carrier_id = temp_ids[0]
                orm_write_data["property_delivery_carrier"]=target_delivery_carrier_id
                    
                

        elif datum_data_type == "State/Province":
            # ['VIC', 'SA', 'NSW', 'QLD', 'North Island', '', 'W.A', 'TAS', 'Vic', 'S.A.', 'ALD', 'ACT', 'Ringwood East', 'Carlton', 'Brunswick', 'WA', 'S.A', 'Tas', 'VC', 'W.A.', 'Tasmania', 'PRICES BELOW INC A 5% DISCOUNT']
            # use given country for state creation if needed
            given_country = datum['Country']
            cr.execute("select id from res_country where name = '%s'" % given_country)
            temp_ids=[x[0] for x in cr.fetchall()]
            country_id = temp_ids[0]
            
            #search for state with the given country
            cr.execute("select id from res_country_state where country_id = %s and name = '%s'" % (country_id,datum[datum_data_type]))
            temp_ids=[x[0] for x in cr.fetchall()]
            if not temp_ids:
                state_data={'name':datum[datum_data_type],'country_id':country_id,'code':datum[datum_data_type]}
                target_state_id=pool('res.country.state').create(state_data)
            else:
                target_state_id=temp_ids[0]
            orm_write_data["state_id"]=target_state_id
        elif datum_data_type == "Title":
            cr.execute("select id from res_partner_title where name= '%s'" % datum[datum_data_type])
            temp_ids=[x[0] for x in cr.fetchall()]
            if not temp_ids:
                target_title_id = pool('res.partner.title').create({'name':datum[datum_data_type]})
            else:
                target_title_id = temp_ids[0]
               
            orm_write_data["title"]=target_title_id
        elif datum_data_type == "Type":
            orm_write_data["customer"]=1
        elif datum_data_type == 'Customer since':
            orm_write_data['customer_since_date']=datetime.datetime.strptime(datum[datum_data_type],'%d/%m/%Y').strftime('%Y-%m-%d')
        elif datum_data_type=='Gender':
            orm_write_data['gender']=datum[datum_data_type].lower()
            
            
    if orm_write_data:
         print 'orm_write_data','%s out of %s' % (data_count+1,len(target_data)), orm_write_data
         pool('res.partner').create(orm_write_data)

            
            
    
        



