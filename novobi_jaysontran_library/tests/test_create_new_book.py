
from odoo.tests import tagged
from odoo import fields, _
from odoo.exceptions import ValidationError
from odoo.odoo.tools.safe_eval import datetime
from odoo.tests import common, Form


@tagged('post_install', '-at_install', 'create_book')
class TestCreateNewBook(common.TransactionCase):

    @classmethod
    def setUp(cls):
        # Precondition
        cls.isbn_test = 'isbn_test'
        cls.existed_book = {
            'name': 'Test book',
            'short_name': 'Test book short name',
            'date_release': datetime.now(),
            'isbn': cls.isbn_test,
            'status': 'available',
        }
        cls.new_book_same_isbn = {
            'name': 'Test book2',
            'short_name': 'name',
            'date_release': datetime.now(),
            'isbn': cls.isbn_test,
            'status': 'borrowed',
        }


    @classmethod
    def tearDown(self):
        super().tearDown()
        self.env['library.book'].search(['isbn', '=', self.isbn_test]).unlink()


    def test_create_new_book(self):
        self.env['library.book'].create(self.existed_book)
        new_book= self.env['library.book'].create(self.new_book_same_isbn)
        self.assertRaises(ValidationError(_("ISBN must be unique")))

