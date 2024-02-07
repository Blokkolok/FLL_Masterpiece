from pybricks.tools import hub_menu
from pybricks.hubs import PrimeHub

# Programok indítása menuből

hub = PrimeHub()
# Utoljára indított tárolt érték olvasása
elozo = hub.system.storage(0,read=1)

# Választási lehetőségek, hogy a következő legyen az első
if elozo == b'\x01':
   selected = hub_menu("2", "3", "4", "5", "6", "7", "1") 
elif elozo == b'\x02':
    selected = hub_menu("3", "4", "5", "6", "7", "1", "2")
elif elozo == b'\x03':
    selected = hub_menu("4", "5", "6", "7", "1", "2", "3")
elif elozo == b'\x04':
    selected = hub_menu("5", "6", "7", "1", "2", "3", "4")
elif elozo == b'\x05':
    selected = hub_menu("6", "7", "1", "2", "3", "4", "5")
elif elozo == b'\x06':
    selected = hub_menu("7", "1", "2", "3", "4", "5", "6")
else:
    selected = hub_menu("1", "2", "3", "4", "5", "6", "7")
# Utoljára indított tárolása
irando= [int(selected)]
hub.system.storage(0, write=bytes(irando))

# Programok futtatása a választás alapján
if selected == "1":
    import e1so_run
elif selected == "2":
    import h3rmadik_run
elif selected == "3":
    import n4gyedik_run
elif selected == "4":
    import o5odik_run
elif selected == "5":
    import h6todik_run
elif selected == "6":
    import h7tedik_run
elif selected == "7":
    import ny8dik_run
