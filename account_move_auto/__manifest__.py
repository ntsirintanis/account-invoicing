{
    "name": "Account Move Auto",
    "summary": """
       Template for invoicing product lines""",
    "version": "13.0.1.0.0",
    "license": "AGPL-3",
    "author": "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/server-auth",
    "development_status": "Beta",
    "depends": ["account"],
    "data": [
        "security/ir.model.access.csv",
        "views/account_move_auto_views.xml",
        "demo/account_move_auto.xml",
    ],
    "demo": [],
}
