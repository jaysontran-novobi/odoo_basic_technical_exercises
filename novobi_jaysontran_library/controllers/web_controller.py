
import odoo.http as http
from odoo.http import request
class MyController(http.Controller):

    @http.route(['/library/book/<isbn>'], auth='none', methods=['PUT'], type='json', csrf=False, cors='*')
    def handler(self, isbn, **kw):
        target = request.env['library.book'].sudo().search([('isbn', '=', isbn)])
        request_body = request.jsonrequest
        if target:
            try:
                target.write(request_body)
                return {
                    'msg': "Updated book successfully",
                    'status': True
                }
            except Exception as exception:
                return {
                    'msg': f"Failed to update book: {exception.__cause__}",
                    'status': False
                }
        return {
            'msg': f"Could not find book with isbn: {isbn}",
            'status': False
        }
