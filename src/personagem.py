# src/personagem.py

class Personagem:
    """
    Representa um personagem com seus atributos básicos, raça e classe.
    """
    def __init__(self, raca, classe, forca=0, destreza=0, constituicao=0, inteligencia=0, sabedoria=0, carisma=0):
        self.raca = raca
        self.classe = classe
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma

    def exibir_atributos(self):
        """
        Exibe a ficha completa do personagem.
        """
        print("--- FICHA DO PERSONAGEM ---")
        print(f"Raça: {self.raca.nome}")
        print(f"Classe: {self.classe.nome}")
        print("-" * 25)
        print("Atributos:")
        print(f"Força: {self.forca}")
        print(f"Destreza: {self.destreza}")
        print(f"Constituição: {self.constituicao}")
        print(f"Inteligência: {self.inteligencia}")
        print(f"Sabedoria: {self.sabedoria}")
        print(f"Carisma: {self.carisma}")
        print("-" * 25)
        print("Detalhes da Raça:")
        print(f"Movimento: {self.raca.movimento}m")
        print(f"Infravisão: {self.raca.infravisao}")
        print(f"Alinhamento: {self.raca.alinhamento}")
        print(f"Habilidades Especiais:\n{self.raca.descrever_habilidades()}")
        print("-" * 25)
        print("Detalhes da Classe (1º Nível):")
        print(self.classe.descrever_classe())
        print("-" * 25)