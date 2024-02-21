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

hajtas.settings(700, 1000, 90, 900)
hajtas.use_gyro(True)

#betolja a kék szakértőt
hajtas.straight(-900)
jobbfeltet.run_time(-500, 1000)
#odamegy a zöld szakértő helyéhez
hajtas.turn(20)
hajtas.straight(-600)
hajtas.turn(65)
hajtas.straight(-270)
hajtas.turn(45)
#felcsapja a kart hogy othagyja a zöld szakértőt
balfeltet.run_time(500, 1000)
#bemegy a lila szakértővel a területére
hajtas.straight(-390)