# Copyright © 2022 Novobi, LLC
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class LibraryBookBorrower(models.Model):
    _name = 'library.book.borrower'
    _description = 'Library Book Borrower'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', required=True)
    borrowed_books = fields.One2many('library.book', 'isbn', string='Books')
    total_borrowed_books = fields.Integer(string='Total borrowed books', compute='_compute_borrowed_books')

    def _compute_borrowed_books(self):
        for record in self:
            record.total_borrowed_books = len(record.borrowed_books)


    @api.constrains('email')
    def _check_email_exist(self):
        for record in self:
            if record.email or record.email != '':
                raise ValidationError(_('Email has already existed'))
