import pygame, sys
from menu import MainMenu
from battle import Battle

class Game():
    #Função Construtora
    def __init__(self):
        #Inicia o pygame:
        pygame.init()
        
        #Define que o jogo está rodando:
        self.running, self.playing = True , False

        #Define as teclas como falso para alterações futuras:
        self.upKey,self.downKey,self.leftKey,self.rightKey,self.escKey,self.enterKey = False, False, False, False, False, False

        #Define as dimensões da tela
        self.scrWidth,self.scrHeight = 800,600
        
        #Atribuindo a tela à algumas variáveis:
        self.display = pygame.Surface((self.scrWidth,self.scrHeight))
        self.window = pygame.display.set_mode((self.scrWidth,self.scrHeight))
        pygame.display.set_caption('Pykemon do José')
        pygame.display.set_icon(pygame.image.load('data/Sprites/pykemonLogo.png'))

        #Atribuindo a fonte à uma variável:
        self.textFont = 'data/Font/joystix_monospace.ttf'

        #Pegando as classes dos outros arquivos e deixando-as em uma variável
        self.scrMenu = MainMenu(self)
        self.scrBattle = Battle(self, self.scrMenu)

    #Função para checar os eventos:
    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.currMenu.runDisplay = False
                if self.running == False:
                    pygame.quit()
                    break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.enterKey = True
                if event.key == pygame.K_ESCAPE:
                    self.escKey = True
                if event.key == pygame.K_UP:
                    self.upKey = True
                if event.key == pygame.K_DOWN:
                    self.downKey = True
                if event.key == pygame.K_LEFT:
                    self.leftKey = True
                if event.key == pygame.K_RIGHT:
                    self.rightKey = True

    #Função para resetar o boolean das teclas:
    def resetKeys(self):
        self.enterKey,self.escKey,self.upKey,self.downKey,self.leftKey,self.rightKey = False,False,False,False,False,False
    
    #Função para criar o texto:
    def drawText(self,text,size,x,y):
        font = pygame.font.Font(self.textFont,size)
        textSurface = font.render(text,True,(255,255,255))
        textRect = textSurface.get_rect()
        textRect.center = (x,y)
        self.display.blit(textSurface,textRect)
    
    #Função para inserir as imagens:
    def drawImage(self,image,x,y):
        imageRect = image.get_rect()
        imageRect.center = (x,y)
        self.window.blit(image,imageRect)
        
    #Função para o Looping do jogo:
    def gameLoop(self):

        #While para o menu
        while self.running:
            if len(self.scrMenu.pokemons) == 2:
                self.scrMenu.menuMusic.stop()
                break
            self.checkEvents()
            self.window.blit(self.display,(0,0))
            self.scrMenu.displayMenu()
    
        #While para a batalha
        if len(self.scrMenu.pokemons) == 2:
            while self.running:
                self.checkEvents()
                self.display.fill((0,0,0))
                self.scrBattle.battleBackground()
                pygame.display.update()

        self.window.blit(self.display,(0,0))
        pygame.display.update()
        self.resetKeys()