from odoo import http



class MyModule(http.Controller):

    @http.route('/my_module', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('my_module.index', {})
