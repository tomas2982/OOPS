import pygame, random, math, sys, os, time
from pygame.locals import *
pygame.init()
mainClock = pygame.time.Clock()

class Engine:
    def __init__(self, hPwr: int, boom: int, engMass: float, rpm: int, topSpd: float) -> object:
        self.horsepower = hPwr
        self.engineBlowRate = boom
        self.engineMass = engMass
        self.rotationsPerMinute = rpm
        self.topSpeed = topSpd



class Wheels:
    def __init__(self, diameter: int, pop: int, tor: float) -> object:
        self.size = diameter
        self.popRate = pop
        self.torque=tor


class Body:
    def __init__(self, drag: float, mass: float) -> object:
        self.airDrag = drag
        self.bodyMass = mass


class Spoiler:
    def __init__(self, dForce: int, fRate: int) ->object:
        self.downForce = dForce     # add to force
        self.flipRate = fRate



class Boost:
    def __init__(self, nos: int, bigBoom: int) -> object:
        self.nitrous = nos      # to add to top speed
        self.exlpodeRate = bigBoom


class Car:

    def __init__(self, wheel, eng, bod):
        self.wheels = wheel
        self.engine = eng
        self.body = bod


    def setWheels(self):  # diameter of wheels, pop(chance of wheels popping), torque of axles
        wheels1 = Wheels(18, 2, 70)
        wheels2 = Wheels(19, 3, 85)
        wheels3 = Wheels(20, 5, 90)
        choice = input("Choose Wheels")

        if choice==1:
            setattr(self,'wheels',wheels1)
        if choice==2:
            setattr(self, 'wheels', wheels2)
        if choice==3:
            setattr(self, 'wheels', wheels3)
        N = random.randint(0, 100)
        #print(self.__wheels.size)                              # https://docs.python.org/2/library/random.html
        if self.wheels.popRate <= N:  # Wheels blow out
           self.wheels.Torque=0

        print ("Size ", self.wheels.size, " wheels with a torque of ", self.wheels.torque, " and poprate of ", self.wheels.popRate," have been added to car")

    def setEngine(self):  # hPwr of engine, boom(chance engine blows up), engMass, rpm, topSpeed of car
        engine1 = Engine(150, 1, .3, 4000, 300)
        engine2 = Engine(200, 2, .3, 4500, 325)
        engine3 = Engine(250, 5, .5, 5000, 365)
        choice = input("Choose Engine")
        if choice==1:
            self.engine = engine1
        if choice==2:
            self.engine = engine2
        if choice==3:
            self.engine = engine3
        #N = random.randint(0, 99)
      #  if self.__engine.engineBlowRate <= N:  # engine has blown out
     #       self.__engine.topSpeed=0

        print(self.engine.horsepower, " horsepower engine has been added to car")

    def setBody(self):  # drag (air resistance), mass
        body1 = Body(.25, 1.5)  # drag, mass
        body2 = Body(.2, 1.3)
        body3 = Body(.19, 1.3)
        choice = input("Choose Body")
        if choice == 1:
            self.body = body1
        if choice == 2:
            self.body = body2
        if choice == 3:
            self.body = body3
        print(self.body.bodyMass, " ton body has been installed on car")

    def carMass(self):  # addition of body mass and engine mass
        x = self.body.bodyMass + self.engine.engineMass
        return x

    def carForce(self):
        F = self.wheels.torque/(self.wheels.size/2)
        return F

    def getAccel(self):
        # https://www.carbibles.com/transmission-guide/ (to get the average gear ratio and derive torque on wheels)
        # https://www.quora.com/How-do-I-calculate-the-acceleration-of-a-car-when-I-have-rpm-torque-mass-horse-power-and-speed-at-different-gear-ratios
        # (to get the torque and calculate for the acceleration)
        f = self.carForce()              # self.__wheels.torque/(self.__wheels.size/2)
        m = self.carMass()                # self.__body.bodyMass + self.__engine.engineMass
        a = f / m
        return a

    """
    def getCurrentSpeed(self):
        F = self.carForce()             # self.__wheels.torque / (self.__wheels.size / 2)
        m = self.body.bodyMass + self.engine.engineMass
        a = F / m
        v0 = a*mainClock
        vf = a*mainClock + v0
        if vf >= self.engine.topSpeed:
            vf = self.engine.topSpeed
        return vf 
    """
    def getFinishTime(self):
        F = self.wheels.torque / (self.wheels.size / 2)
        m = self.body.bodyMass + self.engine.engineMass
        a = F / m
        d = 402.336  # distance (1/4 mile in meters)
        t = math.sqrt((2*d)/a)
        return t
    #acceleration = getAccel()
    #currentSpeed = getCurrentSpeed()
    #force = None
    #totalMass = carMass()


class sportCar(Car):
    def __init__(self, wheel, eng, bod, spoil):
        super().__init__(wheel, eng, bod)
        self.spoiler = spoil

    def setWheels(self): #diameter of wheels, pop(chance of wheels popping), torque of axles
        wheels1 = Wheels(18, 2, 70)
        wheels2 = Wheels(19, 3, 85)
        wheels3 = Wheels(20, 5, 90)
        wheels4 = Wheels(19, 2, 80)
        wheels5 = Wheels(20, 4, 95)
        choice = input("Choose Wheels")

        if choice==1:
            self.wheels = wheels1
        if choice==2:
            self.wheels = wheels2
        if choice==3:
            self.wheels = wheels3
        if choice == 4:
            self.wheels = wheels4
        if choice==5:
            self.wheels = wheels5
       # N = random.randint(0, 100) #https://docs.python.org/2/library/random.html
       # if self.__wheels.popRate <= N: #Wheels blow out
      #      self.__wheels.Torque=0

        print ("Wheel choice #" , choice, " has been chosen")

    def setEngine(self): #hPwr of engine, boom(chance engine blows up), engMass, rpm, topSpeed of car
        engine1 = Engine(150, 1, .3, 4000, 300)
        engine2 = Engine(200, 2, .3, 4500, 325)
        engine3 = Engine(250, 5, .5, 5000, 365)
        engine4 = Engine(250, 2, .2, 4500, 370)
        engine5 = Engine(300, 3, .3, 5000, 385)
        choice = input("Choose Engine")
        if choice==1:
            self.engine = engine1
        if choice==2:
            self.engine = engine2
        if choice==3:
            self.engine = engine3
        if choice==4:
            self.engine = engine4
        if choice==5:
            self.engine = engine5

     #   N = random.randint(0, 100)
     #   if self.__engine.engineBlowRate <= N:#engine has blown out
     #       self.__engine.topSpeed=0

        print("Engine choice #", choice, " has been chosen")

    def setBody(self): #drag (air resistance), mass
        body1 = Body(.25, 1.5) #drag, mass
        body2 = Body(.2, 1.3)
        body3 = Body(.19, 1.3)
        body4 = Body(.18, 1.4)
        body5 = Body(.18, 1.1)

        choice = input("Choose Engine")
        if choice == 1:
            self.body = body1
        if choice == 2:
            self.body = body2
        if choice == 3:
            self.body = body3
        if choice == 4:
            self.body = body4
        if choice == 5:
            self.body = body5
        print("Body choice #", choice, " has been chosen")


class hyperCar(sportCar):
    def __init__(self, wheel, eng, bod, spoil, boost):
        super().__init__(wheel, eng, bod, spoil)
        self.__spoiler = spoil

    def setWheels(self):  # diameter of wheels, pop(chance of wheels popping), torque of axles
        wheels1 = Wheels(18, 2, 70)
        wheels2 = Wheels(19, 3, 85)
        wheels3 = Wheels(20, 5, 90)
        wheels4 = Wheels(19, 2, 80)
        wheels5 = Wheels(20, 4, 95)
        choice = input("Choose Wheels")

        if choice == 1:
            self.wheels = wheels1
        if choice == 2:
            self.wheels = wheels2
        if choice == 3:
            self.wheels = wheels3
        if choice == 4:
            self.wheels = wheels4
        if choice == 5:
            self.wheels = wheels5
    #    N = random.randint(0, 100)  # https://docs.python.org/2/library/random.html
     #   if self.__wheels.popRate <= N:  # Wheels blow out
     #       self.__wheels.Torque = 0

        print("Wheel choice #", choice, " has been chosen")

    def setEngine(self):  # hPwr of engine, boom(chance engine blows up), engMass, rpm, topSpeed of car
        engine1 = Engine(150, 1, .3, 4000, 300)
        engine2 = Engine(200, 2, .3, 4500, 325)
        engine3 = Engine(250, 5, .5, 5000, 365)
        engine4 = Engine(250, 2, .2, 4500, 370)
        engine5 = Engine(300, 3, .3, 5000, 385)
        choice = input("Choose Engine")
        if choice == 1:
            self.engine = engine1
        if choice == 2:
            self.engine = engine2
        if choice == 3:
            self.engine = engine3
        if choice == 4:
            self.engine = engine4
        if choice == 5:
            self.engine = engine5

     #   N = random.randint(0, 100)
    #    if self.__engine.engineBlowRate <= N:  # engine has blown out
     #       self.__engine.topSpeed = 0

        print("Engine choice #", choice, " has been chosen")

    def setBody(self):  # drag (air resistance), mass
        body1 = Body(.25, 1.5)  # drag, mass
        body2 = Body(.2, 1.3)
        body3 = Body(.19, 1.3)
        body4 = Body(.18, 1.4)
        body5 = Body(.18, 1.1)

        choice = input("Choose Engine")
        if choice == 1:
            self.body = body1
        if choice == 2:
            self.body = body2
        if choice == 3:
            self.body = body3
        if choice == 4:
            self.body = body4
        if choice == 5:
            self.body = body5
        print("Body choice #", choice, " has been chosen")




class bigCar(Car):
    def __init__(self, wheel, eng, bod):
        super().__init__(wheel, eng, bod)

    def setWheels(self):  # diameter of wheels, pop(chance of wheels popping), torque of axles
        wheels1 = Wheels(18, 2, 70)
        wheels2 = Wheels(19, 3, 85)
        wheels3 = Wheels(20, 5, 90)
        wheels4 = Wheels(21, 6, 100)
        choice = input("Choose Wheels")

        if choice==1:
            self._wheels = wheels1
        if choice==2:
            self._wheels = wheels2
        if choice==3:
            self._wheels = wheels3
        if choice==4:
            self._wheels = wheels4

     #   N = random.randint(0, 100)  # https://docs.python.org/2/library/random.html
    #    if self.__wheels.popRate <= N:  # Wheels blow out
    #        self.__wheels.Torque=0

        print ("Wheel choice #" , choice, " has been chosen")

    def setEngine(self):  # hPwr of engine, boom(chance engine blows up), engMass, rpm, topSpeed of car
        engine1 = Engine(200, 1, .4, 4000, 300)
        engine2 = Engine(250, 2, .4, 4500, 325)
        engine3 = Engine(300, 5, .5, 5000, 365)
        engine4 = Engine(350, 6, .6, 5500, 380)
        choice = input("Choose Engine")
        if choice==1:
            self.engine = engine1
        if choice==2:
            self.engine = engine2
        if choice==3:
            self.engine = engine3
        if choice==4:
            self.engine = engine4

      #  N = random.randint(0, 100)
   #     if self.__engine.engineBlowRate <= N:  # engine has blown out
    #        self.__engine.topSpeed=0

        print("Engine choice #", choice, " has been chosen")

    def setBody(self):  # drag (air resistance), mass
        body1 = Body(.25, 1.5) # drag, mass
        body2 = Body(.21, 1.3)
        body3 = Body(.19, 1.5)
        body4 = Body(.2, 1.4)
        choice = input("Choose Engine")
        if choice == 1:
            self.body = body1
        if choice == 2:
            self.body = body2
        if choice == 3:
            self.body = body3
        if choice == 4:
            self.body = body4
        print("Body choice #", choice, " has been chosen")


class rocketCar(bigCar):
    def __init__(self, wheel, eng, bod):
        super().__init__(wheel, eng, bod)



raceCar1 = Car(Wheels(18, 2, 70),Engine(250, 3, .3, 4750, 325),Body(.2, 1.3))
raceCar2 = Car(Wheels(19, 3, 80),Engine(200, 2, .3, 4500, 350),Body(.19, 1.4))
zoomBoy = sportCar(Wheels(19, 2, 80),Engine(250, 2, .2, 4500, 370), Body(.19, 1.3),Spoiler(4,2))
fatBoy = bigCar(Wheels(21, 6, 100), Engine(300, 5, .5, 5000, 365),Body(.2, 1.4))
PCPBABY = hyperCar(Wheels(19, 2, 80),Engine(300, 3, .3, 5000, 385),Body(.18, 1.4),Spoiler(4,2),Boost(30,10))


print("max accel: ", raceCar1.getAccel(), " m/s^2 Finish time: ",raceCar1.getFinishTime(), "seconds")

print("max accel: ", raceCar2.getAccel(), " m/s^2 Finish time: ", raceCar2.getFinishTime(), "seconds")

print("max accel: ", zoomBoy.getAccel(), " m/s^2 Finish time: ", zoomBoy.getFinishTime(), "seconds")

print("max accel: ", fatBoy.getAccel(), " m/s^2 Finish time: ", fatBoy.getFinishTime(), "seconds")

print("max accel: ", PCPBABY.getAccel(), " m/s^2 Finish time: ", PCPBABY.getFinishTime(), "seconds")
