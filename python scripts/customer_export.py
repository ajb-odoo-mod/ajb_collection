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
csv_file = open('Documents.csv','r')
count_limit=999999999999999999999999999999
reader = csv.reader(csv_file)
headers=[]
current_sales_invoice=[]
line_headers=[]

target_fields=['Address 1', 'Address 2', 'Country', 'Customer', 'Customer #', 'Customer ref', 'E-mail', 'Email', 'Post/Zip code', 'Price List', 'State/Province', 'Telephone', 'Town/City']

target_data=[]

# Open Sales invoice importer
for counter,row in enumerate(reader):
    if row and counter <= count_limit:
#         print 'row',row
        
        #distinguish main header
        if row and len(row)> 2 and row[1] == 'Customer':
            headers=row
        #distinguish sales invoice entry
#         elif row and row[0] == 'Sales Invoice':
    
        temp=[]
        for h_count,header in enumerate(headers):
            if header in target_fields:
                temp.append((header,row[h_count])) 
        current_sales_invoice.append(tuple(temp))


            

    elif not row and counter <= count_limit:
        if current_sales_invoice:
            target_data.append(tuple(current_sales_invoice))
        current_sales_invoice=[]
        sale_order_line_signal=False
        import_signal=False
        

            
print 'raw count',len(target_data)
print 'deduplicated count',len(set(target_data))
