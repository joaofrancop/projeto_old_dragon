# model/classe.py

class Classe:
    """Classe base para todas as classes de personagem."""
    def __init__(self):
        self.nome = "Base"
        self.pv_inicial = 0
        self.dado_vida = 0
        self.ba = 0
        self.jp_inicial = 0
        self.proficiencias = []
        self.habilidades = []

    def to_dict(self):
        """Converte a classe para um dicionário."""
        return {
            "nome": self.nome,
            "pv_inicial": self.pv_inicial,
            "dado_vida": self.dado_vida,
            "ba": self.ba,
            "jp_inicial": self.jp_inicial,
            "proficiencias": self.proficiencias,
            "habilidades": self.habilidades
        }


class Guerreiro(Classe):
    """Classe Guerreiro, baseada no Livro I, pág. 28."""
    def __init__(self):
        super().__init__()
        self.nome = "Guerreiro"
        self.pv_inicial = 10
        self.dado_vida = 10
        self.ba = 1
        self.jp_inicial = 5
        self.proficiencias = ["Todas as Armas", "Todas as Armaduras"]
        self.habilidades = ["Aparar", "Maestria em Arma", "Ataque Extra"]


class Clerigo(Classe):
    """Classe Clérigo, baseada no Livro I, pág. 32."""
    def __init__(self):
        super().__init__()
        self.nome = "Clérigo"
        self.pv_inicial = 8
        self.dado_vida = 8
        self.ba = 1
        self.jp_inicial = 5
        self.proficiencias = ["Armas Impactantes", "Todas as Armaduras"]
        self.habilidades = ["Magias Divinas", "Afastar Mortos-Vivos", "Cura Milagrosa"]


class Ladrao(Classe):
    """Classe Ladrão, baseada no Livro I, pág. 36."""
    def __init__(self):
        super().__init__()
        self.nome = "Ladrão"
        self.pv_inicial = 6
        self.dado_vida = 6
        self.ba = 1
        self.jp_inicial = 5
        self.proficiencias = ["Armas Pequenas ou Médias", "Armaduras Leves"]
        self.habilidades = ["Ataque Furtivo", "Ouvir Ruídos", "Talentos de Ladrão"]


class Mago(Classe):
    """Classe Mago, baseada no Livro I, pág. 42."""
    def __init__(self):
        super().__init__()
        self.nome = "Mago"
        self.pv_inicial = 4
        self.dado_vida = 4
        self.ba = 0
        self.jp_inicial = 5
        self.proficiencias = ["Armas Pequenas", "Nenhuma Armadura"]
        self.habilidades = ["Magias Arcanas", "Grimório", "Ler Magias", "Detectar Magias"]