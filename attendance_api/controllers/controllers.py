# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request
import xmlrpc, xmlrpc.client
import json, math
from odoo.addons.web.controllers.main import serialize_exception
from xmlrpc.server import SimpleXMLRPCServer
from odoo import models,registry, SUPERUSER_ID

class AttendanceApi(http.Controller):
    @http.route('/attendance_api/hello/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/attendance_api/login', type='json', auth="none", website=True, methods=['POST'])
    def nasabah(self, **kw):
        xmlrpclib = xmlrpc.client
        url, db, username, password = 'http://127.0.0.1:8069', http.request.env.cr.dbname, kw.get('username'), kw.get('password')
        models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
        common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        try:
            uid = common.authenticate(db, username, password, {})
            res = models.execute_kw(db, uid, password, 
                'res.partner', 'search_read', [[['id', '=', uid]]], 
                {'fields': ['id', 'name'], 'limit': 1})
            return res
        except Exception as e:
            return {'Error':'Invalid Request', 'e' : e}

    
