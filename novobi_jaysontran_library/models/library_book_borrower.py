# Copyright © 2022 Novobi, LLC
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class LibraryBookBorrower(models.Model):
    _name = 'library.book.borrower'
    _description = 'Library Book Borrower'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    borrowed_book_ids = fields.One2many('library.book', 'current_borrower_id', string='Books')
    total_borrowed_books = fields.Integer(string='Total borrowed books', compute='_compute_borrowed_books')

    @api.depends('borrowed_book_ids')
    def _compute_borrowed_books(self):
        for record in self:
            record.total_borrowed_books = len(record.borrowed_book_ids)


    @api.constrains('email')
    #Invoked on the records on which one of the named fields has been modified.
    def _check_email_exist(self):
        email_lst = self.search([]).mapped('email')
        if len(set(email_lst)) != len(email_lst):
            raise ValidationError(_("Email existed"))

    def print_report(self):
        return self.env.ref('novobi_jaysontran_library.action_report_borrower').report_action(self, config=False)

