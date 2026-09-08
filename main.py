print("===== CampusCart =====")

name = input("Enter your name: ")

print("Welcome to CampusCart,", name)
choice = input("Choose an option: ")

print("You selected:", choice)
print("===== CampusCart =====")
print("Welcome to CampusCart!")

# Inventory
inventory = {
    "101": {"name": "Notebook", "price": 2.50, "stock": 15},
    "102": {"name": "Pen", "price": 1.50, "stock": 20},
    "103": {"name": "Backpack", "price": 25.00, "stock": 8},
    "104": {"name": "Water Bottle", "price": 10.00, "stock": 10}
}

# Shopping cart
cart = []

while True:
    print("\n===== MENU =====")
    print("1. View Catalogue")
    print("2. Add Item to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        print("\n===== CATALOGUE =====")

        for item_id, item in inventory.items():
            print(
                item_id,
                "-",
                item["name"],
                "| Price: $", item["price"],
                "| Stock:", item["stock"]
            )

    elif choice == "2":
        item_id = input("Enter the product ID: ").strip()

        if item_id not in inventory:
            print("Invalid product ID.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        if quantity > inventory[item_id]["stock"]:
            print("Not enough stock available.")
            continue

        item = inventory[item_id]

        cart.append({
            "id": item_id,
            "name": item["name"],
            "price": item["price"],
            "qty": quantity,
            "subtotal": item["price"] * quantity
        })

        print(item["name"], "added to cart.")

    elif choice == "3":
        print("\n===== YOUR CART =====")

        if not cart:
            print("Your cart is empty.")
        else:
            cart_total = 0

            for item in cart:
                print(
                    item["name"],
                    "| Quantity:", item["qty"],
                    "| Subtotal: $", format(item["subtotal"], ".2f")
                )
                cart_total += item["subtotal"]

            print("Cart Total: $", format(cart_total, ".2f"))

    elif choice == "4":
        if not cart:
            print("Your cart is empty.")
            continue

        subtotal = 0

        for item in cart:
            subtotal += item["subtotal"]

        discount = 0

        if subtotal > 20:
            discount = subtotal * 0.10

        total = subtotal - discount

        print("\n===== RECEIPT =====")

        for item in cart:
            print(
                item["name"],
                "x", item["qty"],
                "= $", format(item["subtotal"], ".2f")
            )

        print("-------------------------")
        print("Subtotal: $", format(subtotal, ".2f"))
        print("Discount: $", format(discount, ".2f"))
        print("Total:    $", format(total, ".2f"))

        # Reduce stock after checkout
        for item in cart:
            inventory[item["id"]]["stock"] -= item["qty"]

        print("Checkout successful!")
        cart.clear()

    elif choice == "5":
        print("Thank you for using CampusCart!")
        break

    else:
        print("Invalid choice. Please choose 1-5.")