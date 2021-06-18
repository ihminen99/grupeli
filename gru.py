import pygame
import sys
from pygame.locals import *

pygame.init()

koko = (500,600) 
ruutu = pygame.display.set_mode(koko)

taustavari = (255, 255, 255) 
pallovari = (255, 0, 0) 


#käsittelee tapahtumia
def gru():
    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



#piirtää  asioita
def piirtaja():
    napit =  pygame.mouse.get_pressed()
    if not napit[0]:
        ruutu.fill(taustavari)
    paikka = pygame.mouse.get_pos()
    pygame.draw.circle(ruutu, pallovari, paikka, 20)
    




while True:
    gru()
    piirtaja()
    pygame.display.flip()