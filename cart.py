"""
cart.py - Cart & Receipt Management Engine
Handles item selections, cart total calculation, and receipt streaming.
"""

def add_to_cart(cart, product_id, product_name, price, quantity):
    """Adds or updates an item quantity in the cart dictionary."""
    if product_id in cart:
        cart[product_id]["quantity"] += quantity
        cart[product_id]["subtotal"] = round(cart[product_id]["quantity"] * price, 2)
    else:
        cart[product_id] = {
            "name": product_name,
            "price": price,
            "quantity": quantity,
            "subtotal": round(quantity * price, 2)
        }
    return cart

def calculate_cart_subtotal(cart):
    """Computes total cost of all cart items."""
    return round(sum(item["subtotal"] for item in cart.values()), 2)

def stream_receipt_lines(cart, quote_details):
    """
    Generator Function: Yields formatted receipt lines one by one.
    """
    yield "====== RECEIPT ======"
    for item in cart.values():
        yield f"{item['name']} x {item['quantity']} = ${item['subtotal']:.2f}"
    yield "---------------------"
    yield f"Subtotal: ${quote_details['subtotal']:.2f}"
    yield f"Discount: ${quote_details['discount']:.2f}"
    yield f"Tax:      ${quote_details['tax']:.2f}"
    yield f"Total:    ${quote_details['total']:.2f}"
    yield "====================="