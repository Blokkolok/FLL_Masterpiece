"""  7. futás
Indulás: Jobb oldal, ÉSZAK NYUGAT-ra keretből
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

hajtas.use_gyro(True)
hajtas.settings(300, 1000, 90, 900)
hajtas.straight(650)
jobbfeltet.run_time(500, 1000, wait=False)
balfeltet.run_time(600, 3000)

# Kimenetel, végén időre hajtás
#hajtas.straight(-650)
hajtas.drive(-300, 0) 
wait(2000)
