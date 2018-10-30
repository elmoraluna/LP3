import pygame, random
from pygame.locals import *

HEIGHT = 800 
WIDTH = 600
FPS = 60

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((HEIGHT, WIDTH))
    pygame.display.set_caption("Arkanoid")
    reloj = pygame.time.Clock()
    barra = Barra(pantalla, 500, 300, 100, 10, (0, 0, 0))
    pelota = Bola(pantalla, 100, 100, 20, (255, 0, 0))
    almacen = Almacen(pantalla)
    almacen.generacion()

    #ejecutando = True
    while True:
        #Inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #ejecutando = False
                pygame.quit()
                sys.exit()
            """elif event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    barra.cambio(-barra.velx)
                elif event.key == K_RIGHT:
                    barra.cambio(barra.velx)"""
        #Updates

        #Renderizado
        pantalla.fill((93, 97, 104))
        almacen.generacion()
        pelota.cambio()
        barra.cambio(barra.velx)
        #pantalla.blit(barra, barra.rect)
        pygame.display.flip()
        #pygame.display.update()
        reloj.tick(FPS)

class Bola:
    def __init__(self, pantalla, x, y, ancho, color):
        self.pantalla = pantalla
        self.x = x
        self.y = y
        self.color = color
        self.ancho = ancho
        self.rect = Rect(x, y, ancho, ancho)
        self.velx = 5
        self.vely = 5
    
    def cambio(self):
        self.x += self.velx
        self.y += self.vely
        self.rect = Rect(self.x, self.y, self.ancho, self.ancho)
        pygame.draw.circle(self.pantalla, self.color, (int(self.x), int(self.y)), int(self.ancho/2))
        if self.x < 0 or self.x > WIDTH:    #En caso colisione en algún lado 
            self.velx *= -1
        if self.y < 0:                      #En caso colisione con el borde superior
            self.vely *= -1
        if self.y > HEIGHT:                 #En caso caiga la bola
            return False

class Bloque:
    def __init__(self, pantalla, x, y, ancho, altura, color):
        self.pantalla = pantalla
        self.x = x
        self.y = y
        self.color = color
        self.ancho = ancho
        self.altura = altura
        self.rect = Rect(x, y, ancho, altura)
    
    def vmBloque(self):
        pygame.draw.rect(self.pantalla, self.color, self.rect)
        

class Almacen(Bloque):
    def __init__(self, pantalla):
        self.pantalla = pantalla
        #self.matriz = Bloque[10][3]

    def generacion(self):                   #Generación de bloques
        for i in range(3):
            for j in range(10):
                bloque = Bloque(self.pantalla, j*80, i*30, 80, 30, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
                bloque.vmBloque()
                #self.matriz[i][j] = bloque

class Barra:
    def __init__(self, pantalla, x, y, ancho, altura, color):
        self.pantalla = pantalla
        self.x = x
        self.y = y
        self.color = color
        self.ancho = ancho
        self.altura = altura
        self.rect = Rect(x, y, ancho, altura)
        self.velx = 5

    def cambio(self, velx):
        self.x += velx          #Variación de la posición
        self.rect = Rect(self.x, self.y, self.ancho, self.altura)
        pygame.draw.rect(self.pantalla, self.color, self.rect)


if __name__ == "__main__":
    main()
