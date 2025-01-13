# Vending Machine Program

def display_menu(menu):
    #Display the menu with items and prices categorized.
    print("\nWelcome to the Easy Snacks Machine!") #the welcoming message
    print("Here is the menu:")
    groups = {}
    for key, value in menu.items():
        category = value['category']
        if category not in groups:
            groups[category] = []
        groups[category].append((key, value['name'], value['price']))

    for category, items in groups.items():
        print(f"\n{category}:")
        for key, name, price in items:
            print(f"  {key}: {name} - ${price:.2f}")

def select_item(menu, simulated_input=None):
    #Prompt user to select an item.
    while True:
        if simulated_input:
            if not simulated_input:
                return None
            selection = simulated_input.pop(0).lower()
        else:
            try:
                selection = input("\nEnter the item number you want to purchase (or 'cancel' to cancel order): ").lower() #allows the user to ordder or cancel the pruchase
            except OSError:
                print("Interactive input not supported. Terminating.") #displays if the user inputs something invalid
                return None
        
        if selection == 'cancel':
            return None
        if selection in menu:
            return selection
        print("Sorry,invalid choice. Please try again.") #displays if the user inputs something invalid

def process_payment(price, simulated_input=None):
    #Handle payment process.
    print(f"The price is ${price:.2f}. Please select a payment method.") #shows the price of the product
    while True:
        if simulated_input:
            if not simulated_input:
                return None
            method_of_payment = simulated_input.pop(0).lower()
        else:
            try:
                method_of_payment = input("Enter payment method (cash/card): ").lower() #allows the user to choose a payment method between cash or card
            except OSError:
                print("Interactive input not supported. Terminating.")  #displays if the user inputs something invalid
                return None

        if method_of_payment == 'cash':
            return process_cash_payment(price, simulated_input)
        elif method_of_payment == 'card':
            return process_card_payment(price, simulated_input)
        else:
            print("Invalid payment method. Please choose (cash/card).")  #displays if the user inputs something invalid payment method

def process_cash_payment(price, simulated_input=None):
    #Handle cash payment.
    print("You have selected cash payment.") #if the user selects cash payment
    total_entered = 0.0
    while total_entered < price:
        try:
            if simulated_input:
                if not simulated_input:
                    return None
                inserted = float(simulated_input.pop(0))
            else:
                inserted = float(input(f"Insert amount (remaining: ${price - total_entered:.2f}): ")) 

            if inserted <= 0:
                print("Please insert a valid amount.") #displays if the user inputs something invalid amount
            else:
                total_entered += inserted
        except (ValueError, OSError):
            print("Invalid input. Please enter a number.")  #displays if the user inputs something invalid number

    balance = total_entered - price
    if balance > 0:
        print(f"Transaction complete! Your balance is ${balance:.2f}.")  #shows the users balance 
    else:
        print("Transaction complete! No balance.") #if the user has no balance

def process_card_payment(price, simulated_input=None):
    #Handle card payment.
    print("You selected card payment.") #if the user select card payment method
    while True:
        try:
            if simulated_input:
                if not simulated_input:
                    return None
                card_ID = simulated_input.pop(0)
            else:
                card_ID = input("Enter your card number: ") #asking the user to enter 8-digit number

            if len(card_ID) == 8 and card_ID.isdigit():
                print(f"Transaction complete! ${price:.2f} has been charged to your card.") #once the user has inserted the number
                break
            else:
                print("Invalid card number. Please enter a 8-digit card number.") #displays if the user inputs something invalid 8-digit number
        except OSError:
            print("Interactive input not supported. Terminating.") #displays if the user inputs something invalid
            return None

def vending_machine(simulated_input=None):
    #Main function for the vending machine.
    menu = {
        '101': {'name': 'Coco-cola', 'price': 2.50, 'category': 'Beverages'},
        '102': {'name': 'Pepsi', 'price': 2.50, 'category': 'Beverages'},
        '103': {'name': 'Sprite', 'price': 2.50, 'category': 'Beverages'},
        '104': {'name': '7up', 'price': 2.50, 'category': 'Beverages'},
        '105': {'name': 'Fanta', 'price':2.50, 'category': 'Beverages'},
        
        '201': {'name': 'Monster', 'price': 12.50, 'category': 'Energy drinks'},
        '202': {'name': 'Redbull', 'price': 12.50, 'category': 'Energy drinks'},
        '203': {'name': 'Rockstar', 'price': 5.50, 'category': 'Energy drinks'},
        '204': {'name': 'Celsius', 'price': 6.50, 'category': 'Energy drinks'},
        '205': {'name': 'bang energy', 'price':14.50, 'category': 'Energy drinks'},

        '301': {'name': 'Lays', 'price': 3.50, 'category': 'Snacks'},
        '302': {'name': 'Bingo!', 'price': 3.50, 'category': 'Snacks'},
        '303': {'name': 'Cheetos', 'price': 3.50, 'category': 'Snacks'},
        '304': {'name': 'Kurkura', 'price': 4.50, 'category': 'Snacks'},
        '305': {'name': 'Doritos', 'price':4.50, 'category': 'Snacks'},

        '401': {'name': 'Diary milk', 'price': 2.50, 'category': 'Chocolates'},
        '402': {'name': 'KitKat', 'price': 2.50, 'category': 'Chocolates'},
        '403': {'name': 'Snickers', 'price': 2.50, 'category': 'Chocolates'},
        '404': {'name': '5 Stars', 'price': 2.50, 'category': 'Chocolates'},
        '405': {'name': 'Galaxy', 'price':2.50, 'category': 'Chocolates'},
    }

    while True:
        display_menu(menu)
        choice = select_item(menu, simulated_input)
        if choice is None:
            print("Thank you for using the Easy Snacks machine. Goodbye!") #once the user is done using the vending machince 
            break

        item = menu[choice]
        print(f"You selected {item['name']}.")
        process_payment(item['price'], simulated_input)

# Run the vending machine program
if __name__ == "__main__":
    vending_machine()
