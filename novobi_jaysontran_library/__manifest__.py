# Copyright © 2022 Novobi, LLC
# See LICENSE file for full copyright and licensing details.

{
    "name": "Novobi: Library Book",
    "summary": "Novobi: Library Book",
    "version": "15.0.1",
    "category": "Tools",
    "website": "https://novobi.com",
    "author": "Novobi, LLC",
    "license": "OPL-1",
    "depends": [
        "novobi_library_book"
    ],
    "excludes": [],
    "data": [
        # ============================== DATA =================================
        'data/cron_job.xml',
        # ============================== VIEWS ================================
        'views/library_book_views.xml',
        # ============================== SECURITY ================================
        'security/library_book_groups.xml',
        'security/ir.model.access.csv',

        # ============================== REPORT =============================
        'report/borrower_reports.xml',
        'report/borrower_templates.xml',

        # ============================== WIZARDS =============================
        'wizards/library_book_lease.xml',
        #           
    ],
    "application": True,
    "installable": True,

    'assets': {
        'web.assets_backend': [
            'novobi_jaysontran_library/static/src/js/date_widget.js',
        ],
    },
}
