import pygame, random
from menu import MainMenu

#Criando a ID de cada pokémon através de um dicionário:
def playerPokemon(self, pokemon):
    #Sprites dos Pokémons:
    self.bulbaBack = pygame.image.load('data/Sprites/spritesPokemon/bulbassaurBack.png')
    self.bulbaFront = pygame.image.load('data/Sprites/spritesPokemon/bulbassaurFront.png')
    self.charBack = pygame.image.load('data/Sprites/spritesPokemon/charmanderBack.png')
    self.charFront = pygame.image.load('data/Sprites/spritesPokemon/charmanderFront.png')
    self.pidBack = pygame.image.load('data/Sprites/spritesPokemon/pidgeyBack.png')
    self.pidFront = pygame.image.load('data/Sprites/spritesPokemon/pidgeyFront.png')
    self.pikaFront = pygame.image.load('data/Sprites/spritesPokemon/pikachuFront.png')
    self.pikaBack = pygame.image.load('data/Sprites/spritesPokemon/pikachuBack.png')
    self.squiFront = pygame.image.load('data/Sprites/spritesPokemon/squirtleFront.png')
    self.squiBack = pygame.image.load('data/Sprites/spritesPokemon/squirtleBack.png')

    if pokemon == 1: #Bulbassaur
        return{
            'name': 'Bulbassaur',
            'frontSprite': self.bulbaFront,
            'backSprite': self.bulbaBack,
            'HP': 45,
            'attack': 49,
            'defense': 49,
            'moves': [Tackle, VineWhip]
        }
    elif pokemon == 2: #Charmander
        return{
            'name': 'Charmander',
            'frontSprite': self.charFront,
            'backSprite': self.charBack,
            'attack': 52,
            'defense': 43,
            'HP': 39,
            'moves': [Tackle, Ember]
        }
    elif pokemon == 3: #Pidgey            
        return{
            'name': 'Pidgey',
            'frontSprite': self.pidFront,
            'backSprite': self.pidBack,
            'HP': 40,
            'attack': 45,
            'defense': 40,
            'moves': [Tackle, Gust]
        }
    elif pokemon == 4: #Pikachu
        return{
            'name': 'Pikachu',
            'frontSprite': self.pikaFront,
            'backSprite': self.pikaBack,
            'HP': 35,
            'attack': 55,
            'defense': 40,
            'moves': [Tackle, ThunderShock]
        }
    elif pokemon == 5: #Squirtle
        return{
            'name': 'Squirtle',
            'frontSprite': self.squiFront,
            'backSprite': self.squiBack,
            'HP': 44,
            'attack': 48, 
            'defense': 65,
            'moves': [Tackle, WaterGun]
        }

class Move():
    def __init__(self,Name,Power):
        self.Name = Name
        self.Power = Power
        #self.Stats1 = playerPokemon(pokemons[0])
        #self.Stats2 = playerPokemon(pokemons[1])

        #atkStats = (self.Stats1['attack'], self.Stats2['attack'])
        #defStats = (self.Stats1['defense'], self.Stats2['defense'])

        #Define os pokémons no level 4:
        self.pokeLevel = 4
    
    #Função para calcular o valor do dano do ataque/move:
    def attack(self):
        damage = ((((2*self.pokeLevel/5)+2) * Power * (self.atkStats/self.defStats)/50)+2) * random.uniform(0.85,1)
        
        #Inserindo a opção de erro ou acerto para deixar "mais justo":
        miss = random.choices([True,False])
        if miss == True:
            return False, 0
        else:
            return True, damage

Tackle = Move('Tackle', 40)
VineWhip = Move('Vine Whip', 45)
Ember = Move('Ember', 40)
Gust = Move('Gust', 40)
ThunderShock = Move('Thunder Shock', 40)
WaterGun = Move('Water Gun', 40)
