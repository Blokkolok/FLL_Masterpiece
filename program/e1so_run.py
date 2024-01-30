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
hajtas = DriveBase(bal_motor, jobb_motor, wheel_diameter=56, axle_track=145)

# Sárkány hátuljához
hajtas.settings(300, 1500, 90, 900)
hajtas.use_gyro(True)

hajtas.straight(170)
# Erőssen kanyarodunk, hogy kilökjük a sárkányt
hajtas.settings(300, 1500, 400, 3000)
hajtas.turn(22)
# Vissza kanyar, vissza tolat
hajtas.settings(300, 1500, 90, 900)
hajtas.turn(-22)
hajtas.straight(-300)
# Befordul és elmegy a hangkeverőig, közben leteszi a kart
hajtas.turn(42)
balfeltet.run_time(-600, 1500, wait=False)
hajtas.straight(400)
# emel és lassan megy 
hajtas.settings(10, 1500, 30, 300)
balfeltet.run_time(200, 2000, wait=False)
wait(500)
# kicsit közeleb megy emel
hajtas.straight(10)



# Lassan kifordulunk a kezelőpult alól
hajtas.settings(300, 1500, 30, 300)
hajtas.turn(15)

#néni begyüjtése sok lépésben
#továbbfordul a pult után
hajtas.settings(300, 1500, 90, 900)
hajtas.turn(35)
#olyan helyzetbe mozog hogy oda tudjon menni a nénihez
hajtas.straight(-100)
hajtas.turn(35)
hajtas.straight(300)
hajtas.turn(-103)
#odamegy a nénihez
hajtas.straight(115)
#begyűjti a nénit
balfeltet.run_time(-400, 1000)
#fordulva haza megy
hajtas.straight(-100)
hajtas.turn(70)
hajtas.straight(-480)



