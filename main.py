class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_quantity(self, quantity):
        self.quantity = quantity


class DiscountedProduct(Product):
    def __init__(self, id, name, price, quantity, discount_percentage):
        super().__init__(id, name, price, quantity)
        self.discount_percentage = discount_percentage

    def get_discount_percentage(self):
        return self.discount_percentage

    def get_price(self):
        discount = self.price * (self.discount_percentage / 100)
        discounted_price = self.price - discount
        return discounted_price


def add_product(inventory, product):
    product_id = get_unique_id(inventory)
    if 'discount' in product:
        discounted_product = DiscountedProduct(
            product_id, product['name'], product['price'], product['quantity'], product['discount']
        )
        inventory[product_id] = discounted_product
    else:
        inventory[product_id] = Product(product_id, product['name'], product['price'], product['quantity'])
    print("Product added successfully!!!")


def update_product(inventory, product):
    product_id = product.get_id()
    if product_id in inventory:
        inventory[product_id] = product
        print("Product updated successfully!!!")
    else:
        print("Product ID not found in the inventory.")


def remove_product(inventory, product_id):
    if product_id in inventory:
        del inventory[product_id]
        print("Product removed successfully!!!")
    else:
        print("Product ID not found in the inventory.")


def search_product(inventory, search_query):
    found_products = []
    for product in inventory.values():
        if search_query.lower() in product.get_name().lower():
            found_products.append(product)

    if found_products:
        print("Matching products:")
        display_products(found_products)
    else:
        print("No matching products found.")


def display_products(products):
    for product in products:
        print("---------------------------------------------------------------------------")
        print(
            f"ID: {product.get_id()}, Name: {product.get_name()}, Price: ${product.get_price():.2f}, "
            f"Quantity: {product.get_quantity()}, Discount: {product.get_discount_percentage()}%")

        print("---------------------------------------------------------------------------")


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_unique_id(inventory):
    if inventory:
        return max(inventory.keys()) + 1
    else:
        return 1


def display_inventory(inventory):
    if inventory:
        print("Current inventory:")
        display_products(inventory.values())
    else:
        print("Inventory is empty.")


def main():
    inventory = {}

    while True:
        print("====== Inventory Management System ======")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Remove Product")
        print("4. Search Product")
        print("5. Display Inventory")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter product name: ")
            price = get_float_input("Enter product price: ")
            quantity = get_int_input("Enter product quantity: ")
            discount = get_int_input("Enter discount %: ")

            product = {'name': name, 'price': price, 'quantity': quantity, 'discount': discount}
            add_product(inventory, product)

        elif choice == '2':
            product_id = int(input("Enter product ID: "))
            if product_id in inventory:
                product = inventory[product_id]
                name = input("Enter new product name: ")
                price = float(input("Enter new product price: "))
                quantity = int(input("Enter new product quantity: "))
                discount = int(input("Enter new product discount: "))
                product.set_name(name)
                product.set_price(price)
                product.set_quantity(quantity)
                product.discount_percentage = discount
                update_product(inventory, product)
            else:
                print("Product ID not found in the inventory.")

        elif choice == '3':
            product_id = int(input("Enter product ID: "))
            remove_product(inventory, product_id)

        elif choice == '4':
            search_query = input("Enter search query: ")
            search_product(inventory, search_query)

        elif choice == '5':
            display_inventory(inventory)

        elif choice == '6':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == '__main__':
    main()
