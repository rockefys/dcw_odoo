# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
 
class wms_help(osv.osv):
    _name = 'wms.help'
    _description = u'wms help'
    _columns = {
        'title':fields.char( u'标题',size=255,select=True),
        'date_create':fields.date(u'创建日期',select=True),
        'content':fields.text(u'内容',size=255),
    }
 
wms_help()
