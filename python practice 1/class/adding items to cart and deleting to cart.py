class Flipkart():
    def __init__(self):
        self.items={}
        self.priceDetails={"notebook":20,"pencil":10}
    def add_items(self,itemname,quantity):
        self.items[itemname]=quantity
    def removing_from_cart(self,item):
        del self.items[item]
    def getting_items(self):
        print(self.items)
    def total_price(self):
        total_price=0
        for itemname,quantity in self.items.items():
            total_price+=self.priceDetails[itemname]*quantity
        return total_price


book_object=Flipkart()
adding=book_object.add_items("notebook",5)
book_object.getting_items()
book_object.add_items("pencil",5)
book_object.getting_items()
removing=book_object.removing_from_cart("notebook")


book_object.getting_items()
total_p=book_object.total_price()
print(total_p)

