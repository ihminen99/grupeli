import pygame
import sys
import random
from pygame.locals import *

pygame.init()
pygame.font.init()
pygame.mixer.init()

koko = (500,600) 
ruutu = pygame.display.set_mode(koko)

# lataus
pelaaja = pygame.image.load("gru whatssap car.png")
maa = pygame.image.load("landia.png")
paha = pygame.image.load("paha.png")

pelaaja = pygame.transform.scale(pelaaja, (100,100))
paha = pygame.transform.scale(paha, (100,100))

#musa
pygame.mixer.music.load("mario.mp3")
pygame.mixer.music.play(-1)

amogus = pygame.mixer.Sound("amogus.mp3")
iso_kukus = pygame.mixer.Sound("iso kukus.mp3")

# tekstit
pellifontti = pygame.font.SysFont("Impact", 40)
loppufontti = pygame.font.SysFont("Impact", 40)
pelivari = (255, 17, 0)
loppuvari = (158, 21, 11)

# muuttujat
pelaajax = 250
pelaajay = 450
nopeus = 11
vihunopeus = 10
hp = 10
on_tehty = False
ennatys = 0.0


vihut = [
    [100,100],
    [200,200],
    [300,300]]

# ennätyksen lukeminen
with open("ennatys","r") as Tiedosto:
    luettu = Tiedosto.read()
    ennatys = int(luettu)


# ajastin
    kello = pygame.time.Clock()
FPS = 30
alkuaika = pygame.time.get_ticks()

taustavari = (15, 117, 25) 

#käsittelee tapahtumia
def gru():
    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()   
            sys.exit()

#ohjaa peliä
def pelilogiikka(): 
    global pelaajax, pelaajay, hp, ennatys   

    nappi = pygame.key.get_pressed()
    if nappi[pygame.K_d]:
        pelaajax += nopeus
    if nappi[pygame.K_a]:
        pelaajax -= nopeus

#Pysäyttää
    if pelaajax < 0:
        pelaajax = 0
    if pelaajax > 500-100:     # ruudun leveys - pelaajan leveys
        pelaajax = 500-100
    for vihu in vihut:
            vihu[1] += vihunopeus
            if vihu[1] > 600:
                vihu[1] = -100
                vihu[0] = random.randint(10, 500-100-10)


    aika = pygame.time.get_ticks()-alkuaika
    if aika >= ennatys:
        ennatys = aika


    for vihu in vihut:
        if vihu[1] +100 > pelaajay and vihu[1] < pelaajay+100:
            if vihu[0] +100 > pelaajax and vihu[0] < pelaajax+100:
                hp -= 1
                amogus.play()

                vihu[1] = -100
                vihu[0] = random.randint(10, 500-100-10)


#piirtää  asioita
def piirtaja():
    ruutu.blit(maa,(0,0))   # tausta piirto
    ruutu.blit(pelaaja,(pelaajax, pelaajay)) # pelaaja piirto

    # vihu piirto
    for viholinen in vihut:
        ruutu.blit(paha, viholinen)


# tekstiin piiirto
    hpteksti = pellifontti.render("Elämä: "+str(hp), False, pelivari )
    ruutu.blit(hpteksti, (30,30))
    aika = pygame.time.get_ticks()-alkuaika
    aikateksti = pellifontti.render("aika: "+str(aika/1000), False, pelivari )
    ruutu.blit(aikateksti, (30,70))
    
    ennatysteksti = pellifontti.render("Ennatys: "+str(ennatys/1000), False, pelivari )
    ruutu.blit(ennatysteksti,(30,120))


def gameover():
    global on_tehty

    if not on_tehty:
        on_tehty = True
        pygame.mixer.music.stop()
        amogus.play

        with open("ennatys","w") as Tiedosto:
            Tiedosto.write(str(ennatys))




    ruutu.fill(loppuvari)
    teksti = loppufontti.render("gru törmäsi", True, (255, 255, 255))
    ruutu.blit(teksti, (30, 30))

    ennatysteksti = pellifontti.render("Ennatys: "+str(ennatys/1000), False, pelivari )
    ruutu.blit(ennatysteksti,(30,120))




#voitto
def voitto():
    global on_tehty
    if not on_tehty:
        on_tehty = True
        pygame.mixer.music.stop()
        iso_kukus.play()
        with open("ennatys","w") as Tiedosto:
            Tiedosto.write(str(ennatys))




    ruutu.fill(loppuvari)
    teksti = loppufontti.render("gru voitti", True, (16, 74, 31))
    ruutu.blit(teksti, (30, 30))

    ennatysteksti = pellifontti.render("Ennatys: "+str(ennatys/1000), False, pelivari )
    ruutu.blit(ennatysteksti,(30,120))





# silmukkaaaa
while True:
    gru()
    aika = pygame.time.get_ticks()-alkuaika

    
    if hp <= 0:
        gameover()

    elif aika > 100000:
        voitto()
    else:
        pelilogiikka()
        piirtaja()

    pygame.display.flip()
    kello.tick(FPS)