import pygame
pygame.init()
tamanopantalla=500
tamanocubo=20
ncubospatalla=int(tamanopantalla/tamanocubo)

screen = pygame.display.set_mode([tamanopantalla,tamanopantalla])



piedra = pygame.image.load("piedra.png")

piedra = pygame.transform.scale(piedra, [int(tamanocubo*1.5),int(tamanocubo*1.5)])

tierra = pygame.image.load("tierra.png")

tierra = pygame.transform.scale(tierra, [int(tamanocubo*1.5),int(tamanocubo*1.5)])

mundo= [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]*ncubospatalla for i in range(ncubospatalla)]

for a in range(3):
    for e in range(3):
        for i in range(3):
            mundo[a+11][e+11][i+11]=tierra
#mundo[10][13][5]=0
#for e in range(9):
 #   for a in range(ncubospatalla):
  #      for i in range(ncubospatalla):
   #         mundo[e][a][i]=piedra

#for a in range(ncubospatalla):
 #   for i in range(ncubospatalla):
  #      mundo[9][a][i]=tierra

print(mundo)

def cor3a2d(x,y,z):
    x2=x
    y2=y
    y2=(tamanopantalla/tamanocubo)-y2
    x2=x2+z*(1/2)
    y2=y2-z*(1/2)
    return(x2*tamanocubo,y2*tamanocubo)

def cuadrado(x,y):
    pygame.draw.line(screen,(0, 0, 255),(x,y),(x+tamanocubo,y),5)
    pygame.draw.line(screen,(0, 0, 255),(x,y),(x,y+tamanocubo),5)
    pygame.draw.line(screen,(0, 0, 255),(x+tamanocubo,y+tamanocubo),(x+tamanocubo,y),5)
    pygame.draw.line(screen,(0, 0, 255),(x+tamanocubo,y+tamanocubo),(x,y+tamanocubo),5)

def cubo(x,y,z):
    y=y+1
    x,y=cor3a2d(x,y,z)
    cuadrado(x,y)
    cuadrado(x+(tamanocubo/2),y-(tamanocubo/2))
    pygame.draw.line(screen,(0, 0, 255),(x,y),(x+(tamanocubo/2),y-(tamanocubo/2)),5)
    pygame.draw.line(screen,(0, 0, 255),(x+tamanocubo,y),(x+tamanocubo+(tamanocubo/2),y-(tamanocubo/2)),5)
    pygame.draw.line(screen,(0, 0, 255),(x,y+tamanocubo),(x+(tamanocubo/2),y+tamanocubo-(tamanocubo/2)),5)
    pygame.draw.line(screen,(0, 0, 255),(x+tamanocubo,y+tamanocubo),(x+tamanocubo+(tamanocubo/2),y+tamanocubo-(tamanocubo/2)),5)

def bloque(tipo,x,y,z):
    x,y=cor3a2d(x,y,z)
    y=y-tamanocubo*1.5
    if tipo!=0:
        screen.blit(tipo, [x, y])

def printmundo(munndo):
    for a in range(ncubospatalla):
        for e in range(ncubospatalla):
            for i in reversed(range(ncubospatalla)):
                bloque(munndo[a][e][i],e,a,i)

def printmundo2():
    for a in range(ncubospatalla):
        for e in range(ncubospatalla):
            for i in reversed(range(ncubospatalla)):
                bloque(mundo[a][e][i],e,a,i)

def cubovisible(munndo,x,y,z):
    if munndo[x][y+1][z]==0 or munndo[x+1][y][z]==0 or munndo[x][y][z-1]==0:
        return(True)
    else:
        return(False)

def bloquepulsado():
    (xr,yr)=pygame.mouse.get_pos()
    for a in range(ncubospatalla):
        for e in range(ncubospatalla):
            for i in range(ncubospatalla):
                (xb,yb)=cor3a2d(a,e,i)
                if xr>xb and xr<(xb+int(tamanocubo*1.5)) and yr>yb and yr<(yb+int(tamanocubo*1.5)) and cubovisible(mundo,a,e,i)==True and mundo[a][e][i]!=0:
                    mundo[a][e][i]=0
                    print("adios")
                    return()     



running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bloquepulsado()
            print("hola")


    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    mundo[9][9][9]=0
    printmundo2()
   
    # Flip the display
    pygame.display.flip()
