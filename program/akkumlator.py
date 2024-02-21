from pybricks.hubs import PrimeHub
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop


hub = PrimeHub()

while True:
    mV = hub.battery.voltage()
    
    if mV > 8000:
        hub.light.on(Color.GREEN)
    elif mV < 7700:
        hub.light.on(Color.RED)
    else:
        hub.light.on(Color.YELLOW)
    hub.display.number(mV/100) # csak 2 számjegyet tud kiírni
    wait(500)
