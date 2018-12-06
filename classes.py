import pygame, random, math, sys, os, time
from pygame.locals import *
pygame.init()
mainClock = pygame.time.Clock()

class Engine:
    def __init__(self, hPwr: int, boom: int, engMass: float, rpm: int, topSpd: float):
        self.horsepower = hPwr
        self.engineBlowRate = boom
        self.engineMass = engMass
        self.rotationsPerMinute = rpm
        self.topSpeed = topSpd



class Wheels:
    def __init__(self, diameter: int, pop: int, tor: float):
        self.size = diameter
        self.popRate = pop
        self.torque=tor


class Body:
    def __init__(self, drag: float, mass: float):
        self.airDrag = drag
        self.bodyMass = mass


class Spoiler:
    def __init__(self, dForce: int, fRate: int):
        self.downForce = dForce     # add to force
        self.flipRate = fRate



class Boost:
    def __init__(self, nos: int, bigBoom: int):
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
        N = random.randint(0, 100)      # https://docs.python.org/2/library/random.html

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
        N = random.randint(0, 99)
        if self.engine.engineBlowRate <= N:  # engine has blown out
            self.engine.topSpeed=0

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

    def printSpecs(self):
        print("Wheel: ")
        print("     size: ",self.wheels.size, " inches")
        print("     pop rate: ", self.wheels.popRate, " %")
        print("     torque: ", self.wheels.torque, " N/m")
        print("Engine: ")
        print("     Horsepower: ", self.engine.horsepower, " hP")
        print("     Blow rate: ", self.engine.engineBlowRate, " %")
        print("     Mass: ", self.engine.engineMass, " tons")
        print("     Engine RPM", self.engine.rotationsPerMinute)
        print("     Top speed: ", self.engine.topSpeed, " m/s")
        print("Body: ")
        print("     Mass: ", self.body.bodyMass, " tons")
        print("     Drag Coeff.: ", self.body.airDrag)

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
        N = random.randint(0, 100) #https://docs.python.org/2/library/random.html
        if self.wheels.popRate <= N: #Wheels blow out
            self.wheels.Torque=0

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

        N = random.randint(0, 100)
        if self.engine.engineBlowRate <= N:#engine has blown out
            self.engine.topSpeed=0

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
        self.spoiler = spoil
        self.booster = boost

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
        N = random.randint(0, 100)  # https://docs.python.org/2/library/random.html
        if self.wheels.popRate <= N:  # Wheels blow out
            self.wheels.Torque = 0

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

        N = random.randint(0, 100)
        if self.engine.engineBlowRate <= N:  # engine has blown out
            self.engine.topSpeed = 0

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
            self.wheels = wheels1
        if choice==2:
            self.wheels = wheels2
        if choice==3:
            self.wheels = wheels3
        if choice==4:
            self.wheels = wheels4

        N = random.randint(0, 100)  # https://docs.python.org/2/library/random.html
        if self.wheels.popRate <= N:  # Wheels blow out
            self.wheels.Torque=0

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

        N = random.randint(0, 100)
        if self.engine.engineBlowRate <= N:  # engine has blown out
            self.engine.topSpeed=0

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

def buildCar():
    print("Car choices: Car, SportCar, BigCar, HyperCar: ")
    carChoice = input("Which car you want: ")
    if carChoice ==1:
        newCar = Car(0,0,0)
    elif carChoice ==2:
        newCar = sportCar(0,0,0,0)
    elif carChoice == 3:
        newCar = bigCar(0,0,0)
    elif carChoice == 4:
        newCar = hyperCar(0,0,0,0,0)

    wheels1 = Wheels(18, 2, 70)
    wheels2 = Wheels(19, 3, 85)
    wheels3 = Wheels(20, 5, 90)
    print("Wheel Choices: Wheel set 1, Wheel set 2, Wheel set 3: ")
    wheelChoice = input("Choose wheels: ")
    if wheelChoice ==1:
        newWheels = wheels1
    elif wheelChoice ==2:
        newWheels = wheels2
    elif wheelChoice == 3:
        newWheels = wheels3

    newCar.wheels = newWheels


    engine1 = Engine(150, 1, .3, 4000, 300)
    engine2 = Engine(200, 2, .3, 4500, 325)
    engine3 = Engine(250, 5, .5, 5000, 365)
    print("Engine Choices: Engine 1, Engine 2, Engine 3: ")
    engineChoice = input("Choose engine: ")
    if engineChoice == 1:
        newEngine = engine1
    elif engineChoice == 2:
        newEngine = engine2
    elif engineChoice == 3:
        newEngine = engine3

    newCar.engine = newEngine

    body1 = Body(.25, 1.5)  # drag, mass
    body2 = Body(.2, 1.3)
    body3 = Body(.19, 1.3)
    print("Body Choices: Body 1, Body 2, Body 3: ")
    bodyChoice = input("Choose body: ")
    if bodyChoice == 1:
        newBody = body1
    elif bodyChoice == 2:
        newBody = body2
    elif bodyChoice == 3:
        newBody = body3
    newCar.body = newBody

    return newCar
