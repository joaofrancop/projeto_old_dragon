# model/gerador_atributos.py

import random

class GeradorDeAtributos:
    """
    Responsável por gerar os atributos do personagem
    de acordo com os diferentes estilos de jogo do Old Dragon.
    """
    def _rolar_3d6(self):
        """Rola 3 dados de 6 faces e retorna a soma."""
        return sum(random.randint(1, 6) for _ in range(3))

    def _rolar_4d6_descartar_menor(self):
        """Rola 4 dados de 6 faces, descarta o menor e retorna a soma."""
        rolagens = [random.randint(1, 6) for _ in range(4)]
        rolagens.remove(min(rolagens))
        return sum(rolagens)

    def gerar_estilo_classico(self):
        """
        Gera atributos rolando 3d6 seis vezes e distribuindo-os na ordem fixa.
        No estilo clássico, rola-se 3d6 seis vezes e distribui-se entre os atributos
        seguindo a ordem: Força, Destreza, Constituição, Inteligência, Sabedoria e Carisma.
        """
        return {
            "forca": self._rolar_3d6(),
            "destreza": self._rolar_3d6(),
            "constituicao": self._rolar_3d6(),
            "inteligencia": self._rolar_3d6(),
            "sabedoria": self._rolar_3d6(),
            "carisma": self._rolar_3d6()
        }

    def gerar_resultados_livre(self, estilo):
        """
        Gera os 6 resultados de rolagem para os estilos Aventureiro ou Heróico.
        A distribuição é feita pelo front-end.
        """
        if estilo == 'aventureiro':
            return [self._rolar_3d6() for _ in range(6)]
        elif estilo == 'heroico':
            return [self._rolar_4d6_descartar_menor() for _ in range(6)]
        else:
            raise ValueError("Estilo de atributo inválido para geração livre.")