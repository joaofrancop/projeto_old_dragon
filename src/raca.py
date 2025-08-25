class Raca:
    """Classe base para todas as raças de personagem.
    Define características comuns e a estrutura das habilidades.
    """
    def __init__(self):
        self.nome = "Base"
        self.movimento = 0
        self.infravisao = "Não"
        self.alinhamento = "Qualquer"

    def descrever_habilidades(self):
        """Descreve as habilidades especiais da raça."""
        return "Nenhuma habilidade especial."


class Humano(Raca):
    """Raça Humano, baseada no Livro I, pág. 18.
    Os mais comuns, versáteis e adaptáveis.
    """
    def __init__(self):
        super().__init__()
        self.nome = "Humano"
        self.movimento = 9  # metros
        self.infravisao = "Não"
        self.alinhamento = "Qualquer"

    def descrever_habilidades(self):
        habilidades = [
            "Aprendizado: Bônus de 10% sobre toda experiência (XP) recebida.",
            "Adaptabilidade: Recebe um bônus de +1 em uma única Jogada de Proteção (JP) à sua escolha."
        ]
        return "\n".join(habilidades)


class Elfo(Raca):
    """Raça Elfo, baseada no Livro I, pág. 20.
    Longevos, misteriosos e graciosos habitantes das florestas.
    """
    def __init__(self):
        super().__init__()
        self.nome = "Elfo"
        self.movimento = 9  # metros
        self.infravisao = "18 metros"
        self.alinhamento = "Tendência à neutralidade"

    def descrever_habilidades(self):
        habilidades = [
            "Percepção Natural: Detecta portas secretas com 1-2 em 1d6 se procurando.",
            "Graciosos: Bônus de +1 em qualquer teste de JPD.",
            "Arma Racial: Bônus de +1 nos danos causados com arcos.",
            "Imunidades: Imune a efeitos de sono e paralisia de Ghoul."
        ]
        return "\n".join(habilidades)


class Anao(Raca):
    """Raça Anão, baseada no Livro I, pág. 22.
    Orgulhosos habitantes dos salões sob a montanha.
    """
    def __init__(self):
        super().__init__()
        self.nome = "Anão"
        self.movimento = 6  # metros
        self.infravisao = "18 metros"
        self.alinhamento = "Tendência à ordem"

    def descrever_habilidades(self):
        habilidades = [
            "Mineradores: Detecta anomalias em pedras com 1-2 em 1d6 se procurando.",
            "Vigoroso: Bônus de +1 em qualquer teste de JPC.",
            "Restrição de Armas: Restrito a armas médias e pequenas. Armas grandes forjadas como item anão são consideradas médias.",
            "Inimigos: Ataques contra orcs, ogros e hobgoblins são fáceis."
        ]
        return "\n".join(habilidades)


class Halfling(Raca):
    """Raça Halfling, baseada no Livro I, pág. 24.
    Perspicazes e curiosos aventureiros.
    """
    def __init__(self):
        super().__init__()
        self.nome = "Halfling"
        self.movimento = 6  # metros
        self.infravisao = "Não"
        self.alinhamento = "Tendência à neutralidade"

    def descrever_habilidades(self):
        habilidades = [
            "Furtivos: Consegue se esconder com 1-2 em 1d6.",
            "Destemidos: Bônus de +1 em qualquer teste de JPS.",
            "Bons de Mira: Ataques à distância com armas de arremesso são fáceis.",
            "Pequenos: Ataques de criaturas grandes ou maiores são difíceis de acertar.",
            "Restrições: Apenas armaduras de couro e armas pequenas ou médias. Armas médias precisam de duas mãos."
        ]
        return "\n".join(habilidades)