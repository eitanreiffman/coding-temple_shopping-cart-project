# Build a shopping cart program with the following capabilities:

# 1) Takes in an input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The User can also clear the current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, prints out a receipt of the items with total and quantity.

# I would also like to give the user limited options.
# If they don't add an item that's on the list, the item won't get added

# So basically there should be 2 separate dictionaries.
# One that shows the user's shopping cart, and another that shows the available items in the store

# Available Store Items:
available_items = {
    "Baked Goods" : {
            "Bread" : {
            "White" : 2.50,
            "Rye" : 2.75,
            "Sourdough" : 2.75,
            "Whole Wheat" : 2.75
        },
        "Croissant" : {
            "Butter" : 3.00,
            "Chocolate" : 3.50 
        },
        "Danish" : {
            "Cheese" : 3.50,
            "Chocolate" : 3.50,
        },
    },
    "Produce" : {
        "Apple" : {
            "Granny Smith" : 1.00,
            "Pink Lady" : 1.25,
            "Gala" : 1.25 
        },
        "Orange" : {
            "Blood" : 1.25,
            "Navel" : 1.25
        },
        "Nectarine" : 1.35,
        "Peach" : 1.35,
        "Mango" : 1.75
    },
    "Drinks" : {
        "Soda" : {
            "Coke" : 2.00,
            "Sprite" : 2.00,
            "Root Beer" : {
                "A&W" : 2.00,
                "Barqs" : 1.75
        }},
        "Juice" : {
            "Orange" : {
                "Tropicana" : 3.50,
                "Florida's Natural" : 3.00
            },
            "Apple" : 3.50,
            "V8" : 4.50
        },
        "Milk" : {
            "Non-Fat" : 1.50,
            "Low-Fat" : 1.75,
            "Whole" : 2.00 
        },
        "Water" : {
            "Poland Spring" : 1.50,
            "Dasani" : 1.75,
            "Sparkletts" : 1.50
        }
    },
    "Meat Counter" : {
        "Steak" : {
            "T-Bone" : 10.00,
            "Rib-Eye" : 9.50,
            "Skirt" : 9.00
        },
        "Hamburger" : {
            "Regular" : 6.00,
            "Veggie" : 6.50,
            "Turkey" : 6.25
        },
        "Sausage" : {
            "Polish" : 6.00,
            "Bratwurst" : 6.50,
            "Knackwurst" : 6.50,
            "Chorizo" : 6.50
        } 
    },
    "Cheese Counter" : {
        "Mozzarella" : {
            "Shredded" : 4.25,
            "Block" : 4.00
        },
        "Cheddar" : {
            "Shredded" : 4.25,
            "Block" : 4.00
        },
        "Muenster" : {
            "Sliced" : 4.50,
            "Block" : 4.25
        },
        "Gouda" : 4.50,
        "Brie" : 5.00,
        "Provolone" : 5.00,
        "Camembert" : 5.00 
    },
}

print("\nWelcome to Eitan's Very Limited Virtual Store!\n\n"
        "Feel free to browse the place and add anything you like to your shopping cart.\n\n"
        "Unfortunately, what you see is what there is.\n\n"
        "You can only add an item if it exists in the virtual store.\n")

# Defining the customer's cart, which is empty for now
user_cart = {}

# The available items in the store are part of a global dictionary outside of this function

username = input("Please enter your name: ").title()

print(f"\nHi {username}\n")

x = ""
y = ""

# Let's hash out what needs to be done
# With this While loop, it will always start with a very basic question:
# What would you like to do now?
# Enter "browse" to browse the store
# Enter "cart" to see your shopping cart
# Enter "remove" to remove an item from you list
# Enter "clear" to clear all the items on your list
# Enter "checkout" to checkout
# The while loop will continue to run as long as "x" doesn't equal "yes",
# Which it won't until the user checks out and confirms they're done by entering "yes"


while x != "yes":
    do_now = input("What would you like to do now?\n\n"
            "Enter 'browse' to browse the store\n\n"
            "Enter 'cart' to see your shopping cart\n\n"
            "Enter 'remove' to remove an item from your cart\n\n"
            "Enter 'clear' to clear all items from your cart\n\n"
            "Enter 'checkout' to check out: ")
    
    while do_now.lower() != "browse" or "cart" or "remove" or "clear" or "checkout":
    # This is a while loop within a while loop that'll ensure the user can only move
    # forward with the shopping process if they enter one of the requested words

        if do_now.lower() == "browse":
            print("\nThese are the different food sections:\n\n\t")
            for section in available_items:
                print(section)

            choose_section = input("\nWhich food section would you like to browse? ").title()
            while choose_section.title() not in available_items:
                print("\nThis food section doesn't exist.\n"
                      "\nPlease type in one of the following food sections:\n\n")
                for section in available_items:
                    print(section)

                choose_section = input("").title()
   
            if choose_section in available_items:
                print(f"\nYou've just entered the {choose_section} section.\n"
                       "\nIf anything interests you, type the item to see if there are different varieties.")

                if choose_section == "Baked Goods":
                    print("Here are the different baked goods available:\n")
                    for baked_good in available_items["Baked Goods"]:
                        print(baked_good)

                if choose_section == "Produce":
                    print("Here is the different produce available:\n")
                    for produce in available_items["Produce"]:
                        print(produce)

                if choose_section == "Drinks":
                    print("Here are the different drinks available:\n")
                    for drink in available_items["Drinks"]:
                        print(drink)

                if choose_section == "Meat Counter":
                    print("Here are the different kinds of meat available:\n")
                    for meat in available_items["Meat Counter"]:
                        print(meat)

                if choose_section == "Cheese Counter":
                    print("Here are the different cheeses available:\n")
                    for cheese in available_items["Cheese Counter"]:
                        print(cheese)

            break

        if do_now.lower() == "cart":
            print("\nHere's your shopping cart\n\n")
            
            if len(user_cart) == 0:
                print("Your cart is currently empty.")

            else:
                print("Here's your cart")

            break

        if do_now.lower() == "remove":
            print("\nHere's your shopping cart\n\n")            
            
            if len(user_cart) == 0:
                print("Your cart is currently empty.")

            else:
                print("Here's your cart")
            
            break

        if do_now.lower() == "clear":
            print("\nHere's your shopping cart\n\n")
            
            if len(user_cart) == 0:
                print("Your cart is currently empty.")

            else:
                print("Here's your cart")
                
            break

        if do_now.lower() == "checkout":
            print("\nHere's your shopping cart\n\n")

            if len(user_cart) == 0:
                print("Your cart is currently empty.")

            else:
                print("Here's your cart")
           
            break
    
        else:
            do_now = input("\nSorry, your response didn't match.\n\n"
                        "You must enter either 'browse', 'cart', 'remove', 'clear', or 'checkout': ")
    


    x = input("\nThe total price of your items is blank. Are you sure you want to pay and check out? ").lower()