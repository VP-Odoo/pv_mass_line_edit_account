{
    "name": "Mass Line Edit – Account",
    "version": "18.0.1.0.1",
    "summary": "Mass editing of invoice/journal entry lines",
    "author": "PV-Odoo",
    "category": "Accounting",
    "license": "LGPL-3",
    "depends": ["account"],
    "data": [
        "views/account_move_line_views.xml",
    ],
    "images": ["static/description/banner.png"],
    "installable": True,
    "application": False,
    "description": """
Mass Line Edit for Accounting
=============================

This module allows you to quickly update multiple invoice or journal entry lines at once in Odoo Accounting.

Features:
---------
* **Master Toggle**: Add a *Select All Lines* checkbox at the top of the invoice/journal form to enable bulk selection.
* **Per-Line Control**: Each line gets an *Apply to All* toggle (boolean switch).
* **Mass Editing**: When you edit a field on one line with *Apply to All* enabled, the same change is automatically applied to all other selected lines in the same document.
* Works on both the *Invoice Lines* tab and the *Journal Items* tab.
* Prevents infinite loops with a safe propagation mechanism.

Benefits:
---------
* Save time by editing once and applying changes to multiple lines.
* Reduce human error by ensuring consistent values across invoices and journal entries.

""",
}
