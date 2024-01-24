class Product:
    def __init__(self,name,price,deal_price,ratings):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.ratings=ratings
    def display_product_details(self):
        print("product Name: {}".format(self.name))
        print("product price: {}".format(self.price))
        print("deal_price: {} ".format(self.deal_price))
        print("ratings: {}".format(self.ratings))
p=Product("Book",20,15,4)
# p.display_product_details()

class Electronic_items(Product):
    def set_warranty(self,warranty_in_months):
        self.warranty_in_months=warranty_in_months
    def get_warranty(self):
        return self.warranty_in_months
    
    def display_electronic_details(self):
        self.display_product_details()
        print("warranty in months : {}".format(self.warranty_in_months))
        print("")
        
class Grocery_item(Product):
    def set_expiry_date(self,expiry_date):
        self.expiry_date=expiry_date
    def get_expiry_date(self):
        return self.expiry_date
    def display_grocery_details(self):
        self.display_product_details()
        print("expiry_date : {}".format(self.expiry_date))

    


class Order:
    def __init__(self,delivery_speed,delivery_address):
        self.items_in_cart=[]
        self.delivery_speed=delivery_speed
        self.delivery_address=delivery_address
    def add_item(self,product,quantity):
        self.items_in_cart.append((product,quantity))
    def display_order_details(self):
        for product,quantity in self.items_in_cart:
            Product.display_product_details()
            print("Quantity : {}".format(quantity))
            


        

e_item=Electronic_items("realme 10 pro",25000,20000,4.4)
# e_item.display_product_details()
e_item.set_warranty(24)
# print(e_item.get_warranty())
e_item.display_electronic_details()

g_item=Grocery_item("milk",25,20,4.6)
g_item.set_expiry_date(2033)
g_item.display_grocery_details()

# order=Order("prime","hyderabad")
# order.add_item("tv",2)
# order.add_item("mlk",5)
# order.display_order_details()