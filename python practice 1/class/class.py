class Moblie:
    def __init__(self,model,camera):
        self.model=model
        self.camera=camera
    def make_call(self,number):
        print("calling..{}".format(number))
mobile_obj=Moblie("Galaxy M51","64 MP")
mobile_obj.make_call(9515901050)
print(mobile_obj.model)