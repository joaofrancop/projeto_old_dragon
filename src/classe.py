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

    def descrever_classe(self):
        """Descreve as principais características da classe."""
        desc = [
            f"Nome: {self.nome}",
            f"PV Inicial: {self.pv_inicial} + modificador de CON",
            f"Dado de Vida (pós 1º nível): 1d{self.dado_vida}",
            f"Base de Ataque (1º nível): {self.ba}",
            f"Jogada de Proteção (1º nível): {self.jp_inicial}",
            f"Proficiências: {', '.join(self.proficiencias)}",
            f"Habilidades: {', '.join(self.habilidades)}"
        ]
        return "\n".join(desc)


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