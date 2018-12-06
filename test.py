from classes import *

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
