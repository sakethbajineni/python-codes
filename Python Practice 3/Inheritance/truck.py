class Car:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self.color=color
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction
        self.is_engine_started=False
        self.speed=0
        self.current_speed=0
    def start_engine(self):
        self.is_engine_started=True
        print(self.is_engine_started)
        
    def stop_engine(self):
        self.is_engine_started=False
        print(self.is_engine_started)
    def accelerate(self):
        if not self.is_engine_started:
            print("Car has not started yet")
        else:
            self.current_speed+=self.acceleration
            if self.current_speed>=self.max_speed:
                self.current_speed=self.max_speed
           
    def apply_brakes(self):
        if self.current_speed>=self.tyre_friction:
            self.current_speed-=self.tyre_friction
        else:
            print("Car has not started yet")

    def sound_horn(self):
        if self.is_engine_started:
            print("Honk Honk")
        else:
            print("Car has not started yet")
class Truck(Car):
    def __init__(self, color, max_speed, acceleration, tyre_friction,max_cargo_weight):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        self.max_cargo_weight=max_cargo_weight
        self.cargo_weight=0
        self.load=0
    def load_cargo(self,cargo_weight):
        if self.load>=self.max_cargo_weight:
            print("Cannot load cargo more than max limit : 100")
        elif self.is_engine_started:
            print("Cannot load cargo ,truck in motion")
        self.load=cargo_weight
    def unload_cargo(self,cargo_weight):
        if self.is_engine_started:
            print("Cannot load the cargo,truck is in motion")
        else:
            self.load=self.load-cargo_weight
            if self.load<=0:
                self.load=0

    def sound_horn(self):
        super().sound_horn()


def default_test():
    truck=Truck(color="Red",max_speed=250,acceleration=10 ,tyre_friction=3 ,max_cargo_weight=100)
    print(truck.is_engine_started)
    truck.load_cargo(cargo_weight=50)
    print(truck.load)
    truck.unload_cargo(cargo_weight=25)
    print(truck.load)
    truck.unload_cargo(cargo_weight=70)
    print(truck.load)
    truck.load_cargo(cargo_weight=120)
    truck.load_cargo(cargo_weight=20)

    truck.start_engine()
    print(truck.is_engine_started)
    truck.load_cargo(cargo_weight=40)
    truck.unload_cargo(cargo_weight=10)
    truck.sound_horn()
    truck.stop_engine()
    truck.sound_horn()
default_test()