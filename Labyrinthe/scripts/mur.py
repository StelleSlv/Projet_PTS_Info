import pygame

import random



def path():

    mur_enleve_V = []
    mur_enleve_H = []
    a = 1 #random.randint(1,3)
    if a ==1:
        mur_enleve_V = [(0,2),(0,3)]
        mur_enleve_H = [(0,0),(0,1),(2,2)]
    elif a == 2:
        mur_enleve_V = []
        mur_enleve_H = []
    elif a == 3:
        mur_enleve_V = []
        mur_enleve_H = []
    return mur_enleve_V, mur_enleve_H


class Bordure :
    def __init__(self,jeu,skin):
        self.jeu = jeu
        self.skin = skin
        self.pos = [[0,0],[0,16],[1200,16],[0,720]]

    def Rendu_Bordure(self,surface):
        for i in range (0,1216,16):
            surface.blit(self.skin,(self.pos[0][0]+i, self.pos[0][1]))
            surface.blit(self.skin, (self.pos[3][0] + i, self.pos[3][1]))
        for i in range (0,704,16):
            surface.blit(self.skin, (self.pos[1][0], self.pos[1][1] + i))
            surface.blit(self.skin, (self.pos[2][0], self.pos[2][1] + i))

class Mur_Vert :
    def __init__(self,jeu,skin):
        self.jeu = jeu
        self.skin = skin
        self.pos = [48, 16]
        self.list_pos = []


    def yaMur(self):
        mat_Mur_v=[]
        for i in range(24):
            list = []
            for j in range(15):
                list.append(random.randint(0,1))
            mat_Mur_v.append(list)

        return mat_Mur_v


    def Rendu_Mur_vert(self,surface,path,mat_mur_v):
        path_v = path
        ya_Mur = mat_mur_v
        for i in range(24):
            for j in range(15):
                if ya_Mur[i][j] and (i,j) not in path_v:

                    self.pos = [48 + i * 48, 16 + j * 48]
                    surface.blit(self.skin, self.pos),surface.blit(self.skin,(self.pos[0],self.pos[1]+16))
                    self.list_pos.append(self.pos)


    def collision(self,obstacles):
        for pos in self.list_pos:
            obstacles.append(pygame.Rect(pos[0], pos[1], 16, 32))



class Mur_Hor :
    def __init__(self,jeu,skin):
        self.jeu = jeu
        self.skin = skin
        self.pos = [16, 48]
        self.list_pos = []


    def yaMur(self):
        mat_Mur_h=[]
        for i in range(25):
            list = []
            for j in range(14):
                list.append(random.randint(0,1))
            mat_Mur_h.append(list)

        return mat_Mur_h


    def Rendu_Mur_hor(self,surface,path,mat_mur_h):
        path_h = path
        ya_Mur = mat_mur_h
        for i in range(25):
            for j in range(14):
                if ya_Mur[i][j] and (i,j) not in path_h :
                    self.pos = [16 + i * 48, 48 + j * 48]
                    surface.blit(self.skin, self.pos),surface.blit(self.skin,(self.pos[0]+16,self.pos[1]))
                    self.list_pos.append(self.pos)

    def collision(self, obstacles):
        for pos in self.list_pos:
            obstacles.append(pygame.Rect(pos[0], pos[1], 32, 16))

class Mur :
    def __init__(self,jeu,skin):
        self.jeu = jeu
        self.skin = skin
        self.pos = [48,48]
        self.list_pos = []

    def Rendu_Mur(self,surface):
        for i in range(24):
            for j in range(14):
                self.pos = [48 + i * 48, 48 + j * 48]
                surface.blit(self.skin, self.pos)
                self.list_pos.append(self.pos)

    def collision(self, obstacles):
        for pos in self.list_pos:
            obstacles.append(pygame.Rect(pos[0], pos[1], 16, 16))

