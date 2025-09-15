# model/personagem.py

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

    def to_dict(self):
        """
        Converte o objeto Personagem e seus sub-objetos para um dicionário,
        permitindo que seja retornado como JSON.
        """
        return {
            "raca": {
                "nome": self.raca.nome,
                "movimento": self.raca.movimento,
                "infravisao": self.raca.infravisao,
                "alinhamento": self.raca.alinhamento,
                "habilidades": self.raca.descrever_habilidades().split('\n')
            },
            "classe": {
                "nome": self.classe.nome,
                "pv_inicial": self.classe.pv_inicial,
                "dado_vida": self.classe.dado_vida,
                "ba": self.classe.ba,
                "jp_inicial": self.classe.jp_inicial,
                "proficiencias": self.classe.proficiencias,
                "habilidades": self.classe.habilidades
            },
            "forca": self.forca,
            "destreza": self.destreza,
            "constituicao": self.constituicao,
            "inteligencia": self.inteligencia,
            "sabedoria": self.sabedoria,
            "carisma": self.carisma
        }

    # O método 'exibir_atributos' não é mais necessário para o front-end,
    # pois a exibição será feita no HTML.
    # Mas você pode mantê-lo para debug se desejar.