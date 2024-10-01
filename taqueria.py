menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0  # Initialize total outside the loop

while True:
    try:
        purchase = input("Enter your order, please! ").title()

        if purchase in menu:
            print(f"Your purchase of {purchase} is ${menu[purchase]:.2f}")
            total += menu[purchase]  # Add to total
            print(f"Total so far: ${total:.2f}")
        else:
            print("Item not found. Please try again.")
    except EOFError:  # Catch Ctrl+D (EOF)
        print("\nThank you. Final total is ${:.2f}".format(total))
        break  # Exit the loop when Ctrl+D is pressed
