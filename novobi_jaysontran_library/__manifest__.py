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
        # ============================== WIZARDS =============================
        #           
    ],
    "application": True,
    "installable": True,
}
