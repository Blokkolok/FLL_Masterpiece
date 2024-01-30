"""  8. futás
Indulás: Jobb oldal, NYUGAT-ra pontos helyről
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
jobbfeltet = Motor(Port.F)
#balszinszenzor = ColorSensor(Port.A)
#jobbszinszenzor = ColorSensor(Port.E)
# Hajtás, motorok, kerék és tengelytáv megadása
hajtas = DriveBase(bal_motor, jobb_motor, wheel_diameter=56, axle_track=145)

hajtas.settings(400, 1000, 90, 900)
hajtas.use_gyro(True)
# Odamegy Filmnél lerakja 
hajtas.straight(850)
# Filmnél lerakja 
jobbfeltet.run_time(500, 1000)
# Odamegy popkornhoz
hajtas.straight(290)
hajtas.turn(20)
hajtas.straight(500)
hajtas.turn(70)
hajtas.straight(60)
# Popkornnál lerakja 
jobbfeltet.run_time(500, 1000)
# Odamegy gördeszka
hajtas.straight(200)
hajtas.turn(40)
hajtas.straight(270)