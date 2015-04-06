#######################################################################
# AJB Partner modifications
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

class res_partner_job_title(osv.Model):
    _name="res.partner.job.title"
    _columns={
              'name':fields.char('Name', size=64, required=False, readonly=False),
              }
    
class res_partner(osv.Model):
    _inherit="res.partner"
    
    _columns={
              'salesorder_ref':fields.char('Salesorder.com Reference', size=64, required=False, readonly=False),
              'balance': fields.float('Opening Balance at time of changing software', digits=(16, 2)),
              'first_name':fields.char('First Name', size=64, required=False, readonly=False),
              'last_name':fields.char('Last Name',size=64,required=False,readonly=False),
              'gender':fields.selection([
                  ('male','Male'),
                  ('female','Female'),
                   ],    'Gender', select=True, readonly=False),
              'job_title_id':fields.many2one('res.partner.job.title', 'Job Title', required=False), 
              'assistant_name':fields.char('Assistant Name', size=64, required=False, readonly=False),
              'assistant_phone':fields.char('Assistant Phone', size=64, required=False, readonly=False),
              'customer_since_date': fields.date('Customer Since'),
              'login':fields.char('Login', size=64, required=False, readonly=False),
#               'class_1':fields.char('Class 1', size=64, required=False, readonly=False),
#               'class_2':fields.char('Class 2', size=64, required=False, readonly=False),
#               'class_3':fields.char('Class 3', size=64, required=False, readonly=False),
              'class_1_id':fields.many2one('res.partner.category','Class 1'),
              'class_2_id':fields.many2one('res.partner.category','Class 2'),
              'class_3_id':fields.many2one('res.partner.category','Class 3'),
              'phone2': fields.char('Phone 2'),
              'email':fields.char('Accounts Email'),
              'email2':fields.char('Purchasing Managers Email'),
              
              }
    _defaults={
               'comment':'14 days',
               }