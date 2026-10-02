import pygame
import random

pygame.init()

largopantalla = 1080

anchopantalla = 1940

tamanocubo = 20

xjugador = 100*tamanocubo

yjugador = 60*tamanocubo

velocidad=2

screen = pygame.display.set_mode([anchopantalla,largopantalla])

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)

steve = pygame.image.load("steve.png")

steve = pygame.transform.scale(steve,[tamanocubo,tamanocubo*2])

inventariop = pygame.image.load("inventariop.png")

inventariop = pygame.transform.scale(inventariop,[int((anchopantalla/3)),int(anchopantalla/3/182*22)])

piedra = pygame.image.load("piedra.png")

piedra = pygame.transform.scale(piedra, [tamanocubo,tamanocubo])

tnt = pygame.image.load("tnt.png")

tnt = pygame.transform.scale(tnt, [tamanocubo,tamanocubo])

tierra = pygame.image.load("tierra.png")

tierra = pygame.transform.scale(tierra, [tamanocubo,tamanocubo])

suelo = pygame.image.load("suelo.png")

suelo = pygame.transform.scale(suelo, [tamanocubo,tamanocubo])

tronco = pygame.image.load("tronco.png")

tronco = pygame.transform.scale(suelo, [tamanocubo,tamanocubo])




inventario=[]
for i in range(9):
    inventario.append([0,0])
mundo=[]

"""for a in range(tamanocubo0):
    mundo.append([])
    for i in range(100):
        if i>40:
            mundo[a].append(piedra)
        elif i==40:
            mundo[a].append(tierra)
        else:
            mundo[a].append(0)
print(mundo)"""

""" for i in range(40):
    filay.append(0)


filay.append(tierra)

for i in range(59):
    filay.append(piedra)

for i in range(tamanocubo0):
    mundo.append(filay) """




    
def crearmundo():
    alturasmundo=[]
    alturasmundo.append(random.randint(60,70))
    llano_segido=1
    probabilidad=1
    for i in range(200):
        toca_nivel=random.randint(1,probabilidad*(8-llano_segido))
        if toca_nivel!=1:
            alturasmundo.append(alturasmundo[i])
            llano_segido=llano_segido+1
        elif toca_nivel==1 and random.randint(1,2)==1:
            alturasmundo.append(alturasmundo[i]+1)
            llano_segido=1
        else:
            alturasmundo.append(alturasmundo[i]-1)
            llano_segido=1
    return(alturasmundo)
lo_que_va_a_ser_mundo=crearmundo()
def escribir_mundo():
    for i in range(len(lo_que_va_a_ser_mundo)):
        mundo.append([])
        for a in range(100-lo_que_va_a_ser_mundo[i]):
            mundo[i].append(0)
        mundo[i].append(tierra)
        for a in range(2):
            mundo[i].append(suelo)
        for a in range(lo_que_va_a_ser_mundo[i]-3):
            mundo[i].append(piedra)
escribir_mundo()
def cuadrado(x,y):
    if mundo[x][y]!=0:
        screen.blit(mundo[x][y],[((x*tamanocubo)-xjugador+970),((y*tamanocubo)-yjugador)+600])

def imprimir_mundo():
    for x in range(len(mundo)):
        for y in range(len(mundo[0])):
            cuadrado(x,y)

def dbp():
    (xr,yr)=pygame.mouse.get_pos()
    xr=xr+xjugador-970
    yr=yr+yjugador-600
    xr=int(xr/tamanocubo)
    yr=int(yr/tamanocubo)
    mundo[xr][yr]=0

def pbp(bloque):
    (xr,yr)=pygame.mouse.get_pos()
    xr=xr+xjugador-970
    yr=yr+yjugador-600
    xr=int(xr/tamanocubo)
    yr=int(yr/tamanocubo)
    if mundo[xr][yr]==0:
        mundo[xr][yr]=bloque

def etnt():
    (xr,yr)=pygame.mouse.get_pos()
    xr=xr+xjugador-970
    yr=yr+yjugador-600
    xr=int(xr/tamanocubo)
    yr=int(yr/tamanocubo)
    if mundo[xr][yr]==tnt:
        for x in range(5):
            for y in range(5):
                mundo[xr-2+x][yr-2+y]=0


running=True
movingx=0
velocidady=0
gravedad=0.1

while running==True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:    
                dbp()
            if event.button == 2:
                pbp(tnt)
            if event.button == 3:
                pbp(piedra)
                etnt()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                movingx=1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                movingx=0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                movingx=-1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                movingx=0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL:
                velocidad=4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LCTRL:
                velocidad=2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if  mundo[int((xjugador/tamanocubo))][int((yjugador/tamanocubo)-1)]!=0:
                    velocidady=3
                
    imprimir_mundo()

    if  mundo[int((xjugador/tamanocubo))][int((yjugador/tamanocubo)-1)]!=0 and velocidady<=0:
        velocidady=0
    else:
        velocidady=velocidady-gravedad

    if mundo[int((xjugador/tamanocubo)+1)][int((yjugador/tamanocubo)-2)]==0 and movingx>0:
        xjugador=xjugador+movingx*velocidad
    if mundo[int((xjugador/tamanocubo))][int((yjugador/tamanocubo)-2)]==0 and movingx<0:
        xjugador=xjugador+movingx*velocidad

    yjugador=yjugador-velocidady
    screen.blit(inventariop,[(anchopantalla-(anchopantalla/3))/2,900])
    screen.blit(steve,[anchopantalla/2,largopantalla/2])

    pygame.display.flip()
    screen.fill(white)