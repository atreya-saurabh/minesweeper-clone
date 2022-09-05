# Export



# Import
import pygame
from pygame.locals import *
import random
import time
import sys
import os
pygame.init()


# Attach
width, height = [0, 0]
look = pygame.display
screen = look.set_mode((width, height), pygame.FULLSCREEN)
sx = screen.get_width()
sy = screen.get_height()
def keep(i,p,a=0):
    if a == 0 :
        pos = p
    else :
        x = i.get_width()
        pos = [p[0]-(x/2),p[1]]
    screen.blit(i,pos)
    
events = pygame.event.get
def pic(name):
    return pygame.image.load(os.path.join('./',name))

X = pygame.QUIT
M1 = pygame.MOUSEBUTTONDOWN
M2 = pygame.MOUSEBUTTONUP
K1 = pygame.KEYDOWN
K2 = pygame.KEYUP
clock = pygame.time.Clock()
tick = clock.tick
mouse = pygame.mouse.get_pos
rect = pygame.draw.rect
cir = pygame.draw.circle
poly = pygame.draw.polygon
line = pygame.draw.line
lines = pygame.draw.lines
fill = screen.fill
wait = time.sleep
Music = pygame.mixer.music
ticks = pygame.time.get_ticks
mz = look.iconify
choose = random.choice
getfont = pygame.font.match_font

    

# Extra
white = Color('white')
yellow = Color('yellow')
green = Color('green')
red = Color('red')
blue = Color('blue')
l1_blue = [65,105,225,0]
l2_blue = [132,112,255,0]
black = Color('black')
purple = Color('purple')
orange = Color('orange')
gold = Color('gold')
silver = [192,192,192,0]
grey = Color('grey')
violet = Color('violet')
pink = Color('pink')
brown = Color('brown')
colors = [green, red, blue, black, purple, orange, gold, silver, grey, violet, pink, brown]
"""Excludes yellow & white for convenience!"""
PalatinoLinotype = getfont('palatinolinotype')
Serif = getfont('calibri')
Times = getfont('timesnewroman')
Comic = getfont('comicsansms')
Agency = getfont('agencyfb')
Arial = getfont('arial')
Calibri = getfont('calibri')
Heedling = getfont('heedling')
fonts = [PalatinoLinotype,Serif,Times,Comic,Agency,Arial,Calibri,Heedling]

keys1 = {K_a:'a', K_b:'b', K_c:'c', K_d:'d', K_e:'e', K_f:'f', K_g:'g', K_h:'h', K_i:'i', K_j:'j', K_k:'k', K_l:'l', K_m:'m', 
        K_n:'n', K_o:'o', K_p:'p', K_q:'q', K_r:'r', K_s:'s', K_t:'t', K_u:'u', K_v:'v', K_w:'w', K_x:'x', K_y:'y', K_z:'z',
        K_COLON: ':', K_SEMICOLON: ';', K_AT : '@', K_QUESTION : '?', K_EXCLAIM : '!', K_SPACE : ' ', K_HASH : '#', K_PLUS : '+',
        K_MINUS : '-', K_PERIOD : '.', K_COMMA : ',', K_ASTERISK : '*', K_QUOTE : "'", K_QUOTEDBL : '"', K_AMPERSAND : '&',
        K_LEFTPAREN : '(', K_RIGHTPAREN : ')', K_SLASH : '/', K_0 : 0, K_1 : 1, K_2 : 2, K_3 : 3, K_4 : 4, K_5 : 5,
        K_6 : 6, K_7 : 7, K_8 : 8, K_9 : 9, K_LESS : '<', K_GREATER : '>', K_EQUALS : '=', K_UNDERSCORE : '_',
        K_RIGHTBRACKET : ']', K_LEFTBRACKET : '[', K_BACKSLASH:"\\", K_BACKQUOTE:'`'}

keys2 = {K_a:'A', K_b:'B', K_c:'C', K_d:'D', K_e:'E', K_f:'F', K_g:'G', K_h:'H', K_i:'I', K_j:'J', K_k:'K', K_l:'L', K_m:'M', 
        K_n:'N', K_o:'O', K_p:'P', K_q:'Q', K_r:'R', K_s:'S', K_t:'T', K_u:'U', K_v:'V', K_w:'W', K_x:'X', K_y:'Y', K_z:'Z',
        K_COLON: ':', K_SEMICOLON: ':', K_AT : '@', K_QUESTION : '?', K_EXCLAIM : '!', K_SPACE : ' ', K_HASH : '#', K_PLUS : '+',
        K_MINUS : '_', K_PERIOD : '>', K_COMMA : '<', K_ASTERISK : '*', K_QUOTE : '"', K_QUOTEDBL : '"', K_AMPERSAND : '&',
        K_LEFTPAREN : '(', K_RIGHTPAREN : ')', K_SLASH : '?', K_0 : ')', K_1 : '!', K_2 : '@', K_3 : '#', K_4 : '$', K_5 : '%',
        K_6 : '^', K_7 : '&', K_8 : '*', K_9 : '(', K_LESS : '<', K_GREATER : '>', K_EQUALS : '+', K_UNDERSCORE : '_',
        K_RIGHTBRACKET : '}', K_LEFTBRACKET : '{', K_BACKSLASH:"|", K_BACKQUOTE:'~'}

kpdks = {K_KP0:0, K_KP1:1, K_KP2:2, K_KP3:3, K_KP4:4, K_KP5:5, K_KP6:6, K_KP7:7, K_KP8:8, K_KP9:9,
        K_KP_PERIOD:'.', K_KP_DIVIDE:'/', K_KP_MULTIPLY:'*', K_KP_MINUS:'-', K_KP_PLUS:'+', K_KP_ENTER:'', K_KP_EQUALS:'='}

# Functions
def bye():
    pygame.quit()
    sys.exit()

    



def find_equidistant(a,b,n):
    send_list = []
    dif = float(b-a)
    each = float(dif/(n+1))
    send_list.append(float(a))
    for i in range(n):
        send_list.append(float(a+(each*(i+1))))
    send_list.append(float(b))
    return send_list
    
def change_laps(var,l1,l2,b,i,w):
    if var <= l1 :
        b = True
    elif var >= l2 :
        b = False
    if not w :
        return b
    if b :
        return i
    else :
        return -i

def change_bool(b,v,l,c,wb):
    if wb :
        rb = v < l
        return bool(rb==b)
    else :
        if v>=l :
            return -1
        else :
            return c

def fade(i,f,p):
    if p>1 :
        p = 1
    i1 = i[0]
    i2 = i[1]
    i3 = i[2]
    f1 = f[0]
    f2 = f[1]
    f3 = f[2]
    p1 = (f1-i1)*p
    p2 = (f2-i2)*p
    p3 = (f3-i3)*p
    r1 = i1+p1
    r2 = i2+p2
    r3 = i3+p3
    if len(i)==4:
        return [r1,r2,r3,i[3]]
    else :
        return [r1,r2,r3]

def text(t,col,size,pos,ha,va,f=1,l=0):
    t_font = pygame.font.Font(fonts[f],int(size))
    t_pic = t_font.render(str(t),1,col)
    if l != 0 and t_pic.get_width() > l :
        for x in range(size):
            t_font = pygame.font.Font(fonts[f],size-x)
            t_pic = t_font.render(str(t),1,col)
            if t_pic.get_width() < l :
                break
    pic_x = t_pic.get_width()
    pic_y = t_pic.get_height()
    if ha == 1 :
        pos_x = pos[0]-(pic_x/2)
    elif ha == 2 :
        pos_x = pos[0]-pic_x
    else :
        pos_x = pos[0]
    if va == 1 :
        pos_y = pos[1]-(pic_y/2)
    elif va == 2 :
        pos_y = pos[1]-pic_y
    else :
        pos_y = pos[1]
    pos = [pos_x, pos_y]
    keep(t_pic,pos)

    
    

def hexagon(text,tc,ts,hc,vc,bc,l,b,pos,sb,sbc,cover,cc,f,el=0):
    if el != 0 :
        parts = el
    else :
        parts = l/5
    if sb != 0 :
        c = sbc[sb-1]
    else :
        c = bc
    rect(screen,c,[pos[0]+(parts),pos[1],l-(2*parts),b])
    poly(screen,c,[[pos[0],pos[1]+(b/2)],[pos[0]+(parts),pos[1]],[pos[0]+(parts),pos[1]+b]])
    poly(screen,c,[[pos[0]+l,pos[1]+(b/2)],[pos[0]+l-parts,pos[1]],[pos[0]+l-parts,pos[1]+b]])
    if cover :
        lines(screen,cc,1,[[pos[0],pos[1]+(b/2)+2],[pos[0]+(parts),pos[1]+b+2],[pos[0]+l-parts,pos[1]+b+2],
                           [pos[0]+l,pos[1]+(b/2)+2],[pos[0]+l-parts,pos[1]],[pos[0]+(parts),pos[1]]],5)
    t_font = pygame.font.Font(fonts[f],ts)
    t_pic = t_font.render(str(text),1,tc)
    tpx = t_pic.get_width()
    tpy = t_pic.get_height()
    if hc :
        tx = pos[0]+(l/2)-(tpx/2)
    else :
        tx = pos[0]+(parts)
    if vc :
        ty = pos[1]+(b/2)-(tpy/2)
    else :
        ty = pos[1]
    tpos = [tx,ty]
    keep(t_pic,tpos)

"""
text: text in hexagon
tc: text color
ts: text size
hc: horizontal centre align
vc: vertical centre align
bc: background color
l: length of the hexagon (no compromising about extra length)
b: breadth of the hexagon
pos: position of the hexagon
sb: no. of the background color (bc @ 0, sbc[0] @ 1, sbc[1] @ 2 ....)(not compulsory...set it to 0)
sbc: list of other background colors(not compulsory...set it to [])
cover: bool whether cover is required
cc: color of the cover (useless and can be set to anything if cover = False)
f: font type: PalatinoLinotype at 0, Microsoft Sans Serif at 1....(refer fonts)
el=0: length of the part from which hexagon's upper vertice starts
"""

def tsurf(t,s,c,f) :
    t_font = pygame.font.Font(fonts[f],int(s))
    t_pic = t_font.render(str(t),1,c)
    return t_pic

    
def text_box(text,ts,tc,hc,vc,pos,l,b,bc,cc,ct,barb,f,m=None):
    if m != None :
        m0 = m[0]
        m1 = m[1]
        b_r = (pos[0]<=m0<=(pos[1]+l)) and (pos[1]<=m1<=(pos[1]+b))
        return b_r
    else :
        rect(screen,bc,[pos[0],pos[1],l,b])
        rect(screen,cc,[pos[0],pos[1],l,b],ct)
        t_font = pygame.font.Font(fonts[f],ts)
        t_pic = t_font.render(text,1,tc)
        t_x = t_pic.get_width()
        t_y = t_pic.get_height()
        if hc :
            pos_x = pos[0]+(l/2)-(t_x/2)
        else :
            pos_x = pos[0]+5
        if vc :
            pos_y = pos[1]+(b/2)-(t_y/2)
        else :
            pos_y = pos[1]+5
        if barb :
            if tc == grey :
                pygame.draw.line(screen,black,[pos_x+2,pos_y],[pos_x+2,pos_y+t_y],2)
            else :
                pygame.draw.line(screen,black,[pos_x+2+t_x,pos_y],[pos_x+2+t_x,pos_y+t_y],2)                
        keep(t_pic,[pos_x,pos_y])

"""

"""

def keep_with_frame(pic,pos,fc1,fc2,t):
    keep(pic,pos)
    px = pic.get_width()
    py = pic.get_height()
    rect(screen,fc1,[pos[0]-t,pos[1]-t,px+(2*t),t])
    rect(screen,fc1,[pos[0]-t,pos[1]+py,px+(2*t),t])
    rect(screen,fc2,[pos[0]-t,pos[1],t,py])
    rect(screen,fc2,[pos[0]+px,pos[1],t,py])

def on(rect,p):
    r = Rect(rect)
    b = r.collidepoint(p)
    return b

def roundoff(x,i):
    a = int(x/i)*i
    b = int((x/i)+1)*i
    if abs(x-a)>abs(x-b):
        return b
    else :
        return a

def jumble(l):
    a = []
    while 1 :
        x = random.choice(l)
        if x not in a :
            a.append(x)
        if len(l) == len(a) :
            break
    return a

def In(p,r):
    if (r[0]<=p[0]<=(r[0]+r[2])) and (r[1]<=p[1]<=(r[1]+r[3])):
        return 1
    else :
        return 0


# Display

ric = 20
clore = [sx-50,5,40,40]
minre = [sx-100,5,40,40]
upcol = [white,yellow]


def borders():
    rect(screen,grey,[0,0,sx,50])
    rect(screen,grey,[0,50,20,sy-50])
    rect(screen,grey,[20,sy-20,sx-20,20])
    rect(screen,grey,[sx-20,50,20,sy-50])
    
def flip(m):
    borders()
    cb = In(m,clore)
    mb = In(m,minre)
    cir(screen,upcol[cb],[clore[0]+ric,clore[1]+ric],ric)
    cir(screen,upcol[mb],[minre[0]+ric,minre[1]+ric],ric)
    line(screen,black,[sx-40,15],[sx-20,35])
    line(screen,black,[sx-40,35],[sx-20,15])
    line(screen,black,[sx-95,25],[sx-65,25])
    cir(screen,green,[25,25],10)
    cir(screen,yellow,[50,25],10)
    cir(screen,white,[75,25],10)
    cir(screen,l1_blue,[100,25],10)
    cir(screen,red,[125,25],10)    
    pygame.display.flip()
    
def increase(v,r,maxi):
    if (v+r)<=maxi:
        return v + r
    else :
        return maxi

def decrease(v,r,mini):
    if (v-r)>=mini:
        return v - r
    else :
        return mini

def color(c):
    if type(c) is str :
        return Color(c)
    elif type(c) is list :
        return c

def pwc(n,s,c,p):
    repeat = 0
    for i in range(n):
        cir(screen,c,[s+p[0]+repeat,p[1]],s)
        repeat += 2*(s)+5

def rev(x):
    return int(not x)


# Classes and Functions to be Exported

def Label(lis,end):
    t = lis[0]          #Text
    tc = color(lis[1])  #TextColor
    ts = lis[2]         #TextSize
    pos = lis[3]        #Position
    ha = lis[4]         #Horizontal Center Align
    va = lis[5]         #Vertical Center Align
    f = lis[6]          #Font Index
    mp = mouse()        #Mouse Position
    if end[0]:
        fill(white)
    text(t,tc,ts,pos,ha,va,f)
    if end[1]:
        flip(mp)

def Box(lis,end):
    tp = lis[0]         #Text/pic
    tc = color(lis[1])  #TextColor/0
    ts = lis[2]         #TextSize/0
    r = lis[3]          #Rectangle for box
    bc = color(lis[4])  #Background Color
    boc = color(lis[5]) #Border Color
    f = lis[6]          #Font Index
    mp = mouse()
    if end[0] :
        fill(white)
    rect(screen,bc,r)
    rect(screen,boc,r,1)
    if ts != 0 :
        text(tp,tc,ts,[r[0]+(r[2]/2),r[1]+(r[3]/2)],1,1,f)        
    else :
        p = pic(tp)
        x = p.get_width()
        y = p.get_height()
        pos = [r[0]+(r[2]/2)-(x/2),r[1]+(r[3]/2)-(y/2)]
        keep(p,pos)
    if end[1] :
        flip(mp)

def BoxOfText(lis,lin,end):
    r = lis[0]
    bc = color(lis[1])
    boc = color(lis[2])
    mp = mouse()
    if end[0]:
        fill(white)
    rect(screen,bc,r)
    rect(screen,boc,r,1)
    for l in lin :
        text(l[0],color(l[1]),l[2],l[3],l[4],l[5],l[6])
    if end[1]:
        flip(mp)
        

nc = {
    0 : [' ','black',20,[],'white',silver,0],
    1 : ['1',l1_blue,20,[],'yellow',silver,0],
    2 : ['2','red',20,[],l2_blue,silver,0],
    3 : ['3','green',20,[],'gold',silver,0],
    4 : ['4','brown',20,[],'pink',silver,0],
    5 : ['5','pink',20,[],'brown',silver,0],
    6 : ['6','gold',20,[],'green',silver,0],
    7 : ['7',l2_blue,20,[],'red',silver,0],
    8 : ['8','yellow',20,[],l1_blue,silver,0],
    9 : ['Bomb.png',0,0,[],'white',silver,0]
    }

def draw_grid(grid):
    r = len(grid)
    c = len(grid[0])
    px = (sx/2)-((25*c)/2)
    py = (sy/2)-((25*r)/2)
    pb = py
    for p in grid :
        pa = px
        for q in p :
            Box([nc[q][0],nc[q][1],nc[q][2],[pa,pb,25,25],nc[q][4],nc[q][5],nc[q][6]],[0,0])
            pa += 25
        pb += 25

def draw_cover(grid):
    r = len(grid)
    c = len(grid[0])
    px = (sx/2)-((25*c)/2)
    py = (sy/2)-((25*r)/2)
    pb = py
    for p in grid :
        pa = px
        for q in p :
            if q == 1 :
                Box(['','white',20,[pa,pb,25,25],'black','white',0],[0,0])
            elif q == 2 :
                Box(['!','red',20,[pa,pb,25,25],'black','white',0],[0,0])
            elif q == 3 :
                Box(['?','gold',20,[pa,pb,25,25],'black','white',0],[0,0])
            pa += 25
        pb += 25

marker_grids = []

class DrawGrid(object):
    def __init__(self,g):
        self.grid = g
        self.x = len(self.grid[0])
        self.y = len(self.grid)
        self.px1 = (sx/2)-((self.x*25)/2)
        self.py1 = (sy/2)-((self.y*25)/2)
        self.px2 = (sx/2)+((self.x*25)/2)
        self.py2 = (sy/2)+((self.y*25)/2)
        self.positions = []
        self.myg = []
        self.win = 0
        self.lose = 0
        pbc = self.py1
        for p in self.grid :
            pac = self.px1
            mygp = []
            poss = []
            for q in p :
                mygp.append(1)
                poss.append([pac,pbc])
                pac += 25
            self.myg.append(mygp)
            self.positions.append(poss)
            pbc += 25
    def value_update(self):
        self.t_no = self.x*self.y
        self.no_b = 0
        for q in self.grid :
            for p in q :
                if p == 9 :
                    self.no_b += 1
        self.free = self.t_no-self.no_b
        self.closed = 0
        self.opened = 0
        self.bombno = 0
        self.doubts = 0
        for p in self.myg :
            for q in p :
                if q == 0 :
                    self.opened += 1
                elif q == 1 :
                    self.closed += 1
                elif q == 2 :
                    self.bombno += 1
                elif q == 3 :
                    self.doubts += 1
        if not self.lose :
            if self.opened == self.free :
                self.win = 1
    def draw(self,end):
        self.value_update()
        if end[0]:
            fill(white)
        draw_grid(self.grid)
        draw_cover(self.myg)
        mp = mouse()
        if end[1]:
            flip(mp)
    def clear(self,fid__,sid__):
        self.myg[fid__][sid__] = 0
        if fid__ > 0 :
            if sid__ > 0 :                
                if self.grid[fid__-1][sid__-1] == 0 and self.myg[fid__-1][sid__-1] != 0 :
                    self.clear(fid__-1,sid__-1)
                else :
                    self.myg[fid__-1][sid__-1] = 0            
            if self.grid[fid__-1][sid__] == 0 and self.myg[fid__-1][sid__] != 0 :
                self.clear(fid__-1,sid__)
            else :
                self.myg[fid__-1][sid__] = 0
            if sid__ < (self.x-1) :                
                if self.grid[fid__-1][sid__+1] == 0 and self.myg[fid__-1][sid__+1] != 0 :
                    self.clear(fid__-1,sid__+1)
                else :
                    self.myg[fid__-1][sid__+1] = 0
        if sid__ > 0 :            
            if self.grid[fid__][sid__-1] == 0 and self.myg[fid__][sid__-1] != 0 :
                self.clear(fid__,sid__-1)
            else :
                self.myg[fid__][sid__-1] = 0
        if sid__ < (self.x-1) :            
            if self.grid[fid__][sid__+1] == 0 and self.myg[fid__][sid__+1] != 0 :
                self.clear(fid__,sid__+1)
            else :
                self.myg[fid__][sid__+1] = 0
        if fid__ < (self.y-1) :
            if sid__ > 0 :                
                if self.grid[fid__+1][sid__-1] == 0 and self.myg[fid__+1][sid__-1] != 0 :
                    self.clear(fid__+1,sid__-1)
                else :
                    self.myg[fid__+1][sid__-1] = 0            
            if self.grid[fid__+1][sid__] == 0 and self.myg[fid__+1][sid__] != 0 :
                self.clear(fid__+1,sid__)
            else :
                self.myg[fid__+1][sid__] = 0
            if sid__ < (self.x-1) :                
                if self.grid[fid__+1][sid__+1] == 0 and self.myg[fid__+1][sid__+1] != 0 :
                    self.clear(fid__+1,sid__+1)
                else :
                    self.myg[fid__+1][sid__+1] = 0
    def ms(self,mpd):
        left = mpd[0]
        right = mpd[2]
        mp = mouse()
        mx = mp[0]
        my = mp[1]
        fid = -1
        sid = -1
        if left and (self.px1 < mx < self.px2) and (self.py1 < my < self.py2) :
            for q in self.positions :
                for p in q :
                    if (p[0]<mx<(p[0]+25)) and (p[1]<my<(p[1]+25)) :
                        fid = self.positions.index(q)
                        sid = q.index(p)
                        break
                if (fid >= 0) and (sid >= 0) :
                    break
            if (fid>=0) and (sid>=0):
                self.myg[fid][sid] = 0
                if self.grid[fid][sid] == 9 :
                    self.lose = 1
                    pa = 0
                    for p in self.grid :
                        qb = 0
                        for q in p :
                            if q == 9 :
                                self.myg[pa][qb] = 0
                            qb += 1
                        pa += 1
                if self.grid[fid][sid] == 0 :
                    self.clear(fid,sid)
                self.draw([0,0])
        elif right and (self.px1 < mx < self.px2) and (self.py1 < my < self.py2) :
            for q in self.positions :
                for p in q :
                    if (p[0]<mx<(p[0]+25)) and (p[1]<my<(p[1]+25)) :
                        fid = self.positions.index(q)
                        sid = q.index(p)
                        break
                if (fid >= 0) and (sid >= 0) :
                    break
            if (fid>=0) and (sid>=0):
                if 1 <= self.myg[fid][sid] <= 2 :
                    self.myg[fid][sid] += 1
                    self.draw([0,0])
                elif self.myg[fid][sid] == 3 :
                    self.myg[fid][sid] = 1
                    self.draw([0,0])    
    def get(self):
        return [self.t_no,self.no_b,self.free,self.closed,self.opened,self.bombno,self.doubts]
    def win_or_lose(self):
        return [self.win,self.lose]


class Timer(object):
    def __init__(self):
        self.c = pygame.time.Clock()
        self.t = 0
    def get(self):
        self.t += self.c.tick()
        self.ti = int(self.t/1000.0)
        return self.ti

buttons = [[],[],[]]

class Button(object):
    def __init__(self,lis,end):
        t = lis[0]
        self.t = t
        r = lis[1]
        self.r = r
        tc = color(lis[2])
        ts = lis[3]
        bcl = []
        bc = None
        for c in lis[4] :
            bcl.append(color(c))
        borc = color(lis[5])
        fontind = lis[6]
        if t not in buttons[0]:
            buttons[0].append(t)
            buttons[1].append(0.0)
            buttons[2].append(0)
        self.bid = buttons[0].index(self.t)
        mp = mouse()
        monb = In(mp,r)
        if monb and buttons[2][self.bid] < 2 :
            buttons[1][self.bid] = increase(buttons[1][self.bid],0.04,1)
        elif buttons[2][self.bid] < 2 :
            buttons[1][self.bid] = decrease(buttons[1][self.bid],0.08,0)
        if buttons[2][self.bid] == 0 :
            bc = fade(bcl[0],bcl[1],buttons[1][self.bid])
        elif buttons[2][self.bid] == 1 and bc != bcl[2]:
            bc = bcl[2]
            buttons[2][self.bid] = 2
            buttons[1][self.bid] = 0
        elif buttons[2][self.bid] == 2 :
            bc = fade(bcl[2],bcl[0],buttons[1][self.bid])
            buttons[1][self.bid] = increase(buttons[1][self.bid],0.02,1)
            if buttons[1][self.bid] == 1 :
                buttons[2][self.bid] = 3
        else :
            bc = bcl[2]
        if end[0] :
            fill(white)        
        rect(screen,bc,r)
        rect(screen,borc,r,2)
        mx = r[0]+(r[2]/2)
        my = r[1]+(r[3]/2)
        text(t,tc,ts,[mx,my],1,1,fontind)
        if end[1] :
            flip(mp)
    def click(self):
        self.bid = buttons[0].index(self.t)
        mp = mouse()
        if In(mp,self.r):
            buttons[2][self.bid] = 1
    def get(self):
        self.bid = buttons[0].index(self.t)
        if buttons[2][self.bid] == 3 :
            return 1            
        else :
            return 0
    def delete(self):
        self.bid = buttons[0].index(self.t)
        buttons[0].remove(buttons[0][self.bid])
        buttons[1].remove(buttons[1][self.bid])
        buttons[2].remove(buttons[2][self.bid])



TextBoxes = [[],[],[],[],[]]


class TextBox(object):
    def __init__(self,lis,end,typg=None):
        h = lis[0]                                      #Hint
        pr = lis[1]                                     #Rect or line (len 4 for rect, 3 for line)
        ts = lis[2]                                     #Text Size
        if len(pr)==4 :
            r = pr
        elif len(pr)==3:
            r = [pr[0],pr[1]-ts-2,pr[0]+pr[2],ts+5]     #Makes line a rect (for convenience!)
        self.r = r                                      #Feeds the given rect to the class
        tcl = lis[3]                                    #List of two colors(1st for hint, 2nd for text)
        brl = lis[4]                                    #List of two colors(1st for inactive border, 2nd for active border)
        f = lis[5]                                      #Font index
        gac = lis[6]                                    #Active or not
        self.ty = typg
        mp = mouse()                                    #Mouse Position
        if h not in TextBoxes[0]:
            TextBoxes[0].append(h)                      #hint
            TextBoxes[1].append(gac)                    #active or not
            TextBoxes[2].append('')                     #text input
            TextBoxes[3].append(0)                      #marker active or not
            TextBoxes[4].append(0.00)                   #marker timing
        self.tid = TextBoxes[0].index(h)                #ID of this textbox in the list TextBoxes
        br = color(brl[TextBoxes[1][self.tid]])         #Selects color for border from gac
        self.t = TextBoxes[2][self.tid]                 #Feeds the input(ed) text to the class
        if end[0]:
            fill(white)
        if len(pr) == 4 :
            rect(screen,white,r)
            rect(screen,br,r,2)
        elif len(pr) == 3 :
            line(screen,br,[pr[0],pr[1]],[pr[0]+pr[2],pr[1]],2)
        if self.t == '' :
            tc = color(tcl[0])            
            pos = [r[0]+5,r[1]+(r[3]/2)]
            text(h,tc,ts,pos,0,1,f)
        if self.t != '' :
            tc = color(tcl[1])
            if self.ty == None or self.ty == 'Normal' or self.ty == 'Numbers':                
                pos = [r[0]+5,r[1]+(r[3]/2)]
                text(self.t,tc,ts,pos,0,1,f)
            elif self.ty == 'Password':
                radi = ts/5
                ncs = len(self.t)
                pos = [r[0]+5,r[1]+(r[3]/2)]
                pwc(ncs,radi,tc,pos)      
        if end[1]:
            flip(mp)
    def click(self):
        mp = mouse()
        TextBoxes[1][self.tid] = In(mp,self.r)
    def get(self):
        if self.ty == None or self.ty == 'Normal' or self.ty == 'Password':
            return self.t
        elif self.ty == 'Numbers' :
            if self.t == '' :
                return 0
            else :
                return int(self.t)
    def typ(self,updown,key):
        if TextBoxes[1][self.tid]:
            if key == K_LSHIFT or key == K_RSHIFT :
                if updown :
                    TextBoxes[4][self.tid] = 1
                else :
                    TextBoxes[4][self.tid] = 0
            if updown :
                shift = TextBoxes[4][self.tid]
                if key in keys1 or key in keys2 :
                    if shift :
                        if self.ty == None or self.ty == 'Normal' or self.ty == 'Password':
                            TextBoxes[2][self.tid] += str(keys2[key])
                        elif self.ty == 'Numbers':
                            if type(keys2[key]) == int :
                                TextBoxes[2][self.tid] += str(keys2[key])
                    else :
                        if self.ty == None or self.ty == 'Normal' or self.ty == 'Password':
                            TextBoxes[2][self.tid] += str(keys1[key])
                        elif self.ty == 'Numbers':
                            if type(keys1[key]) == int :
                                TextBoxes[2][self.tid] += str(keys1[key])
                elif key in kpdks :
                    if self.ty == None or self.ty == 'Normal' or self.ty == 'Password':
                        TextBoxes[2][self.tid] += str(kpdks[key])
                    elif self.ty == 'Numbers' :
                        if type(kpdks[key]) == int :
                            TextBoxes[2][self.tid] += str(kpdks[key])
                if key == K_BACKSPACE :
                    TextBoxes[2][self.tid] = TextBoxes[2][self.tid][:len(TextBoxes[2][self.tid])-1]
    def delete(self):
        TextBoxes[0].remove(buttons[0][self.tid])
        TextBoxes[1].remove(buttons[1][self.tid])
        TextBoxes[2].remove(buttons[2][self.tid])
        TextBoxes[3].remove(buttons[3][self.tid])
        TextBoxes[4].remove(buttons[4][self.tid])
         


        
"""        
elif event == K1 :
                key = e.key
                if key in keys :
                    if shift_key :
                        if keys[key] == '1' :
                            text_to_type = '!'
                        elif keys[key] == '2' :
                            text_to_type = '@'
                        elif keys[key] == '3' :
                            text_to_type = '#'
                        elif keys[key] == '4' :
                            text_to_type = '$'
                        elif keys[key] == '5' :
                            text_to_type = '%'
                        elif keys[key] == '6' :
                            text_to_type = '^'
                        elif keys[key] == '7' :
                            text_to_type = '&'
                        elif keys[key] == '8' :
                            text_to_type = '*'
                        elif keys[key] == '9' :
                            text_to_type = '('
                        elif keys[key] == '0' :
                            text_to_type = ')'
                        elif keys[key] == '-' :
                            text_to_type = '_'
                        elif keys[key] == '=' :
                            text_to_type = '+'
                        elif keys[key] == '[' :
                            text_to_type = '{'
                        elif keys[key] == ']' :
                            text_to_type = '}'
                        elif keys[key] == ';' :
                            text_to_type = ':'   
                        elif keys[key] == "'" :
                            text_to_type = '"'    
                        elif keys[key] == '/' :
                            text_to_type = '?'
                        elif keys[key] == '.' :
                            text_to_type = '>'
                        elif keys[key] == ',' :
                            text_to_type = '<'                 
                        else :
                            text_to_type = keys[key].upper()
                    else :
                        text_to_type = keys[key].lower()
                    text_type += text_to_type
                elif key == K_BACKSPACE :
                    text_type = text_type[:len(text_type)-1]
                elif key == K_RSHIFT or key == K_LSHIFT :
                    shift_key = True
                elif key == K_KP_ENTER :
                    d_n_b_2 = True
            elif event == K2 :
                key = e.key
                if key == K_RSHIFT or key == K_LSHIFT :
                    shift_key = False
"""

m1 = [[0,0]]

def Events(btns,tbxs,mbxs):
    mp = mouse()    
    for mbx in mbxs :
        m = pygame.mouse.get_pressed()
        if m1[0] != m :
            mbx.ms(m)
            m1[0] = m
    for e in events():
        event = e.type
        if event == X :
            bye()
        elif event == M1 :
            if In(mp,clore):
                bye()
            elif In(mp,minre):
                mz()
            for btn in btns :
                btn.click()
            for tbx in tbxs :
                tbx.click()
        elif event == K1 :
            key = e.key 
            for tbx in tbxs :
                tbx.typ(1,key)
        elif event == K2 :
            key = e.key
            for tbx in tbxs :
                tbx.typ(0,key)