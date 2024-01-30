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
gombok = []
narancsig = False
while not (Button.RIGHT in gombok or Button.LEFT in gombok):
    gombok = hub.buttons.pressed()
    wait(10)
    if  Button.LEFT in gombok:
        hub.light.on(Color.ORANGE)
        narancsig = True

hajtas.use_gyro(True)
hajtas.settings(300, 1000, 90, 900)
# Kicsit ki és forful
hajtas.straight(-100)
hajtas.turn(10)
# Hátramegy ráfordul rááll
hajtas.straight(-545) #555
hajtas.turn(-55)
hajtas.straight(-230)

hajtas.turn(-20)
if narancsig:
    hajtas.turn(20)
    hajtas.straight(50)
    wait(500)
    hajtas.straight(-80)
    hajtas.straight(95)
    hajtas.turn(65)
else:
    hajtas.straight(95)
    hajtas.turn(85)

# Kimenetel, végén időre hajtás
hajtas.drive(300, 0) 
wait(3000)

