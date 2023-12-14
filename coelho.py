# Um programa que simula um coelho realista muito puto fazendo bruxaria

# Importar as bibliotecas necessárias
import random
import time

# Definir as variáveis globais
coelho = "🐰" # O símbolo do coelho
cenoura = "🥕" # O símbolo da cenoura
caldeirao = "🍲" # O símbolo do caldeirão
magia = "✨" # O símbolo da magia
raiva = "😡" # O símbolo da raiva
predadores = ["🐺", "🐍", "🦅", "🐱"] # A lista dos símbolos dos predadores
ingredientes = ["🌿", "🍄", "🌰", "🍎", "🌼", "🌙", "🔥", "💧"] # A lista dos símbolos dos ingredientes
feitiços = ["🤢", "🤮", "🤕", "🤒", "🥶", "🥵", "😴", "😵"] # A lista dos símbolos dos feitiços
objetivos = ["🏠", "🌳", "🌎", "🌞", "🌈", "🌠", "👫", "👑"] # A lista dos símbolos dos objetivos

# Definir a classe Coelho
class Coelho:

    # Inicializar o coelho com seus atributos
    def __init__(self, nome, cor, fome, sede, saude, humor):
        self.nome = nome # O nome do coelho
        self.cor = cor # A cor do coelho
        self.fome = fome # O nível de fome do coelho (0 a 100)
        self.sede = sede # O nível de sede do coelho (0 a 100)
        self.saude = saude # O nível de saúde do coelho (0 a 100)
        self.humor = humor # O nível de humor do coelho (0 a 100)

    # Definir o método que mostra o estado do coelho
    def mostrar_estado(self):
        print(f"Nome: {self.nome}")
        print(f"Cor: {self.cor}")
        print(f"Fome: {self.fome}")
        print(f"Sede: {self.sede}")
        print(f"Saúde: {self.saude}")
        print(f"Humor: {self.humor}")

    # Definir o método que faz o coelho comer uma cenoura
    def comer_cenoura(self):
        global cenoura
        print(f"{coelho} {self.nome} come uma {cenoura}.")
        self.fome -= 10 # Reduzir o nível de fome em 10
        self.sede += 5 # Aumentar o nível de sede em 5
        self.saude += 5 # Aumentar o nível de saúde em 5
        self.humor += 5 # Aumentar o nível de humor em 5
        time.sleep(1) # Esperar 1 segundo

    # Definir o método que faz o coelho beber água
    def beber_agua(self):
        print(f"{coelho} {self.nome} bebe água.")
        self.sede -= 10 # Reduzir o nível de sede em 10
        self.fome += 5 # Aumentar o nível de fome em 5
        self.saude += 5 # Aumentar o nível de saúde em 5
        self.humor += 5 # Aumentar o nível de humor em 5
        time.sleep(1) # Esperar 1 segundo

    # Definir o método que faz o coelho se curar
    def se_curar(self):
        print(f"{coelho} {self.nome} se cura.")
        self.saude += 10 # Aumentar o nível de saúde em 10
        self.fome += 10 # Aumentar o nível de fome em 10
        self.sede += 10 # Aumentar o nível de sede em 10
        self.humor += 10 # Aumentar o nível de humor em 10
        time.sleep(1) # Esperar 1 segundo

    # Definir o método que faz o coelho se divertir
    def se_divertir(self):
        print(f"{coelho} {self.nome} se diverte.")
        self.humor += 10 # Aumentar o nível de humor em 10
        self.fome += 10 # Aumentar o nível de fome em 10
        self.sede += 10 # Aumentar o nível de sede em 10
        self.saude -= 5 # Reduzir o nível de saúde em 5
        time.sleep(1) # Esperar 1 segundo

    # Definir o método que faz o coelho fazer bruxaria
    def fazer_bruxaria(self):
        global caldeirao, magia, raiva, predadores, ingredientes, feitiços, objetivos
        print(f"{coelho} {self.nome} faz bruxaria.")
        self.humor -= 10 # Reduzir o nível de humor em 10
        self.fome += 10 # Aumentar o nível de fome em 10
        self.sede += 10 # Aumentar o nível de sede em 10
        self.saude -= 10 # Reduzir o nível de saúde em 10
        alvo = random.choice(predadores) # Escolher um alvo aleatório entre os predadores
        ingrediente = random.choice(ingredientes) # Escolher um ingrediente aleatório entre os ingredientes
        feitico = random.choice(feitiços) # Escolher um feitiço aleatório entre os feitiços
        objetivo = random.choice(objetivos) # Escolher um objetivo aleatório entre os objetivos
        print(f"{coelho} {self.nome} coloca {ingrediente} no {caldeirao}.")
        print(f"{coelho} {self.nome} diz um encantamento.")
        print(f"{magia} {magia} {magia}")
        print(f"{coelho} {self.nome} lança {feitico} em {alvo}.")
        print(f"{alvo} fica {feitico}.")
        print(f"{coelho} {self.nome} fica {raiva}.")
        print(f"{coelho} {self.nome} quer {objetivo}.")
        time.sleep(1) # Esperar 1 segundo

# Criar um coelho realista muito puto
coelho_puto = Coelho("Puto", "Branco", 50, 50, 50, 0)

# Mostrar o estado do coelho
coelho_puto.mostrar_estado()

# Fazer o coelho fazer bruxaria 10 vezes
for i in range(10):
    coelho_puto.fazer_bruxaria()

# Mostrar o estado do coelho
coelho_puto.mostrar_estado()
