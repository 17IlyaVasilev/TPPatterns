import pygame
from abc import ABC, abstractmethod


pygame.init()


class IWarrior:
    health = 0
    usual_health = 0
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


class ILWarrior(IWarrior):
    x = 40
    y = 475

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
    usual_health = health
    short_power = 20
    long_power = 0
    time_of_attack = 2
    time_for_attack = 0
    speed_x = 0.4
    speed_y = 0
    width = 60
    height = 62
    death = True
    tip = "LI"
    y = 475 - height


class CLArcher(ILWarrior):
    health = 70
    usual_health = health
    short_power = 5
    long_power = 20
    time_of_attack = 3
    time_for_attack = 0
    speed_x = 0.4
    speed_y = 0
    width = 54
    height = 70
    death = True
    tip = "LA"
    y = 475 - height


class CLHorseman(ILWarrior):
    health = 200
    usual_health = health
    short_power = 50
    long_power = 0
    time_of_attack = 4
    time_for_attack = 0
    speed_x = 0.8
    speed_y = 0
    width = 75
    height = 76
    death = True
    tip = "LH"
    y = 475 - height


class CLDragon(ILWarrior):
    health = 500
    usual_health = health
    long_power = 100
    short_power = 60
    time_of_attack = 5
    time_for_attack = 0
    speed_x = 1.5
    speed_y = 0
    width = 150
    height = 89
    death = True
    tip = "LD"
    y = 475 - height


class CLGolem(ILWarrior):
    health = 1000
    usual_health = health
    long_power = 0
    short_power = 20
    time_of_attack = 7
    time_for_attack = 0
    speed_x = 0.2
    speed_y = 0
    width = 81
    height = 100
    death = True
    tip = "LG"
    y = 475 - height


class IRWarrior(IWarrior):
    x = 1200
    y = 475

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
    usual_health = health
    short_power = 20
    long_power = 0
    time_of_attack = 2
    time_for_attack = 0
    speed_x = -0.4
    speed_y = 0
    width = 48
    height = 60
    death = True
    tip = "RI"
    y = 475 - height


class CRArcher(IRWarrior):
    health = 70
    usual_health = health
    short_power = 5
    long_power = 20
    time_of_attack = 3
    time_for_attack = 0
    speed_x = -0.4
    speed_y = 0
    width = 56
    height = 70
    death = True
    tip = "RA"
    y = 475 - height


class CRHorseman(IRWarrior):
    health = 200
    usual_health = health
    short_power = 50
    long_power = 0
    time_of_attack = 4
    time_for_attack = 0
    speed_x = -0.8
    speed_y = 0
    width = 93
    height = 75
    death = True
    tip = "RH"
    y = 475 - height


class CRDragon(IRWarrior):
    health = 500
    usual_health = health
    long_power = 100
    short_power = 50
    time_of_attack = 5
    time_for_attack = 0
    speed_x = -1.5
    speed_y = 0
    width = 150
    height = 123
    death = True
    tip = "RD"
    y = 475 - height


class CRGolem(IRWarrior):
    health = 1000
    usual_health = health
    long_power = 0
    short_power = 20
    time_of_attack = 7
    time_for_attack = 0
    speed_x = -0.2
    speed_y = 0
    width = 89
    height = 110
    death = True
    tip = "RG"
    y = 475 - height


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