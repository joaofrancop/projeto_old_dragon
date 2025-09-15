# 🐉 Criador de Personagem Old Dragon

Este projeto é uma aplicação web para a criação de personagens do RPG Old Dragon, implementada em Python. A ferramenta permite aos usuários gerar personagens de nível 1, escolhendo entre as raças e classes básicas e selecionando um dos três estilos de distribuição de atributos.

A aplicação foi desenvolvida seguindo o princípio da **arquitetura MVC (Model-View-Controller)** e utiliza o framework **Flask** para a interface web.

## 🚀 Funcionalidades

  * **Geração de Atributos**: Suporte aos três estilos de criação de personagem do manual:
      * **Clássico**: Rola 3d6 para cada atributo em uma ordem fixa[cite: 445].
      * **Aventureiro**: Rola 3d6 seis vezes e permite ao usuário distribuir os valores livremente[cite: 450].
      * **Heróico**: Rola 4d6 (descartando o menor) seis vezes e permite a distribuição livre[cite: 454].
  * **Seleção de Raças**: Escolha entre Humano, Elfo, Anão e Halfling[cite: 529]. [cite\_start]Cada raça possui características e habilidades únicas, como movimento, infravisão e bônus raciais[cite: 528].
  * **Seleção de Classes**: Escolha entre Guerreiro, Clérigo, Ladrão e Mago[cite: 293]. [cite\_start]Cada classe define as proficiências em armas e armaduras, além de habilidades de classe[cite: 815, 816].
  * **Interface Web Dinâmica**: O front-end, construído com HTML, CSS e JavaScript, interage com o back-end via requisições HTTP para criar uma experiência de usuário fluida, especialmente nos modos de distribuição de atributos livres.

## 📂 Arquitetura do Projeto

O projeto segue a arquitetura MVC para separar as responsabilidades e garantir a modularidade e a manutenibilidade do código.

```
projeto_old_dragon/
├── app/
│   ├── controllers/            # O Controller: Lida com as rotas e a lógica de requisições.
│   │   └── main_controller.py
│   ├── static/                 # A View: Onde ficam os arquivos estáticos (CSS e JS).
│   │   ├── style.css
│   │   └── script.js
│   ├── templates/              # A View: Onde ficam os arquivos HTML.
│   │   └── index.html
│   └── __init__.py
├── model/                      # O Model: A lógica de negócio e os dados.
│   ├── classe.py
│   ├── gerador_atributos.py
│   ├── personagem.py
│   └── raca.py
└── run.py                      # Ponto de entrada da aplicação Flask.
```

  - **Model**: As classes em `model/` representam as regras e os dados do jogo, como os atributos de um `Personagem` e as características de uma `Raca` ou `Classe`.
  - **View**: O arquivo `index.html` é a interface que o usuário vê. O JavaScript em `static/script.js` manipula a interface e se comunica com o back-end.
  - **Controller**: O `main_controller.py` atua como a "ponte", recebendo as escolhas do usuário do front-end e usando as classes do `model` para gerar a ficha do personagem, retornando os dados como JSON.

## ⚙️ Como Rodar o Projeto

1.  **Instale o Python 3** em sua máquina.
2.  **Clone o repositório** para sua máquina local.
3.  **Instale as dependências** do projeto (a única necessária é o Flask):
    ```sh
    pip install Flask
    ```
4.  **Execute a aplicação** a partir do diretório raiz do projeto:
    ```sh
    python run.py
    ```
5.  **Acesse o site** no seu navegador pelo endereço que o servidor Flask fornecer (geralmente `http://127.0.0.1:5000`).

-----

**Autor**: João Franco Pinheiro

