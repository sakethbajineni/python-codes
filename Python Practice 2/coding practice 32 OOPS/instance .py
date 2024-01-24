class Cart:
    flat_discount=0
    min_bill=100
    def __init__(self):
        self.items={}
    def add_items(self,item_name,quantity):
        self.items[item_name]=quantity
    def display_items(self):
        print(self.items)
        self.flat_discount=20
        print(self.flat_discount)
a=Cart()
b=Cart()
a.add_items("book",3)
b.add_items("pen",5)
# print(a.items)
a.display_items()
b.display_items()

