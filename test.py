from main import *

print("Choose 1 for Easy, 2 For Medium, 3 for Hard, 4 for Multi-Car Race")
choice = int(input("Mode you want: "))
if choice == 1:
    myCar1 = Car("User Car",Wheels(18, 2, 70), Engine(250, 3, .3, 4750, 325), Body(.2, 1.3))     #CHANGE VALUES FOR CAR HERE
    #wheel args. size, popRate, torque |  engine args. horsepower, blowRate, mass, RPM, topspeed | body args. air drag, mass
    enemyCar1 = Car("Bad Car",Wheels(random.randint(18, 20), random.randint(0, 5), random.randint(60, 70))
                    , Engine(random.randint(100, 200), random.randint(0, 5), random.uniform(1.0, 1.8),
                             random.randint(4000, 4200), random.randint(0, 100))
                    , Body(random.uniform(0.3, 0.4), random.uniform(2.0, 2.5)))
    print("myCar1")
    myCar1.printSpecs()
    print("max accel: ", myCar1.getAccel(), " m/s^2 Finish time: ", myCar1.getFinishTime(), "seconds")
    print("enemyCar1")
    enemyCar1.printSpecs()
    print("max accel: ", enemyCar1.getAccel(), " m/s^2 Finish time: ", enemyCar1.getFinishTime(), "seconds")
    carList = [myCar1, enemyCar1]
    winnersList = []
    for x in carList:
        winnersList.append(x.getFinishTime())
    winner = carList[winnersList.index(min(winnersList))]    #finds winner from list of times
    print(winner.carName)

elif choice == 2:
    myCar1 = Car("User Car", Wheels(20, 2, 60), Engine(250, 3, .3, 4750, 325), Body(.2, 1.3)) #CHANGE VALUES FOR CAR HERE
    #wheel args. size, popRate, torque |  engine args. horsepower, blowRate, mass, RPM, topspeed | body args. air drag, mass
    enemyCar1 = bigCar("Bad Car",Wheels(random.randint(19, 22), random.randint(0, 4), random.randint(75, 85))
                    , Engine(random.randint(275, 375), random.randint(0, 4), random.uniform(0.5, 0.8),
                             random.randint(5000, 5500), random.randint(75, 125))
                    , Body(random.uniform(0.2, 0.3), random.uniform(1.5, 2.0)))
    print("myCar1")
    myCar1.printSpecs()
    print("max accel: ", myCar1.getAccel(), " m/s^2 Finish time: ", myCar1.getFinishTime(), "seconds")
    print("enemyCar1")
    enemyCar1.printSpecs()
    print("max accel: ", enemyCar1.getAccel(), " m/s^2 Finish time: ", enemyCar1.getFinishTime(), "seconds")
    carList = [myCar1, enemyCar1]
    winnersList = []
    for x in carList:
        winnersList.append(x.getFinishTime())
    winner = carList[winnersList.index(min(winnersList))]    #finds winner from list of times
    print(winner.carName)

elif choice == 3:
    myCar1 = Car("User Car", Wheels(20, 2, 60), Engine(250, 3, .3, 4750, 325), Body(.2, 1.3))#CHANGE VALUES FOR CAR HERE
    #wheel args. size, popRate, torque |  engine args. horsepower, blowRate, mass, RPM, topspeed | body args. air drag, mass
    enemyCar1 = Car("Bad Car", Wheels(random.randint(16, 18), random.randint(0, 3), random.randint(90, 100))
                    , Engine(random.randint(400, 600), random.randint(0, 5), random.uniform(0.5, 0.8),
                             random.randint(5500, 6750), random.randint(100, 150))
                    , Body(random.uniform(0.2, 0.25), random.uniform(1.5, 1.8)))
    print("myCar1")
    myCar1.printSpecs()
    print("max accel: ", myCar1.getAccel(), " m/s^2 Finish time: ", myCar1.getFinishTime(), "seconds")
    print("enemyCar1")
    enemyCar1.printSpecs()
    print("max accel: ", enemyCar1.getAccel(), " m/s^2 Finish time: ", enemyCar1.getFinishTime(), "seconds")
    carList = [myCar1,enemyCar1]
    winnersList = []        #list for finish times
    for x in carList:
        winnersList.append(x.getFinishTime())
    winner = carList[winnersList.index(min(winnersList))]    #finds winner from list of times
    print(winner.carName)

elif choice == 4:
    raceCar1 = Car("RaceCar1",Wheels(18, 2, 70), Engine(250, 3, .3, 4750, 325), Body(.2, 1.3))
    raceCar2 = Car("RaceCar2",Wheels(19, 3, 80), Engine(200, 2, .3, 4500, 350), Body(.19, 1.4))
    zoomBoy = sportCar("SportCar",Wheels(19, 2, 80), Engine(250, 2, .2, 4500, 370), Body(.19, 1.3), Spoiler(4, 2))
    fatBoy = bigCar("BiGCAR",Wheels(21, 6, 100), Engine(300, 5, .5, 5000, 365), Body(.2, 1.4))
    PCPBABY = hyperCar("PCPBABY",Wheels(19, 2, 80), Engine(300, 3, .3, 5000, 385), Body(.18, 1.4), Spoiler(4, 2), Boost(30, 10))
    print("raceCar1")
    raceCar1.printSpecs()
    print("max accel: ", raceCar1.getAccel(), " m/s^2 Finish time: ", raceCar1.getFinishTime(), "seconds")
    print("raceCar2")
    raceCar2.printSpecs()
    print("max accel: ", raceCar2.getAccel(), " m/s^2 Finish time: ", raceCar2.getFinishTime(), "seconds")
    print("sportCar1")
    zoomBoy.printSpecs()
    print("max accel: ", zoomBoy.getAccel(), " m/s^2 Finish time: ", zoomBoy.getFinishTime(), "seconds")
    print("BiGCAR")
    fatBoy.printSpecs()
    print("max accel: ", fatBoy.getAccel(), " m/s^2 Finish time: ", fatBoy.getFinishTime(), "seconds")
    print("PCPBABY")
    PCPBABY.printSpecs()
    print("max accel: ", PCPBABY.getAccel(), " m/s^2 Finish time: ", PCPBABY.getFinishTime(), "seconds")

    carList = [raceCar1, raceCar2, zoomBoy, fatBoy, PCPBABY]
    winnersList = []
    for x in carList:
        winnersList.append(x.getFinishTime())
    winner = carList[winnersList.index(min(winnersList))]    #finds winner from list of times
    print(winner.carName)

print("end of game")
