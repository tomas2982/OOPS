from main import *
"""
raceCar1 = Car(Wheels(18, 2, 70),Engine(250, 3, .3, 4750, 325),Body(.2, 1.3))
raceCar2 = Car(Wheels(19, 3, 80),Engine(200, 2, .3, 4500, 350),Body(.19, 1.4))
zoomBoy = sportCar(Wheels(19, 2, 80),Engine(250, 2, .2, 4500, 370), Body(.19, 1.3),Spoiler(4,2))
fatBoy = bigCar(Wheels(21, 6, 100), Engine(300, 5, .5, 5000, 365),Body(.2, 1.4))
PCPBABY = hyperCar(Wheels(19, 2, 80),Engine(300, 3, .3, 5000, 385),Body(.18, 1.4),Spoiler(4,2),Boost(30,10))
print("raceCar1")
raceCar1.printSpecs()
print("max accel: ", raceCar1.getAccel(), " m/s^2 Finish time: ",raceCar1.getFinishTime(), "seconds")
print("raceCar2")
raceCar2.printSpecs()
print("max accel: ", raceCar2.getAccel(), " m/s^2 Finish time: ", raceCar2.getFinishTime(), "seconds")
print("sportCar1")
zoomBoy.printSpecs()
print("max accel: ", zoomBoy.getAccel(), " m/s^2 Finish time: ", zoomBoy.getFinishTime(), "seconds")
print("bigCar")
fatBoy.printSpecs()
print("max accel: ", fatBoy.getAccel(), " m/s^2 Finish time: ", fatBoy.getFinishTime(), "seconds")
print("hyperCar")
PCPBABY.printSpecs()
print("max accel: ", PCPBABY.getAccel(), " m/s^2 Finish time: ", PCPBABY.getFinishTime(), "seconds")
carList=[raceCar1,raceCar2,zoomBoy,fatBoy,PCPBABY]
winnersList = []
for x in carList:
    winnersList.append(x.getFinishTime())
winner = carList[winnersList.index(min(winnersList))]
print(winner)
"""

print("Choose 1 for Easy, 2 For Medium, 3 for Hard")
choice = int(input("Difficulty you want: "))
if choice == 1:
    print("WHYARENTYOUDOINGANYTHING")
    myCar1 = Car(Wheels(18, 2, 70), Engine(250, 3, .3, 4750, 325), Body(.2, 1.3))

    enemyCar1 = Car(Wheels(random.randint(18, 20), random.randint(0, 5), random.randint(60, 70))
                    , Engine(random.randint(100, 200), random.randint(0, 5), random.uniform(1.0, 1.8),
                             random.randint(4000, 4200), random.randint(0, 100))
                    , Body(random.uniform(0.3, 0.4), random.uniform(2.0, 2.5)))
    print("myCar1")
    myCar1.printSpecs()
    print("max accel: ", myCar1.getAccel(), " m/s^2 Finish time: ", myCar1.getFinishTime(), "seconds")
    print("enemyCar1")
    enemyCar1.printSpecs()
    print("max accel: ", enemyCar1.getAccel(), " m/s^2 Finish time: ", enemyCar1.getFinishTime(), "seconds")

elif choice == 2:
    myCar1 = Car(Wheels(18, 2, 70), Engine(250, 3, .3, 4750, 325), Body(.2, 1.3))

    enemyCar1 = bigCar(Wheels(random.randint(19, 22), random.randint(0, 4), random.randint(65, 75))
                    , Engine(random.randint(175, 250), random.randint(0, 4), random.uniform(1.0, 1.7),
                             random.randint(4200, 4500), random.randint(0, 100))
                    , Body(random.uniform(0.2, 0.3), random.uniform(1.5, 2.0)))
    print("myCar1")
    myCar1.printSpecs()
    print("max accel: ", myCar1.getAccel(), " m/s^2 Finish time: ", myCar1.getFinishTime(), "seconds")
    print("enemyCar1")
    enemyCar1.printSpecs()
    print("max accel: ", enemyCar1.getAccel(), " m/s^2 Finish time: ", enemyCar1.getFinishTime(), "seconds")

elif choice == 3:
    myCar1 = Car(Wheels(18, 2, 70), Engine(250, 3, .3, 4750, 325), Body(.2, 1.3))

    enemyCar1 = Car(Wheels(random.randint(20, 23), random.randint(0, 3), random.randint(70, 80))
                    , Engine(random.randint(100, 200), random.randint(0, 5), random.uniform(1.0, 1.8),
                             random.randint(4500, 4750), random.randint(0, 100))
                    , Body(random.uniform(0.2, 0.25), random.uniform(1.5, 1.8)))
    print("myCar1")
    myCar1.printSpecs()
    print("max accel: ", myCar1.getAccel(), " m/s^2 Finish time: ", myCar1.getFinishTime(), "seconds")
    print("enemyCar1")
    enemyCar1.printSpecs()
    print("max accel: ", enemyCar1.getAccel(), " m/s^2 Finish time: ", enemyCar1.getFinishTime(), "seconds")

print("end of game")
