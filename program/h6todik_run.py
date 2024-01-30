"""  6. futás
Indulás: Jobb oldal, ÉSZAK NYUGAT-ra keretből
"""
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
allapot = 0
pressed = []
# Jobb oldali hajtás motor, F port
jobb_motor = Motor(Port.A)

# Jobb oldali hajtás motor, B port, forgásirány előrefelé
bal_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
balfeltet = Motor(Port.B)
jobbfeltet = Motor(Port.F)
#balszinszenzor = ColorSensor(Port.A)
#jobbszinszenzor = ColorSensor(Port.E)
# Hajtás, motorok, kerék és tengelytáv megadása
hajtas = DriveBase(bal_motor, jobb_motor, wheel_diameter=56, axle_track=145)
hajtas.settings(300, 1500, 90, 900)
#felszedi a két figurát
hajtas.straight(360)
hajtas.turn(-30)
hajtas.straight(50)
hajtas.settings(300, 1500, 45, 450)
hajtas.turn(-60)
hajtas.settings(200, 1000, 90, 900)
hajtas.straight(100)
hajtas.settings(300, 1000, 90, 900)
#jobbfeltet.run_time(600, 1000)
#jobbfeltet.run_time(-600, 1000)
# Kitolja az embereket
hajtas.turn(-110)
hajtas.straight(220)
hajtas.straight(-100)
#odamegy a színpadhoz
hajtas.turn(-85)
hajtas.straight(350)
hajtas.turn(-45)
hajtas.straight(120)
hajtas.turn(85)

hajtas.straight(230)
#megcsinálja a színpadot
jobbfeltet.run_time(500, 1000, wait=False)
balfeltet.run_time(-400, 1000 )
hajtas.straight(-150)
hajtas.turn(90)
# Időre hajtva kimegy
hajtas.drive(500,0)
wait(1500)