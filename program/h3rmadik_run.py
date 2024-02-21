"""  3. futás
Indulás: Bal oldal, ÉSZAK-ra keret mellől a faltól
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
jobbfeltet = Motor(Port.F)
#balszinszenzor = ColorSensor(Port.C)
#jobbszinszenzor = ColorSensor(Port.E)
# Hajtás, motorok, kerék és tengelytáv megadása
hajtas = DriveBase(bal_motor, jobb_motor, wheel_diameter=56, axle_track=145)

hub.light.on(Color.VIOLET)

hajtas.use_gyro(True)
hajtas.settings(300, 1000, 90, 900)
# Kicsit ki és forful
hajtas.straight(100)
hajtas.turn(10)
#Előremegy ráfordul rááll
hajtas.straight(595) #555
hajtas.turn(-45)
hajtas.straight(210) 
# Lecsap az emberre
balfeltet.run_time(-700, 1000)
hajtas.straight(-95)
hajtas.turn(55)

# Kimenetel, végén időre hajtás
hajtas.drive(-400, 0) 
wait(2500)

