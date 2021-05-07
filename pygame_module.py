import pygame
import var
import unit
import img
import object


pygame.init()


window = pygame.display.set_mode((1280, 640))
screen = pygame.Surface((1280, 640))

bigfont = pygame.font.Font('imgs/font.ttf', 100)
myfont = pygame.font.Font('imgs/font.ttf', 50)
smallfont = pygame.font.Font('imgs/font.ttf', 30)
semallfont = pygame.font.Font('imgs/font.ttf', 20)
efont = pygame.font.Font('imgs/font.ttf', 30)
befont = pygame.font.Font('imgs/font.ttf', 40)
bigefont = pygame.font.Font('imgs/font.ttf', 100)

def start():
    screen.fill((255, 255, 255))
    screen.blit(img.BackGround, (0, 0))
    screen.blit(myfont.render("Enter your names in console, please.", False, (0, 0, 0)), (100, 50))
    saveUpdates()

def end():
    screen.fill((255, 255, 255))
    screen.blit(img.BackGround, (0, 0))
    if var.RCastle.HP <= 0:
        screen.blit(bigefont.render(var.Player1 + " win", False, (0, 0, 0)), (300, 20))
    if var.LCastle.HP <= 0:
        screen.blit(bigefont.render(var.Player2 + " win", False, (0, 0, 0)), (300, 20))
    var.flag = False


def checkKeyDown():
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            var.done = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            var.done = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_1:
            #buyLI()
            var.list_of_com.append('buyLI')
        if e.type == pygame.KEYDOWN and e.key == pygame.K_2:
            #buyLA()
            var.list_of_com.append('buyLA')
        if e.type == pygame.KEYDOWN and e.key == pygame.K_3:
            #buyLH()
            var.list_of_com.append('buyLH')
        if e.type == pygame.KEYDOWN and e.key == pygame.K_4:
            #buyLG()
            var.list_of_com.append('buyLG')
        if e.type == pygame.KEYDOWN and e.key == pygame.K_5:
            #buyLD()
            var.list_of_com.append('buyLD')

        if e.type == pygame.KEYDOWN and e.key == pygame.K_6:
            #buyRI()
            var.list_of_com.append('buyRI')
        if e.type == pygame.KEYDOWN and e.key == pygame.K_7:
            #buyRA()
            var.list_of_com.append('buyRA')
        if e.type == pygame.KEYDOWN and e.key == pygame.K_8:
            #buyRH()
            var.list_of_com.append('buyRH')
        if e.type == pygame.KEYDOWN and e.key == pygame.K_9:
            #buyRG()
            var.list_of_com.append('buyRG')
        if e.type == pygame.KEYDOWN and e.key == pygame.K_0:
            #buyRD()
            var.list_of_com.append('buyRD')

        if e.type == pygame.KEYDOWN and e.key == pygame.K_q:
            #X2on(True)
            var.list_of_com.append('X21')

        if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
            #X3on(True)
            var.list_of_com.append('X31')

        if e.type == pygame.KEYDOWN and e.key == pygame.K_e:
            #HHPon(True)
            var.list_of_com.append('HHP1')

        if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
            #FHPon(True)
            var.list_of_com.append('FHP1')

        if e.type == pygame.KEYDOWN and e.key == pygame.K_u:
            #X2on(False)
            var.list_of_com.append('X20')

        if e.type == pygame.KEYDOWN and e.key == pygame.K_i:
            #X3on(False)
            var.list_of_com.append('X30')

        if e.type == pygame.KEYDOWN and e.key == pygame.K_o:
            # HHPon(False)
            var.list_of_com.append('HHP0')

        if e.type == pygame.KEYDOWN and e.key == pygame.K_p:
            #FHPon(False)
            var.list_of_com.append('FHP0')

        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            #GodModeOn(True)
            var.list_of_com.append('GM1')

        if e.type == pygame.KEYDOWN and e.key == pygame.K_k:
            #GodModeOn(False)
            var.list_of_com.append('GM0')

        if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
            #lvlup(True)
            var.list_of_com.append('LVLUP1')

        if e.type == pygame.KEYDOWN and e.key == pygame.K_l:
            #lvlup(False)
            var.list_of_com.append('LVLUP0')


def updateUnitCastle():
    var.unitgraph.clear()
    var.unitx.clear()
    var.unity.clear()
    var.line.clear()

    temp = pygame.Surface((var.LCastle.width, var.LCastle.height))
    temp.fill((255, 255, 255))
    temp.blit(img.LC, (0, 0))
    temp.set_colorkey((255, 255, 255))
    if (var.Lpow[0].used):
        temp.blit(img.X2, (10, 140))
    if (var.Lpow[1].used):
        temp.blit(img.X3, (10, 180))
    if (var.Lpow[4].used):
        temp.blit(img.GM, (10, 220))
    var.unitgraph.append(temp)
    var.unitx.append(var.LCastle.x)
    var.unity.append(var.LCastle.y)
    kek = pygame.Surface((1, 1))
    kek.fill((255, 255, 255))
    kek.set_colorkey((255, 255, 255))
    var.line.append(kek)

    temp = pygame.Surface((var.RCastle.width, var.RCastle.height))
    temp.fill((255, 255, 255))
    temp.blit(img.RC, (0, 0))
    temp.set_colorkey((255, 255, 255))
    if (var.Rpow[0].used):
        temp.blit(img.X2, (25, 140))
    if (var.Rpow[1].used):
        temp.blit(img.X3, (25, 180))
    if (var.Rpow[4].used):
        temp.blit(img.GM, (25, 220))
    var.unitgraph.append(temp)
    var.unitx.append(var.RCastle.x)
    var.unity.append(var.RCastle.y)
    kek = pygame.Surface((1, 1))
    kek.fill((255, 255, 255))
    kek.set_colorkey((255, 255, 255))
    var.line.append(kek)

    for i in var.LCastle.Army:
        temp = pygame.Surface((i.width, i.height))
        temp.fill((255, 255, 255))
        line = pygame.Surface((i.width + 2, 6))
        line.fill((0, 0, 0))
        rline = pygame.Surface((i.health * i.width / i.usual_health, 4))
        rline.fill((0, 255, 0))
        line.blit(rline, (1, 1))
        if (i.tip == "LI"):
            temp.blit(img.LI, (0, 0))
        elif (i.tip == "LA"):
            temp.blit(img.LA, (0, 0))
        elif (i.tip == "LH"):
            temp.blit(img.LH, (0, 0))
        elif (i.tip == "LG"):
            temp.blit(img.LG, (0, 0))
        elif (i.tip == "LD"):
            temp.blit(img.LD, (0, 0))
        temp.set_colorkey((255, 255, 255))
        var.unitgraph.append(temp)
        var.unitx.append(i.x)
        var.unity.append(i.y)
        var.line.append(line)

    for i in var.RCastle.Army:
        temp = pygame.Surface((i.width, i.height))
        temp.fill((255, 255, 255))
        line = pygame.Surface((i.width + 2, 6))
        line.fill((0, 0, 0))
        rline = pygame.Surface((i.health * i.width / i.usual_health, 4))
        rline.fill((0, 255, 0))
        line.blit(rline, (1, 1))
        if (i.tip == "RI"):
            temp.blit(img.RI, (0, 0))
        elif (i.tip == "RA"):
            temp.blit(img.RA, (0, 0))
        elif (i.tip == "RH"):
            temp.blit(img.RH, (0, 0))
        elif (i.tip == "RG"):
            temp.blit(img.RG, (0, 0))
        elif (i.tip == "RD"):
            temp.blit(img.RD, (0, 0))
        temp.set_colorkey((255, 255, 255))
        var.unitgraph.append(temp)
        var.unitx.append(i.x)
        var.unity.append(i.y)
        var.line.append(line)

def updatepowertut():
    X2 = pygame.Surface((40, 40))
    X3 = pygame.Surface((40, 40))
    HHP = pygame.Surface((40, 40))
    FHP = pygame.Surface((40, 40))
    GM = pygame.Surface((40, 40))
    LU = pygame.Surface((40, 40))

    X2.fill((255, 255, 255))
    X3.fill((255, 255, 255))
    HHP.fill((255, 255, 255))
    FHP.fill((255, 255, 255))
    GM.fill((255, 255, 255))
    LU.fill((255, 255, 255))

    X2.blit(img.X2, (0, 0))
    X3.blit(img.X3, (0, 0))
    HHP.blit(img.HHP, (0, 0))
    FHP.blit(img.HP, (0, 0))
    GM.blit(img.GM, (0, 0))
    LU.blit(img.LU, (0, 0))

    Ltut = pygame.Surface((240, 80))
    Rtut = pygame.Surface((240, 80))
    Ltut.fill((255, 255, 255))
    Rtut.fill((255, 255, 255))

    Ltut.blit(X2, (0, 0))
    Ltut.blit(X3, (40, 0))
    Ltut.blit(HHP, (80, 0))
    Ltut.blit(FHP, (120, 0))
    Ltut.blit(GM, (160, 0))
    Ltut.blit(LU, (200, 0))

    Ltut.blit(efont.render('Q', False, (0, 0, 0)), (0, 40))
    Ltut.blit(efont.render('W', False, (0, 0, 0)), (40, 40))
    Ltut.blit(efont.render('E', False, (0, 0, 0)), (80, 40))
    Ltut.blit(efont.render('R', False, (0, 0, 0)), (120, 40))
    Ltut.blit(efont.render('A', False, (0, 0, 0)), (160, 40))
    Ltut.blit(efont.render('S', False, (0, 0, 0)), (200, 40))

    Rtut.blit(X2, (0, 0))
    Rtut.blit(X3, (40, 0))
    Rtut.blit(HHP, (80, 0))
    Rtut.blit(FHP, (120, 0))
    Rtut.blit(GM, (160, 0))
    Rtut.blit(LU, (200, 0))

    Rtut.blit(efont.render('U', False, (0, 0, 0)), (0, 40))
    Rtut.blit(efont.render('I', False, (0, 0, 0)), (40, 40))
    Rtut.blit(efont.render('O', False, (0, 0, 0)), (80, 40))
    Rtut.blit(efont.render('P', False, (0, 0, 0)), (120, 40))
    Rtut.blit(efont.render('K', False, (0, 0, 0)), (160, 40))
    Rtut.blit(efont.render('L', False, (0, 0, 0)), (200, 40))

    Ltut.set_colorkey((255, 255, 255))
    Rtut.set_colorkey((255, 255, 255))

    screen.blit(Ltut, (var.LCastle.x, var.LCastle.y + var.LCastle.height))
    screen.blit(Rtut, (var.RCastle.x + var.RCastle.width - 240, var.RCastle.y + var.RCastle.height))


def updateunit():
    I = pygame.Surface((200, 40))
    A = pygame.Surface((200, 40))
    H = pygame.Surface((200, 40))
    G = pygame.Surface((200, 40))
    D = pygame.Surface((200, 40))

    I.fill((255, 255, 255))
    A.fill((255, 255, 255))
    H.fill((255, 255, 255))
    G.fill((255, 255, 255))
    D.fill((255, 255, 255))

    I.blit(efont.render('1', False, (0, 0, 0)), (0, 0))
    A.blit(efont.render('2', False, (0, 0, 0)), (0, 0))
    H.blit(efont.render('3', False, (0, 0, 0)), (0, 0))
    G.blit(efont.render('4', False, (0, 0, 0)), (0, 0))
    D.blit(efont.render('5', False, (0, 0, 0)), (0, 0))

    I.blit(img.LIH, (40, 0))
    A.blit(img.LAH, (40, 0))
    H.blit(img.LHH, (40, 0))
    G.blit(img.LGH, (40, 0))
    D.blit(img.LDH, (40, 0))

    I.blit(befont.render(" " + str(var.LCastle.I), False, (0, 0, 0)), (80, 0))
    A.blit(befont.render(" " + str(var.LCastle.A), False, (0, 0, 0)), (80, 0))
    H.blit(befont.render(" " + str(var.LCastle.H), False, (0, 0, 0)), (80, 0))
    G.blit(befont.render(" " + str(var.LCastle.G), False, (0, 0, 0)), (80, 0))
    D.blit(befont.render(" " + str(var.LCastle.D), False, (0, 0, 0)), (80, 0))

    I.set_colorkey((255, 255, 255))
    A.set_colorkey((255, 255, 255))
    H.set_colorkey((255, 255, 255))
    G.set_colorkey((255, 255, 255))
    D.set_colorkey((255, 255, 255))

    screen.blit(I, (var.LCastle.x, var.LCastle.y + var.LCastle.height + 80))
    screen.blit(A, (var.LCastle.x, var.LCastle.y + var.LCastle.height + 120))
    screen.blit(H, (var.LCastle.x + 250, var.LCastle.y + var.LCastle.height + 40))
    screen.blit(G, (var.LCastle.x + 250, var.LCastle.y + var.LCastle.height + 80))
    screen.blit(D, (var.LCastle.x + 250, var.LCastle.y + var.LCastle.height + 120))

    I = pygame.Surface((200, 40))
    A = pygame.Surface((200, 40))
    H = pygame.Surface((200, 40))
    G = pygame.Surface((200, 40))
    D = pygame.Surface((200, 40))

    I.fill((255, 255, 255))
    A.fill((255, 255, 255))
    H.fill((255, 255, 255))
    G.fill((255, 255, 255))
    D.fill((255, 255, 255))

    I.blit(efont.render('6', False, (0, 0, 0)), (0, 0))
    A.blit(efont.render('7', False, (0, 0, 0)), (0, 0))
    H.blit(efont.render('8', False, (0, 0, 0)), (0, 0))
    G.blit(efont.render('9', False, (0, 0, 0)), (0, 0))
    D.blit(efont.render('0', False, (0, 0, 0)), (0, 0))

    I.blit(img.RIH, (40, 0))
    A.blit(img.RAH, (40, 0))
    H.blit(img.RHH, (40, 0))
    G.blit(img.RGH, (40, 0))
    D.blit(img.RDH, (40, 0))

    I.blit(befont.render(" " + str(var.RCastle.I), False, (0, 0, 0)), (80, 0))
    A.blit(befont.render(" " + str(var.RCastle.A), False, (0, 0, 0)), (80, 0))
    H.blit(befont.render(" " + str(var.RCastle.H), False, (0, 0, 0)), (80, 0))
    G.blit(befont.render(" " + str(var.RCastle.G), False, (0, 0, 0)), (80, 0))
    D.blit(befont.render(" " + str(var.RCastle.D), False, (0, 0, 0)), (80, 0))

    I.set_colorkey((255, 255, 255))
    A.set_colorkey((255, 255, 255))
    H.set_colorkey((255, 255, 255))
    G.set_colorkey((255, 255, 255))
    D.set_colorkey((255, 255, 255))

    screen.blit(I, (var.RCastle.x + var.RCastle.width - 450, var.RCastle.y + var.RCastle.height + 40))
    screen.blit(A, (var.RCastle.x + var.RCastle.width - 450, var.RCastle.y + var.RCastle.height + 80))
    screen.blit(H, (var.RCastle.x + var.RCastle.width - 450, var.RCastle.y + var.RCastle.height + 120))
    screen.blit(G, (var.RCastle.x + var.RCastle.width - 200, var.RCastle.y + var.RCastle.height + 80))
    screen.blit(D, (var.RCastle.x + var.RCastle.width - 200, var.RCastle.y + var.RCastle.height + 120))


def updateCost():
    cost = pygame.Surface((700, 120))
    cost.fill((255, 255, 255))

    I = pygame.Surface((180, 40))
    I.fill((255, 255, 255))
    I.blit(img.LIH, (0, 0))
    I.blit(img.RIH, (40, 0))
    I.blit(efont.render(" " + str(var.Costs.I), False, (0, 0, 0)), (80, 5))

    A = pygame.Surface((180, 40))
    A.fill((255, 255, 255))
    A.blit(img.LAH, (0, 0))
    A.blit(img.RAH, (40, 0))
    A.blit(efont.render(" " + str(var.Costs.A), False, (0, 0, 0)), (80, 5))

    H = pygame.Surface((180, 40))
    H.fill((255, 255, 255))
    H.blit(img.LHH, (0, 0))
    H.blit(img.RHH, (40, 0))
    H.blit(efont.render(" " + str(var.Costs.H), False, (0, 0, 0)), (80, 5))

    G = pygame.Surface((180, 40))
    G.fill((255, 255, 255))
    G.blit(img.LGH, (0, 0))
    G.blit(img.RGH, (40, 0))
    G.blit(efont.render(" " + str(var.Costs.G), False, (0, 0, 0)), (80, 5))

    D = pygame.Surface((180, 40))
    D.fill((255, 255, 255))
    D.blit(img.LDH, (0, 0))
    D.blit(img.RDH, (40, 0))
    D.blit(efont.render(" " + str(var.Costs.D), False, (0, 0, 0)), (80, 5))

    X2 = pygame.Surface((140, 40))
    X2.fill((255, 255, 255))
    X2.blit(img.X2, (0, 0))
    X2.blit(efont.render(" " + str(object.CUpDamageX2.cost), False, (0, 0, 0)), (40, 5))

    X3 = pygame.Surface((140, 40))
    X3.fill((255, 255, 255))
    X3.blit(img.X3, (0, 0))
    X3.blit(efont.render(" " + str(object.CUpDamageX3.cost), False, (0, 0, 0)), (40, 5))

    HHP = pygame.Surface((140, 40))
    HHP.fill((255, 255, 255))
    HHP.blit(img.HHP, (0, 0))
    HHP.blit(efont.render(" " + str(object.CRestoreHalfHP.cost), False, (0, 0, 0)), (40, 5))

    FHP = pygame.Surface((140, 40))
    FHP.fill((255, 255, 255))
    FHP.blit(img.HP, (0, 0))
    FHP.blit(efont.render(" " + str(object.CRestoreFullHP.cost), False, (0, 0, 0)), (40, 5))

    GM = pygame.Surface((140, 40))
    GM.fill((255, 255, 255))
    GM.blit(img.GM, (0, 0))
    GM.blit(efont.render(" " + str(object.CGodMode.cost), False, (0, 0, 0)), (40, 5))

    LU = pygame.Surface((180, 40))
    LU.fill((255, 255, 255))
    LU.blit(img.LU, (0, 0))
    LU.blit(smallfont.render(" LVL * 10", False, (0, 0, 0)), (40, 5))

    cost.blit(I, (0, 0))
    cost.blit(A, (0, 40))
    cost.blit(H, (0, 80))
    cost.blit(G, (180, 0))
    cost.blit(D, (180, 40))
    cost.blit(X2, (360, 0))
    cost.blit(X3, (360, 40))
    cost.blit(GM, (360, 80))
    cost.blit(HHP, (500, 0))
    cost.blit(FHP, (500, 40))
    cost.blit(LU, (500, 80))

    cost.set_colorkey((255, 255, 255))
    screen.blit(cost, (320, 0))


def updateGraph():
    updateUnitCastle()
    screen.fill((255, 255, 255))
    screen.blit(img.BackGround, (0, 0))
    for i in range(len(var.unitgraph)):
        screen.blit(var.unitgraph[i], (var.unitx[i], var.unity[i]))
        if (i > 1):
            screen.blit(var.line[i], (var.unitx[i], var.unity[i] - 6))



def updateCount():
    screen.blit(myfont.render(str(var.LCastle.money), False, (0, 0, 0)), (0, 0))
    sz = len(str(var.RCastle.money))
    screen.blit(myfont.render(str(var.RCastle.money), False, (0, 0, 0)), (1280 - 30 * sz, 0))
    screen.blit(befont.render(str(var.LCastle.HP), False, (0, 0, 0)), (0, 120))
    sz = len(str(var.RCastle.HP))
    screen.blit(befont.render(str(var.RCastle.HP), False, (0, 0, 0)), (1280 - 20 * sz, 120))


def saveUpdates():
    window.blit(screen, (0, 0))
    pygame.display.update()


def quit():
    pygame.quit()
