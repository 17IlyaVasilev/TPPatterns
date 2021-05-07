from abc import ABC, abstractmethod
import time
import unittest


class ICastle:
    countArmy = 0
    HP = 10000
    LVL = 1
    power = 5
    money = 0
    money_speed = 1
    time_of_attack = 20
    cur_time = 0
    width = 75
    height = 300
    I = 0
    A = 0
    H = 0
    G = 0
    D = 0
    x = 0
    y = 0

    def __init__(self):
        pass

    @abstractmethod
    def unit_add(self, unit):
        pass

    @abstractmethod
    def unitDeath(self):
        pass

    def updateLVL(self):
        self.LVL += 1

    def getI(self):
        return self.I

    def getA(self):
        return self.A

    def getH(self):
        return self.H

    def getG(self):
        return self.G

    def getD(self):
        return self.D

    def getMoney(self):
        return self.money

    def getHP(self):
        return self.HP

    def getLVL(self):
        return self.LVL

    def getCountArmy(self):
        return self.countArmy

    def getPower(self):
        return self.power

    def upLVL(self):
        self.LVL += 1

    def setMoney(self, value):
        self.money += value

    def setHP(self, value):
        self.HP -= value

    def setPower(self, value):
        self.power += value


class CLCastleArmy(ICastle):
    x = 0
    y = 175
    Army = []

    def __init__(self):
        super().__init__()

    def unit_add(self, unit):
        self.Army.append(unit)
        self.countArmy += 1
        if unit.tip == "I":
            self.I += 1
        if unit.tip == "A":
            self.A += 1
        if unit.tip == "H":
            self.H += 1
        if unit.tip == "G":
            self.G += 1
        if unit.tip == "D":
            self.D += 1

    def unitDeath(self):
        temp = []
        for i in self.Army:
            if i.death:
                temp.append(i)
            else:
                self.countArmy -= 1
            if i.tip == "I":
                self.I -= 1
            if i.tip == "A":
                self.A -= 1
            if i.tip == "H":
                self.H -= 1
            if i.tip == "G":
                self.G -= 1
            if i.tip == "D":
                self.D -= 1
        self.Army = temp


class CRCastleArmy(ICastle):
    x = 1205
    y = 175
    Army = []

    def __init__(self):
        super().__init__()

    def unit_add(self, unit):
        self.Army.append(unit)
        self.countArmy += 1
        if unit.tip == "I":
            self.I += 1
        if unit.tip == "A":
            self.A += 1
        if unit.tip == "H":
            self.H += 1
        if unit.tip == "G":
            self.G += 1
        if unit.tip == "D":
            self.D += 1

    def unitDeath(self):
        temp = []
        for i in self.Army:
            if i.death:
                temp.append(i)
            else:
                self.countArmy -= 1
            if i.tip == "I":
                self.I -= 1
            if i.tip == "A":
                self.A -= 1
            if i.tip == "H":
                self.H -= 1
            if i.tip == "G":
                self.G -= 1
            if i.tip == "D":
                self.D -= 1
        self.Army = temp


class CFactoryLCastleArmy:
    def create(self):
        return CLCastleArmy


class CFactoryRCastleArmy:
    def create(self):
        return CRCastleArmy


class IPower:
    cost = 0
    time_per_1 = 0
    all_time = 0
    start_time = 0
    used = False
    mult = 0

    @abstractmethod
    def usePower(self, Castle):
        pass

    @abstractmethod
    def updatePower(self, Castle):
        pass


class CUpDamageX2(IPower):
    cost = 20
    time_per_1 = 10
    all_time = 0
    start_time = 0
    mult = 2

    def __init__(self):
        super().__init__()

    def usePower(self, Castle):
        if self.used:
            self.all_time += self.time_per_1
        else:
            self.used = True
            self.all_time += self.time_per_1
            for i in Castle.Army:
                i.short_power *= self.mult
                i.long_power *= self.mult
            self.start_time = time.time()

    def updatePower(self, Castle):
        if self.used and time.time() >= self.start_time + self.all_time:
            self.used = False
            self.all_time = 0
            self.start_time = 0
            for i in Castle.Army:
                i.short_power /= self.mult
                i.long_power /= self.mult


class CUpDamageX3(IPower):
    cost = 30
    time_per_1 = 7
    all_time = 0
    start_time = 0
    mult = 3

    def __init__(self):
        super().__init__()

    def usePower(self, Castle):
        if self.used:
            self.all_time += self.time_per_1
        else:
            self.used = True
            self.all_time += self.time_per_1
            for i in Castle.Army:
                i.short_power *= self.mult
                i.long_power *= self.mult
            self.start_time = time.time()

    def updatePower(self, Castle):
        if self.used and time.time() >= self.start_time + self.all_time:
            self.used = False
            self.all_time = 0
            self.start_time = 0
            for i in Castle.Army:
                i.short_power /= self.mult
                i.long_power /= self.mult


class CRestoreHalfHP(IPower):
    cost = 50
    mult = 0.5

    def __init__(self):
        super().__init__()

    def usePower(self, Castle):
        for i in Castle.Army:
            i.health += self.mult * i.usual_health
            if i.health > i.usual_health:
                i.health = i.usual_health


class CRestoreFullHP(IPower):
    cost = 100
    mult = 1

    def __init__(self):
        super().__init__()

    def usePower(self, Castle):
        for i in Castle.Army:
            i.health = self.mult * i.usual_health


class CGodMode(IPower):
    GodHP = CRestoreFullHP()
    GodDamage = CUpDamageX2()
    cost = 300
    used = False
    time_per_1 = 10
    all_time = 0
    start_time = 0
    GodHP.mult = 5
    GodDamage.mult = 5
    GodDamage.time_per_1 = time_per_1
    GodHP.time_per_1 = time_per_1

    def __init__(self):
        super().__init__()

    def usePower(self, Castle):
        if not self.used:
            self.used = True
            self.start_time = time.time()
        self.all_time += self.time_per_1
        self.GodHP.usePower(Castle)
        self.GodDamage.usePower(Castle)

    def updatePower(self, Castle):
        if self.used and time.time() >= self.start_time + self.all_time:
            self.used = False
            self.GodHP.mult = 1
            self.GodHP.usePower(Castle)
            self.GodDamage.updatePower(Castle)


'''class TestUnitMethods(unittest.TestCase):
    class CUnit:
        health = 100
        usual_health = 100
        short_power = 20
        long_power = 0
        time_of_attack = 2
        time_for_attack = 0
        speed_x = 0.1
        speed_y = 0
        width = 40
        height = 40
        death = True
        tip = "I"
        x = 0
        y = 0

        def __init__(self):
            pass

        def get_x(self):
            return self.x

        def get_y(self):
            return self.y

        def get_health(self):
            return self.health

        def get_short_power(self):
            return self.short_power

        def get_long_power(self):
            return self.long_power

        def get_time_of_attack(self):
            return self.time_of_attack

        def get_time_for_attack(self):
            return self.time_for_attack

        def get_speed_x(self):
            return self.speed_x

        def get_speed_y(self):
            return self.speed_y

        def get_width(self):
            return self.width

        def get_height(self):
            return self.height

        def get_death(self):
            return self.death

        def get_tip(self):
            return self.tip

        def movement(self):
            self.x += self.speed_x
            self.y += self.speed_y

        def attack(self, warrior):
            if self.time_for_attack >= self.time_of_attack:
                self.time_for_attack -= self.time_of_attack
                warrior.health -= self.short_power
                if warrior.health <= 0:
                    warrior.death = False
                    warrior.x = 10000
                    warrior.y = 10000

    LCastle = CFactoryLCastleArmy().create()
    RCastle = CFactoryRCastleArmy().create()
    for i in range(1, 11):
        temp = CUnit()
        LCastle.unit_add(LCastle, temp)

    def test_Castle(self):
        LC = CFactoryLCastleArmy().create()
        RC = CFactoryRCastleArmy().create()
        a = 10000
        self.assertIsNotNone(LC)
        self.assertIsNotNone(RC)
        self.assertEqual(a, LC.HP)
        self.assertEqual(a, RC.HP)
        self.assertEqual(a, LC.getHP(LC))
        self.assertEqual(a, RC.getHP(RC))
        LC.setMoney(LC, 1000)
        RC.setMoney(RC, 1000)
        self.assertEqual(1000, LC.getMoney(LC))
        self.assertEqual(1000, RC.getMoney(RC))
        self.assertEqual(10, LC.getCountArmy(LC))
        LC.Army[5].death = False
        LC.unitDeath(LC)
        self.assertEqual(9, LC.getCountArmy(LC))

    def test_upX2(self):
        temp = self.CUnit
        UPX2 = CUpDamageX2()
        UPX2.usePower(self.LCastle)
        self.assertEqual(2 * temp.short_power, self.LCastle.Army[1].short_power)
        UPX2.updatePower(self.LCastle)
        self.assertEqual(2 * temp.short_power, self.LCastle.Army[1].short_power)
        time.sleep(10)
        UPX2.updatePower(self.LCastle)
        self.assertEqual(temp.short_power, self.LCastle.Army[1].short_power)

    def test_upX3(self):
        temp = self.CUnit
        UPX2 = CUpDamageX3()
        UPX2.usePower(self.LCastle)
        self.assertEqual(3 * temp.short_power, self.LCastle.Army[1].short_power)
        UPX2.updatePower(self.LCastle)
        self.assertEqual(3 * temp.short_power, self.LCastle.Army[1].short_power)
        time.sleep(7)
        UPX2.updatePower(self.LCastle)
        self.assertEqual(temp.short_power, self.LCastle.Army[1].short_power)

    def test_restoreHalfHp(self):
        temp = self.CUnit
        UPX2 = CRestoreHalfHP()
        self.LCastle.Army[1].health -= 60
        self.assertEqual(temp.usual_health - 60, self.LCastle.Army[1].health)
        UPX2.usePower(self.LCastle)
        self.assertEqual(temp.usual_health - 10, self.LCastle.Army[1].health)

    def test_restoreFullHp(self):
        temp = self.CUnit
        UPX2 = CRestoreFullHP()
        self.LCastle.Army[1].health -= 10
        self.assertEqual(temp.usual_health - 10, self.LCastle.Army[1].health)
        UPX2.usePower(self.LCastle)
        self.assertEqual(temp.usual_health, self.LCastle.Army[1].health)

    def test_godmode(self):
        temp = self.CUnit
        UPX2 = CGodMode()
        UPX2.usePower(self.LCastle)
        self.assertEqual(5 * temp.short_power, self.LCastle.Army[1].short_power)
        self.assertEqual(5 * temp.usual_health, self.LCastle.Army[1].health)
        UPX2.updatePower(self.LCastle)
        self.assertEqual(5 * temp.short_power, self.LCastle.Army[1].short_power)
        self.assertEqual(5 * temp.usual_health, self.LCastle.Army[1].health)
        time.sleep(10)
        UPX2.updatePower(self.LCastle)
        self.assertEqual(temp.short_power, self.LCastle.Army[1].short_power)
        self.assertEqual(temp.usual_health, self.LCastle.Army[1].health)



if __name__ == '__main__':
    unittest.main()'''
