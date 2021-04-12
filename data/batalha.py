import pygame, sys, random
from data.ataques import ataque


class Batalha():
    def __init__(self, Jogo):
        #Importa as Funções do Jogo
        self.Jogo = Jogo

        #Sprites da Interface
        self.s_fundo = pygame.image.load('data/Sprites/FundoPokemon.png')
        self.s_texto = pygame.image.load('data/Sprites/text_bar.png')
        self.s_ataques = pygame.image.load('data/Sprites/pp_bar.png')
        self.s_opcoes = pygame.image.load('data/Sprites/fgt_options.png')
        self.s_vidaadv = pygame.image.load('data/Sprites/barra_1.png')
        self.s_vidasua = pygame.image.load('data/Sprites/barra_2.png')
        self.s_semvida = pygame.image.load('data/Sprites/barra_sem_vida.png')
        self.s_vidaamarela = pygame.image.load('data/Sprites/vida_amarela.png')
        self.s_vidavermelha = pygame.image.load('data/Sprites/vida_vermelha.png')

        #Sprites da Batalha
        self.s_slam = pygame.image.load('data/Sprites/Slam.png')
        self.s_bite = pygame.image.load('data/Sprites/Bite.png')
        self.s_sand = pygame.image.load('data/Sprites/Sand.png')
        self.s_thunder = pygame.image.load('data/Sprites/Thunder.png')
        self.s_wave = pygame.image.load('data/Sprites/Wave.png')
        self.s_solar = pygame.image.load('data/Sprites/Solar_Beam.png')
        self.s_vine = pygame.image.load('data/Sprites/Vine_Whip.png')
        self.s_growl = pygame.image.load('data/Sprites/Growl.png')
        self.s_seed = pygame.image.load('data/Sprites/Seed.png')
        self.s_barrier = pygame.image.load('data/Sprites/Barrier.png')
        self.s_confusion = pygame.image.load('data/Sprites/Confusion.png')
        self.s_slap = pygame.image.load('data/Sprites/Slap.png')
        self.s_psybeam = pygame.image.load('data/Sprites/Psybeam.png')
        self.s_heal = pygame.image.load('data/Sprites/Heart.png')

        #Sons e Musicas
        self.m_selecionar = pygame.mixer.Sound('data/Sons/selecionar.wav')
        self.m_batalha = pygame.mixer.Sound('data/Sons/batalha.wav')
        self.m_vitoria = pygame.mixer.Sound('data/Sons/vitoria.wav')
        self.m_tackle = pygame.mixer.Sound('data/Sons/Tackle.wav')
        self.m_quick_atack = pygame.mixer.Sound('data/Sons/Quick_Attack.wav')
        self.m_bite = pygame.mixer.Sound('data/Sons/Bite.wav')
        self.m_thunder = pygame.mixer.Sound('data/Sons/Thunder.wav')
        self.m_wave = pygame.mixer.Sound('data/Sons/Wave.wav')
        self.m_double_team = pygame.mixer.Sound('data/Sons/Double_Team.wav')
        self.m_solar_beam = pygame.mixer.Sound('data/Sons/Solar_Beam.wav')
        self.m_vine_whip = pygame.mixer.Sound('data/Sons/Vine_Whip.wav')
        self.m_growl = pygame.mixer.Sound('data/Sons/Growl.wav')
        self.m_seed = pygame.mixer.Sound('data/Sons/Seed.wav')
        self.m_barrier = pygame.mixer.Sound('data/Sons/Barrier.wav')
        self.m_slap = pygame.mixer.Sound('data/Sons/Slap.wav')
        self.m_pysbeam = pygame.mixer.Sound('data/Sons/Psybeam.wav')
        self.m_heal = pygame.mixer.Sound('data/Sons/heal.wav')

        #Vidas
        self.Sua_Vida = 50
        self.Adv_Vida = 50

    def que_pokemon(self, Pok):
        #Converte o numero que representa o Pokemon para suas caracteristicas atraves de um dicionario
        if Pok == 1:
            return {
                'nome': "Eevee",
                'sprite_frente': pygame.image.load('data/Sprites/FEevee.png'),
                'sprite_costas': pygame.image.load('data/Sprites/CEevee.png'),
                'cor': (197,152,96),
                'ataques': [
                ataque('Investida', 'Normal', 40, 95, 35, 35),
                ataque('Atq. Rapido', 'Normal', 35, 100, 30, 30),
                ataque('Derrubada', 'Normal', 90, 85, 20, 20),
                ataque('Mordida', 'Sombrio', 60, 100, 10, 10),
                ataque('Atq. Areia', 'Terra', None, 100, 15, 15)]
            }
        if Pok == 2:
            return {
                'nome': "Pikachu",
                'sprite_frente': pygame.image.load('data/Sprites/FPikachu.png'),
                'sprite_costas': pygame.image.load('data/Sprites/CPikachu.png'),
                'cor': (238,215,77),
                'ataques': [
                ataque('Chq. Trovão', 'Elétrico', 40, 100, 30, 30),
                ataque('Onda Trovão', 'Elétrico', None, 90, 20, 20),
                ataque('Time Duplo', 'Normal', None, None, 15, 15),
                ataque('Batida', 'Normal', 80, 75, 20, 20),
                ataque('Cauda Chcot.', 'Normal', None, 100, 30, 30)]
            }
        if Pok == 3:
            return {
                'nome': "Bulbassauro",
                'sprite_frente': pygame.image.load('data/Sprites/FBulbassauro.png'),
                'sprite_costas': pygame.image.load('data/Sprites/CBulbassauro.png'),
                'cor': (139,203,182),
                'ataques': [
                ataque('Smnt. Prst.', 'Planta', None, 90, 10, 10),
                ataque('Raio Solar', 'Planta', 120, 100, 10, 10),
                ataque('Vinha Chcot.', 'Planta', 45, 100, 25, 25),
                ataque('Rugir', 'Normal', None, 100, 40, 40),
                ataque('Cauda Chcot.', 'Normal', None, 100, 30, 30)]
            }
        if Pok == 4:
            return {
                'nome': "Mr. Mime",
                'sprite_frente': pygame.image.load('data/Sprites/FMr.Mime.png'),
                'sprite_costas': pygame.image.load('data/Sprites/CMr.Mime.png'),
                'cor': (226,96,116),
                'ataques': [
                ataque('Barreira', 'Psíquico', None, 100, 20, 20),
                ataque('Confusão', 'Psíquico', 50, 100, 25, 25),
                ataque('Meditação', 'Psíquico', None, None, 40, 40),
                ataque('Duplo Tapa', 'Normal', 15, 85, 10, 10),
                ataque('Raio Psqc.', 'Psíquico', 65, 100, 20, 20)]
            }
        if Pok == 5:
            return {
                'nome': "Vileplume",
                'sprite_frente': pygame.image.load('data/Sprites/FVileplume.png'),
                'sprite_costas': pygame.image.load('data/Sprites/CVileplume.png'),
                'cor': (133,146,185),
                'ataques': [
                ataque('Absorver', 'Planta', 20, 100, 25, 25),
                ataque('Pó Venenoso', 'Venenoso', None, 75, 35, 35),
                ataque('Pó de Sono', 'Planta', None, 75, 15, 15),
                ataque('Aroma Doce', 'Normal', None, 100, 20, 20),
                ataque('Pétalas', 'Planta', 120, 100, 10, 10)]
            }

    def escrever_caixa_de_texto(self, texto, y, anima=True):
        #Escreve uma mensagem na caixa de texto da batalha        
        #A variavel anima diz se o texto tera animacao ou nao
        if anima == False:
            self.Jogo.escrever_texto(texto, 35, (255,255,255), 35, y, 'sup_esq')
        else:
            txt = ''
            for letra in texto:
                txt += letra
                self.Jogo.escrever_texto(txt, 35, (255,255,255), 35, y, 'sup_esq')

                pygame.display.update()
                pygame.time.delay(20)

    def escrever_ataques(self, qual='todos', cor=(0,0,0)):
        #Escreve os nomes do ataques do Pokemon do Jogador
        fonte = pygame.font.Font(self.Jogo.fonte1, 25)

        coords = [(25, 465), (25, 515), (275, 465), (275, 515)]

        if qual == 'todos':
            for x in self.Seu_Pokemon['ataques'][0:4]:
                ataque_superf = fonte.render(x.Nome, True, cor)
                ataque_rect = ataque_superf.get_rect()
                ataque_rect.topleft = coords[0]
                self.Jogo.janela.blit(ataque_superf, ataque_rect)
                coords.pop(0)
        else:
            for x in self.Seu_Pokemon['ataques'][qual:qual+1]:
                ataque_superf = fonte.render(x.Nome, True, cor)
                ataque_rect = ataque_superf.get_rect()
                ataque_rect.topleft = coords[qual]
                self.Jogo.janela.blit(ataque_superf, ataque_rect)
    
    def vida(self):
        #Calcula a vida e como está a barra de vida

        #Valores das Vidas
        if self.Pokemon_Adversario['vida_atual'] > self.Adv_Vida:
            self.Pokemon_Adversario['vida_atual'] -= 1
        if self.Pokemon_Adversario['vida_atual'] < self.Adv_Vida:
            self.Pokemon_Adversario['vida_atual'] += 1

        if self.Seu_Pokemon['vida_atual'] > self.Sua_Vida:
            self.Seu_Pokemon['vida_atual'] -= 1
        if self.Seu_Pokemon['vida_atual'] < self.Sua_Vida:
            self.Seu_Pokemon['vida_atual'] += 1
        
        #Cores das Barras de Vida
        if self.Seu_Pokemon['vida_atual'] > 25:
            self.Seu_Pokemon['vida_cor'] = (100,229,149)
        if self.Seu_Pokemon['vida_atual'] <= 25:
            self.Seu_Pokemon['vida_cor'] = (248,217,58)
        if self.Seu_Pokemon['vida_atual'] <= 10:
            self.Seu_Pokemon['vida_cor'] = (255,109,82)

        if self.Pokemon_Adversario['vida_atual'] > 25:
            self.Pokemon_Adversario['vida_cor'] = (100,229,149)
        if self.Pokemon_Adversario['vida_atual'] <= 25:
            self.Pokemon_Adversario['vida_cor'] = (248,217,58)
        if self.Pokemon_Adversario['vida_atual'] <= 10:
            self.Pokemon_Adversario['vida_cor'] = (255,109,82)
        
        #Larguras das Barras de Vida
        self.largura_adv = self.Pokemon_Adversario['vida_atual']/50 * 160
        self.largura_sua = self.Seu_Pokemon['vida_atual']/50 * 160
   
    def checar_vida(self):
        d1 = abs(self.Adv_Vida - self.Pokemon_Adversario['vida_atual'])
        d2 = abs(self.Sua_Vida - self.Seu_Pokemon['vida_atual'])
        if d1 < 1 and d2 < 1: self.vidas_certas = True
        else: self.vidas_certas = False

    def fundo_da_batalha(self, anima=True):
        #Dispõe todos os elementos do fundo da batalha em seu lugar
        self.Jogo.imprimir_imagem(self.s_fundo)
        self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
        self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], 200, 290)
        self.Jogo.imprimir_imagem(self.s_texto)
        self.Jogo.imprimir_imagem(self.s_opcoes)

        self.fundo_basico()

        self.escrever_caixa_de_texto("O quê fará", self.Cima, anima)
        self.escrever_caixa_de_texto(f"{self.Seu_Pokemon['nome']}?", self.Baixo, anima)
        pygame.display.update()

    def fundo_basico(self):
        self.vida()
        self.checar_vida()
        pygame.draw.rect(self.Jogo.janela, self.Seu_Pokemon['vida_cor'], (578, 338, self.largura_sua, 13))
        pygame.draw.rect(self.Jogo.janela, self.Pokemon_Adversario['vida_cor'], (172, 119, self.largura_adv, 13))
        self.Jogo.imprimir_imagem(self.s_vidasua)
        self.Jogo.imprimir_imagem(self.s_vidaadv)
        self.Jogo.escrever_texto(f"{self.Seu_Pokemon['vida_atual']}/50", 25, (0,0,0), 635, 357, 'sup_esq')
        self.Jogo.escrever_texto(f"{self.Pokemon_Adversario['vida_atual']}/50", 25, (0,0,0), 225, 137, 'sup_esq')

        self.Jogo.escrever_texto(self.Seu_Pokemon['nome'], 25, (0,0,0), 470, 292, 'sup_esq')
        self.Jogo.escrever_texto(self.Pokemon_Adversario['nome'], 25, (0,0,0), 60, 72, 'sup_esq')

    def animacoes(self, qual):
        def Investida():
            x = 200
            while x < 350:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x += 20
            
            self.m_tackle.play()

            while x > 200:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x -= 20

            for x in range(2):
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], 200, 290)

                self.fundo_basico()

                pygame.display.update()
                pygame.time.delay(300)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                pygame.display.update()
                pygame.time.delay(300)

        def Atq_Rapido():

            self.m_quick_atack.play()
            x = 200
            while x < 350:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x += 30

            while x > 200:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x -= 30

            for x in range(2):
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], 200, 290)

                self.fundo_basico()

                pygame.display.update()
                pygame.time.delay(300)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                pygame.display.update()
                pygame.time.delay(300)

        def Derrubada():
            x = 200
            while x > 50:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x -= 5

            while x < 200:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                self.Jogo.imprimir_imagem(self.s_slam, 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x += 25

            self.m_tackle.play()
            self.Jogo.imprimir_imagem(self.s_slam, 600, 180)
            pygame.display.update()

            for x in range(2):
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], 200, 290)

                self.fundo_basico()

                pygame.display.update()
                pygame.time.delay(300)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                pygame.display.update()
                pygame.time.delay(300)
        
        def Mordida():
            x = 200
            while x < 350:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x += 20
            
            self.m_bite.play()
            self.Jogo.imprimir_imagem(self.s_bite, 600, 180)
            pygame.display.update()

            while x > 200:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                self.Jogo.imprimir_imagem(self.s_bite, 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x -= 20

            for x in range(2):
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], 200, 290)

                self.fundo_basico()

                pygame.display.update()
                pygame.time.delay(300)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                pygame.display.update()
                pygame.time.delay(300)

        def Atq_Areia():
            x = 200
            while x > 100:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x -= 10

            while x < 200:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                self.Jogo.imprimir_imagem(self.s_sand, 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x += 30

            self.Jogo.imprimir_imagem(self.s_sand, 600, 180)
            self.m_tackle.play()
            pygame.display.update()

        def Chq_Trovao():
            self.m_thunder.play()
            self.Jogo.imprimir_imagem(self.s_thunder, 600, 80)
            pygame.display.update()
            pygame.time.delay(1000)

        def Onda_Trovao():
            self.m_wave.play()
            self.Jogo.imprimir_imagem(self.s_wave)
            self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], 200, 290)
            pygame.display.update()
            pygame.time.delay(1000)

        def Time_Duplo():
            x1, x2 = 200, 200
            while x1 < 350:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], x1, 290)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], x2, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x1 += 25
                x2 -= 25
            
            self.m_double_team.play()

            while x1 > 175:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], x1, 290)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], x2, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x1 -= 25
                x2 += 25

        def Batida():
            x = 200
            while x < 350:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x += 20
            
            self.m_tackle.play()
            self.Jogo.imprimir_imagem(self.s_slam, 600, 180)
            pygame.display.update()

            while x > 200:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], x, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                self.Jogo.imprimir_imagem(self.s_slam, 600, 180)

                self.fundo_basico()
                pygame.display.update()
                x -= 20

            for x in range(2):
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], 200, 290)

                self.fundo_basico()

                pygame.display.update()
                pygame.time.delay(300)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                pygame.display.update()
                pygame.time.delay(300)

        def Smnt_Prst1():
            x, y = 200, 290
            self.m_seed.play()
            while y > 220:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_seed, x, y)
                pygame.display.update()
                y -= 7 #11 frames
                x += 480/11
            pygame.time.delay(1000)            

        def Smnt_Prst2():
            x, y = 600, 180
            self.m_heal.play()
            while y < 350:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_heal, x, y)
                pygame.display.update()
                y += 14 #11 frames
                x -= 360/11
            pygame.time.delay(1000) 
        
        def Cauda_Chcot():
            for z in range(4):
                x = 200
                while x < 350:
                    self.Jogo.imprimir_imagem(self.s_fundo)
                    self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], x, 290)
                    self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)

                    self.fundo_basico()
                    pygame.display.update()
                    x += 60
                
                self.m_quick_atack.play()

                while x > 200:
                    self.Jogo.imprimir_imagem(self.s_fundo)
                    self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], x, 290)
                    self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)

                    self.fundo_basico()
                    pygame.display.update()
                    x -= 60

        def Raio_Solar1():
            y = 140
            self.m_solar_beam.play()
            while y < 290:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_solar, 200, y)
                pygame.display.update()
                y += 10
            pygame.time.delay(1000)

        def Raio_Solar2():
            x, y = 200, 290
            self.m_solar_beam.play()
            while y > 160:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_solar, x, y)
                pygame.display.update()
                y -= 10
                x += 400/11
            pygame.time.delay(1000)

        def Vinha_Chcot():
            x, y = 370, 190
            self.m_vine_whip.play()
            while y < 290:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_vine, x, y)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], 200, 290)
                pygame.display.update()
                y += 10 #11 frames
                x += 10
            pygame.time.delay(1000)

        def Rugir():
            x, y = 250, 315
            self.m_growl.play()
            while y > 0:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                self.Jogo.imprimir_imagem(self.s_growl, x, y)
                self.fundo_basico()
                pygame.display.update()
                y -= 18 #11 frames
                x += 540/11
            pygame.time.delay(1000)
        
        def Barreira():
            y = 510
            self.m_barrier.play()
            while y > 290:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                self.Jogo.imprimir_imagem(self.s_barrier, 200, y)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_texto)
                self.escrever_caixa_de_texto("Mr. Mime usou", self.Cima, False)
                self.escrever_caixa_de_texto("Barreira!", self.Baixo, False)
                y -= 4
                pygame.display.update()

        def Confusao():
            x, y = 200, 150
            self.m_solar_beam.play()
            while y < 450:
                self.Jogo.imprimir_imagem(self.s_confusion, x, y)
                self.Jogo.imprimir_imagem(self.s_texto)
                self.escrever_caixa_de_texto("Mr. Mime usou", self.Cima, False)
                self.escrever_caixa_de_texto("Confusão!", self.Baixo, False)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                self.fundo_basico()
                pygame.display.update()
                y += 7
                x += 28/3
        
        def Meditação():
            x, y = 600, 450
            self.m_solar_beam.play()
            while y > 150:
                self.Jogo.imprimir_imagem(self.s_confusion, x, y)
                self.Jogo.imprimir_imagem(self.s_texto)
                self.escrever_caixa_de_texto("Mr. Mime usou", self.Cima, False)
                self.escrever_caixa_de_texto("Meditação!", self.Baixo, False)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                self.fundo_basico()
                pygame.display.update()
                y -= 7
                x -= 28/3            

        def Duplo_Tapa():
            x = 550
            self.m_slap.play()
            while x < 650:
                self.Jogo.imprimir_imagem(self.s_fundo)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                self.fundo_basico()
                self.Jogo.imprimir_imagem(self.s_slap, x, 180)
                pygame.display.update()
                x += 10

        def Raio_Psqc():
            xp, yp = 200, 290
            xc, yc = 200, 150
            self.m_pysbeam.play()
            while yp > 0:
                self.Jogo.imprimir_imagem(self.s_confusion, xc, yc)
                self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], 200, 290)
                self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)
                self.Jogo.imprimir_imagem(self.s_psybeam, xp, yp)
                self.Jogo.imprimir_imagem(self.s_texto)
                self.escrever_caixa_de_texto("Mr. Mime usou", self.Cima, False)
                self.escrever_caixa_de_texto("Raio Psíquico!", self.Baixo, False)
                self.fundo_basico()
                pygame.display.update()
                yp -= 7
                xp += 280/11
                yc += 7
                xc += 28/3
            pygame.time.delay(1000)            
        
        if qual == "Investida": Investida()
        if qual == "Atq. Rapido": Atq_Rapido()
        if qual == "Derrubada": Derrubada()
        if qual == "Mordida": Mordida()
        if qual == "Atq. Areia": Atq_Areia()
        if qual == "Chq. Trovão": Chq_Trovao()
        if qual == "Onda Trovão": Onda_Trovao()
        if qual == "Time Duplo": Time_Duplo()
        if qual == "Batida": Batida()
        if qual == "Smnt. Prst.1": Smnt_Prst1()
        if qual == "Smnt. Prst.2": Smnt_Prst2()
        if qual == "Cauda Chcot.": Cauda_Chcot()
        if qual == "Raio Solar1": Raio_Solar1()
        if qual == "Raio Solar2": Raio_Solar2()
        if qual == "Vinha Chcot.": Vinha_Chcot()
        if qual == "Rugir": Rugir()
        if qual == "Barreira": Barreira()
        if qual == "Confusão": Confusao()
        if qual == "Meditação": Meditação()
        if qual == "Duplo Tapa": Duplo_Tapa()
        if qual == "Raio Psqc.": Raio_Psqc()

    def entrada_da_batalha(self, Seu_Pokemon, Pokemon_Adversario):
        #Definindo os Pokemons
        self.Seu_Pokemon = self.que_pokemon(Seu_Pokemon)
        self.Pokemon_Adversario = self.que_pokemon(Pokemon_Adversario)

        self.Seu_Pokemon['vida_atual'] = 50
        self.Pokemon_Adversario['vida_atual'] = 50
        self.Seu_Pokemon['falha_na_precisao'] = 0
        self.Pokemon_Adversario['falha_na_precisao'] = 0
        self.Seu_Pokemon['falha_na_defesa'] = 1
        self.Pokemon_Adversario['falha_na_defesa'] = 1

        self.Seu_Pokemon['ataques'].remove(random.choice(self.Seu_Pokemon['ataques']))
        self.Pokemon_Adversario['ataques'].remove(random.choice(self.Pokemon_Adversario['ataques']))

        if self.Pokemon_Adversario['nome'] == "Eevee" or self.Pokemon_Adversario['nome'] == "Vileplume": artigo = "Uma"
        else: artigo = "Um"

        #Coordenadas y para escrever o texto na caixa de texto
        self.Cima, self.Baixo = 460, 510

        #Animação de Entrada
        pygame.time.delay(100)
        self.m_batalha.play(-1)

        #Fundo Basico da Batalha
        self.Jogo.imprimir_imagem(self.s_fundo)
        self.Jogo.imprimir_imagem(self.s_texto)

        #Pokemon Adversario
        self.escrever_caixa_de_texto(f"{artigo} {self.Pokemon_Adversario['nome']} selvagem", self.Cima)
        self.escrever_caixa_de_texto(f"entra em cena!", self.Baixo)
        y = -40
        while y < 180:
            self.Jogo.imprimir_imagem(self.s_fundo)
            self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, y)
            y += 3
            pygame.display.update()

        pygame.time.delay(500)

        #Seu Pokemon
        self.Jogo.imprimir_imagem(self.s_texto)
        self.escrever_caixa_de_texto(f"Vai {self.Seu_Pokemon['nome']}!", self.Cima)
        y = 510
        while y > 290:
            self.Jogo.imprimir_imagem(self.s_fundo)
            self.Jogo.imprimir_imagem(self.Pokemon_Adversario['sprite_frente'], 600, 180)

            self.Jogo.imprimir_imagem(self.Seu_Pokemon['sprite_costas'], 200, y)
            self.Jogo.imprimir_imagem(self.s_texto)
            self.escrever_caixa_de_texto(f"Vai {self.Seu_Pokemon['nome']}!", self.Cima, False)
            y -= 3.8
            pygame.display.update()

        pygame.time.delay(100)
        
        #Iniciando a Batalha
        self.fundo_da_batalha()


    def loop(self, Seu_Pokemon, Pokemon_Adversario):
        #Introduz a Batalha
        self.entrada_da_batalha(Seu_Pokemon, Pokemon_Adversario)

        anima = False
        opcao = [1, 1]
        batalhando = True
        self.Seu_Pokemon['solar_beam'] = False, 0
        self.Seu_Pokemon['Turnos'], usado = False, False

        while batalhando:
            self.Jogo.checar_eventos()

            if self.Seu_Pokemon['solar_beam'][0] == True:
                self.Jogo.imprimir_imagem(self.s_texto)
                self.escrever_caixa_de_texto(f"{self.Seu_Pokemon['nome']} usou", self.Cima)
                self.escrever_caixa_de_texto("Raio Solar!", self.Baixo)
                self.animacoes("Raio Solar2")
                self.Adv_Vida -= self.Seu_Pokemon['solar_beam'][1]
                self.Seu_Pokemon['solar_beam'] = False, 0

            if self.Seu_Pokemon['Turnos'] == True and usado == False:
                self.Jogo.imprimir_imagem(self.s_texto)
                self.escrever_caixa_de_texto(f"A vida de {self.Pokemon_Adversario['nome']}", self.Cima)
                self.escrever_caixa_de_texto("foi sugada!", self.Baixo)
                self.Adv_Vida -= 3
                self.Sua_Vida += 3
                self.animacoes("Smnt. Prst.2")
                usado = True
                pygame.time.delay(500)

            #Checa se outra opção foi selecionada para tocar o efeito sonoro
            opcao_atual = opcao.copy()
            #Variavel que faz a animação do texto acontecer quando volta-se ao menu das opcoes
            Voltou_A_Opcoes = False

            #Reseta ao estado fundamental da tela para se alguma alteracao for feita
            self.fundo_da_batalha(anima)

            #Navega-se pelas opcoes de acao por uma lista com coordenadas x e y, que podem ser 1 ou 2
            if opcao == [1, 1]: self.Jogo.escrever_texto("LUTAR", 30, self.Seu_Pokemon['cor'], 495, 481, 'centro')
            if opcao == [1, 2]: self.Jogo.escrever_texto("POKÉMON", 30, self.Seu_Pokemon['cor'], 520, 543, 'centro')
            if opcao == [2, 1]: self.Jogo.escrever_texto("BOLSA", 30, self.Seu_Pokemon['cor'], 684, 481, 'centro')
            if opcao == [2, 2]: self.Jogo.escrever_texto("CORRER", 30, self.Seu_Pokemon['cor'], 696, 542, 'centro')
            
            #Muda a opcao selecionada
            if self.Jogo.cima: opcao[1] -= 1
            if self.Jogo.baixo: opcao[1] += 1
            if self.Jogo.direita: opcao[0] += 1
            if self.Jogo.esquerda: opcao[0] -= 1

            for x in range(2):
                if opcao[x] <= 0: opcao[x] = 1
                if opcao[x] >= 3: opcao[x] = 2

            #Efeito Sonoro
            if opcao != opcao_atual:
                self.m_selecionar.play()

            #Seleciona opcao atual
            if self.Jogo.ENTER and self.vidas_certas == True:
                self.m_selecionar.play()

                if opcao == [1, 1]: #LUTAR
                    self.Jogo.resetar_teclas()
                    menu_ataques = True

                    atq = [1, 1]
                    while menu_ataques:
                        self.Jogo.checar_eventos()

                        self.Jogo.imprimir_imagem(self.s_ataques)
                        self.escrever_ataques()

                        atq_atual = atq.copy()
                        #Navega-se pelos ataques por uma lista com coordenadas x e y, que podem ser 1 ou 2 (Indica-se o PP do ataque e seu Tipo)
                        if atq == [1, 1]: atq_selecionado = 0
                        if atq == [1, 2]: atq_selecionado = 1
                        if atq == [2, 1]: atq_selecionado = 2
                        if atq == [2, 2]: atq_selecionado = 3

                        self.escrever_ataques(atq_selecionado, self.Seu_Pokemon['cor'])
                        self.Jogo.escrever_texto(f"{self.Seu_Pokemon['ataques'][atq_selecionado].PPatual}/{self.Seu_Pokemon['ataques'][atq_selecionado].PP}", 25, (0,0,0), 720, 482, 'centro')
                        self.Jogo.escrever_texto(f"{self.Seu_Pokemon['ataques'][atq_selecionado].Tipo}", 25, (0,0,0), 558, 535, 'sup_esq')

                        #Muda o ataque selecionado
                        if self.Jogo.cima: atq[1] -= 1
                        if self.Jogo.baixo: atq[1] += 1
                        if self.Jogo.direita: atq[0] += 1
                        if self.Jogo.esquerda: atq[0] -= 1

                        for x in range(2):
                            if atq[x] <= 0: atq[x] = 1
                            if atq[x] >= 3: atq[x] = 2

                        #Efeito Sonoro
                        if atq != atq_atual:
                            self.m_selecionar.play()

                        #Seleciona opcao atual
                        if self.Jogo.ENTER:
                            self.m_selecionar.play()
                            self.Jogo.imprimir_imagem(self.s_texto)
                            pygame.display.update()

                            if self.Seu_Pokemon['ataques'][atq_selecionado].Nome == "Smnt. Prst.":
                                self.escrever_caixa_de_texto(f"{self.Seu_Pokemon['nome']} usou", self.Cima)
                                self.escrever_caixa_de_texto("Semente Parasita!", self.Baixo)                                
                            elif self.Seu_Pokemon['ataques'][atq_selecionado].Nome != "Raio Solar":
                                self.escrever_caixa_de_texto(f"{self.Seu_Pokemon['nome']} usou", self.Cima)
                                self.escrever_caixa_de_texto(f"{self.Seu_Pokemon['ataques'][atq_selecionado].Nome}!", self.Baixo)

                            self.Seu_Pokemon['ataques'][atq_selecionado].PPatual -= 1

                            acertou, dano = self.Seu_Pokemon['ataques'][atq_selecionado].usar(self.Seu_Pokemon['falha_na_precisao'], self.Seu_Pokemon['falha_na_defesa'])

                            if acertou == 'Precisao':
                                self.animacoes(self.Seu_Pokemon['ataques'][atq_selecionado].Nome)
                                self.Pokemon_Adversario['falha_na_precisao'] += 1
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto("A precisão de", self.Cima)
                                self.escrever_caixa_de_texto(f"{self.Pokemon_Adversario['nome']} caiu!", self.Baixo)
                                pygame.time.delay(1500)

                            if acertou == 'Defesa_adv':
                                self.animacoes(self.Seu_Pokemon['ataques'][atq_selecionado].Nome)
                                self.Pokemon_Adversario['falha_na_defesa'] += 0.1
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto("A defesa de", self.Cima)
                                self.escrever_caixa_de_texto(f"{self.Pokemon_Adversario['nome']} caiu!", self.Baixo)
                                pygame.time.delay(1500)

                            if acertou == 'Defesa_sua':
                                self.animacoes(self.Seu_Pokemon['ataques'][atq_selecionado].Nome)
                                self.Seu_Pokemon['falha_na_defesa'] -= 0.1
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto("A defesa de", self.Cima)
                                self.escrever_caixa_de_texto(f"{self.Seu_Pokemon['nome']} subiu!", self.Baixo)
                                pygame.time.delay(1500)

                            if acertou == 'Ataque_seu':
                                self.animacoes(self.Seu_Pokemon['ataques'][atq_selecionado].Nome)
                                self.Pokemon_Adversario['falha_na_defesa'] += 0.1
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto("O ataque de", self.Cima)
                                self.escrever_caixa_de_texto(f"{self.Seu_Pokemon['nome']} subiu!", self.Baixo)
                                pygame.time.delay(1500)                         

                            if acertou == 'Turnos':
                                self.animacoes("Smnt. Prst.1")
                                self.Seu_Pokemon['Turnos'] = True
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto(f"{self.Pokemon_Adversario['nome']} foi", self.Cima)
                                self.escrever_caixa_de_texto("semeado!", self.Baixo)
                                pygame.time.delay(1500)

                            if acertou == 'Derrubada':
                                self.animacoes('Derrubada')
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.Adv_Vida -= dano[0]
                                self.Sua_Vida -= dano[1]
                                self.escrever_caixa_de_texto("Parte do dano", self.Cima)
                                self.escrever_caixa_de_texto("rebateu!", self.Baixo)
                                pygame.time.delay(3000)

                            if acertou == 'Raio Solar':
                                self.animacoes("Raio Solar1")
                                self.Seu_Pokemon['solar_beam'] = True, dano
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto(f"{self.Seu_Pokemon['nome']} carrega", self.Cima)
                                self.escrever_caixa_de_texto("o ataque!", self.Baixo)
                                pygame.time.delay(1500)

                            if acertou == 'Duplo Tapa':
                                for hit in range(len(dano)):
                                    self.animacoes("Duplo Tapa")
                                    self.Adv_Vida -= dano[hit]
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto(f"Acertou {len(dano)} vezes!", self.Cima)
                                pygame.time.delay(1500)  


                            if acertou == True:
                                self.animacoes(self.Seu_Pokemon['ataques'][atq_selecionado].Nome)
                                self.Adv_Vida -= dano

                            elif acertou == False:
                                pygame.time.delay(1000)
                                self.Jogo.imprimir_imagem(self.s_texto)
                                self.escrever_caixa_de_texto(f"{self.Seu_Pokemon['nome']} errou", self.Cima)
                                self.escrever_caixa_de_texto("o ataque!", self.Baixo)
                                pygame.display.update()
                                pygame.time.delay(1500)
                            
                            pygame.time.delay(10)
                            Voltou_A_Opcoes = True
                            menu_ataques = False
                            usado = False
                        #Volta ao menu das opcoes de acao
                        if self.Jogo.ESC:
                            Voltou_A_Opcoes = True
                            self.m_selecionar.play()
                            menu_ataques = False

                        pygame.display.update()
                        self.Jogo.resetar_teclas()

                if opcao == [2, 2]: #CORRER
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.Jogo.resetar_teclas()

            #Realiza a animacao de escrever caso o jogador volte ao menu de opcoes de acao
            anima = True
            if Voltou_A_Opcoes: continue
            anima = False