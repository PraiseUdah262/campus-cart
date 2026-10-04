"""
Inventory Engine 
Handles stock checks, price quotes, and inventory filtering/sorting.
"""

def show_inventory(inventory):
    """Prints the available inventory in a formatted CLI table."""
    print(f"\n{'ID':<6}{'Product':<18}{'Price':<10}{'Stock':<6}")
    print("-" * 40)
    for item_id, item in inventory.items():
        print(f"{item_id:<6}{item['name']:<18}₦{item['price']:<9}{item['stock']:<6}")
    print()


def is_stock_available(inventory, item_id, requested_qty):
    """Safely checks if enough stock is available for an item."""
    item = inventory.get(item_id)
    if not item or requested_qty <= 0:
        return False
    return item["stock"] >= requested_qty


def update_item_stock(inventory, item_id, qty_change):
    """Modifies stock count. Pass negative numbers to deduct stock on checkout."""
    if item_id in inventory and (inventory[item_id]["stock"] + qty_change) >= 0:
        inventory[item_id]["stock"] += qty_change
        return True
    return False


def get_price_quote(inventory, item_id, qty, tax_rate=0.0, discount_rate=0.10, discount_threshold=2000):
    """Calculates subtotal, applicable discount, tax, and total quote."""
    if item_id not in inventory:
        return None

    unit_price = inventory[item_id]["price"]
    subtotal = unit_price * qty
    discount = (subtotal * discount_rate) if subtotal > discount_threshold else 0.0
    taxable = subtotal - discount
    tax = taxable * tax_rate
    total = taxable + tax

    return {
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "total": total
    }


# Lambdas for stock filtering and price sorting
filter_in_stock = lambda inv: dict(
    filter(lambda pair: pair[1]["stock"] > 0, inv.items())
)

sort_by_price = lambda inv: dict(
    sorted(inv.items(), key=lambda pair: pair[1]["price"])
)


if __name__ == "__main__":
    # Test inventory matching main.py
    inventory = {
        "101": {"name": "Notebook", "price": 200, "stock": 30},
        "102": {"name": "Pen", "price": 100, "stock": 40},
        "103": {"name": "Calculator", "price": 2000, "stock": 30},
        "104": {"name": "Stapler", "price": 2500, "stock": 25},
        "105": {"name": "A4 Paper", "price": 3000, "stock": 25},
        "106": {"name": "Document Folder", "price": 150, "stock": 20},
        "107": {"name": "Spiral Bind", "price": 300, "stock": 30},
    }

    print("Checking inventory display:")
    show_inventory(inventory)

    print("Checking stock check (10 Pens):", is_stock_available(inventory, "102", 10))

    print("\nQuote for 2 Calculators:")
    print(get_price_quote(inventory, "103", 2))

    print("\nDeducting 5 Pens from stock:")
    update_item_stock(inventory, "102", -5)
    print("New Pen stock:", inventory["102"]["stock"])

    print("\nIn-stock items:")
    print(list(filter_in_stock(inventory).keys()))

    print("\nSorted by price (ascending):")
    for item_id, details in sort_by_price(inventory).items():
        print(f"{details['name']}: ₦{details['price']}")