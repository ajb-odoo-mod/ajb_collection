
#######################################################################
# AJB Account invoice model modification
# Copyright (C) 2013 Romeo Abulencia #
# Author: romeo abulencia <romeo.abulencia@gmail.com>
# Maintainer: romeo abulencia <romeo.abulencia@gmail.com> #
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. # # This program is distributed in the hope that it will be useful, # but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details. #
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>. 
#######################################################################
import time

from openerp.osv import osv, fields

from openerp import tools, SUPERUSER_ID
from openerp.tools.translate import _
from openerp.tools.mail import plaintext2html


class account_invoice(osv.Model):
    _inherit='account.invoice'

    def _ajb_reformat_date(self, cr, uid, ids, name, arg, context=None):
        res = {}
        if not isinstance(ids,list):
            ids =[ids]
        for invoice_dict in self.read(cr, uid, ids, ['date_invoice'],context=context):
            res[invoice_dict['id']]=''
            if invoice_dict and 'date_invoice' in invoice_dict and invoice_dict['date_invoice']:
                res[invoice_dict['id']]=time.strftime('%d/%m/%Y',time.strptime(invoice_dict['date_invoice'],'%Y-%m-%d'))

        return res    

    _columns={
              'reformatted_date_invoice': fields.function(_ajb_reformat_date, string='date', type='date'),

              }
    
class mail_notification(osv.Model):
    _inherit='mail.notification'
    
    #overloaded to modify email footer
    def get_signature_footer(self, cr, uid, user_id, res_model=None, res_id=None, context=None, user_signature=True):
        """ Format a standard footer for notification emails (such as pushed messages
            notification or invite emails).
            Format:
                <p>--<br />
                    Administrator
                </p>
                <div>
                    <small>Sent from <a ...>Your Company</a> using <a ...>OpenERP</a>.</small>
                </div>
        """
        footer = ""
        if not user_id:
            return footer

        # add user signature
        user = self.pool.get("res.users").browse(cr, SUPERUSER_ID, [user_id], context=context)[0]
        if user_signature:
            if user.signature:
                signature = user.signature
            else:
                signature = "--<br />%s" % user.name
            footer = tools.append_content_to_html(footer, signature, plaintext=False)

        # add company signature
        if user.company_id.website:
            website_url = ('http://%s' % user.company_id.website) if not user.company_id.website.lower().startswith(('http:', 'https:')) \
                else user.company_id.website
            company = "<a style='color:inherit' href='%s'>%s</a>" % (website_url, user.company_id.name)
        else:
            company = user.company_id.name
        #sent_by = _('Sent by %(company)s using %(odoo)s')
        sent_by = _('Sent by %(company)s')

        signature_company = '<br /><small>%s</small>' % (sent_by % {
            'company': company,
            'odoo': "<a style='color:inherit' href='https://www.odoo.com/'>Odoo</a>"
        })
        footer = tools.append_content_to_html(footer, signature_company, plaintext=False, container_tag='div')

        return footer    
    
class mail_mail(osv.Model):
    """ Update of mail_mail class, to add the signin URL to notifications. """
    _inherit = 'mail.mail'

    def _get_partner_access_link(self, cr, uid, mail, partner=None, context=None):
        """ Generate URLs for links in mails:
            - partner is not an user: signup_url
            - partner is an user: fallback on classic URL
        """
        if context is None:
            context = {}
        partner_obj = self.pool.get('res.partner')
        if partner and not partner.user_ids:
            contex_signup = dict(context, signup_valid=True)
            signup_url = partner_obj._get_signup_url_for_action(cr, SUPERUSER_ID, [partner.id],
                                                                action='mail.action_mail_redirect',
                                                                model=mail.model, res_id=mail.res_id,
                                                                context=contex_signup)[partner.id]
#             return ", <span class='oe_mail_footer_access'><small>%(access_msg)s <a style='color:inherit' href='%(portal_link)s'>%(portal_msg)s</a></small></span>" % {
#                 'access_msg': _('access directly to'),
#                 'portal_link': signup_url,
#                 'portal_msg': '%s %s' % (context.get('model_name', ''), mail.record_name) if mail.record_name else _('your messages '),
#             }
            return """<br><br>
<span class='oe_mail_footer_access'><small>
<a href="https://www.facebook.com/northdowncraftbeer">https://www.facebook.com/northdowncraftbeer</a><br>
<a href="https://twitter.com/northdownbeer">https://twitter.com/northdownbeer</a><br>
<a href="http://instagram.com/northdowncraftbeer/">http://instagram.com/northdowncraftbeer/</a><br>
</small></span>
            """
        else:
            return super(mail_mail, self)._get_partner_access_link(cr, uid, mail, partner=partner, context=context)
        
    
