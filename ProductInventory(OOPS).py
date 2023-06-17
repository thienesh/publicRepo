class ProductInventory:
    def __init__(self):
        self.inventory = []

    def add_product(self, name, price, quantity):
        product = {"name": name, "price": price, "quantity": quantity}
        self.inventory.append(product)

    def remove_product(self, name):
        for product in self.inventory:
            if product["name"] == name:
                self.inventory.remove(product)
                break

    def get_product(self, name):
        for product in self.inventory:
            if product["name"] == name:
                return product
        return None

    def get_inventory_value(self):
        t_value = 0
        for product in self.inventory:
            t_value += product["price"] * product["quantity"]
        return t_value


# Create an instance of the ProductInventory class
inventory = ProductInventory()

# Add three products to the inventory
inventory.add_product("Apple", 0.99, 10)
inventory.add_product("Banana", 0.99, 20)
inventory.add_product("Orange", 1.49, 15)

# Remove the product with the name "Banana" from the inventory
inventory.remove_product("Banana")
inventory.remove_product("Apple")

# Get the product with the name from the inventory and print its details
apple_product = inventory.get_product("Apple")
Banana_product = inventory.get_product("Banana")
Orange_product = inventory.get_product("Orange")
No_product = inventory.get_product("kiwi")
if apple_product:
    print("Product Details:")
    print("Name:", apple_product["name"])
    print("Price:", apple_product["price"])
    print("Quantity:", apple_product["quantity"], "\n")
if Banana_product:
    print("Product Details:")
    print("Name:", Banana_product["name"])
    print("Price:", Banana_product["price"])
    print("Quantity:", Banana_product["quantity"], "\n")
if Orange_product:
    print("Product Details:")
    print("Name:", Orange_product["name"])
    print("Price:", Orange_product["price"])
    print("Quantity:", Orange_product["quantity"], "\n")
else:
    print("Product not found in inventory.")

# Calculate and print the total value of the inventory
total_value = inventory.get_inventory_value()
print("Total inventory value:", total_value)
