import pygame

class Menu():
    def __init__(self,game):
        #Linka o menu.py com o game.py:
        self.game = game

        #Variáveis para as posições dos botões a fim de facilitar a leitura:
        self.midWidth, self.midHeight = self.game.scrWidth//1.95, self.game.scrHeight//2

        #Define a boolean do menu:
        self.runDisplay = True

        #Define o retângulo do cursor:
        self.cursorRect = pygame.Rect(0,0,20,20)

        #Offset do cursor:
        self.offset = -200

        #Efeitos Sonoros:
        self.enterSFX = pygame.mixer.Sound('data/Sounds/menuEnter.wav')
        self.cursorSFX = pygame.mixer.Sound('data/Sounds/menuSelection.wav')
        self.menuMusic = pygame.mixer.Sound('data/Sounds/menuMusic.wav')

    def drawCursor(self):
        self.game.drawText('#',40,self.cursorRect.x,self.cursorRect.y)
    
    def scrBlit(self):
        self.game.window.blit(self.game.display,(0,0))
        pygame.display.update()
        self.game.resetKeys()

class MainMenu(Menu):
    def __init__(self, game):
        #Definindo as coordenadas das opções do menu:
        Menu.__init__(self, game)
        self.state = "Bulbassaur"
        self.poke1X, self.poke1Y = self.midWidth,self.midHeight - 120
        self.poke2X, self.poke2Y = self.midWidth,self.midHeight - 40
        self.poke3X, self.poke3Y = self.midWidth,self.midHeight + 40
        self.poke4X, self.poke4Y = self.midWidth,self.midHeight + 120
        self.poke5X, self.poke5Y = self.midWidth,self.midHeight + 200
        self.cursorRect.midtop = (self.poke1X + self.offset, self.poke1Y)

        #Lista que pega os 2 pokemons selecionados:
        self.pokemons = []  

  
    #Função para mover o cursor entre as opções:
    def moveCursor(self):
        if self.game.downKey:
            if self.state == 'Bulbassaur':
                self.cursorRect.midtop = (self.poke2X + self.offset, self.poke2Y)
                self.state = 'Charmander'
                self.cursorSFX.play()
            elif self.state == 'Charmander':
                self.cursorRect.midtop = (self.poke3X + self.offset, self.poke3Y)
                self.state = 'Pidgey'
                self.cursorSFX.play()
            elif self.state == 'Pidgey':
                self.cursorRect.midtop = (self.poke4X + self.offset, self.poke4Y)
                self.state = 'Pikachu'
                self.cursorSFX.play()
            elif self.state == 'Pikachu':
                self.cursorRect.midtop = (self.poke5X + self.offset, self.poke5Y)
                self.state = 'Squirtle'
                self.cursorSFX.play()
            elif self.state == 'Squirtle':
                self.cursorRect.midtop = (self.poke1X + self.offset, self.poke1Y)
                self.state = 'Bulbassaur'
                self.cursorSFX.play()
        elif self.game.upKey:
            if self.state == 'Bulbassaur':
                self.cursorRect.midtop = (self.poke5X + self.offset, self.poke5Y)
                self.state = 'Squirtle'
                self.cursorSFX.play()
            elif self.state == 'Charmander':
                self.cursorRect.midtop = (self.poke1X + self.offset, self.poke1Y)
                self.state = 'Bulbassaur'
                self.cursorSFX.play()
            elif self.state == 'Pidgey':
                self.cursorRect.midtop = (self.poke2X + self.offset, self.poke2Y)
                self.state = 'Charmander'
                self.cursorSFX.play()
            elif self.state == 'Pikachu':
                self.cursorRect.midtop = (self.poke3X + self.offset, self.poke3Y)
                self.state = 'Pidgey'
                self.cursorSFX.play()
            elif self.state == 'Squirtle':
                self.cursorRect.midtop = (self.poke4X + self.offset, self.poke4Y)
                self.state = 'Pikachu'
                self.cursorSFX.play()
    
    #Função para escolher o pokémon:
    def checkInput(self):
        self.moveCursor()
        if self.game.enterKey:
            self.enterSFX.play()
            if self.state == 'Bulbassaur':
                self.pokemons.append(1)
            elif self.state == 'Charmander':
                self.pokemons.append(2)
            elif self.state == 'Pidgey':
                self.pokemons.append(3)
            elif self.state == 'Pikachu':
                self.pokemons.append(4)
            elif self.state == 'Squirtle':
                self.pokemons.append(5)
        
    #Mostrando o texto das opções do menu:
    def displayMenu(self):
        self.menuMusic.play(-1)
        while len(self.pokemons) < 2:
            self.game.checkEvents()
            self.checkInput()
            self.game.display.fill(((0,0,0)))
            self.game.drawText('Select your Pokémon!', 40, self.game.scrWidth//2, 50)
            self.game.drawText('Bulbassaur', 40, self.poke1X,self.poke1Y)
            self.game.drawText('Charmander', 40, self.poke2X,self.poke2Y)
            self.game.drawText('Pidgey', 40, self.poke3X,self.poke3Y)
            self.game.drawText('Pikachu', 40, self.poke4X,self.poke4Y)
            self.game.drawText('Squirtle', 40, self.poke5X,self.poke5Y)
            self.drawCursor()
            self.scrBlit()
            print(self.pokemons)
    
    def definePokemons(self):
        global pokemons
        pokemons = self.pokemons
        return pokemons



    
    
    
