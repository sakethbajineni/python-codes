class Mobile:
    def __init__(self,model,camera):
        self.model=model
        self.camera=camera
    def get_model(self):
        print(self.model)
    def update_model(self,model):
        self.model=model
mobile_obj_1=Mobile("Realme 10 pro 5g","108MP")
mobile_obj_1.get_model()
mobile_obj_1.update_model("Realme")
mobile_obj_1.get_model()