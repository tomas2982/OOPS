import pygame, random, sys, os, time
from pygame.locals import *
pygame.init()
mainClock = pygame.time.Clock()
class Car:

    def __init__(self, wheel, eng, bod):
        self.__wheels = wheel
        self.__engine = eng
        self.__body = bod

    def setWheels(self): #diameter of wheels, pop(chance of wheels popping), torque of axles, gear ratio
        wheels1 = Wheels(18, .02, 70)
        wheels2 = Wheels(19, .03, 85)
        wheels3 = Wheels(20, .05, 90)
        choice = input("Choose Wheels")

        if choice==1:
            self.__wheels = wheels1
        if choice==2:
            self.__wheels = wheels2
        if choice==3:
            self.__wheels = wheels3

        print ("Wheel choice #" , choice, " has been chosen")

    def setEngine(self): #hPwr of engine, boom(chance engine blows up), engMass, rpm
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

        print("Engine choice #", choice, " has been chosen")

    def setBody(self): #drag (air resistance), mass
        body1 = Body(.25, 1.5) #drag, mass
        body2 = Body(.2, 1.3)
        body3 = Body(.19, 1.3)
        choice = input("Choose Engine")
        if choice == 1:
            self.__body = body1
        if choice == 2:
            self.__body = body2
        if choice == 3:
            self.__body = body3

        print("Body choice #", choice, " has been chosen")


    def carMass(self): #addition of body mass and engine mass
        x = self.__body.bodyMass + self.__engine.engineMass
        return x

    def carForce(self):
        F = self.__wheels.torque/(self.__wheels.size/2)
        return F

    def getAccel(self):
    #https://www.carbibles.com/transmission-guide/ (to get the average gear ratio)
    #https://www.quora.com/How-do-I-calculate-the-acceleration-of-a-car-when-I-have-rpm-torque-mass-horse-power-and-speed-at-different-gear-ratios
    #(to get the torque and calculate for the acceleration)
        F = self.__wheels.torque/(self.__wheels.size/2)
        m=self.__body.bodyMass + self.__engine.engineMass
        a = F/m
        return a


    def getCurrentSpeed(self):
        F = self.__wheels.torque / (self.__wheels.size / 2)
        m = self.__body.bodyMass + self.__engine.engineMass
        a = F / m
        speed = a*mainClock
        if speed>=self.__engine.topSpeed
            speed=self.__engine.topSpeed
        return speed


    acceleration = getAccel()
    topSpeed = None
    force = None
    totalMass = carMass()


class sportCar(Car):
    def __init__(self, wheel, eng, bod, spoil):
        super().__init__(wheel, eng, bod)
        self.__spoiler = spoil







class hyperCar(sportCar):




class bigCar(Car):



class rocketCar(bigCar):


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
