# class cars
class Cars:
    def __init__(self, brand, model, color,fuel):
        self.brand= brand
        self.model= model
        self.color=color
        self.fuel= fuel

    def speed(self, kilometer_per_hour):
        self.kilometer= kilometer_per_hour
        #pass

    def start(self, move):
        self.time_start= move
        #pass
    def halt(self, paulse):
        self.stop= paulse
        #pass
    def air_condition(self, temperature):
        self.temperature =temperature
       # pass
    def usb_port(self,port):
        self.port= port
        #pass

# declaring object
   
toyota_car = Cars("Henux","Camry","Blue", "Petrol")

print("The Brand of the Car is :", toyota_car.brand)
print("The model of the car is:", toyota_car.model)
print("The Color of the car is :", toyota_car.color)
print("The car uses :", toyota_car.fuel)

toyota_car.start("Remote control")
toyota_car.halt("brake")
toyota_car.air_condition(20)
toyota_car.usb_port("Charging USB port")
        
print("the car is control with :", toyota_car.time_start)
print("the car uses  :", toyota_car.stop, "to stop")
print("the car has :", toyota_car.temperature, "Decree Air condition")
print("the car has  :", toyota_car.port, "For phone charging")




        

     