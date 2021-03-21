import unittest
from abc import ABC, abstractmethod


start_pos_left_x = 40
start_pos_left_y = 350
start_pos_right_x = 1200
start_pos_right_y = 350


class IWarrior:
    health = 0
    short_power = 0
    long_power = 0
    time_of_attack = 0
    time_for_attack = 0
    speed_x = 0
    speed_y = 0
    death = True
    x = 0
    y = 0
    width = 0
    height = 0
    tip = ""

    @abstractmethod
    def get_x(self):
        pass

    @abstractmethod
    def get_y(self):
        pass

    @abstractmethod
    def get_health(self):
        pass

    @abstractmethod
    def get_short_power(self):
        pass

    @abstractmethod
    def get_long_power(self):
        pass

    @abstractmethod
    def get_time_of_attack(self):
        pass

    @abstractmethod
    def get_time_for_attack(self):
        pass

    @abstractmethod
    def get_speed_x(self):
        pass

    @abstractmethod
    def get_speed_y(self):
        pass

    @abstractmethod
    def get_width(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_death(self):
        pass

    @abstractmethod
    def get_tip(self):
        pass

    @abstractmethod
    def movement(self):
        pass

    @abstractmethod
    def attack(self, warrior):
        pass


class ILWarrior:
    health = 0
    short_power = 0
    long_power = 0
    time_of_attack = 0
    time_for_attack = 0
    speed_x = 0
    speed_y = 0
    death = True
    x = start_pos_left_x
    y = start_pos_left_y
    width = 0
    height = 0
    tip = ""

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


class CLInfantry(ILWarrior):
    health = 100
    short_power = 20
    long_power = 0
    time_of_attack = 2
    time_for_attack = 0
    speed_x = 0.1
    speed_y = 0
    width = 40
    height = 40
    death = True
    tip = "LI"


class CLArcher(ILWarrior):
    health = 70
    short_power = 5
    long_power = 20
    time_of_attack = 3
    time_for_attack = 0
    speed_x = 0.1
    speed_y = 0
    width = 40
    height = 48
    death = True
    tip = "LA"


class CLHorseman(ILWarrior):
    health = 200
    short_power = 50
    long_power = 0
    time_of_attack = 4
    time_for_attack = 0
    speed_x = 0.2
    speed_y = 0
    width = 50
    height = 43
    death = True
    tip = "LH"


class CLDragon(ILWarrior):
    health = 500
    long_power = 100
    short_power = 60
    time_of_attack = 7
    time_for_attack = 0
    speed_x = 0.3
    speed_y = 0
    width = 72
    height = 46
    death = True
    tip = "LD"


class CLGolem(ILWarrior):
    health = 1000
    long_power = 0
    short_power = 20
    time_of_attack = 7
    time_for_attack = 0
    speed_x = 0.05
    speed_y = 0
    width = 50
    height = 61
    death = True
    tip = "LG"


class IRWarrior:
    health = 0
    short_power = 0
    long_power = 0
    time_of_attack = 0
    time_for_attack = 0
    speed_x = 0
    speed_y = 0
    death = True
    x = start_pos_right_x
    y = start_pos_right_y
    width = 0
    height = 0
    tip = ""


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

    def __init__(self):
        pass

    def movement(self):
        self.x -= self.speed_x
        self.y += self.speed_y

    def attack(self, warrior):
        if self.time_for_attack >= self.time_of_attack:
            self.time_for_attack -= self.time_of_attack
            warrior.health -= self.short_power
            if warrior.health <= 0:
                warrior.death = False
                warrior.x = 10000
                warrior.y = 10000


class CRInfantry(IRWarrior):
    health = 100
    short_power = 20
    long_power = 0
    time_of_attack = 2
    time_for_attack = 0
    speed_x = 0.1
    speed_y = 0
    width = 40
    height = 53
    death = True
    tip = "RI"


class CRArcher(IRWarrior):
    health = 70
    short_power = 5
    long_power = 20
    time_of_attack = 3
    time_for_attack = 0
    speed_x = 0.1
    speed_y = 0
    width = 50
    height = 62
    death = True
    tip = "RA"


class CRHorseman(IRWarrior):
    health = 200
    short_power = 50
    long_power = 0
    time_of_attack = 4
    time_for_attack = 0
    speed_x = 0.2
    speed_y = 0
    width = 55
    height = 37
    death = True
    tip = "RH"


class CRDragon(IRWarrior):
    health = 500
    long_power = 100
    short_power = 50
    time_of_attack = 7
    time_for_attack = 0
    speed_x = 0.3
    speed_y = 0
    width = 70
    height = 43
    death = True
    tip = "RD"


class CRGolem(IRWarrior):
    health = 1000
    long_power = 0
    short_power = 20
    time_of_attack = 7
    time_for_attack = 0
    speed_x = 0.05
    speed_y = 0
    width = 50
    height = 65
    death = True
    tip = "RG"


class IFactoryWarriors():
    @abstractmethod
    def create(self):
        pass


class CFactoryLInfantry(IFactoryWarriors):
    def create(self):
        return CLInfantry()


class CFactoryLArcher(IFactoryWarriors):
    def create(self):
        return CLArcher()


class CFactoryLHorseman(IFactoryWarriors):
    def create(self):
        return CLHorseman()


class CFactoryLDragon(IFactoryWarriors):
    def create(self):
        return CLDragon()


class CFactoryLGolem(IFactoryWarriors):
    def create(self):
        return CLGolem()


class CFactoryRInfantry(IFactoryWarriors):
    def create(self):
        return CRInfantry()


class CFactoryRArcher(IFactoryWarriors):
    def create(self):
        return CRArcher()


class CFactoryRHorseman(IFactoryWarriors):
    def create(self):
        return CRHorseman()


class CFactoryRDragon(IFactoryWarriors):
    def create(self):
        return CRDragon()


class CFactoryRGolem(IFactoryWarriors):
    def create(self):
        return CRGolem()

class CLCastleArmy():
    LArmy = []
    countArmy = 0
    HP = 10000
    LVL = 1
    power = 0
    money = 0
    money_speed = 1
    LI = 0
    LA = 0
    LH = 0
    LG = 0
    LD = 0

    def __init__(self):
        pass

    def unitDeath(self):
        temp = []
        for i in self.LArmy:
            if i.death:
                temp.append(i)
        self.LArmy = temp
        self.countArmy = len(temp)


class CRCastleArmy():
    RArmy = []
    countArmy = 0
    HP = 10000
    LVL = 1
    power = 0
    money = 0
    money_speed = 1
    RI = 0
    RA = 0
    RH = 0
    RG = 0
    RD = 0

    def __init__(self):
        pass

    def unitDeath(self):
        temp = []
        for i in self.RArmy:
            if i.death:
                temp.append(i)
        self.RArmy = temp
        self.countArmy = len(temp)


class CFactoryLCastleArmy():
    def create(self):
        return CLCastleArmy

class CFactoryRCastleArmy():
    def create(self):
        return CRCastleArmy


class CFactoryLMain():
    def __init__(self):
        pass

    def createLI(self):
        return CFactoryLInfantry()

    def createLA(self):
        return CFactoryLArcher()

    def createLH(self):
        return CFactoryLHorseman()

    def createLG(self):
        return CFactoryLGolem()

    def createLD(self):
        return CFactoryLDragon()

    def createLC(self):
        return CFactoryLCastleArmy()


class CFactoryRMain():
    def __init__(self):
        pass

    def createRI(self):
        return CFactoryRInfantry()

    def createRA(self):
        return CFactoryRArcher()

    def createRH(self):
        return CFactoryRHorseman()

    def createRG(self):
        return CFactoryRGolem()

    def createRD(self):
        return CFactoryRDragon()

    def createRC(self):
        return CFactoryRCastleArmy()

class TestUnitMethods(unittest.TestCase):
    FLM = CFactoryLMain()
    FRM = CFactoryRMain()
    LCArmy = FLM.createLC().create()
    RCArmy = FRM.createRC().create()

    def test_Infantry(self):
        LI = self.FLM.createLI().create()
        RI = self.FRM.createRI().create()
        self.LCArmy.LArmy.append(LI)
        self.RCArmy.RArmy.append(RI)
        self.LCArmy.countArmy += 1
        self.RCArmy.countArmy += 1
        a = 100
        self.assertEqual(40, LI.get_x())
        self.assertEqual(1200, RI.get_x())
        self.assertEqual(a, LI.get_health())
        self.assertEqual(a, RI.get_health())
        self.assertIsNotNone(self.LCArmy.LArmy[self.LCArmy.countArmy - 1])
        self.assertIsNotNone(self.RCArmy.RArmy[self.RCArmy.countArmy - 1])
        self.assertEqual(a, self.LCArmy.LArmy[self.LCArmy.countArmy - 1].health)
        self.assertEqual(a, self.RCArmy.RArmy[self.RCArmy.countArmy - 1].health)
        self.LCArmy.LArmy[self.LCArmy.countArmy - 1].death = False
        self.RCArmy.RArmy[self.RCArmy.countArmy - 1].death = False
        b = self.LCArmy.countArmy - 1
        self.LCArmy.unitDeath(self.LCArmy)
        self.RCArmy.unitDeath(self.RCArmy)
        self.assertEqual(b, self.LCArmy.countArmy)
        self.assertEqual(b, self.RCArmy.countArmy)


    def test_Archer(self):
        LA = self.FLM.createLA().create()
        RA = self.FRM.createRA().create()
        self.LCArmy.LArmy.append(LA)
        self.RCArmy.RArmy.append(RA)
        self.LCArmy.countArmy += 1
        self.RCArmy.countArmy += 1
        a = 70
        self.assertEqual(40, LA.get_x())
        self.assertEqual(1200, RA.get_x())
        self.assertEqual(a, LA.get_health())
        self.assertEqual(a, RA.get_health())
        self.assertIsNotNone(self.LCArmy.LArmy[self.LCArmy.countArmy - 1])
        self.assertIsNotNone(self.RCArmy.RArmy[self.RCArmy.countArmy - 1])
        self.assertEqual(a, self.LCArmy.LArmy[self.LCArmy.countArmy - 1].health)
        self.assertEqual(a, self.RCArmy.RArmy[self.RCArmy.countArmy - 1].health)
        self.LCArmy.LArmy[self.LCArmy.countArmy - 1].death = False
        self.RCArmy.RArmy[self.RCArmy.countArmy - 1].death = False
        b = self.LCArmy.countArmy - 1
        self.LCArmy.unitDeath(self.LCArmy)
        self.RCArmy.unitDeath(self.RCArmy)
        self.assertEqual(b, self.LCArmy.countArmy)
        self.assertEqual(b, self.RCArmy.countArmy)

    def test_Horseman(self):
        LH = self.FLM.createLH().create()
        RH = self.FRM.createRH().create()
        self.LCArmy.LArmy.append(LH)
        self.RCArmy.RArmy.append(RH)
        self.LCArmy.countArmy += 1
        self.RCArmy.countArmy += 1
        a = 200
        self.assertEqual(40, LH.get_x())
        self.assertEqual(1200, RH.get_x())
        self.assertEqual(a, LH.get_health())
        self.assertEqual(a, RH.get_health())
        self.assertIsNotNone(self.LCArmy.LArmy[self.LCArmy.countArmy - 1])
        self.assertIsNotNone(self.RCArmy.RArmy[self.RCArmy.countArmy - 1])
        self.assertEqual(a, self.LCArmy.LArmy[self.LCArmy.countArmy - 1].health)
        self.assertEqual(a, self.RCArmy.RArmy[self.RCArmy.countArmy - 1].health)
        self.LCArmy.LArmy[self.LCArmy.countArmy - 1].death = False
        self.RCArmy.RArmy[self.RCArmy.countArmy - 1].death = False
        b = self.LCArmy.countArmy - 1
        self.LCArmy.unitDeath(self.LCArmy)
        self.RCArmy.unitDeath(self.RCArmy)
        self.assertEqual(b, self.LCArmy.countArmy)
        self.assertEqual(b, self.RCArmy.countArmy)

    def test_Golem(self):
        LG = self.FLM.createLG().create()
        RG = self.FRM.createRG().create()
        self.LCArmy.LArmy.append(LG)
        self.RCArmy.RArmy.append(RG)
        self.LCArmy.countArmy += 1
        self.RCArmy.countArmy += 1
        a = 1000
        self.assertEqual(40, LG.get_x())
        self.assertEqual(1200, RG.get_x())
        self.assertEqual(a, LG.get_health())
        self.assertEqual(a, RG.get_health())
        self.assertIsNotNone(self.LCArmy.LArmy[self.LCArmy.countArmy - 1])
        self.assertIsNotNone(self.RCArmy.RArmy[self.RCArmy.countArmy - 1])
        self.assertEqual(a, self.LCArmy.LArmy[self.LCArmy.countArmy - 1].health)
        self.assertEqual(a, self.RCArmy.RArmy[self.RCArmy.countArmy - 1].health)
        self.LCArmy.LArmy[self.LCArmy.countArmy - 1].death = False
        self.RCArmy.RArmy[self.RCArmy.countArmy - 1].death = False
        b = self.LCArmy.countArmy - 1
        self.LCArmy.unitDeath(self.LCArmy)
        self.RCArmy.unitDeath(self.RCArmy)
        self.assertEqual(b, self.LCArmy.countArmy)
        self.assertEqual(b, self.RCArmy.countArmy)

    def test_Dragon(self):
        LD = self.FLM.createLD().create()
        RD = self.FRM.createRD().create()
        self.LCArmy.LArmy.append(LD)
        self.RCArmy.RArmy.append(RD)
        self.LCArmy.countArmy += 1
        self.RCArmy.countArmy += 1
        a = 500
        self.assertEqual(40, LD.get_x())
        self.assertEqual(1200, RD.get_x())
        self.assertEqual(a, LD.get_health())
        self.assertEqual(a, RD.get_health())
        self.assertIsNotNone(self.LCArmy.LArmy[self.LCArmy.countArmy - 1])
        self.assertIsNotNone(self.RCArmy.RArmy[self.RCArmy.countArmy - 1])
        self.assertEqual(a, self.LCArmy.LArmy[self.LCArmy.countArmy - 1].health)
        self.assertEqual(a, self.RCArmy.RArmy[self.RCArmy.countArmy - 1].health)
        self.LCArmy.LArmy[self.LCArmy.countArmy - 1].death = False
        self.RCArmy.RArmy[self.RCArmy.countArmy - 1].death = False
        b = self.LCArmy.countArmy - 1
        self.LCArmy.unitDeath(self.LCArmy)
        self.RCArmy.unitDeath(self.RCArmy)
        self.assertEqual(b, self.LCArmy.countArmy)
        self.assertEqual(b, self.RCArmy.countArmy)

    def test_Castle(self):
        LC = self.FLM.createLC().create()
        RC = self.FRM.createRC().create()
        a = 10000
        self.assertIsNotNone(LC)
        self.assertIsNotNone(RC)
        self.assertEqual(a, LC.HP)
        self.assertEqual(a, RC.HP)


if __name__ == '__main__':
    unittest.main()


