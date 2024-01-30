"""  4. futás
Indulás: Bal oldal, KELET-re keretből
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

#felcsapja a kart
balfeltet.run_time(-400, 700, wait=False)
jobbfeltet.run_time(-150, 2000, wait=False)
#odamegy a virtuális izéhez
jobbfeltet.run_time(-150, 2000, wait=False)
hajtas.straight(250)
hajtas.curve(500, -50)
hajtas.straight(250)
hajtas.turn(-40)
hajtas.straight(100)
balfeltet.run_time(600, 2500) 
balfeltet.run_time(-500, 500)


#hajtas.straight(350)
#hajtas.turn(-90)

#hajtas.turn(-85)
#hajtas.straight(385)
#hajtas.turn(20)
#hajtas.straight(55)
#betolja az innovációs projektet meg a nénit meg a bácsit
hajtas.straight(-150)
#hajtas.turn(20)
hajtas.turn(20)
hajtas.straight(270)
jobbfeltet.run_time(400, 1300)

#odamegy a toronyhoz
hajtas.straight(-150)
hajtas.turn(70)
hajtas.straight(270)
hajtas.turn(45)
hajtas.straight(-255)
hajtas.turn(45)
balfeltet.run_time(400, 700, wait=False)
hajtas.straight(210)
#feltolja a tornyot és beejti a tagot
balfeltet.run_time(-300, 5000)
#megcsinálja a virágot
balfeltet.run_time(400, 800)
#balfeltet.stop() 
balfeltet.run_time(-150, 2500, wait=False)
hajtas.straight(-80)
hajtas.turn(-110)
hajtas.straight(180)
hajtas.turn(50)
hajtas.curve(350, -30)
hajtas.curve(500, 90)
#Időre megyünk ki
hajtas.drive(400, 0)
wait(500)
