"""  2. futás
Indulás: Bal oldal, KELET-rE keretből
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

hajtas.settings(300, 1500, 90, 900)
hajtas.use_gyro(True)

balfeltet.run_time(400, 800, wait=False)
hajtas.straight(200)
hajtas.turn(30)
hajtas.straight(280)
hajtas.turn(-30)
hajtas.straight(130)
balfeltet.run_time(-600, 1500)
hajtas.straight(-120)
hajtas.turn(-50)
balfeltet.run_time(600, 1500, wait=False)
wait(200)
hajtas.turn(35)
hajtas.straight(-400)
