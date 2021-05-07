import unit
import var
import time
import pygame_module as extra_mod


def inter(x1, x2, db1):
    if x1 >= x2 - db1 and x1 < 10000 and x2 < 10000:
        return True
    else:
        return False


def namesput():
    print("Enter the name of the first player")
    var.Player1 = input()
    print("Enter the name of the second player")
    var.Player2 = input()


def start():
    extra_mod.start()


def end():
    extra_mod.end()
    extra_mod.saveUpdates()


def X2on(a):
    if (a):
        if (var.LCastle.money >= var.Lpow[0].cost):
            var.LCastle.money -= var.Lpow[0].cost
            var.Lpow[0].usePower(var.LCastle)
    else:
        if (var.RCastle.money >= var.Rpow[0].cost):
            var.RCastle.money -= var.Rpow[0].cost
            var.Rpow[0].usePower(var.RCastle)


def X3on(a):
    if (a):
        if (var.LCastle.money >= var.Lpow[1].cost):
            var.LCastle.money -= var.Lpow[1].cost
            var.Lpow[1].usePower(var.LCastle)
    else:
        if (var.RCastle.money >= var.Rpow[1].cost):
            var.RCastle.money -= var.Rpow[1].cost
            var.Rpow[1].usePower(var.RCastle)


def HHPon(a):
    if (a):
        if (var.LCastle.money >= var.Lpow[2].cost):
            var.LCastle.money -= var.Lpow[2].cost
            var.Lpow[2].usePower(var.LCastle)
    else:
        if (var.RCastle.money >= var.Rpow[2].cost):
            var.RCastle.money -= var.Rpow[2].cost
            var.Rpow[2].usePower(var.RCastle)


def FHPon(a):
    if (a):
        if (var.LCastle.money >= var.Lpow[3].cost):
            var.LCastle.money -= var.Lpow[3].cost
            var.Lpow[3].usePower(var.LCastle)
    else:
        if (var.RCastle.money >= var.Rpow[3].cost):
            var.RCastle.money -= var.Rpow[3].cost
            var.Rpow[3].usePower(var.RCastle)


def GodModeOn(a):
    if (a):
        if (var.LCastle.money >= var.Lpow[4].cost):
            var.LCastle.money -= var.Lpow[4].cost
            var.Lpow[4].usePower(var.LCastle)
    else:
        if (var.RCastle.money >= var.Rpow[4].cost):
            var.RCastle.money -= var.Rpow[4].cost
            var.Rpow[4].usePower(var.RCastle)


def lvlup(a):
    if (a):
        if (var.LCastle.money >= var.LCastle.LVL * 10):
            var.LCastle.money -= var.LCastle.LVL * 10
            var.LCastle.updateLVL(var.LCastle)
    else:
        if (var.RCastle.money >= var.RCastle.LVL * 10):
            var.RCastle.money -= var.RCastle.LVL * 10
            var.RCastle.updateLVL(var.RCastle)


def buyLI():
    if var.LCastle.money >= var.Costs.I:
        var.LCastle.Army.append(unit.CFactoryLMain().createLI().create())
        var.LCastle.money -= var.Costs.I
        var.LCastle.I += 1


def buyLA():
    if var.LCastle.money >= var.Costs.A:
        var.LCastle.Army.append(unit.CFactoryLMain().createLA().create())
        var.LCastle.money -= var.Costs.A
        var.LCastle.A += 1


def buyLH():
    if var.LCastle.money >= var.Costs.H:
        var.LCastle.Army.append(unit.CFactoryLMain().createLH().create())
        var.LCastle.money -= var.Costs.H
        var.LCastle.H += 1


def buyLG():
    if var.LCastle.money >= var.Costs.G:
        var.LCastle.Army.append(unit.CFactoryLMain().createLG().create())
        var.LCastle.money -= var.Costs.G
        var.LCastle.G += 1


def buyLD():
    if var.LCastle.money >= var.Costs.D:
        var.LCastle.Army.append(unit.CFactoryLMain().createLD().create())
        var.LCastle.money -= var.Costs.D
        var.LCastle.D += 1



def buyRI():
    if var.RCastle.money >= var.Costs.I:
        var.RCastle.Army.append(unit.CFactoryRMain().createRI().create())
        var.RCastle.money -= var.Costs.I
        var.RCastle.I += 1


def buyRA():
    if var.RCastle.money >= var.Costs.A:
        var.RCastle.Army.append(unit.CFactoryRMain().createRA().create())
        var.RCastle.money -= var.Costs.A
        var.RCastle.A += 1


def buyRH():
    if var.RCastle.money >= var.Costs.H:
        var.RCastle.Army.append(unit.CFactoryRMain().createRH().create())
        var.RCastle.money -= var.Costs.H
        var.RCastle.H += 1


def buyRG():
    if var.RCastle.money >= var.Costs.G:
        var.RCastle.Army.append(unit.CFactoryRMain().createRG().create())
        var.RCastle.money -= var.Costs.G
        var.RCastle.G += 1


def buyRD():
    if var.RCastle.money >= var.Costs.D:
        var.RCastle.Army.append(unit.CFactoryRMain().createRD().create())
        var.RCastle.money -= var.Costs.D
        var.RCastle.D += 1


def checkKeyDown():
    extra_mod.checkKeyDown()
    for i in var.list_of_com:
        if i == 'buyLI':
            buyLI()
        if i == 'buyLA':
            buyLA()
        if i == 'buyLH':
            buyLH()
        if i == 'buyLG':
            buyLG()
        if i == 'buyLD':
            buyLD()
        if i == 'buyRI':
            buyRI()
        if i == 'buyRA':
            buyRA()
        if i == 'buyRH':
            buyRH()
        if i == 'buyRG':
            buyRG()
        if i == 'buyRD':
            buyRD()
        if i == 'X21':
            X2on(True)
        if i == 'X20':
            X2on(False)
        if i == 'X31':
            X3on(True)
        if i == 'X30':
            X3on(False)
        if i == 'HHP1':
            HHPon(True)
        if i == 'HHP0':
            HHPon(False)
        if i == 'FHP1':
            FHPon(True)
        if i == 'FHP0':
            FHPon(False)
        if i == 'GM1':
            GodModeOn(True)
        if i == 'GM0':
            GodModeOn(False)
        if i == 'LVLUP1':
            lvlup(True)
        if i == 'LVLUP0':
            lvlup(False)
    var.list_of_com.clear()



def unitVSunit():
    for i in var.LCastle.Army:
        for j in var.RCastle.Army:
            if inter(i.x, j.x, i.width):
                if (i.death and j.death):
                    if (j.time_for_attack + j.time_of_attack <= time.time()):
                        i.health -= j.short_power
                        j.time_for_attack = time.time()
                    if (i.time_for_attack + i.time_of_attack <= time.time()):
                        j.health -= i.short_power
                        i.time_for_attack = time.time()
                    if (i.health <= 0):
                        i.death = False
                        if (i.tip == "LI"):
                            var.LCastle.I -= 1
                        elif (i.tip == "LA"):
                            var.LCastle.A -= 1
                        elif (i.tip == "LH"):
                            var.LCastle.H -= 1
                        elif (i.tip == "LG"):
                            var.LCastle.G -= 1
                        elif (i.tip == "LD"):
                            var.LCastle.D -= 1
                    if (j.health <= 0):
                        j.death = False
                        if (j.tip == "RI"):
                            var.RCastle.I -= 1
                        elif (j.tip == "RA"):
                            var.RCastle.A -= 1
                        elif (j.tip == "RH"):
                            var.RCastle.H -= 1
                        elif (j.tip == "RG"):
                            var.RCastle.G -= 1
                        elif (j.tip == "RD"):
                            var.RCastle.D -= 1


def unitVScastle():
    for i in var.LCastle.Army:
        if inter(i.x, var.RCastle.x, i.width):
            if (i.death and var.RCastle.HP > 0):
                if (i.time_for_attack + i.time_of_attack <= time.time()):
                    var.RCastle.HP -= i.short_power
                    if (var.RCastle.HP <= 0):
                        var.RCastle.HP = 0
                        end()
                    i.time_for_attack = time.time()
                if (var.RCastle.cur_time + var.RCastle.time_of_attack <= time.time()):
                    i.health -= var.RCastle.power
                    var.RCastle.cur_time = time.time()
                if (i.health <= 0):
                    i.death = False

    for i in var.RCastle.Army:
        if inter(var.LCastle.x, i.x, var.LCastle.width):
            if (i.death and var.LCastle.HP > 0):
                if (i.time_for_attack + i.time_of_attack <= time.time()):
                    var.LCastle.HP -= i.short_power
                    if (var.LCastle.HP <= 0):
                        var.LCastle.HP = 0
                        end()
                    i.time_for_attack = time.time()
                if (var.LCastle.cur_time + var.LCastle.time_of_attack <= time.time()):
                    i.health -= var.LCastle.power
                    var.LCastle.cur_time = time.time()
                if (i.health <= 0):
                    i.death = False

def updateGran():
    var.LGran = 1215
    var.RGran = 65
    for i in var.RCastle.Army:
        if i.x + 10 < var.LGran:
            var.LGran = i.x + 10

    for i in var.LCastle.Army:
        if i.x + i.width - 10 > var.RGran:
            var.RGran = i.x + i.width - 10


def moveUnit():
    updateGran()

    for i in var.LCastle.Army:
        if (i.x + i.speed_x + i.width < var.LGran):
            i.x += i.speed_x
            i.y += i.speed_y

    for i in var.RCastle.Army:
        if (i.x + i.speed_x > var.RGran):
            i.x += i.speed_x
            i.y += i.speed_y


def fight():
    unitVSunit()
    unitVScastle()
    var.LCastle.unitDeath(var.LCastle)
    var.RCastle.unitDeath(var.RCastle)


def updateScreen():
    extra_mod.updateGraph()
    extra_mod.updateCount()
    extra_mod.updatepowertut()
    extra_mod.updateunit()
    extra_mod.updateCost()
    extra_mod.saveUpdates()


def updatePowers():
    var.Lpow[0].updatePower(var.LCastle)
    var.Lpow[1].updatePower(var.LCastle)
    var.Lpow[4].updatePower(var.LCastle)
    var.Rpow[0].updatePower(var.RCastle)
    var.Rpow[1].updatePower(var.RCastle)
    var.Rpow[4].updatePower(var.RCastle)


def updateMoney():
    if var.LCastle.cur_time == 0:
        var.LCastle.cur_time = time.time()
    else:
        if var.LCastle.cur_time + 1 <= time.time():
            var.LCastle.money += var.LCastle.money_speed * var.LCastle.LVL
            var.LCastle.cur_time = time.time()

    if var.RCastle.cur_time == 0:
        var.RCastle.cur_time = time.time()
    else:
        if var.RCastle.cur_time + 1 <= time.time():
            var.RCastle.money += var.RCastle.money_speed * var.RCastle.LVL
            var.RCastle.cur_time = time.time()


def quit():
    extra_mod.quit()






