# src/main.py

from .personagem import Personagem
from .gerador_atributos import GeradorDeAtributos
from .raca import Humano, Elfo, Anao, Halfling
from .classe import Guerreiro, Clerigo, Ladrao, Mago

def selecionar_raca():
    """Menu para seleção da raça."""
    racas_disponiveis = {
        "1": Humano(),
        "2": Elfo(),
        "3": Anao(),
        "4": Halfling()
    }
    print("\nEscolha a raça do seu personagem:")
    for key, raca in racas_disponiveis.items():
        print(f"{key}. {raca.nome}")
    
    escolha = input("Digite o número da raça: ")
    return racas_disponiveis.get(escolha)


def selecionar_classe():
    """Menu para seleção da classe."""
    classes_disponiveis = {
        "1": Guerreiro(),
        "2": Clerigo(),
        "3": Ladrao(),
        "4": Mago()
    }
    print("\nEscolha a classe do seu personagem:")
    for key, classe in classes_disponiveis.items():
        print(f"{key}. {classe.nome}")
    
    escolha = input("Digite o número da classe: ")
    return classes_disponiveis.get(escolha)


def main():
    gerador = GeradorDeAtributos()
    
    print("Bem-vindo ao Gerador de Personagens Old Dragon!")
    
    # 1. Seleção de Raça
    raca_escolhida = selecionar_raca()
    if not raca_escolhida:
        print("Escolha de raça inválida. Encerrando.")
        return
        
    # 2. Seleção de Classe
    classe_escolhida = selecionar_classe()
    if not classe_escolhida:
        print("Escolha de classe inválida. Encerrando.")
        return
    
    # 3. Seleção do Estilo de Atributos
    print("\nEscolha um estilo de geração de atributos:")
    print("1. Estilo Clássico (3d6, ordem fixa)")
    print("2. Estilo Aventureiro (3d6, livre escolha)")
    print("3. Estilo Heróico (4d6, livre escolha)")
    
    escolha_estilo = input("Digite o número da sua escolha: ")

    atributos_gerados = {}
    if escolha_estilo == '1':
        print("\nGerando atributos no Estilo Clássico...")
        atributos_gerados = gerador.gerar_estilo_classico()
    elif escolha_estilo == '2':
        print("\nGerando atributos no Estilo Aventureiro...")
        atributos_gerados = gerador.gerar_estilo_aventureiro()
    elif escolha_estilo == '3':
        print("\nGerando atributos no Estilo Heróico...")
        atributos_gerados = gerador.gerar_estilo_heroico()
    else:
        print("Escolha de estilo inválida. Encerrando.")
        return

    # 4. Criação e Exibição do Personagem
    meu_personagem = Personagem(raca_escolhida, classe_escolhida, **atributos_gerados)
    meu_personagem.exibir_atributos()

if __name__ == "__main__":
    main()