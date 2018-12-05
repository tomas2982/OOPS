


class Car:

    def __init__(self, wheel, eng, bod):
        self.__wheels = wheel
        self.__engine = eng
        self.__body = bod

    def setWheels(self):
        wheels1 = Wheels(18, 2)
        wheels2 = Wheels(19, 3)
        wheels3 = Wheels(20, 5)
        choice = input("Choose Wheels")

        if choice==1:
            self.__wheels = wheels1
        if choice==2:
            self.__wheels = wheels2
        if choice==3:
            self.__wheels = wheels3

        print ("Wheel choice #" , choice, " has been chosen")

    def setEngine(self):
        engine1 = Engine(150, 1, .3)
        engine2 = Engine(200, 2, .3)
        engine3 = Engine(250, 5, .5)
        choice = input("Choose Engine")
        if choice==1:
            self.__engine = engine1
        if choice==2:
            self.__engine = engine2
        if choice==3:
            self.__engine = engine3

        print("Engine choice #", choice, " has been chosen")

    def setBody(self):
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


    def carMass(self):
        x = self.__body.bodyMass + self.__engine.engineMass
        return x

    def getAccel(self):


    def getCurrentSpeed(self):

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
    def __init__(self, hPwr, boom, engMass):
        self.horsepower = hPwr
        self.engineBlowRate = boom
        self.engineMass = engMass

class Wheels:
    def __init__(self, diameter, pop):
        self.size = diameter
        self.popRate = pop

class Body:
    def __init__(self, drag, mass):
        self.airDrag = drag
        self.bodyMass = mass


