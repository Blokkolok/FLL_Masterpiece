# Program működése

Program környezet: Mi már 3 éve micropythonban programozzunk a robotot. Az idei év kezdetén elhatároztuk, hogy ki fogjuk próbálni az összes elérhető futtató környezetet.
Kipróbáltuk az alap spike-osat, annak is több verzióját, amihez a coachunk segítségével vissza butítottuk a robotot. Kipróbáltuk a vs codeon belül futó környezetet is, illetve a pybrick-et és annak beta változatát. Ezek közül a **pybrick betát**(https://beta.pybricks.com/) találtuk a számunkra legjobbnak. [Részletek blogunkon](https://www.blokkolok.hu/pybricks-python/) 
Itt a robot az alap mozgás parancsoknál is giroszkóppal nézi a mozgást és ha kell korrigálja azt.
Az eddigi években ehhez saját függvényeket írtunk, idén viszont erre nem volt szükség a pybrick mozgató parancsai elég pontosak. 

***menu.py*** a futtatandó program, a működéshez ez a program importálja be az összes futtatandó feladatot, amik közül a gombokkal lehet választani.
A gyorsabb váltásokat segítendő a menü mindig a következő futás programjával töltődik be.
