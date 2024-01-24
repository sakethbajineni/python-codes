class Cart:
    min_value=10
    flat_discount=20
    def __init__(self):
        pass
    def display_name(self):
        print(self.flat_discount)
    @classmethod
    def update_flat_discount(cls,new_flat_discount):
        cls.flat_discount=new_flat_discount
    @staticmethod
    def greet():
        print("static method")
a=Cart()
print(Cart.flat_discount)
Cart.update_flat_discount(50)
print(Cart.flat_discount)
a.display_name()
print(Cart.greet())


