import pygame, sys
from data.menu import *
from data.batalha import *


class Jogo:
    def __init__(self):
        #Configuração Geral
        pygame.init()
        self.rodando = True

        #Importa o Menu para o Jogo
        self.menu = Menu(self)

        #Importa a Batalha para o Jogo
        self.batalha = Batalha(self)

        #Configurando a Janela
        self.largura, self.altura = 800, 600
        self.janela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption('Pokémon')
        pygame.display.set_icon(pygame.image.load('data/Sprites/pokeball.png'))

        #Definindo o Nome da Fonte e as Teclas Usadas
        self.fonte1 = 'data/Fontes/joystix_monospace.ttf'
        self.fonte2 = 'data/Fontes/pokemon_fire_red.ttf'
        self.ENTER, self.cima, self.baixo, self.esquerda, self.direita, self.ESC = False, False, False, False, False, False

    def checar_eventos(self):
        for event in pygame.event.get():

            #Fecha o Jogo se o Usuario Aperta o X
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Avisa se as Teclas de Ação são pressionadas
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: self.ENTER = True
                if event.key == pygame.K_UP: self.cima = True
                if event.key == pygame.K_DOWN: self.baixo = True
                if event.key == pygame.K_LEFT: self.esquerda = True
                if event.key == pygame.K_RIGHT: self.direita = True
                if event.key == pygame.K_ESCAPE: self.ESC = True

    def resetar_teclas(self):
        #Reseta as Teclas de Ação
        self.ENTER, self.cima, self.baixo, self.esquerda, self.direita, self.ESC = False, False, False, False, False, False

    def escrever_texto(self, texto, tamanho, cor, x, y, orientacao):
        #Escreve texto com suas determinadas caracteristicas
        fonte = pygame.font.Font(self.fonte1, tamanho)
        texto_superf = fonte.render(texto, True, (cor))
        texto_rect = texto_superf.get_rect()
        if orientacao == 'centro': texto_rect.center = (x,y)
        if orientacao == 'sup_esq': texto_rect.topleft = (x,y)
        if orientacao == 'esq': texto_rect.midleft = (x,y)
        self.janela.blit(texto_superf, texto_rect)

        #Retorna as coordenadas do retangulo para a localizacao das pokebolas na selecao de pokemon em menu.escolher_pokemons
        return texto_rect

    def imprimir_imagem(self, imagem, x=400, y=300):
        #Imprime na tela imagem com suas determinadas coordenadas 
        imagem_rect = imagem.get_rect()
        imagem_rect.center = (x,y)
        self.janela.blit(imagem, imagem_rect)

    def loop(self):
        #Abre o Menu do Jogo e pega os Pokémons do jogo
        Seu_Pokemon, Pokemon_Adversario = self.menu.main_menu()

        self.batalha.loop(Seu_Pokemon, Pokemon_Adversario)

        while self.rodando:
            self.checar_eventos()
            self.janela.fill((0,0,0))

            pygame.display.update()
            self.resetar_teclas()