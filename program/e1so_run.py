"""  1. futás
Indulás: Bal oldal, ÉSZAK-ra keretből
!!! Indítás után ki kell venni a keretet !!!
"""
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
# Jobb oldali hajtás motor, F port
jobb_motor = Motor(Port.A)

# Jobb oldali hajtás motor, B port, forgásirány előrefelé
bal_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
balfeltet = Motor(Port.B)
#jobbfeltet = Motor(Port.F)
#balszinszenzor = ColorSensor(Port.A)
#jobbszinszenzor = ColorSensor(Port.E)
# Hajtás, motorok, kerék és tengelytáv megadása
hajtas = DriveBase(bal_motor, jobb_motor, wheel_diameter=56, axle_track=128)

# Sárkány hátuljához
hajtas.settings(300, 1500, 90, 900)
hajtas.use_gyro(True)

hajtas.straight(160)
# Erőssen kanyarodunk, hogy kilökjük a sárkányt
hajtas.settings(300, 1500, 400, 3000)
hajtas.turn(22)
# Vissza kanyar, vissza tolat
hajtas.settings(300, 1500, 90, 900)
hajtas.turn(-22)
hajtas.straight(-290)
# Befordul és elmegy a hangkeverőig, közben leteszi a kart
hajtas.turn(42)
balfeltet.run_time(-600, 1000, wait=False)
hajtas.straight(425)
# emel és lassan megy 
hajtas.settings(10, 1500, 30, 300)
balfeltet.run_time(400, 1000, wait=False) #, wait=False
wait(800)
# kicsit közeleb megy emel
#hajtas.straight(10)
# Lassan kifordulunk a kezelőpult alól
hajtas.settings(300, 1500, 30, 900)
hajtas.turn(20)
#hátramegy, hogy odamehessen a hajóhoz
hajtas.settings(300, 1500, 90, 900)
hajtas.straight(-100)
#odamegy a hajóhoz
hajtas.turn(113)
hajtas.curve(260, -85)
hajtas.straight(90)
#lecsapja a kart a kamerának
balfeltet.run_time(-600, 1000, wait=False)
wait(750)
#behúzza a hajót a jó helyre
hajtas.straight(-130)
hajtas.turn(-45)
#kifordul a hajótól
balfeltet.run_time(600, 1000, wait=False)
wait(200)
hajtas.turn(30)
#hátramegy, hogy odamenjen a nénihez
hajtas.straight(-200)
#jó irányba fordul, odamegy a nénihez
hajtas.turn(-40)
hajtas.straight(350)
#lecsap, hazaviszi a nénit
balfeltet.run_time(-600, 1000)
hajtas.straight(-100)
#hajtas.turn(30)
#hajtas.settings(400, 1500, 90, 900)
#hajtas.curve(-800, -30)
hajtas.drive(-500, 25)
wait(1000)
#felemeli a kart 
balfeltet.run_time(600, 1000)



