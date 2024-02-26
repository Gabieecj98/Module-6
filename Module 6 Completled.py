Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:39) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
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
        print("Number of Items:", self.get_num_items_in_cart())
        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price:.2f} = ${item.item_price * item.item_quantity:.2f}")
        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost:.2f}")
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

            
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
    item1 = ItemToPurchase("Wine", "Cabernet Sauvignon", 99.00, 2)
    item2 = ItemToPurchase("Snickers", "Original", 1.50, 5)
    item3 = ItemToPurchase("Eggs", "Cage Free", 8.00, 1)
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
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
Enter the item name: Hershey Bar
Enter the item description: Milk Chocolate
Enter the item price: 1.59
Enter the item quantity: 3

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: r
Enter the item name to remove: Eggs

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: c
Enter the item name to modify: Wine
Enter the new quantity: 1

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
Wine: Cabernet Sauvignon
Snickers: Original
Hershey Bar: Milk Chocolate

MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
Choose an option: o
Gabriela Johnson's Shopping Cart - February 1, 2020
Number of Items: 9
Wine 1 @ $99.00 = $99.00
Snickers 5 @ $1.50 = $7.50
Hershey Bar 3 @ $1.59 = $4.77
Total: $111.27

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
        print("Number of Items:", self.get_num_items_in_cart())
        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price:.2f} = ${item.item_price * item.item_quantity:.2f}")
        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost:.2f}")
    def print_descriptions(self):
...         print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
...         print("Item Descriptions")
...         for item in self.cart_items:
...             print(f"{item.item_name}: {item.item_description}")
... 
...             
>>> def print_menu(shopping_cart):
...     while True:
...         print("\nMENU")
...         print("a - Add item to cart")
...         print("r - Remove item from cart")
...         print("c - Change item quantity")
...         print("i - Output items' descriptions")
...         print("o - Output shopping cart")
...         print("q - Quit")
...         choice = input("Choose an option: ")
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
...         elif choice == 'o':
...             shopping_cart.print_total()
...         elif choice == 'q':
...             break
...         else:
...             print("Invalid choice. Please choose a valid option.")
... 
...             
>>> if __name__ == "__main__":
...     cart = ShoppingCart("Gabriela Johnson", "February 1, 2020")
...     item1 = ItemToPurchase("Wine", "Cabernet Sauvignon", 99.00, 2)
...     item2 = ItemToPurchase("Snickers", "Original", 1.50, 5)
...     item3 = ItemToPurchase("Eggs", "Cage Free", 8.00, 1)
...     cart.add_item(item1)
...     cart.add_item(item2)
...     cart.add_item(item3)
...     cart.print_total()
...     print()
...     cart.print_descriptions()
... 
...     
Gabriela Johnson's Shopping Cart - February 1, 2020
Number of Items: 8
Wine 2 @ $99.00 = $198.00
Snickers 5 @ $1.50 = $7.50
Eggs 1 @ $8.00 = $8.00
Total: $213.50

Gabriela Johnson's Shopping Cart - February 1, 2020
Item Descriptions
Wine: Cabernet Sauvignon
Snickers: Original
Eggs: Cage Free
>>> 
