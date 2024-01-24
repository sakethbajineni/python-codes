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
    def __init__(self, name, price, deal_price, ratings,warranty_in_months):
        super().__init__(name, price, deal_price, ratings)
        self.warranty_in_months=warranty_in_months

    def display_product_details2(self):
        self.display_product_details()
        print("warranty in months : {}".format(self.warranty_in_months))
        
class Grocery_item(Product):
    def __init__(self, name, price, deal_price, ratings,expiry_date):
        super().__init__(name, price, deal_price, ratings)
        self.expiry_date=expiry_date
  
    def display_product_details2(self):
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
            product.display_product_details2()
            print("Quantity : {}".format(quantity))
            print("")

        

Tv=Electronic_items("Tv",25000,20000,4.4,2024)
# e_item.display_product_details()
# print(e_item.get_warranty())
# e_item.display_electronic_details()

Milk=Grocery_item("milk",25,20,4.6,99)
# g_item.display_grocery_details()

order=Order("prime","hyderabad")
order.add_item(Tv,3)
order.add_item(Milk,8)
order.display_order_details()