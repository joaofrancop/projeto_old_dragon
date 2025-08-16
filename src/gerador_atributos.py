# src/gerador_atributos.py
import random

class GeradorDeAtributos:
    """
    Responsável por gerar e distribuir os atributos do personagem
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
        seguindo a ordem: Força, Destreza, Constituição, Inteligência, Sabedoria e Carisma[cite: 445].
        """
        atributos = {
            "forca": self._rolar_3d6(),
            "destreza": self._rolar_3d6(),
            "constituicao": self._rolar_3d6(),
            "inteligencia": self._rolar_3d6(),
            "sabedoria": self._rolar_3d6(),
            "carisma": self._rolar_3d6()
        }
        return atributos

    def gerar_estilo_aventureiro(self):
        """
        Gera atributos rolando 3d6 seis vezes e permitindo a distribuição.
        
        No estilo aventureiro, rola-se 3d6 seis vezes e distribui-se como desejar
        os resultados nos seis atributos[cite: 450].
        """
        resultados = [self._rolar_3d6() for _ in range(6)]
        print(f"Resultados obtidos: {resultados}")
        return self._distribuir_pontos_interativo(resultados)

    def gerar_estilo_heroico(self):
        """
        Gera atributos rolando 4d6 (descartando o menor) seis vezes e permitindo a distribuição.
        
        No estilo heróico, rola-se 4d6 (eliminando o d6 mais baixo) seis vezes e distribui-se
        como desejar os resultados nos seis atributos[cite: 454].
        """
        resultados = [self._rolar_4d6_descartar_menor() for _ in range(6)]
        print(f"Resultados obtidos: {resultados}")
        return self._distribuir_pontos_interativo(resultados)
        
    def _distribuir_pontos_interativo(self, pontos):
        """
        Lógica de interação para o usuário alocar os pontos nos atributos.
        """
        atributos = {}
        pontos_disponiveis = list(pontos)
        nomes_atributos = ["Forca", "Destreza", "Constituicao", "Inteligencia", "Sabedoria", "Carisma"]
        
        print("\nAgora, distribua os pontos entre os atributos:")
        for nome_atributo in nomes_atributos:
            print(f"Pontos disponíveis: {pontos_disponiveis}")
            while True:
                try:
                    valor = int(input(f"Atribuir valor para {nome_atributo}: "))
                    if valor in pontos_disponiveis:
                        atributos[nome_atributo.lower()] = valor
                        pontos_disponiveis.remove(valor)
                        break
                    else:
                        print("Valor inválido ou já usado. Escolha um dos valores disponíveis.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
        return atributos