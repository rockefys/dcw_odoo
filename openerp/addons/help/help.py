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
	'type':fields.selection([('summary','概述'),('purchase','采购'),('input','入库'),('output','出库'),('return','退货'),('finance','财务'),('check','盘点'),('other','其他')],'分类',required=True),
    }

    _defaults = {
        'type' : 'summary',
        'date_upd':fields.datetime.now,
    }
 
wms_help()
