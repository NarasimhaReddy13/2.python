"""
Online Shopping 

. Different types of products
. Users can select those products and order them
. Delivery charges may vary based on the delivery speed selected

"""
"""

Product ---  Name, Price, Deal Price, rating, display_product_details(self) -------- Common to all
ElectronicItem + Product  ---- Warranty in Months, Specifications, get_warranty(self) + Inherited from product
GroceryItem + Product  --- Packed Date, Expiry Data, get_expiry_date(self) _ Inherited from product
Laptop + ElectronicItem ---- Operating System , Screen Size + Inherited all from ElectronicItem 

"""

# To model OOP in Python we need class -- with Capital Letter
class Product:
    def __init__(self, name, price, deal_price, ratings): # To define or initialize attributes --- its a special (initializer) method
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_saved = price - deal_price  # Extra -- derived attribute


    # To display product details
    def display_product_details(self): # Instance method
        print("Product: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal Price: {}".format(self.deal_price))
        print("Ratings: {}".format(self.ratings))
        print("You Saved: {}".format(self.you_saved))


    # Method to get deal price
    def get_deal_price(self):
        return self.deal_price



class ElectronicItem(Product): # As we need same attributes in Product --- so we are inheriting Product
    # We can use attributes and methods of Product class

    def __init__(self, name, price, deal_price, ratings, warranty_in_months): 
        # Writing methods in sub which are already in Super class --- is Method Overriding

        super().__init__(name, price, deal_price, ratings)
        self.warranty_in_months = warranty_in_months

    def display_product_details(self):
        super().display_product_details()
        print("Warranty: {} months".format(self.warranty_in_months))



class GroceryItem(Product):

    def __init__(self, name, price, deal_price, ratings, expiry_date):

        super().__init__(name, price, deal_price, ratings)
        self.expiry_date = expiry_date

    def display_product_details(self):
        super().display_product_details()
        print("Expiry Date: {}".format(self.expiry_date))




# To Buy Products
class Order:

    # As delivery Charges are fixed -- so we are not writing in instance --- So write in class variable

    delivery_charges = {"Normal": 0, "Prime Deliver": 100}

    def __init__(self, deliver_method, delivery_address):
        self.items_in_cart = [] # Add items in tuples (product, quantity)

        self.delivery_method = deliver_method
        self.delivery_address = delivery_address


    def add_items(self, product, quantity):
        item = (product, quantity)  # here product is a composition --- as it is a instance of product ( Modelling instance of one class as attributes of another class )

        self.items_in_cart.append(item)

    def display_order_details(self):
        print("Delivery Method: {}".format(self.delivery_method))
        print("Delivery Address: {}".format(self.delivery_address))

        print("")

        print("Products")
        print("-----------------------------------------------")

        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}".format(quantity))
            print("")

        print("-----------------------------------------------")

        total_bill = self.get_total_bill()
        print("Total Bill: {}".format(total_bill))


    def get_total_bill(self):
        total_bill = 0
        for product, quantity in self.items_in_cart:
            total_bill += product.get_deal_price() * quantity



        order_delivery_charges = Order.delivery_charges[self.delivery_method]
        total_bill = total_bill + order_delivery_charges

        return total_bill


    @classmethod
    def update_delivery_charges(cls, delivery_method, charges):
        cls.delivery_charges[delivery_method] = charges 



class Laptop(ElectronicItem):  # Multi-level Inheritance
    def __int__(self, name, price, deal_price, ratings, warranty_in_months, ram, storage):
        super().__init__(name, price, deal_price, ratings, warranty_in_months)
        self.ram =ram
        self.storage = storage

    def display_product_details(self):
        super().display_product_details()

        print("Ram: {}".format(self.ram))
        print("Storage: {}".format(self.storage))




# Creating Product # pro --- Instance of Product

# pro = Product("TV", 40000, 25000, 3.5, 12)  
# pro.display_product_details()


tv = ElectronicItem("TV", 25000, 15000, 3.5, 12)  
# tv.display_product_details()

milk = GroceryItem("Milk", 40, 30, 4.6, "Jan 2030")
# milk.display_product_details()

my_order = Order("Normal", "Hyderabad")
my_order.add_items(tv, 1)
my_order.add_items(milk, 3)



Order.update_delivery_charges("Normal", 10)
my_order.display_order_details()

# lenovo_lap = Laptop("Lenovo 123", 45000, 35000, 4.5, 24, "8 GB", "1 TB SSD")
# lenovo_lap.display_product_details()













class Mobile:
    def __init__(self, model, camera):
        self.model = model
        self.camera= camera

    def update_model(self, model):
        self.model = model

    def make_call(self,number):
        print("calling..{}".format(number))

mobile_obj = Mobile("iPhone 12 Pro", "12 MP")
mobile_obj.make_call(9876543210)

mobile_obj2 = Mobile("iPhone 11 Pro", "8 MP")
mobile_obj2.make_call(98) # Can create multiple Instances
print(mobile_obj2)
print(type(mobile_obj2))

print(mobile_obj2.model)


mobile_obj.update_model("Samsung")
print(mobile_obj.model)


















class Cart:
    flat_discount = 0
    min_bill = 100
    def __init__(self):
        self.items = {}
        self.price_details = {"book": 500, "laptop": 30000}

    def add_item(self, item_name, quantity):
        self.items[item_name] = quantity

    def remove_item(self, item_name):
        del self.items[item_name]

    def update_quantity(self, item_name, quantity):
        self.items[item_name] = quantity

    def get_cart_items(self):
        cart_items = list(self.items.keys())
        return cart_items

    def get_total_price(self):
        total_price = 0
        for item, quantity in self.items.items():
            total_price += quantity * self.price_details[item]
        return total_price

    @staticmethod
    def greet():
        print('Have A Great Shopping')


cart_obj = Cart()
cart_obj.add_item("book", 3)
cart_obj.add_item("laptop", 1)
print(cart_obj.get_total_price())
cart_obj.remove_item("laptop")
print(cart_obj.get_cart_items())
cart_obj.update_quantity("book", 2)
print(cart_obj.get_total_price())



print(Cart.min_bill)

Cart.greet()