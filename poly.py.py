class Instrument:
    def move(self):
        print("Instrument is playing")
        
class Guitar(Instrument):
    def move(self):
         print ("Strumming the guitar")
                
class Pino(Instrument):
    def move(self):
        print("Playing the piano")

instrument =  [Guitar() , Pino()]
for i in instrument:
    i.move()                       








class Vehicle:
    def move (self):
        print("Vehicle is moving")
        
class Car(Vehicle):
    def move(self):
        print("Driving on the road")
        
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")
        
vehicle =[Car(), Bicycle()]
for v in vehicle:
 v.move()