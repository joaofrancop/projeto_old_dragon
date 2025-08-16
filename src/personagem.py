# src/personagem.py

class Personagem:
    """
    Representa um personagem com seus atributos básicos.
    """
    def __init__(self, forca=0, destreza=0, constituicao=0, inteligencia=0, sabedoria=0, carisma=0):
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma

    def exibir_atributos(self):
        """
        Exibe os atributos do personagem de forma formatada.
        """
        print("Atributos do Personagem:")
        print(f"Força: {self.forca}")
        print(f"Destreza: {self.destreza}")
        print(f"Constituição: {self.constituicao}")
        print(f"Inteligência: {self.inteligencia}")
        print(f"Sabedoria: {self.sabedoria}")
        print(f"Carisma: {self.carisma}")