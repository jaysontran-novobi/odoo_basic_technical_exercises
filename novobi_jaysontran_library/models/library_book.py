# Copyright © 2022 Novobi, LLC
# See LICENSE file for full copyright and licensing details.
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class LibraryBook(models.Model):
    _inherit = 'library.book'

    isbn = fields.Char('ISBN', required=True)
    status = fields.Selection([
        ('not_publish', 'Not Published'),
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('lost', 'Lost')],
        default='available',
        string='Status',
    )
    short_name = fields.Char('Short name')
    return_date = fields.Datetime('Return date', help='The date on which the borrower will send the book')
    current_borrower = fields.Many2one('library.book.borrower', string='Current Borrower', tracking=True)
    book_url = fields.Char("Book's URL")

    def open_url_action(self):
        return {
            'type': 'ir.actions.act_url',
            'url': self.book_url,
            'target': 'new'
        }

    def button_lease_action(self):
        view_id = self.env.ref('novobi_jaysontran_library.library_book_lease_view_form').id
        return {
            'type': 'ir.actions.act_window',
            'name': 'library_book_lease_form',
            'res_model': 'library.book.lease',
            'view_id': view_id,
            'context': {'default_book_isbn': self.isbn},
            'view_mode': 'form',
            'target': 'new',
        }

    def _send_email_cron(self):
        overdue_books_lst = self.env['library.book'].search([('return_date', '<', fields.Date.today())])
        email_template = self.env.ref('novobi_library_book.email_template_library_book_to_borrowers')
        ctx = {'overdue_books_lst':  overdue_books_lst}
        email_values = {
            'email_from': 'jayson.tran@novobi.com',
            'email_to': 'jayson.tran@novobi.com'
        }
        email_template.with_context(**ctx).send_mail(self.env.user.company_id.id, force_send=True, email_values=email_values)
    def mark_available(self):
        self.write({'status': 'available', 'current_borrower': False, 'return_date': None})

    def mark_lost(self):
        self.write({'status': 'lost', 'current_borrower': False, 'return_date': None})

    @api.onchange('current_borrower')
    def update_books(self):
        print("Current borrower changed")

    @api.constrains('isbn')
    def _check_unique_isbn(self):
        saved_isbns = self.env['library.book'].search([]).mapped('isbn')
        for record in self:
            if record.isbn in saved_isbns:
                print('ISBN Existed')
                raise ValidationError(_("ISBN must be unique"))






