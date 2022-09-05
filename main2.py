# MINESWEEPER!
# ------------

# Import Libraries and Pack

import random
import Pack
import sys

# Extra

l1_blue = [65,105,225,0]
l2_blue = [132,112,255,0]
silver = [192,192,192,0]




# References!
"""

Fonts : 0.Algerian, 1.MS Sans Serif, 2.Times New Roman, 3.Comic Sans MS, 4.Agency FB, 5.Arial, 6.Calibri, 7. Heedling
Pack.Label(['text',text_color,text_size,position,horizontal_center_align,vertical_center_align,font],[fill,flip])
Pack.Box(['text/pic',text_color/0,text_size/0,rect,background_color,border_color,font/0],[fill,flip])
Pack.BoxOfText([rect,background_color,border_color],[[t,col,size,pos,ha,va,f],...],[fill,flip])
Pack.Button(['text',rect,text_color,text_size,bg_colors:[normal,over_mouse,clicked],border_color,font],[fill,flip])
Pack.Button.get(): returns True after the button is clicked!
Pack.TextBox(['hint',rect/line,text_size,[hint_color,text_color],[inactive_border_color,active_border_color],font,0],[fill,flip],type=None)
Pack.TextBox.get(): returns Input(ed) text
Pack.Events([buttons],[textboxes])

"""

# Pre-loop Variables

Game = 1
First = 1
Second = 0
Third = 0
Play = 0
x = Pack.sx
y = Pack.sy

Given = [0,0,0]

Grid = []

def bye():
    Pack.pygame.quit()
    sys.exit()


    
def process(l):
    r = l[0]
    c = l[1]
    p = l[2]
    n = r*c
    nb = (n*p)/100
    bmbs = []
    while 1 :
        if len(bmbs) < nb :
            a = random.randint(1,n)
            if a not in bmbs :
                bmbs.append(a)
        else :
            break
    bmbs.sort()
    grid1 = []
    cn = 0
    for p in range(r):
        ta = []
        for q in range(c):
            cn += 1
            if cn in bmbs :
                ta.append(1)
            else :
                ta.append(0)
        grid1.append(ta)
    grid2 = []
    cn = 0
    for p in range(r):
        la = []
        for q in range(c):
            cn += 1
            la.append(cn)
        grid2.append(la)
    grid3 = []
    for p in grid2 :
        lta = []
        for q in p :
            a = grid2.index(p)
            b = p.index(q)
            if grid1[a][b] :
                lta.append(9)
            else :
                n_t_a = 0
                amax = len(grid2)-2
                bmax = len(p)-2
                if a >= 1 :
                    if b >= 1 :
                        if grid1[a-1][b-1] :
                            n_t_a += 1
                    if grid1[a-1][b] :
                        n_t_a += 1
                    if b <= bmax :
                        if grid1[a-1][b+1] :
                            n_t_a += 1
                if b >= 1 :
                    if grid1[a][b-1]:
                        n_t_a += 1
                if b <= bmax :
                    if grid1[a][b+1]:
                        n_t_a += 1
                if a <= amax :
                    if b >= 1 :
                        if grid1[a+1][b-1] :
                            n_t_a += 1
                    if grid1[a+1][b] :
                        n_t_a += 1
                    if b <= bmax :
                        if grid1[a+1][b+1] :
                            n_t_a += 1
                lta.append(n_t_a)
        grid3.append(lta)
    return grid3
                
# Loop!

while Game:
    while First :
        Pack.Label(['Minesweeper','red',120,[x/2,70],1,0,0],[1,0])
        B_Play = Pack.Button(['Play',[(x/3)-350,(y/3)-20,700,200],'black',80,[l1_blue,'yellow','green'],silver,4],[0,0])
        B_Quit = Pack.Button(['Quit',[(2*x/3)-350,(2*y/3)-20,700,200],'black',80,[l1_blue,'yellow','green'],silver,4],[0,1])
        Pack.Events([B_Play,B_Quit],[],[])
        if B_Play.get():
            First = 0
            Second = 1
            B_Play.delete()
        if B_Quit.get():
            B_Quit.delete()
            bye()
    while Second :
        Pack.Label(['Minesweeper','blue',100,[x/2,70],1,0,0],[1,0])
        Pack.Label(['Select a Difficulty Level...','black',50,[x/2,200],1,0,1],[0,0])
        B_Easy = Pack.Button(['Easy',[(x/3)-300,(y/3),500,200],'black',80,[l1_blue,'yellow','green'],silver,4],[0,0])
        B_Modr = Pack.Button(['Moderate',[(2*x/3)-300,(y/3),500,200],'black',80,[l1_blue,'orange','green'],silver,4],[0,0])
        B_Hard = Pack.Button(['Hard',[(x/3)-300,(2*y/3),500,200],'black',80,[l1_blue,'red','green'],silver,4],[0,0])
        B_Cust = Pack.Button(['Custom',[(2*x/3)-300,(2*y/3),500,200],'black',80,[l1_blue,'white','green'],silver,4],[0,1])
        Pack.Events([B_Easy,B_Modr,B_Hard,B_Cust],[],[])
        if B_Easy.get():
            B_Easy.delete()
            Second = 0
            Given = [7,8,15]
            Grid = process(Given)
            Play = 1
        if B_Modr.get():
            B_Modr.delete()
            Second = 0
            Given = [10,12,20]
            Grid = process(Given)
            Play = 1
        if B_Hard.get():
            B_Hard.delete()
            Second = 0
            Given = [18,20,20]
            Grid = process(Given)
            Play = 1
        if B_Cust.get():
            B_Cust.delete()
            Second = 0
            Third = 1
    while Third :
        Pack.Label(['Minesweeper','green',100,[x/2,70],1,0,0],[1,0])
        Pack.Label(['No. of Rows:',l2_blue,40,[50,260],0,0,1],[0,0])
        Pack.Label(['No. of Columns:',l2_blue,40,[50,360],0,0,1],[0,0])
        Pack.Label(['Percentage of Bombs:',l2_blue,40,[50,460],0,0,1],[0,0])        
        T_Rows = Pack.TextBox(['5 - 23',[512,300,400],40,['grey','black'],['grey','black'],1,0],[0,0],'Numbers')
        T_Cols = Pack.TextBox(['5 - 39',[512,400,400],40,['grey','black'],['grey','black'],1,0],[0,0],'Numbers')
        T_Perc = Pack.TextBox(['0 - 100',[512,500,400],40,['grey','black'],['grey','black'],1,0],[0,0],'Numbers')
        B_Done = Pack.Button(['Done!',[362,600,300,100],'yellow',60,[l1_blue,'green','brown'],silver,7],[0,1])
        Input_rcp = [T_Rows.get(),T_Cols.get(),T_Perc.get()]
        Pack.Events([B_Done],[T_Rows,T_Cols,T_Perc],[])
        if B_Done.get():
            B_Done.delete()
            Third = 0
            if len(str(Input_rcp[0]))>=1:
                r = int(Input_rcp[0])
            else :
                r = 0
            if len(str(Input_rcp[1]))>=1:
                c = int(Input_rcp[1])
            else :
                c = 0
            if len(str(Input_rcp[2]))>=1:
                p = int(Input_rcp[2])
            else :
                p = -1
            if 5 <= r <= 23 :
                Given[0] = r
            else :
                Given[0] = 10
            if 5 <= c <= 39 :
                Given[1] = c
            else :
                Given[1] = 10
            if 0 <= p < 100 :
                Given[2] = p
            else :
                Given[2] = 40
            Grid = process(Given)
            Play = 1
    if Play :        
        my_grid = Pack.DrawGrid(Grid)
        my_grid.draw([1,0])
        timer = Pack.Timer()
        while Play :
            wl = my_grid.win_or_lose()
            tim = timer.get()
            Pack.Events([],[],[my_grid])
            a = my_grid.get()
            Pack.BoxOfText([[70,100,320,120],l2_blue,silver],
                           [['Field :-','red',20,[80,110],0,0,0],
                            ['No. of Plots : %d' % (a[0]),'green',20,[90,135],0,0,1],
                            ['No. of Bombs : %d' % (a[1]),'green',20,[90,160],0,0,1],
                            ['No. of Free Plots : %d' % (a[2]),'green',20,[90,185],0,0,1]],                            
                           [0,0])
            Pack.BoxOfText([[x-390,100,320,120],l2_blue,silver],
                           [['Player :-','red',20,[x-380,110],0,0,0],
                            ['No. of Plots Hidden : %d' % (a[3]),'green',20,[x-370,135],0,0,1],
                            ['No. of Plots Revealed : %d' % (a[4]),'green',20,[x-370,160],0,0,1],
                            ['Remaining No. of Free Plots : %d' % (a[2]-a[4]),'green',20,[x-370,185],0,0,1]],
                           [0,0])
            while wl[0] :
                Pack.Box(['Bravo! You have solved it!',l1_blue,40,[(x/2)-300,y-240,600,60],'yellow','black',1],[0,0])
                WinB = Pack.Button(['Return',[(x/2)-100,y-160,200,90],'blue',65,['yellow','red','blue'],'black',4],[0,1])
                Pack.Events([WinB],[],[])
                if WinB.get():
                    First = 1
                    Second = 0
                    Third = 0
                    Play = 0
                    wl[0] = 0
                    WinB.delete()
            while wl[1] :
                Pack.Box(['Oops! You hit a bomb!','black',40,[(x/2)-300,y-240,600,60],'red','black',1],[0,0])
                LosB = Pack.Button(['Return',[(x/2)-100,y-160,200,90],'blue',65,['yellow','red','blue'],'black',4],[0,1])
                Pack.Events([LosB],[],[])
                if LosB.get():
                    First = 1
                    Second = 0
                    Third = 0
                    Play = 0
                    wl[1] = 0
                    LosB.delete()
            Pack.Box(['Time : '+str(tim),l1_blue,30,[(x/2)-160,100,320,50],'yellow','black',1],[0,1])