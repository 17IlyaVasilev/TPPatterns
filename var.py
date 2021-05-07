import unit
import img
import object


done = True
flag = True

unitgraph = []
unitx = []
unity = []
line = []
list_of_com = []

Lpow = []
Rpow = []
Lpow.append(object.CUpDamageX2())
Lpow.append(object.CUpDamageX3())
Lpow.append(object.CRestoreHalfHP())
Lpow.append(object.CRestoreFullHP())
Lpow.append(object.CGodMode())

Rpow.append(object.CUpDamageX2())
Rpow.append(object.CUpDamageX3())
Rpow.append(object.CRestoreHalfHP())
Rpow.append(object.CRestoreFullHP())
Rpow.append(object.CGodMode())

LGran = 1230
RGran = 50

Player1 = ""
Player2 = ""

psize = 40

LCastle = object.CFactoryLCastleArmy().create()
RCastle = object.CFactoryRCastleArmy().create()
LCastle.Army.clear()
RCastle.Army.clear()
LCastle.I = 0
LCastle.A = 0
LCastle.H = 0
LCastle.G = 0
LCastle.D = 0
RCastle.I = 0
RCastle.A = 0
RCastle.H = 0
RCastle.G = 0
RCastle.D = 0


class Costs:
    I = 5
    A = 7
    H = 20
    G = 50
    D = 100





