{
    'name': 'AI Inventory Forecasting & Auto-Replenishment Engine',
    'version': '18.0.1.0.0',
    'category': 'Productivity/AI',
    'summary': 'Predict demand and generate purchase orders before stockouts happen.',
    'description': """
        AI Inventory Forecasting & Auto-Replenishment Engine
        ====================================================
        Machine learning demand forecasting and auto-replenishment for
        inventory, procurement, and warehouse operations.

        Features:
        - Demand forecasting based on historical sales data
        - Automatic purchase order generation when stock is low
        - Stockout and overstock risk alerts
        - Reorder point optimization per product
        - Supplier lead time tracking
    """,
    'author': 'SoftaiDev',
    'website': 'https://softaidev.pages.dev',
    'license': 'LGPL-3',
    'price': 299.0,
    'currency': 'USD',
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/ai_erp_inventory_forecast_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
