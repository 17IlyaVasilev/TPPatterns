import sys
import random
import time
import unit
import func
import var
import img


func.start()
func.namesput()


while (var.done):
    func.checkKeyDown()
    if (var.flag):
        func.moveUnit()
        func.fight()
        func.updatePowers()
        func.updateMoney()
        func.updateScreen()
    else:
        func.end()

func.quit()



