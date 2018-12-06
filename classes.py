import pygame, random, math, sys, os, time
from pygame.locals import *
pygame.init()
mainClock = pygame.time.Clock()

class Engine:
    def __init__(self, hPwr, boom, engMass, rpm, topSpd):
        self.horsepower = hPwr
        self.engineBlowRate = boom
        self.engineMass = engMass
        self.rotationsPerMinute = rpm
        self.topSpeed = topSpd


class Wheels:
    def __init__(self, diameter, pop, tor):
        self.size = diameter
        self.popRate = pop
        self.torque=tor


class Body:
    def __init__(self, drag, mass):
        self.airDrag = drag
        self.bodyMass = mass


class Spoiler:
    def __init__(self, dForce):
        self.downForce = dForce


class Boost:
    def __init__(self, nos):
        self.nitrous = nos



class Car:

    def __init__(self, wheel, eng, bod):
        self.__wheels = wheel
        self.__engine = eng
        self.__body = bod

    def setWheels(self):  # diameter of wheels, pop(chance of wheels popping), torque of axles
        wheels1 = Wheels(18, 2, 70)
        wheels2 = Wheels(19, 3, 85)
        wheels3 = Wheels(20, 5, 90)
        choice = input("Choose Wheels")

        if choice==1:
            self.__wheels = wheels1
        if choice==2:
            self.__wheels = wheels2
        if choice==3:
            self.__wheels = wheels3
        N = random.randint(0, 100)  # https://docs.python.org/2/library/random.html
        if self.__wheels.popRate <= N:  # Wheels blow out
            self.__wheels.Torque=0

        print ("Wheel choice #" , choice, " has been chosen")

    def setEngine(self):  # hPwr of engine, boom(chance engine blows up), engMass, rpm, topSpeed of car
        engine1 = Engine(150, 1, .3, 4000, 300)
        engine2 = Engine(200, 2, .3, 4500, 325)
        engine3 = Engine(250, 5, .5, 5000, 365)
        choice = input("Choose Engine")
        if choice==1:
            self.__engine = engine1
        if choice==2:
            self.__engine = engine2
        if choice==3:
            self.__engine = engine3
        N = random.randint(0, 100)
        if self.__engine.engineBlowRate <= N:  # engine has blown out
            self.__engine.topSpeed=0

        print("Engine choice #", choice, " has been chosen")

    def setBody(self):  # drag (air resistance), mass
        body1 = Body(.25, 1.5)  # drag, mass
        body2 = Body(.2, 1.3)
        body3 = Body(.19, 1.3)
        choice = input("Choose Body")
        if choice == 1:
            self.__body = body1
        if choice == 2:
            self.__body = body2
        if choice == 3:
            self.__body = body3
        print("Body choice #", choice, " has been chosen")

    def carMass(self):  # addition of body mass and engine mass
        x = self.__body.bodyMass + self.__engine.engineMass
        return x

    def carForce(self):
        F = self.__wheels.torque/(self.__wheels.size/2)
        return F

    def getAccel(self):
        # https://www.carbibles.com/transmission-guide/ (to get the average gear ratio and derive torque on wheels)
        # https://www.quora.com/How-do-I-calculate-the-acceleration-of-a-car-when-I-have-rpm-torque-mass-horse-power-and-speed-at-different-gear-ratios
        # (to get the torque and calculate for the acceleration)
        f = self.carForce()              # self.__wheels.torque/(self.__wheels.size/2)
        m = self.carMass()                # self.__body.bodyMass + self.__engine.engineMass
        a = f / m
        return a


    def getCurrentSpeed(self):
        F = self.carForce()             # self.__wheels.torque / (self.__wheels.size / 2)
        m = self.__body.bodyMass + self.__engine.engineMass
        a = F / m
        v0 = a*mainClock
        vf = a*mainClock + v0
        if vf >= self.__engine.topSpeed:
            vf = self.__engine.topSpeed
        return vf

    def getFinishTime(self):
        F = self.__wheels.torque / (self.__wheels.size / 2)
        m = self.__body.bodyMass + self.__engine.engineMass
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
        self.__spoiler = spoil

    def setWheels(self): #diameter of wheels, pop(chance of wheels popping), torque of axles
        wheels1 = Wheels(18, 2, 70)
        wheels2 = Wheels(19, 3, 85)
        wheels3 = Wheels(20, 5, 90)
        wheels4 = Wheels(19, 2, 80)
        wheels5 = Wheels(20, 4, 95)
        choice = input("Choose Wheels")

        if choice==1:
            self.__wheels = wheels1
        if choice==2:
            self.__wheels = wheels2
        if choice==3:
            self.__wheels = wheels3
        if choice == 4:
            self.__wheels = wheels4
        if choice==5:
            self.__wheels = wheels5
        N = random.randint(0, 100) #https://docs.python.org/2/library/random.html
        if self.__wheels.popRate <= N: #Wheels blow out
            self.__wheels.Torque=0

        print ("Wheel choice #" , choice, " has been chosen")

    def setEngine(self): #hPwr of engine, boom(chance engine blows up), engMass, rpm, topSpeed of car
        engine1 = Engine(150, 1, .3, 4000, 300)
        engine2 = Engine(200, 2, .3, 4500, 325)
        engine3 = Engine(250, 5, .5, 5000, 365)
        engine4 = Engine(250, 2, .2, 4500, 370)
        engine5 = Engine(300, 3, .3, 5000, 385)
        choice = input("Choose Engine")
        if choice==1:
            self.__engine = engine1
        if choice==2:
            self.__engine = engine2
        if choice==3:
            self.__engine = engine3
        if choice==4:
            self.__engine = engine4
        if choice==5:
            self.__engine = engine5

        N = random.randint(0, 100)
        if self.__engine.engineBlowRate <= N:#engine has blown out
            self.__engine.topSpeed=0

        print("Engine choice #", choice, " has been chosen")

    def setBody(self): #drag (air resistance), mass
        body1 = Body(.25, 1.5) #drag, mass
        body2 = Body(.2, 1.3)
        body3 = Body(.19, 1.3)
        body4 = Body(.18, 1.4)
        body5 = Body(.18, 1.1)

        choice = input("Choose Engine")
        if choice == 1:
            self.__body = body1
        if choice == 2:
            self.__body = body2
        if choice == 3:
            self.__body = body3
        if choice == 4:
            self.__body = body4
        if choice == 5:
            self.__body = body5
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
            self.__wheels = wheels1
        if choice == 2:
            self.__wheels = wheels2
        if choice == 3:
            self.__wheels = wheels3
        if choice == 4:
            self.__wheels = wheels4
        if choice == 5:
            self.__wheels = wheels5
        N = random.randint(0, 100)  # https://docs.python.org/2/library/random.html
        if self.__wheels.popRate <= N:  # Wheels blow out
            self.__wheels.Torque = 0

        print("Wheel choice #", choice, " has been chosen")

    def setEngine(self):  # hPwr of engine, boom(chance engine blows up), engMass, rpm, topSpeed of car
        engine1 = Engine(150, 1, .3, 4000, 300)
        engine2 = Engine(200, 2, .3, 4500, 325)
        engine3 = Engine(250, 5, .5, 5000, 365)
        engine4 = Engine(250, 2, .2, 4500, 370)
        engine5 = Engine(300, 3, .3, 5000, 385)
        choice = input("Choose Engine")
        if choice == 1:
            self.__engine = engine1
        if choice == 2:
            self.__engine = engine2
        if choice == 3:
            self.__engine = engine3
        if choice == 4:
            self.__engine = engine4
        if choice == 5:
            self.__engine = engine5

        N = random.randint(0, 100)
        if self.__engine.engineBlowRate <= N:  # engine has blown out
            self.__engine.topSpeed = 0

        print("Engine choice #", choice, " has been chosen")

    def setBody(self):  # drag (air resistance), mass
        body1 = Body(.25, 1.5)  # drag, mass
        body2 = Body(.2, 1.3)
        body3 = Body(.19, 1.3)
        body4 = Body(.18, 1.4)
        body5 = Body(.18, 1.1)

        choice = input("Choose Engine")
        if choice == 1:
            self.__body = body1
        if choice == 2:
            self.__body = body2
        if choice == 3:
            self.__body = body3
        if choice == 4:
            self.__body = body4
        if choice == 5:
            self.__body = body5
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
            self.__wheels = wheels1
        if choice==2:
            self.__wheels = wheels2
        if choice==3:
            self.__wheels = wheels3
        if choice==4:
            self.__wheels = wheels4

        N = random.randint(0, 100)  # https://docs.python.org/2/library/random.html
        if self.__wheels.popRate <= N:  # Wheels blow out
            self.__wheels.Torque=0

        print ("Wheel choice #" , choice, " has been chosen")

    def setEngine(self):  # hPwr of engine, boom(chance engine blows up), engMass, rpm, topSpeed of car
        engine1 = Engine(200, 1, .4, 4000, 300)
        engine2 = Engine(250, 2, .4, 4500, 325)
        engine3 = Engine(300, 5, .5, 5000, 365)
        engine4 = Engine(350, 6, .6, 5500, 380)
        choice = input("Choose Engine")
        if choice==1:
            self.__engine = engine1
        if choice==2:
            self.__engine = engine2
        if choice==3:
            self.__engine = engine3
        if choice==4:
            self.__engine = engine4

        N = random.randint(0, 100)
        if self.__engine.engineBlowRate <= N:  # engine has blown out
            self.__engine.topSpeed=0

        print("Engine choice #", choice, " has been chosen")

    def setBody(self):  # drag (air resistance), mass
        body1 = Body(.25, 1.5) # drag, mass
        body2 = Body(.21, 1.3)
        body3 = Body(.19, 1.5)
        body4 = Body(.2, 1.4)
        choice = input("Choose Engine")
        if choice == 1:
            self.__body = body1
        if choice == 2:
            self.__body = body2
        if choice == 3:
            self.__body = body3
        if choice == 4:
            self.__body = body4
        print("Body choice #", choice, " has been chosen")


class rocketCar(bigCar):
    def __init__(self, wheel, eng, bod):
        super().__init__(wheel, eng, bod)



raceCar1 = Car(None,None,None)
raceCar1.setBody()
raceCar1.setEngine()
raceCar1.setWheels()
