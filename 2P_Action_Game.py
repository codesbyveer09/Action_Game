import math, pygame, time, random

"""
HOW TO PLAY

Action    |  Player_1  |  Player_2 
__________|____________|___________
Movement  |  a and d   |  j and l  
Jump      |  w         |  i        
Recover   |  s         |  k        
Punch     |  e         |  u        
Blades    |  q         |  o        
Block     |  L_Shift   |  R_Shift  
"""



def init(rd):
                                                                                #Class
    if rd == 1:
        global Player, Disc
        class Player():

            def __init__(self, name, pos, dirn, move = "null", wins = 0):
                self.name = name
                self.pos = pos
                self.h_pos = [0, X//65]
                self.move = move
                self.dirn = dirn
                self.atk_ct = 0
                self.action = {"relax" : False, "jump" : False, "block" : False, "attack" : False}
                self.time = {"attack" : float("inf"), "jump" : float("inf")}
                self.health = 100.0
                self.stamina = 150.0
                self.disc = 3
                self.wins = wins


            def Actn(self, act):
                p1 = l_plrs.index(self)
                p2 = int(not p1)
                if act == "relax":
                    self.pos[1] += X//20
                    self.action["relax"] = True

                elif act == "jump" and self.stamina >= 15:
                    self.action["jump"] = True
                    self.time["jump"] = time.time()
                
                elif act == "attack" and self.stamina >= 20:
                    self.action["attack"] = True
                    self.time["attack"] = time.time()

                elif act == "l attack" and self.stamina >= 15 and self.disc > 0:
                    self.stamina -= 15
                    self.disc -= 1
                    l_disc.append(Disc(self, l_plrs[p2]))

                elif act == "block":
                    self.action["block"] = True


        class Disc(): 
            def __init__(self, PLAYER, PLAYER2):
                self.pos = [PLAYER.pos[0], PLAYER.pos[1] + Y//2 - Y//3]
                self.dirn = str(PLAYER.dirn)
                self.p1 = PLAYER
                self.p2 = PLAYER2

                                                                                    #Clr
        global blue, red, green, yellow, cyan, lime, bright_yellow,\
               orange, white, black, grey, night_blue

        blue = 100, 120, 180
        red = 200, 0, 0
        green = 72, 161, 77
        yellow = 210, 210, 50
        cyan = 85, 150, 200
        lime = 60, 200, 120
        orange = 255, 69, 0
        white = 253, 251, 249
        black = 21, 23, 24
        grey = 150, 150, 150
        night_blue = 0, 0, 30
                                                                                    #CONSTANTS
        global X, Y, g_clr, b_clr
        X, Y = 1280, 720
                                                                                    #variables
        global l_plrs, l_disc
        l_plrs = [Player("PLAYER 1", [X*2//7, Y//2], "right"), Player("PLAYER 2", [(X*5)//7, Y//2], "left")]
        l_disc = []
                                                                                    #Pygame Init
        global SCREEN, f_sz, f_nm, font

        pygame.init()
        pygame.font.init()

        SCREEN = pygame.display.set_mode((X, Y))

        f_sz = int(X//51.2)
        f_nm = "C:/Users/veera/AppData/Local/Microsoft/Windows/Fonts/visitor2.ttf"
        font = pygame.font.Font(f_nm, f_sz)

        pygame.draw.rect(SCREEN, black, pygame.Rect(0, 0, X, Y))
        prt("Press any key to Start", X/2, Y/2, white, ft = pygame.font.Font(f_nm, int(X//16)))
        pygame.display.flip()
        brk=False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    brk=True
                    break
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            if brk==True:
                break

    else:
        l_plrs = [Player("PLAYER 1", [X*2//7, Y//2], "right", l_plrs[0].wins), Player("PLAYER 2", [(X*5)//7, Y//2], "left", l_plrs[1].wins)]
        l_disc = []

    g_clr = (random.randrange(50, 150), random.randrange(50, 150), random.randrange(50, 150))
    b_clr = (random.randrange(0, 50), random.randrange(0, 50), random.randrange(0, 50))

    pygame.draw.rect(SCREEN, b_clr, pygame.Rect(0, 0, X, Y))
    prt("ROUND " + str(rd), X//2, Y//2, g_clr, ft = pygame.font.Font(f_nm, int(X//12.8)))
    pygame.display.flip()
    time.sleep(1)

    pygame.draw.rect(SCREEN, b_clr, pygame.Rect(0, 0, X, Y))
    prt("!!FIGHT!!", X/2, Y/2, g_clr, ft = pygame.font.Font(f_nm, int(X//12.8)))
    pygame.display.flip()
    time.sleep(0.3)

    render()
                                                                                #FUNCTION

def prt(v_nm, x_var, y_var, f_clr, tilt=0, ft = None, bg_clr = None, align = "center"):
    global font
    if ft == None:
        ft = font
    if bg_clr==None:
        text = ft.render(v_nm, True, f_clr)
    else:
        text = ft.render(v_nm, True, f_clr, bg_clr)
    textRect = text.get_rect()
    textRect = (int(x_var), int(y_var))
    if tilt != 0:
        text = pygame.transform.rotate(text, tilt)
    if align == "center":
        textRect = text.get_rect()
        textRect.center = (int(x_var), int(y_var))
    if align == "right":
        text = ft.render(v_nm, True, white)
        textRect = text.get_rect()
        textRect.right = int(x_var)
        textRect[1] = int(y_var)
    SCREEN.blit(text, textRect)


def shade(colour, change=-40):
    colour = list(colour)
    for i in range(3):
        colour[i] += change
    return tuple(colour)


def render():
    global i_time

    pygame.draw.rect(SCREEN, b_clr, pygame.Rect(0, 0, X, Y))

    # Graphics

    pygame.draw.rect(SCREEN, blue, pygame.Rect(l_plrs[0].pos[0]-X//90, l_plrs[0].pos[1], X//45, Y//2 - Y//8))
    pygame.draw.circle(SCREEN, cyan, l_plrs[0].pos, X//35)

    pygame.draw.rect(SCREEN, red, pygame.Rect(l_plrs[1].pos[0]-X//90, l_plrs[1].pos[1], X//45, Y//2 - Y//8))
    pygame.draw.circle(SCREEN, orange, l_plrs[1].pos, X//35)

    pygame.draw.rect(SCREEN, g_clr, pygame.Rect(0, (Y*7)//8, X, Y//8))

    prt("HEALTH: ", X//50, (Y*28.5)//32, white, align = "left")
    prt("STAMINA: ", X//50, (Y*29.5)//32, white, align = "left")
    pygame.draw.rect(SCREEN, shade(g_clr), pygame.Rect((X*5)//50, (Y*28.5)//32, (X/7), Y//45))
    pygame.draw.rect(SCREEN, shade(g_clr), pygame.Rect((X*5)//50, (Y*29.5)//32, (X/7), Y//45))
    pygame.draw.rect(SCREEN, white, pygame.Rect((X*5)//50, (Y*28.5)//32, (X/7)*(l_plrs[0].health/100), Y//45))
    pygame.draw.rect(SCREEN, white, pygame.Rect((X*5)//50, (Y*29.5)//32, (X/7)*(l_plrs[0].stamina/150), Y//45))
    prt(f"<{int(l_plrs[0].health)}>", (X*11)//100 + (X//7), (Y*28.5)//32, white, align = "left")
    prt(f"<{int(l_plrs[0].stamina)}>", (X*11)//100 + (X//7), (Y*29.5)//32, white, align = "left")
    prt("DISC: ", X//50, (Y*30.5)//32, white, align = "left")
    for i in range(3):
        pygame.draw.arc(SCREEN, shade(g_clr), pygame.Rect((X*(5)//50) + (i*X//50), (Y*30.5)//32, X//75, X//75), 0, math.pi-math.radians(40), 3)
        pygame.draw.arc(SCREEN, shade(g_clr), pygame.Rect((X*(5)//50) + (i*X//50), (Y*30.5)//32, X//75, X//75), math.pi, (2*math.pi)-math.radians(40), 3)
    for i in range(l_plrs[0].disc):
        pygame.draw.arc(SCREEN, white, pygame.Rect((X*(5)//50) + (i*X//50), (Y*30.5)//32, X//75, X//75), 0, math.pi-math.radians(40), 3)
        pygame.draw.arc(SCREEN, white, pygame.Rect((X*(5)//50) + (i*X//50), (Y*30.5)//32, X//75, X//75), math.pi, (2*math.pi)-math.radians(40), 3)


    prt(" :HEALTH", X - X//50, (Y*28.5)//32, white, align = "right")
    prt(" :STAMINA", X - X//50, (Y*29.5)//32, white, align = "right")
    pygame.draw.rect(SCREEN, shade(g_clr), pygame.Rect(X - (X*5)//50 - (X/7), (Y*28.5)//32, (X/7), Y//45))
    pygame.draw.rect(SCREEN, shade(g_clr), pygame.Rect(X - (X*5)//50 - (X/7), (Y*29.5)//32, (X/7), Y//45))
    pygame.draw.rect(SCREEN, white, pygame.Rect(X - (X*5)//50 - (X/7)*(l_plrs[1].health/100), (Y*28.5)//32, (X/7)*(l_plrs[1].health/100), Y//45))
    pygame.draw.rect(SCREEN, white, pygame.Rect(X - (X*5)//50 - (X/7)*(l_plrs[1].stamina/150), (Y*29.5)//32, (X/7)*(l_plrs[1].stamina/150), Y//45))
    prt(f"<{int(l_plrs[1].health)}>", X - (X*11)//100 - (X//7), (Y*28.5)//32, white, align = "right")
    prt(f"<{int(l_plrs[1].stamina)}>", X - (X*11)//100 - (X//7), (Y*29.5)//32, white, align = "right")
    prt(" :DISC", X - X//50, (Y*30.5)//32, white, align = "right")
    for i in range(3, 0, -1):
        pygame.draw.arc(SCREEN, shade(g_clr), pygame.Rect(X - (X*(5)//50) - (i*X//50), (Y*30.5)//32, X//75, X//75), 0, math.pi-math.radians(40), 3)
        pygame.draw.arc(SCREEN, shade(g_clr), pygame.Rect(X - (X*(5)//50) - (i*X//50), (Y*30.5)//32, X//75, X//75), math.pi, (2*math.pi)-math.radians(40), 3)
    for i in range(l_plrs[1].disc, 0, -1):
        pygame.draw.arc(SCREEN, white, pygame.Rect(X - (X*(5)//50) - (i*X//50), (Y*30.5)//32, X//75, X//75), 0, math.pi-math.radians(40), 3)
        pygame.draw.arc(SCREEN, white, pygame.Rect(X - (X*(5)//50) - (i*X//50), (Y*30.5)//32, X//75, X//75), math.pi, (2*math.pi)-math.radians(40), 3)


    for i in l_plrs:
        if i.action["block"] and i.dirn == "right":
            pygame.draw.arc(SCREEN, white, pygame.Rect(i.pos[0]-(X//5), (Y//2)-(X//10), (X//2.5), (X//2.5)), -1, 1.875, 10)
        if i.action["block"] and i.dirn == "left":
            pygame.draw.arc(SCREEN, white, pygame.Rect(i.pos[0]-(X//5), (Y//2)-(X//10), (X//2.5), (X//2.5)), math.pi-1.875, math.pi+1, 10)

        if i.action["attack"]:
            if i.dirn == "right":
                pygame.draw.rect(SCREEN, white, pygame.Rect(i.pos[0], i.pos[1]+Y//10, i.h_pos[0], i.h_pos[1]))
                pygame.draw.rect(SCREEN, white, pygame.Rect(i.pos[0]+i.h_pos[0], i.pos[1]+Y//10, X//50, X//50))
            if i.dirn == "left":
                pygame.draw.rect(SCREEN, white, pygame.Rect(i.pos[0]-i.h_pos[0], i.pos[1]+Y//10, i.h_pos[0], i.h_pos[1]))
                pygame.draw.rect(SCREEN, white, pygame.Rect(i.pos[0]-i.h_pos[0]-X//60, i.pos[1]+Y//10, X//60, X//60))

    for i in l_disc:
        pygame.draw.arc(SCREEN, white, pygame.Rect(i.pos[0], i.pos[1], X//50, X//50), math.radians(20)-(20*time.time()), math.pi-math.radians(20)-(20*time.time()), 4)
        pygame.draw.arc(SCREEN, white, pygame.Rect(i.pos[0], i.pos[1], X//50, X//50), math.pi+math.radians(20)-(20*time.time()), (2*math.pi)-math.radians(20)-(20*time.time()), 4)

    try:
        i_time
    except:
        i_time = time.time()
    pygame.draw.rect(SCREEN, white, pygame.Rect(X//2 - X//10, 0, X//5, (Y*2)//32))
    prt(f"{(round(time.time()-i_time-((rd-1)*1.3))//60)} min  {(round(time.time()-i_time-((rd-1)*1.3))%60)} sec", X//2, (Y*1)//32, shade(g_clr), ft = pygame.font.Font(f_nm, int(X//45)))


    pygame.display.flip()


if __name__ == "__main__":
    for rd in range(1,4):

        rdr_time = time.time()
        init(rd)

        while l_plrs[0].health > 0 and l_plrs[1].health > 0:
            if rdr_time+(1/30) <= time.time():

                for i in l_plrs:
                    p1 = l_plrs.index(i)
                    p2 = int(not p1)
                    if i.stamina < 150.0:
                        i.stamina += 0.1
                    if i.health <= 99.98:
                        i.health += 0.02

                    if i.stamina < 0.25:
                        i.move = "null"
                    else:
                        if i.move == "left" and i.pos[0] > X//35:
                            i.pos[0] -= X//150
                            i.stamina -= 0.25
                        elif i.move == "right" and i.pos[0] < X-(X//35):
                            i.pos[0] += X//150
                            i.stamina -= 0.25
                        if i.pos[0]-l_plrs[p2].pos[0] <= 0 and i.action["attack"] == False:
                            i.dirn = "right"
                        elif i.pos[0]-l_plrs[p2].pos[0] >= 0 and i.action["attack"] == False:
                            i.dirn = "left"

                    if i.action["block"] == True:
                        if i.stamina > 1:
                            i.stamina -= 1
                        else:
                            i.action["block"] = False
                    
                    if i.action["relax"] == True and i.stamina <= 149.50 and i.health < 100:
                        i.stamina += 0.5
                        i.health += 0.1

                    if i.action["jump"] == True:
                        if i.time["jump"]+1 > time.time():
                            i.pos[1] -= X//75*(1 - ((time.time()-i.time["jump"])))
                            i.stamina -= 0.3
                        elif i.time["jump"]+1.5 < time.time():
                            i.pos[1] -= X//75*(1 - ((time.time()-i.time["jump"]-0.5)))
                            i.stamina -= 0.125

                    if i.action["attack"] == True:
                        if i.dirn == "right":
                            near = abs(i.pos[0]+i.h_pos[0]-l_plrs[p2].pos[0])
                        else:
                            near = abs(i.pos[0]-i.h_pos[0]-l_plrs[p2].pos[0])

                        if 0 < time.time() - i.time["attack"] <= .25:
                            i.h_pos[0] += X//80
                            if near <= X//30 and l_plrs[p2].action["jump"] == False and i.atk_ct == 0:
                                if l_plrs[p2].action["block"] == True:
                                    mult = 0.125
                                elif l_plrs[p2].action["relax"] == True:
                                    mult = 2
                                else:
                                    mult = 1
                                l_plrs[p2].health -= 10*mult
                                i.stamina -= 4.0
                                i.atk_ct += 1
                            else:
                                i.stamina -= 2

                        elif .25 < time.time() - i.time["attack"] <= .5:
                            if near <= X//30 and l_plrs[p2].action["jump"] == False and i.atk_ct == 0:
                                if l_plrs[p2].action["block"] == True:
                                    mult = 0.125
                                elif l_plrs[p2].action["relax"] == True:
                                    mult = 2
                                else:
                                    mult = 1
                                l_plrs[p2].health -= 10*mult
                                i.stamina -= 0.5
                                i.atk_ct += 1
                            else:
                                i.stamina -= 0


                        elif .5 < time.time()-i.time["attack"] < .75:
                            i.h_pos[0] -= X//80
                            if  abs(i.pos[0]+i.h_pos[0]-l_plrs[p2].pos[0]-X//30) <= X//30 and\
                                abs(i.pos[0]-i.h_pos[0]-l_plrs[p2].pos[0]-X//30) <= X//30 and\
                                l_plrs[p2].action["jump"] == False and i.atk_ct == 1:

                                if l_plrs[p2].action["block"] == True:
                                    mult = 0
                                elif l_plrs[p2].action["relax"] == True:
                                    mult = 1
                                else:
                                    mult = 0.5
                                l_plrs[p2].health -= 10*mult
                                i.stamina -= 0.75
                                i.atk_ct += 1
                            else:
                                i.stamina -= 0.25

                        elif time.time() - i.time["attack"] >= .75:
                            i.h_pos[0] = 0
                            i.time["attack"] = float("inf")
                            i.action["attack"] = False
                            i.atk_ct = 0


                for i in l_disc:
                    if i.dirn == "left":
                        i.pos[0] -= X//39
                    elif i.dirn == "right":
                        i.pos[0] += X//39
                    
                    #disc-player
                    if i.p2.pos[0] - X//35 <= i.pos[0] <= i.p2.pos[0] + X//35 and i.p2.pos[1] - X//35 <= i.pos[1] <= i.p2.pos[1] + Y//2 - Y//8 and\
                        False == i.p2.action["block"]:
                        i.p2.health -= 25.0
                        l_disc.pop(l_disc.index(i))

                    #disc-disc
                    for j in l_disc:
                        if i.p1 != j.p1:
                            if ((i.pos[0]-j.pos[0])**2 + (i.pos[1]-j.pos[1])**2)**1/2 <= float(X//38):
                                l_disc.pop(l_disc.index(i))
                                l_disc.pop(l_disc.index(j))

                render()
                rdr_time = time.time()


            for i in range(len(l_plrs)):

                if l_plrs[i].time["jump"]+2.5 <= time.time():
                    l_plrs[i].pos[1] = Y//2
                    l_plrs[i].action["jump"] = False
                    l_plrs[i].time["jump"]=float("inf")


            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if l_plrs[0].stamina > 0.0:

                        if event.key == pygame.K_a:
                            l_plrs[0].move = "left"
                        elif event.key == pygame.K_d:
                            l_plrs[0].move = "right"

                        if event.key == pygame.K_w and l_plrs[0].action["relax"] == False == l_plrs[0].action["jump"] == l_plrs[0].action["block"]:
                            l_plrs[0].Actn("jump")
                        elif event.key == pygame.K_s and False == l_plrs[0].action["jump"] == l_plrs[1].action["block"]:
                            l_plrs[0].Actn("relax")
                        if event.key == pygame.K_e and False == l_plrs[0].action["attack"]:
                            l_plrs[0].Actn("attack")
                        elif event.key == pygame.K_q:
                            l_plrs[0].Actn("l attack")
                        elif event.key == pygame.K_LSHIFT and l_plrs[0].action["relax"] == False == l_plrs[0].action["jump"]:
                            l_plrs[0].Actn("block")

                    if l_plrs[1].stamina > 5.0:
                        if event.key == pygame.K_j:
                            l_plrs[1].move = "left"
                        elif event.key == pygame.K_l:
                            l_plrs[1].move = "right"

                        if event.key == pygame.K_i and l_plrs[1].action["relax"] == False == l_plrs[1].action["jump"] == l_plrs[1].action["block"]:
                            l_plrs[1].Actn("jump")
                        elif event.key == pygame.K_k and l_plrs[1].action["relax"] == False == l_plrs[1].action["jump"] == l_plrs[1].action["block"]:
                            l_plrs[1].Actn("relax")
                        if event.key == pygame.K_u and False == l_plrs[1].action["attack"]:
                            l_plrs[1].Actn("attack")
                        if event.key == pygame.K_o:
                            l_plrs[1].Actn("l attack")
                        elif event.key == pygame.K_RSHIFT and l_plrs[1].action["relax"] == False == l_plrs[1].action["jump"]:
                            l_plrs[1].Actn("block")

                    if event.key == pygame.K_ESCAPE:
                        exit()


                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_a:
                        l_plrs[0].move = "null"
                    elif event.key == pygame.K_d:
                        l_plrs[0].move = "null"

                    if event.key == pygame.K_j:
                        l_plrs[1].move = "null"
                    elif event.key == pygame.K_l:
                        l_plrs[1].move = "null"

                    if event.key == pygame.K_s and l_plrs[0].action["relax"]:
                        l_plrs[0].action["relax"] = False
                        l_plrs[0].pos[1] -= X//20
                    if event.key == pygame.K_k and l_plrs[1].action["relax"]:
                        l_plrs[1].action["relax"] = False
                        l_plrs[1].pos[1] -= X//20
                    if event.key == pygame.K_LSHIFT and l_plrs[0].action["block"]:
                        l_plrs[0].action["block"] = False
                    if event.key == pygame.K_RSHIFT and l_plrs[1].action["block"]:
                        l_plrs[1].action["block"] = False

        if l_plrs[0].health <= 0:
            l_plrs[1].wins += 1
        if l_plrs[1].health <= 0:
            l_plrs[0].wins += 1

    font = pygame.font.Font(f_nm, int(X//12.8))
    pygame.draw.rect(SCREEN, black, pygame.Rect(0, 0, X, Y))
    if l_plrs[0].wins > l_plrs[1].wins:
        prt("!!PLAYER 1 WON!!", X//2, Y//2, white)
        prt(str(l_plrs[0].wins) + " : " + str(l_plrs[1].wins), X//2, Y//1.5, grey)
    elif l_plrs[0].wins < l_plrs[1].wins:
        prt("!!PLAYER 2 WON!!", X//2, Y//2, white)
        prt(str(l_plrs[0].wins) + " : " + str(l_plrs[1].wins), X//2, Y//1.5, grey)
    pygame.display.flip()
    time.sleep(2.5)

    pygame.font.quit()
    pygame.quit()
