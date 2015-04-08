# -*- coding: utf-8 -*-
from openerp.osv import fields, osv
 
class wms_help(osv.osv):
    _name = 'wms.help'
    _description = u'wms help'
    _columns = {
        'title':fields.char( u'标题',size=255,select=True),
        'date_upd':fields.date(u'更新日期'),
	'content':fields.html(u'内容'),
	'author':fields.char(u'作者',size=50,select=True),
	'type':fields.selection([('purchase','采购'),('input','入库'),('output','出库')],'分类',required=True),
    }

    _defaults = {
        'type' : 'purchase',
	'date_upd':fields.datetime.now,
    }
 
wms_help()
