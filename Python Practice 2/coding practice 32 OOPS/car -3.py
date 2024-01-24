class Car:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self.color=color
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction
        self.is_engine_started=False
        self.current_speed=0
    def start_engine(self):
        self.is_engine_started=True
    def stop_engine(self):
        self.is_engine_started=False
    def accelerate(self):
        if self.is_engine_started==False:
            print("Car not yet started")
        else:
            self.current_speed+=self.acceleration
            if self.current_speed>self.max_speed:
                self.current_speed=self.max_speed
    def apply_brakes(self):
        if self.current_speed>=0:
            self.current_speed=self.current_speed-self.tyre_friction
    def sound_horn(self):
        if self.is_engine_started==True:
            print("Beep,Beep")
        else:
            print("The car not started yet")

def default_test():
    car=Car(color="Red",max_speed=50,acceleration=10,tyre_friction=3)
    car.sound_horn()
    car.start_engine()
    car.sound_horn()
    car.accelerate()
    # print(car.current_speed)
    print(car.current_speed)
    car.apply_brakes()
    print(car.current_speed)
    car.apply_brakes()
    print(car.current_speed)

    car.apply_brakes
    # car.accelerate()
    # car.accelerate()
    print(car.current_speed)
    car.apply_brakes()
    print(car.current_speed)

default_test()