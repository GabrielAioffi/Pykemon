import pygame, sys, random, moves
from menu import MainMenu

class Battle():
    def __init__(self,game,menu):
        #Importando as funções do jogo:
        self.game = game

        #Importando as funções do menu:
        self.menu = menu

        #Sprites da HUD:
        self.p1HP = pygame.image.load('data/Sprites/spritesHUD/barra_2.png')
        self.p2HP = pygame.image.load('data/Sprites/spritesHUD/barra_1.png')
        self.fightOpt = pygame.image.load('data/Sprites/spritesHUD/fgt_options.png')
        self.battleBg = pygame.image.load('data/Sprites/spritesHUD/FundoPokemon.png')
        self.attackBar = pygame.image.load('data/Sprites/spritesHUD/pp_bar.png')
        self.textBar = pygame.image.load('data/Sprites/spritesHUD/text_bar.png')
        self.noHP = pygame.image.load('data/Sprites/spritesHUD/barra_sem_vida.png')
        self.redHP = pygame.image.load('data/Sprites/spritesHUD/vida_vermelha.png')
        self.yellowHP = pygame.image.load('data/Sprites/spritesHUD/vida_amarela.png')

        #Efeitos sonoros:
        self.battleMusic = pygame.mixer.Sound('data/Sounds/batalha.wav')
        self.battleMusic.set_volume(0.2)

        pokemons = self.menu.definePokemons()

        pokemon1 = moves.playerPokemon(pokemons[0])
        pokemon2 = moves.playerPokemon(pokemons[1])

    #Desenhando os cenários do fundo de batalha:
    def battleBackground(self): 
        self.game.drawImage(self.battleBg, 400, 220)
        self.game.drawImage(self.textBar, 400, 520)
        self.game.drawImage(self.fightOpt, 600, 520)
        
        self.game.drawImage(pokemon1['backSprite'], 400, 400)
        self.game.drawImage(pokemon2['frontSprite'], 400, 220)
        self.game.drawText('O que irá fazer?', 40, 400, 300)

        print(pokemon1, pokemon2)

        pygame.display.update()