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
current_sales_invoice={'data':[],'lines':[]}
line_headers=[]
import_signal=False
sale_order_line_signal=False
target_data=[]

# Open Sales invoice importer
for counter,row in enumerate(reader):
    if row and counter <= count_limit:
#         print 'row',row
        
        #distinguish main header
        if row and len(row)> 2 and row[1] == 'Customer':
            headers=row
        #distinguish sales invoice entry
        elif row and row[0] == 'Sales Invoice':
    
            temp=[]
            for h_count,header in enumerate(headers):
                temp.append((header,row[h_count])) 
            current_sales_invoice['data']=dict(temp)
            #distinguish open sales invoice
            if current_sales_invoice['data']['Status']=='OPEN':
                import_signal=True
            
                sale_order_line_signal=True
        
        elif import_signal:
            if sale_order_line_signal:
                #distinguish sales invoice line header
                if row[0]=='Type':
                    line_headers=row
                #distinguish sales invoice line entry
                elif line_headers:
                    temp=[]
                    max_line_header_count=len(line_headers)-1
                    max_line_count=len(row)-1                    
                    for l_count,line_header in enumerate(line_headers):
                        if l_count <= max_line_count:
                            temp.append((line_header,row[l_count]))
                        else:
                            temp.append((line_header,''))
    
                    current_sales_invoice['lines'].append(dict(temp))

            

    elif not row and sale_order_line_signal and import_signal and counter <= count_limit:
        print json.dumps(current_sales_invoice, sort_keys=True, indent=2)
        if current_sales_invoice['data']:
            target_data.append(current_sales_invoice)
        current_sales_invoice={'data':[],'lines':[]}
        sale_order_line_signal=False
        import_signal=False
        
#         print 'current',current_sales_invoice
            

#for counter,line in enumerate(csv_file.readlines()):
#    line=line.replace('\r',"").replace('\n','')
#    if counter <= count_limit:
#        print type(line),len(line.split(',')),'%r'%line
