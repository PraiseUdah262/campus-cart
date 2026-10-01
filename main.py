"""
CampusCart CLI
A command-line tool that lets students browse campus vendor
products, build a cart, and generate a receipt at checkout.
"""

inventory = {
    "101": {"name": "Notebook", "price": 200, "stock": 30},
    "102": {"name": "Pen", "price": 100, "stock": 40},
    "103": {"name": "Calculator", "price": 2000, "stock": 30},
    "104": {"name": "Stapler", "price": 2500, "stock": 25},
    "105": {"name": "A4 Paper", "price": 3000, "stock": 25},
    "106": {"name": "Document Folder", "price": 150, "stock": 20},
    "107": {"name": "Spiral Bind", "price": 300, "stock": 30},
}

cart = []

while True:
    print("================================")
    print("          CAMPUSCART")
    print("================================")
    print("1. View Inventory")
    print("2. Add Item to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Select an option (1-5): ")

    if choice == "1":
        print(f"\n{'ID':<6}{'Product':<18}{'Price':<10}{'Stock':<6}")
        print("-" * 40)
        for item_id, details in inventory.items():
            print(f"{item_id:<6}{details['name']:<18}₦{details['price']:<9}{details['stock']:<6}")
        print()

    elif choice == "2":
        item_id = input("Enter product ID: ")

        if item_id not in inventory:
            print("Product ID not found.\n")
            continue

        try:
            qty = int(input("Enter quantity: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        already_in_cart = 0
        for entry in cart:
            if entry["id"] == item_id:
                already_in_cart += entry["qty"]

        remaining_stock = inventory[item_id]["stock"] - already_in_cart

        if qty > remaining_stock:
            print(f"Not enough stock. Only {remaining_stock} available.\n")
            continue

        subtotal = inventory[item_id]["price"] * qty
        cart.append({"id": item_id, "qty": qty, "subtotal": subtotal})
        print(f"Added {qty} x {inventory[item_id]['name']} to cart.\n")

    elif choice == "3":
        if not cart:
            print("Your cart is empty.\n")
        else:
            print(f"\n{'Product':<18}{'Qty':<6}{'Subtotal':<10}")
            print("-" * 34)
            cart_total = 0
            for entry in cart:
                name = inventory[entry["id"]]["name"]
                print(f"{name:<18}{entry['qty']:<6}₦{entry['subtotal']:<9}")
                cart_total += entry["subtotal"]
            print("-" * 34)
            print(f"TOTAL: ₦{cart_total}\n")

    elif choice == "4":
        if not cart:
            print("Your cart is empty. Add items before checking out.\n")
        else:
            total = 0
            print("\n" + "=" * 34)
            print("             RECEIPT")
            print("=" * 34)
            print(f"{'Product':<18}{'Qty':<6}{'Subtotal':<10}")
            print("-" * 34)
            for entry in cart:
                item_name = inventory[entry["id"]]["name"]
                print(f"{item_name:<18}{entry['qty']:<6}₦{entry['subtotal']:<9}")
                total += entry["subtotal"]
            print("-" * 34)

            if total > 2000:
                discount = total * 0.1
                total -= discount
                print(f"{'Discount (10%)':<24}-₦{discount:<9}")

            print(f"{'TOTAL':<24}₦{total:<9}")
            print("=" * 34)
            print("  Thank you for using CampusCart!")
            print("=" * 34 + "\n")

            for entry in cart:
                inventory[entry["id"]]["stock"] -= entry["qty"]
            cart = []

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1-5.\n")