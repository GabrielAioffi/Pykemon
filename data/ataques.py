import random

class ataque():
    def __init__(self, Nome, Tipo, Poder, Precisao, PPatual, PP):
        self.Nome = Nome
        self.Tipo = Tipo
        self.Poder = Poder
        self.Precisao = Precisao
        self.PP = PP
        self.PPatual = PPatual

    def usar(self, falha_na_precisao, falha_na_defesa):
        if self.Poder == None:
            if self.Nome == 'Atq. Areia' or self.Nome == 'Onda Trovão' or self.Nome == 'Time Duplo':
                return 'Precisao', 0
            if self.Nome == 'Cauda Chcot.':
                return 'Defesa_adv', 0
            if self.Nome == 'Barreira':
                return 'Defesa_sua', 0
            if self.Nome == 'Rugir' or self.Nome == 'Meditação':
                return 'Ataque_seu', 0
            if self.Nome == 'Smnt. Prst.':
                return 'Turnos', 0

        dano = (26/125 * self.Poder + 2) * random.uniform(0.85, 1) * falha_na_defesa
        
        acertou = random.choices([True, False], weights = [self.Precisao - falha_na_precisao, 100 - (self.Precisao - falha_na_precisao)])[0]
        
        if acertou == False:
            return False, 0

        if self.Nome == 'Derrubada':
            dano = dano, 1/4 * dano
            return 'Derrubada', dano
        if self.Nome == 'Raio Solar':
            return 'Raio Solar', dano
        if self.Nome == 'Duplo Tapa':
            danos = []
            hits = random.randrange(2, 6)
            for hit in range(hits):
                dano = (26/125 * self.Poder + 2) * random.uniform(0.85, 1) * falha_na_defesa
                danos.append(dano)
            return 'Duplo Tapa', danos
        if self.Nome == 'Absorver':
            dano = dano[0], 1/2 * dano[0]
            return 'Absorver', dano

        if acertou == True:
            return True, dano

        #Formula do Dano tirada de https://bulbapedia.bulbagarden.net/wiki/Damage
        #Todos os Pokemons estao no nivel 21        