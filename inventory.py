"""
inventory.py - Inventory Management Engine
Manages stock levels, price quotations, and catalog filtering/sorting.
"""

# Default initial product catalog
DEFAULT_CATALOG = {
    101: {"name": "Notebook", "price": 2.5, "stock": 15},
    102: {"name": "Pen", "price": 1.5, "stock": 20},
    103: {"name": "Backpack", "price": 25.0, "stock": 8},
    104: {"name": "Water Bottle", "price": 10.0, "stock": 10}
}

def check_stock_availability(catalog, product_id, quantity):
    """Validates if enough stock exists for a given product."""
    if product_id not in catalog:
        return False, "Product ID not found."
    if catalog[product_id]["stock"] < quantity:
        return False, f"Insufficient stock. Available: {catalog[product_id]['stock']}"
    return True, "Stock available."

def update_stock(catalog, product_id, quantity_change):
    """
    Updates the stock count for a given item (negative values reduce stock).
    """
    if product_id in catalog:
        catalog[product_id]["stock"] += quantity_change
        return True
    return False

def calculate_price_quote(subtotal, tax_rate=0.05, discount_rate=0.10):
    """Calculates tax, applied discount, and final quote."""
    discount = subtotal * discount_rate if subtotal >= 50.0 else 0.0
    tax = (subtotal - discount) * tax_rate
    final_total = subtotal - discount + tax
    return {
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "tax": round(tax, 2),
        "total": round(final_total, 2)
    }

def filter_available_stock(catalog, min_stock=1):
    """
    Lambda function usage: Filters products with stock equal to or greater than min_stock.
    """
    filter_op = lambda item: item[1]["stock"] >= min_stock
    return dict(filter(filter_op, catalog.items()))

def sort_catalog_by_price(catalog, descending=False):
    """
    Lambda function usage: Sorts catalog list by item price.
    """
    sorted_items = sorted(
        catalog.items(),
        key=lambda item: item[1]["price"],
        reverse=descending
    )
    return dict(sorted_items)