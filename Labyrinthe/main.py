import sys
import pygame
import time
import random

from scripts.entite import Joueur, Cle, Ennemi
from scripts.mur import Mur_Vert, Mur_Hor, Mur, Bordure, path

class Jeu:
    def __init__(self):

        pygame.init()
        pygame.display.set_caption('Labyrinthe')

        self.screen = pygame.display.set_mode((1216, 772))  # (32+25*32+24*16,32+36+15*32+14*16)
        self.clock = pygame.time.Clock()

        # creation chemin
        self.chemin = path()

        self.cle = Cle(self)

        self.movement = [False, False, False, False]
        self.joueur = Joueur(self, 'sorciere')

        self.ennemi = Ennemi(self)

        self.skin = pygame.image.load('Labyrinthe/img/mur.png').convert()

        # creation matrice mur verticaux
        self.mur_vert = Mur_Vert(self, self.skin)
        self.list_murV = self.mur_vert.yaMur()

        # creation matrice mur horizontaux
        self.mur_hor = Mur_Hor(self, self.skin)
        self.list_murH = self.mur_hor.yaMur()

        self.mur = Mur(self, self.skin)
        self.bordure = Bordure(self,self.skin)

        # initialisation liste coordonnées des murs
        self.obstacles = []

        print(self.chemin[0])





    def run(self):

        # positionement murs
        self.mur.Rendu_Mur(self.screen)
        self.mur_vert.Rendu_Mur_vert(self.screen, self.chemin[0], self.list_murV)
        self.mur_hor.Rendu_Mur_hor(self.screen, self.chemin[1], self.list_murH)

        # remplissage liste coordonnées murs
        self.mur.collision(self.obstacles)
        self.mur_hor.collision(self.obstacles)
        self.mur_vert.collision(self.obstacles)


        while True:
            # fond d'écran
            self.screen.fill((55, 50, 123))

            #calcul déplacements

            self.hitbox = self.joueur.Collision_joueur()

            self.joueur.mouv([self.movement[3] - self.movement[2], self.movement[1] - self.movement[0]],self.hitbox,self.obstacles)

            self.cle.Collision_cle(self.hitbox)

            self.hitbox_ennemi = self.ennemi.Collision_ennemi()
            a = random.randint(0, 1)
            b = random.randint(0, 1)
            for i in range(6):
                self.ennemi.Mouvement(self.hitbox_ennemi,self.obstacles,[a,b])
            if self.ennemi.Degat(self.hitbox,self.hitbox_ennemi):
                self.joueur.Nb_vie()





            #actualisation visuelle position joueur
            self.joueur.Rendu(self.screen)
            self.cle.Rendu(self.screen)
            self.ennemi.Rendu_Ennemi(self.screen)

            # actualisation visuelle murs
            self.bordure.Rendu_Bordure(self.screen)
            self.mur.Rendu_Mur(self.screen)
            self.mur_vert.Rendu_Mur_vert(self.screen, self.chemin[0],self.list_murV)
            self.mur_hor.Rendu_Mur_hor(self.screen, self.chemin[1], self.list_murH)


            if self.joueur.vie_restante <= 0:
                print('Perdu, la HOOOOONTE')
                pygame.quit()
                sys.exit()

            if self.joueur.pos == [1172,688] and self.cle.obtenue :
                print('gagné ... bref ...')
                pygame.quit()
                sys.exit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_z:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.movement[1] = True
                    if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                        self.movement[2] = True
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_z:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.movement[1] = False
                    if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                        self.movement[2] = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[3] = False

            pygame.display.update()
            self.clock.tick(60)


Jeu().run()