Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:39) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Part1

Class ItemToPurchase:
    
SyntaxError: invalid syntax
class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

        
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name =  customer_name
        self.current_date = current_date
        self.cart_items = []

        
    def add_item(self, item):
        
SyntaxError: unexpected indent
class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

        
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name =  customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_item(self, item):
        self.cart_items.append(item)
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    def modify_item(self, modify_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity !=0:
                    item.item_quantity = modified_item.item_quantity
                return
            print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())
        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price: .2f} = ${item.item_price * item.item_quantity:.2f}")
        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost:.2f}")
    def print_description(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions:)
              
SyntaxError: unterminated string literal (detected at line 38)
        print("Item Description")
              
SyntaxError: unexpected indent

class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name =  customer_name
        self.current_date = current_date
        self.cart_items = []
        
SyntaxError: invalid syntax


class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

        
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name =  customer_name
        self.current_date = current_date
        self.cart_items = []

        
    def add_item(self, item):
        
SyntaxError: unexpected indent

class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

        
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name =  customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_item(self, item):
        self.cart_items.append(item)
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    def modify_item(self, modify_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity !=0:
                    item.item_quantity = modified_item.item_quantity
                return
            print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())
        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price: .2f} = ${item.item_price * item.item_quantity:.2f}")
        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost:.2f}")
    def print_description(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

            
if __name__ == "__main__":
    cart =  ShoppingCart("Gabriela Johnson", "February 1, 2020")
    item1 = ItemToPurchase("Eggs", "White, Large, Pasture-rasied, 3.00, 3)
                           
SyntaxError: unterminated string literal (detected at line 3)
if __name__ == "__main__":
    cart =  ShoppingCart("Gabriela Johnson", "February 1, 2020")
    item1 = ItemToPurchase("Eggs", "White, Large, Pasture-rasied", 3.00, 3)
    item2 = ItemToPurchase("Hershey Bar", "Milk Chocolate", 1.50, 1)
    item3 = ItemToPurchase("Red Wine", "Cabernet Sauvignon", 55.00, 1)

                           
    cart.add_item(item1)
                           
SyntaxError: unexpected indent
if __name__ == "__main__":
    cart =  ShoppingCart("Gabriela Johnson", "February 1, 2020")
    item1 = ItemToPurchase("Eggs", "White, Large, Pasture-rasied", 3.00, 3)
    item2 = ItemToPurchase("Hershey Bar", "Milk Chocolate", 1.50, 1)
    item3 = ItemToPurchase("Red Wine", "Cabernet Sauvignon", 55.00, 1)
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    cart.print_total()
    print()
    cart.print_description()

                           
Gabriela Johnson's Shopping Cart - February 1, 2020
Number of Items: 5
Eggs 3 @ $ 3.00 = $9.00
Hershey Bar 1 @ $ 1.50 = $1.50
Red Wine 1 @ $ 55.00 = $55.00
Total: $65.50

Gabriela Johnson's Shopping Cart - February 1, 2020
Item Descriptions
Eggs: White, Large, Pasture-rasied
Hershey Bar: Milk Chocolate
Red Wine: Cabernet Sauvignon


def print_menu(shopping_cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")
        if choice == 'a':
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item_to_purchase = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            shopping_cart.add_item(item_to_purchase)
        elif choice == 'r':
            item_name = input("Enter the item name to remove: ")
            shopping_cart.remove_item(item_name)
        elif choice == 'c':
            pass
        elif choice == 'i':
            shopping_cart.print_descriptions()
        elif choice == 'o':
            shopping_cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

            
def main():
    cart = ShoppingCart("Gabriela Johnson", "February 1, 2020")
    print_menu(cart)

    
if __name__ == "__main__":
    main()

    

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: a
Enter the item name: Snickers Bar
Enter the item description: Original
Enter the item price: 3.50
Enter the item quantity: 2

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: r
Enter the item name to remove: Snickers Bar

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: c

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: i
Traceback (most recent call last):
  File "<pyshell#128>", line 2, in <module>
    main()
  File "<pyshell#125>", line 3, in main
    print_menu(cart)
  File "<pyshell#121>", line 24, in print_menu
    shopping_cart.print_descriptions()
AttributeError: 'ShoppingCart' object has no attribute 'print_descriptions'. Did you mean: 'print_description'?


class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

        
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name =  customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_item(self, item):
        self.cart_items.append(item)
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    def modify_item(self, modify_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity !=0:
                    item.item_quantity = modified_item.item_quantity
                return
            print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())
        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price: .2f} = ${item.item_price * item.item_quantity:.2f}")
        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost:.2f}")
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

            
if __name__ == "__main__":
    cart =  ShoppingCart("Gabriela Johnson", "February 1, 2020")
    item1 = ItemToPurchase("Eggs", "White, Large, Pasture-rasied", 3.00, 3)
    item2 = ItemToPurchase("Hershey Bar", "Milk Chocolate", 1.50, 1)
    item3 = ItemToPurchase("Red Wine", "Cabernet Sauvignon", 55.00, 1)
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    cart.print_total()
    print()
    cart.print_description()

    
Gabriela Johnson's Shopping Cart - February 1, 2020
Number of Items: 5
Eggs 3 @ $ 3.00 = $9.00
Hershey Bar 1 @ $ 1.50 = $1.50
Red Wine 1 @ $ 55.00 = $55.00
Total: $65.50

Traceback (most recent call last):
  File "<pyshell#138>", line 11, in <module>
    cart.print_description()
AttributeError: 'ShoppingCart' object has no attribute 'print_description'. Did you mean: 'print_descriptions'?
if __name__ == "__main__":
    cart =  ShoppingCart("Gabriela Johnson", "February 1, 2020")
    item1 = ItemToPurchase("Eggs", "White, Large, Pasture-rasied", 3.00, 3)
    item2 = ItemToPurchase("Hershey Bar", "Milk Chocolate", 1.50, 1)
    item3 = ItemToPurchase("Red Wine", "Cabernet Sauvignon", 55.00, 1)
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    cart.print_total()
    print()
    cart.print_descriptions()

    
Gabriela Johnson's Shopping Cart - February 1, 2020
Number of Items: 5
Eggs 3 @ $ 3.00 = $9.00
Hershey Bar 1 @ $ 1.50 = $1.50
Red Wine 1 @ $ 55.00 = $55.00
Total: $65.50

Gabriela Johnson's Shopping Cart - February 1, 2020
Item Descriptions
Eggs: White, Large, Pasture-rasied
Hershey Bar: Milk Chocolate
Red Wine: Cabernet Sauvignon

def print_menu(shopping_cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")
        if choice == 'a':
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item_to_purchase = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            shopping_cart.add_item(item_to_purchase)
        elif choice == 'r':
            item_name = input("Enter the item name to remove: ")
            shopping_cart.remove_item(item_name)
        elif choice == 'c':
            pass
        elif choice == 'i':
            shopping_cart.print_descriptions()
        elif choice == 'o':
            shopping_cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

            
def main():
    cart = ShoppingCart("Gabriela Johnson", "February 1, 2020")
    print_menu(cart)

    
if __name__ == "__main__":
    main()

    

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: a
Enter the item name: Snickers Bar
Enter the item description: Original 
Enter the item price: 2.30
Enter the item quantity: 5

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: r
Enter the item name to remove: Snickers Bar

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: c

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: i
Gabriela Johnson's Shopping Cart - February 1, 2020
Item Descriptions

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: o
Gabriela Johnson's Shopping Cart - February 1, 2020
Number of Items: 0
Total: $0.00

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: 
Invalid choice. Please choose a valid option.

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: 
Invalid choice. Please choose a valid option.

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: 
Invalid choice. Please choose a valid option.

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: q

class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

        
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name =  customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_item(self, item):
        self.cart_items.append(item)
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    def modify_item(self, modify_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity !=0:
                    item.item_quantity = modified_item.item_quantity
                return
            print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())
        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price: .2f} = ${item.item_price * item.item_quantity:.2f}")
        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost:.2f}")
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

            
if __name__ == "__main__":
    cart =  ShoppingCart("Gabriela Johnson", "February 1, 2020")
    item1 = ItemToPurchase("Eggs", "White, Large, Pasture-rasied", 3.00, 3)
    item2 = ItemToPurchase("Hershey Bar", "Milk Chocolate", 1.50, 1)
    item3 = ItemToPurchase("Red Wine", "Cabernet Sauvignon", 55.00, 1)
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    cart.print_total()
    print()
    cart.print_descriptions()

    
Gabriela Johnson's Shopping Cart - February 1, 2020
Number of Items: 5
Eggs 3 @ $ 3.00 = $9.00
Hershey Bar 1 @ $ 1.50 = $1.50
Red Wine 1 @ $ 55.00 = $55.00
Total: $65.50

Gabriela Johnson's Shopping Cart - February 1, 2020
Item Descriptions
Eggs: White, Large, Pasture-rasied
Hershey Bar: Milk Chocolate
Red Wine: Cabernet Sauvignon

def print_menu(shopping_cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")
        if choice == 'a':
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item_to_purchase = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            shopping_cart.add_item(item_to_purchase)
        elif choice == 'r':
            item_name = input("Enter the item name to remove: ")
            shopping_cart.remove_item(item_name)
        elif choice == 'c':
            pass
        elif choice == 'i':
            shopping_cart.print_descriptions()
        elif choice == 'o':
            shopping_cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

            
def main():
    cart = ShoppingCart("Gabriela Johnson", "February 1, 2020")
    print_menu(cart)

    
if __name__ == "__main__":
    main()

    

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: a
Enter the item name: Snickers
Enter the item description: Original
Enter the item price: 2.50
Enter the item quantity: 5

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: r
Enter the item name to remove: Hershey Bar
Item not found in cart. Nothing removed.

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: q

class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

        
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name =  customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_item(self, item):
        self.cart_items.append(item)
    def remove_item(self, item_name):
        item_name_lower = item_name.lower()
        for item in self.cart_items.copy():
            if item.item_name.lower() == item_name_lower:
                self.cart_items.remove(item)
                return
            print("Item not found in cart. Nothing removed.")
    def modify_item(self, modify_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity !=0:
                    item.item_quantity = modified_item.item_quantity
                return
            print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())
        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price: .2f} = ${item.item_price * item.item_quantity:.2f}")
        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost:.2f}")
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

            
if __name__ == "__main__":
    cart =  ShoppingCart("Gabriela Johnson", "February 1, 2020")
    item1 = ItemToPurchase("Eggs", "White, Large, Pasture-rasied", 3.00, 3)
    item2 = ItemToPurchase("Hershey Bar", "Milk Chocolate", 1.50, 1)
    item3 = ItemToPurchase("Red Wine", "Cabernet Sauvignon", 55.00, 1)
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    cart.print_total()
    print()
    cart.print_descriptions()

    
Gabriela Johnson's Shopping Cart - February 1, 2020
Number of Items: 5
Eggs 3 @ $ 3.00 = $9.00
Hershey Bar 1 @ $ 1.50 = $1.50
Red Wine 1 @ $ 55.00 = $55.00
Total: $65.50

Gabriela Johnson's Shopping Cart - February 1, 2020
Item Descriptions
Eggs: White, Large, Pasture-rasied
Hershey Bar: Milk Chocolate
Red Wine: Cabernet Sauvignon

def print_menu(shopping_cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")
        if choice == 'a':
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item_to_purchase = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            shopping_cart.add_item(item_to_purchase)
        elif choice == 'r':
            item_name = input("Enter the item name to remove: ")
            shopping_cart.remove_item(item_name)
        elif choice == 'c':
            pass
        elif choice == 'i':
            shopping_cart.print_descriptions()
        elif choice == 'o':
            shopping_cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

            
def main():
    cart = ShoppingCart("Gabriela Johnson", "February 1, 2020")
    print_menu(cart)

    
if __name__ == "__main__":
    main()

    

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: a
Enter the item name: Snickers Bar
Enter the item description: Original
Enter the item price: 2.50
Enter the item quantity: 4

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: r
Enter the item name to remove: Red Wine
Item not found in cart. Nothing removed.

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: q

class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

        
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name =  customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_item(self, item):
        self.cart_items.append(item)
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
            
SyntaxError: invalid syntax
class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name =  customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_item(self, item):
        self.cart_items.append(item)
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
            
SyntaxError: invalid syntax


class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

        
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name =  customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_item(self, item):
        self.cart_items.append(item)
    def remove_item(self, item_name):
        item_name_lower = item_name.lower()
        for item in self.cart_items.copy():
            if item.item_name.lower() == item_name_lower:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    def modify_item(self, modify_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity !=0:
                    item.item_quantity = modified_item.item_quantity
                return
            print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())
        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price: .2f} = ${item.item_price * item.item_quantity:.2f}")
        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost:.2f}")
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

            
if __name__ == "__main__":
    cart =  ShoppingCart("Gabriela Johnson", "February 1, 2020")
    item1 = ItemToPurchase("Eggs", "White, Large, Pasture-rasied", 3.00, 3)
    item2 = ItemToPurchase("Hershey Bar", "Milk Chocolate", 1.50, 1)
    item3 = ItemToPurchase("Red Wine", "Cabernet Sauvignon", 55.00, 1)
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    cart.print_total()
    print()
    cart.print_descriptions()
    
SyntaxError: invalid syntax
class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

        
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name =  customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_item(self, item):
        self.cart_items.append(item)
    def remove_item(self, item_name):
        item_name_lower = item_name.lower()
        for item in self.cart_items.copy():
            if item.item_name.lower() == item_name_lower:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    def modify_item(self, modify_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity !=0:
                    item.item_quantity = modified_item.item_quantity
                return
            print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())
        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price: .2f} = ${item.item_price * item.item_quantity:.2f}")
        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost:.2f}")
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

            
if __name__ == "__main__":
    cart =  ShoppingCart("Gabriela Johnson", "February 1, 2020")
    item1 = ItemToPurchase("Eggs", "White, Large, Pasture-rasied", 3.00, 3)
    item2 = ItemToPurchase("Hershey Bar", "Milk Chocolate", 1.50, 1)
    item3 = ItemToPurchase("Red Wine", "Cabernet Sauvignon", 55.00, 1)
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    cart.print_total()
    print()
    cart.print_descriptions()

    
Gabriela Johnson's Shopping Cart - February 1, 2020
Number of Items: 5
Eggs 3 @ $ 3.00 = $9.00
Hershey Bar 1 @ $ 1.50 = $1.50
Red Wine 1 @ $ 55.00 = $55.00
Total: $65.50

Gabriela Johnson's Shopping Cart - February 1, 2020
Item Descriptions
Eggs: White, Large, Pasture-rasied
Hershey Bar: Milk Chocolate
Red Wine: Cabernet Sauvignon

def print_menu(shopping_cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")
        if choice == 'a':
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item_to_purchase = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            shopping_cart.add_item(item_to_purchase)
        elif choice == 'r':
            item_name = input("Enter the item name to remove: ")
            shopping_cart.remove_item(item_name)
        elif choice == 'c':
            pass
        elif choice == 'i':
            shopping_cart.print_descriptions()
        elif choice == 'o':
            shopping_cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

            
def main():
    cart = ShoppingCart("Gabriela Johnson", "February 1, 2020")
    print_menu(cart)

    
if __name__ == "__main__":
    main()

    

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: a
Enter the item name: Snickers Bar
Enter the item description: Original
Enter the item price: 2.50
Enter the item quantity: 4

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: r
Enter the item name to remove: Red Wine
Item not found in cart. Nothing removed.

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: c

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: q

class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

        
lass ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name =  customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_item(self, item):
        self.cart_items.append(item)
    def remove_item(self, item_name):
        item_name_lower = item_name.lower()
        for item in self.cart_items.copy():
            if item.item_name.lower() == item_name_lower:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
        
SyntaxError: invalid syntax

class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

        
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name =  customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_item(self, item):
        self.cart_items.append(item)
    def remove_item(self, item_name):
        item_name_lower = item_name.lower()
        for item in self.cart_items.copy():
            if item.item_name.lower() == item_name_lower:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")
    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                return
            print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())
        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price: .2f} = ${item.item_price * item.item_quantity:.2f}")
        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost:.2f}")
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

            
if __name__ == "__main__":
    cart =  ShoppingCart("Gabriela Johnson", "February 1, 2020")
    item1 = ItemToPurchase("Eggs", "White, Large, Pasture-rasied", 3.00, 3)
    item2 = ItemToPurchase("Hershey Bar", "Milk Chocolate", 1.50, 1)
    item3 = ItemToPurchase("Red Wine", "Cabernet Sauvignon", 55.00, 1)
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    cart.print_total()
    print()
    cart.print_descriptions()

    
Gabriela Johnson's Shopping Cart - February 1, 2020
Number of Items: 5
Eggs 3 @ $ 3.00 = $9.00
Hershey Bar 1 @ $ 1.50 = $1.50
Red Wine 1 @ $ 55.00 = $55.00
Total: $65.50

Gabriela Johnson's Shopping Cart - February 1, 2020
Item Descriptions
Eggs: White, Large, Pasture-rasied
Hershey Bar: Milk Chocolate
Red Wine: Cabernet Sauvignon

def print_menu(shopping_cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")
        if choice == 'a':
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item_to_purchase = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            shopping_cart.add_item(item_to_purchase)
        elif choice == 'r':
            item_name = input("Enter the item name to remove: ")
            shopping_cart.remove_item(item_name)
        elif choice == 'c':
            item_name = input("Enter the item name to modify: ")
            new_quantity = int(input("Enter the new quantity: "))
            item_to_modify = ItemToPurchase(item_name, quantity=new_quantity)
            shopping_cart.modify_item(item_to_modify)
        elif choice == 'i':
            shopping_cart.print_descriptions()
        elif choice == 'o':
            shopping_cart.print_total()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

            
def main():
    cart = ShoppingCart("Gabriela Johnson", "February 1, 2020")
    print_menu(cart)

    
if __name__ == "__main__":
    main()

    

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: a
Enter the item name: Snickers Bar
Enter the item description: Original
Enter the item price: 2.50
Enter the item quantity: 5

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: r
Enter the item name to remove: Cup
Item not found in cart. Nothing removed.

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: c
Enter the item name to modify: Snickers Bar
Enter the new quantity: 3

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: i
Gabriela Johnson's Shopping Cart - February 1, 2020
Item Descriptions
Snickers Bar: Original

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: o
Gabriela Johnson's Shopping Cart - February 1, 2020
Number of Items: 3
Snickers Bar 3 @ $ 2.50 = $7.50
Total: $7.50

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: q

def print_menu(shopping_cart):
     while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("p - Output shopping cart")
        print("d - Output items' descriptions")
        print("q - Quit")
        choice = input("Choose an option: ")
        if choice == 'a':
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item_to_purchase = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            shopping_cart.add_item(item_to_purchase)
        elif choice == 'r':
            item_name = input("Enter the item name to remove: ")
            shopping_cart.remove_item(item_name)
        elif choice == 'c':
            item_name = input("Enter the item name to modify: ")
            new_quantity = int(input("Enter the new quantity: "))
            item_to_modify = ItemToPurchase(item_name, quantity=new_quantity)
            shopping_cart.modify_item(item_to_modify)
        elif choice == 'i':
           shopping_cart.print_descriptions()
        elif choice == 'o':
            shopping_cart.print_total()
        elif choice == 'p':
            shopping_cart.print_total()
        elif choice == 'd':
            shopping_cart.print_descriptions()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

            
def main():
    cart = ShoppingCart("Gabriela Johnson", "February 1, 2020")
    print_menu(cart)

    
if __name__ == "__main__":
    main()

    

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
p - Output shopping cart
d - Output items' descriptions
q - Quit
Choose an option: p
Gabriela Johnson's Shopping Cart - February 1, 2020
Number of Items: 0
Total: $0.00

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
p - Output shopping cart
d - Output items' descriptions
q - Quit
Choose an option: d
Gabriela Johnson's Shopping Cart - February 1, 2020
Item Descriptions

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
p - Output shopping cart
d - Output items' descriptions
q - Quit
Choose an option: q

class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        item_name_lower = item_name.lower()
        for item in self.cart_items.copy():
            if item.item_name.lower() == item_name_lower:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_description != "none":
                    item.item_description = modified_item.item_description
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        num_items = self.get_num_items_in_cart()
        if num_items == 0:
            print("SHOPPING CART IS EMPTY")
...             return
... 
...         print("Number of Items:", num_items)
...         for item in self.cart_items:
...             print(f"{item.item_name} {item.item_quantity} @ ${item.item_price:.2f} = ${item.item_price * item.item_quantity:.2f}")
...         total_cost = self.get_cost_of_cart()
...         print(f"Total: ${total_cost:.2f}")
... 
...     def print_descriptions(self):
...         print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
...         print("Item Descriptions")
...         for item in self.cart_items:
...             print(f"{item.item_name}: {item.item_description}")
... 
... 
... def print_menu(shopping_cart):
...     while True:
...         print("\nMENU")
...         print("a - Add item to cart")
...         print("r - Remove item from cart")
...         print("c - Change item quantity")
...         print("i - Output items' descriptions")
...         print("o - Output shopping cart")
...         print("p - Output shopping cart")
...         print("d - Output items' descriptions")
...         print("q - Quit")
... 
...         choice = input("Choose an option: ")
... 
...         if choice == 'a':
...             item_name = input("Enter the item name: ")
...             item_description = input("Enter the item description: ")
...             item_price = float(input("Enter the item price: "))
...             item_quantity = int(input("Enter the item quantity: "))
...             item_to_purchase = ItemToPurchase(item_name, item_description, item_price, item_quantity)
...             shopping_cart.add_item(item_to_purchase)
...         elif choice == 'r':
...             item_name = input("Enter the item name to remove: ")
...             shopping_cart.remove_item(item_name)
...         elif choice == 'c':
...             item_name = input("Enter the item name to modify: ")
...             new_quantity = int(input("Enter the new quantity: "))
...             item_to_modify = ItemToPurchase(item_name, quantity=new_quantity)
...             shopping_cart.modify_item(item_to_modify)
...         elif choice == 'i':
...             shopping_cart.print_descriptions()
...         elif choice == 'o' or choice == 'p':
...             shopping_cart.print_total()
...         elif choice == 'd':
...             shopping_cart.print_descriptions()
...         elif choice == 'q':
...             break
...         else:
...             print("Invalid choice. Please choose a valid option.")
... 
... 
... def main():
...     cart = ShoppingCart("John Doe", "February 1, 2020")
...     print_menu(cart)
... 
... 
... if __name__ == "__main__":
...     main()
... 
SyntaxError: invalid syntax
>>> 
