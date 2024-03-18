import pygame as pg
from pygame.math import Vector2
from dados_inimigos import dados_inimigos


class Inimigo(pg.sprite.Sprite):
    def __init__(self, tipo_inimigo, caminhos, imagens):
        pg.sprite.Sprite.__init__(self)
        self.caminhos = caminhos
        self.pos = Vector2(self.caminhos[0])
        self.target_caminho = 1
        self.vida = dados_inimigos.get(tipo_inimigo)['hp']
        self.dano = dados_inimigos.get(tipo_inimigo)['dano']
        self.velocidade = dados_inimigos.get(tipo_inimigo)['velocidade']
        self.valor = dados_inimigos.get(tipo_inimigo)['valor']
        self.forca = dados_inimigos.get(tipo_inimigo)
        self.image = imagens.get(tipo_inimigo)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self, mundo):
        self.andar(mundo)   
        self.checa_vida(mundo)
    
    def andar(self, mundo):
        if self.target_caminho < len(self.caminhos):
            self.target = Vector2(self.caminhos[self.target_caminho])
            self.movimento = self.target - self.pos
        else:
            #inimigo chegou ao fim do caminho
            self.kill()
            mundo.vida -= self.dano
            mundo.inimigos_passaram += 1
    
    def checa_vida(self, mundo):
        if self.vida <= 0:
            mundo.inimigos_mortos += 1
            self.kill()
            mundo.dinheiro += self.valor 
        
        
            
        
        #calculando distancia até o alvo
        dist = self.movimento.length()
        #checando se a distancia é menor que a velocidade de movimento
        if dist >= (self.velocidade * mundo.velocidade_nivel):
            self.pos += self.movimento.normalize() * (self.velocidade * mundo.velocidade_nivel)
        else:
            if dist!= 0:
                self.pos += self.movimento.normalize() * dist
            self.target_caminho += 1
        self.rect.center = self.pos