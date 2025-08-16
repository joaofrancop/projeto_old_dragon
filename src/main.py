# src/main.py

from .personagem import Personagem
from .gerador_atributos import GeradorDeAtributos

def main():
    gerador = GeradorDeAtributos()
    
    print("Bem-vindo ao Gerador de Atributos Old Dragon!")
    print("Escolha um estilo de geração de atributos:")
    print("1. Estilo Clássico (3d6, ordem fixa)")
    print("2. Estilo Aventureiro (3d6, livre escolha)")
    print("3. Estilo Heróico (4d6, livre escolha)")
    
    escolha = input("Digite o número da sua escolha: ")

    atributos_gerados = {}
    if escolha == '1':
        print("\nGerando atributos no Estilo Clássico...")
        atributos_gerados = gerador.gerar_estilo_classico()
    elif escolha == '2':
        print("\nGerando atributos no Estilo Aventureiro...")
        atributos_gerados = gerador.gerar_estilo_aventureiro()
    elif escolha == '3':
        print("\nGerando atributos no Estilo Heróico...")
        atributos_gerados = gerador.gerar_estilo_heroico()
    else:
        print("Escolha inválida. O programa será encerrado.")
        return

    meu_personagem = Personagem(**atributos_gerados)
    print("\n--- Personagem Criado com Sucesso! ---")
    meu_personagem.exibir_atributos()

if __name__ == "__main__":
    main()