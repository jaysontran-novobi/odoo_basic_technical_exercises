from odoo import models, fields

class LibraryBookLease(models.TransientModel):
    _name = 'library.book.lease'
    _description = 'Library Book Lease'

    book_isbn = fields.Char('ISBN')
    borrower_id = fields.Many2one('library.book.borrower', string='Borrower', required=True)
    date_return = fields.Date(string='Return Date', required=True)
    book_ids = fields.One2many('library.book', store=False, string='Books to borrow', readonly=True)

    def confirm(self):
        self.ensure_one()
        target_book = self.env['library.book'].search([('isbn', '=', self.book_isbn)])
        target_book.write({'current_borrower_id': self.borrower_id.id, 'status': 'borrowed'})
        return {'type': 'ir.actions.act_window_close'}

    def cancel(self):
        return 2