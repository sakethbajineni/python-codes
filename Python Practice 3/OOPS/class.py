class Car:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self.color=color
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction
def defalut_test():
    car=Car(color="Red",max_speed=200,acceleration=10,tyre_friction=3)
    print(car.color)
    print(car.max_speed)
    print(car.acceleration)
    print(car.tyre_friction)

defalut_test()