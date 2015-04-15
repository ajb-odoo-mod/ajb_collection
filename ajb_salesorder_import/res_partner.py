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
    
class res_partner_shipping_method(osv.Model):
    _name="res.partner.shipping.method"
    _columns={
              'name':fields.char('Name',size=64,required=True),
              }
    
class res_partner_shipping_terms(osv.Model):
    _name="res.partner.shipping.terms"
    _columns={
              'name':fields.char('Name',size=64,required=True),
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
              'class_1_id':fields.many2one('res.partner.category','Class 1'),
              'class_2_id':fields.many2one('res.partner.category','Class 2'),
              'class_3_id':fields.many2one('res.partner.category','Class 3'),
              'phone2': fields.char('Phone 2'),
              'email':fields.char('Accounts Email'),
              'email2':fields.char('Purchasing Managers Email'),
              
              #postal addresses
            'postal_street': fields.char('Street'),
            'postal_street2': fields.char('Street2'),
            'postal_zip': fields.char('Zip', size=24, change_default=True),
            'postal_city': fields.char('City'),
            'postal_state_id': fields.many2one("res.country.state", 'State', ondelete='restrict'),
            'postal_country_id': fields.many2one('res.country', 'Country', ondelete='restrict'),   
            
            #Shipping
            'property_delivery_carrier': fields.property(
              type='many2one',
              relation='delivery.carrier',
              string="Ship Via",
              help="This delivery method will be used when invoicing from picking."),            
            'shipping_method_id':fields.many2one('res.partner.shipping.method','Shipping Method'),
            'shipping_terms_id':fields.many2one('res.partner.shiipping.terms','Shipping Terms'),
            'property_account_position': fields.many2one('account.fiscal.position',"Fiscal Position",
            help="The fiscal position will determine taxes and accounts used for the partner."),
            
            'company_name':fields.char('Company',size=64),
            'abn':fields.char('ABN',size=64),
  
              
              }
    
    def _get_default_fiscal_position(self,cr,uid,context=None):
        pool=self.pool.get
        res=[]
        cr.execute("select res_id from ir_model_data where name ='%s'" % 'fiscal_position_normal_taxes_template1')
        target_ids=[x[0] for x in cr.fetchall()]
        if target_ids:
            res=target_ids[0]
        return res

    def default_get(self, cr, uid, fields, context=None):
        values = super(res_partner, self).default_get(cr, uid, fields, context)
        if fields and 'property_account_position' in fields:
            values['property_account_position']=self._get_default_fiscal_position(cr, uid, context={'mode':'from_default_get'})
            
        return values    
        
    
    _defaults={
                'comment':'14 days',
               'property_account_position':_get_default_fiscal_position,
               
               }