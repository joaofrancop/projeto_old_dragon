from flask import Flask, render_template, request, jsonify
from model.raca import Humano, Elfo, Anao, Halfling
from model.classe import Guerreiro, Clerigo, Ladrao, Mago
from model.gerador_atributos import GeradorDeAtributos
from model.personagem import Personagem

app = Flask(__name__, template_folder='../templates', static_folder='../static')

racas_disponiveis = {
    "humano": Humano(),
    "elfo": Elfo(),
    "anao": Anao(),
    "halfling": Halfling()
}

classes_disponiveis = {
    "guerreiro": Guerreiro(),
    "clerigo": Clerigo(),
    "ladrao": Ladrao(),
    "mago": Mago()
}

@app.route('/')
def index():
    return render_template('index.html',
                           racas=racas_disponiveis,
                           classes=classes_disponiveis)

@app.route('/gerar_personagem', methods=['POST'])
def gerar_personagem():
    try:
        data = request.json
        estilo = data['estilo']
        raca_nome = data['raca'].lower()
        classe_nome = data['classe'].lower()

        raca_escolhida = racas_disponiveis.get(raca_nome)
        classe_escolhida = classes_disponiveis.get(classe_nome)

        if not raca_escolhida or not classe_escolhida:
             return jsonify({"error": "Escolha de raça ou classe inválida."}), 400

        gerador = GeradorDeAtributos()

        if estilo == 'classico':
            atributos_gerados = gerador.gerar_estilo_classico()
            personagem = Personagem(raca_escolhida, classe_escolhida, **atributos_gerados)
            return jsonify(personagem.to_dict())
        elif estilo in ['aventureiro', 'heroico']:
            resultados_rolagem = gerador.gerar_resultados_livre(estilo)
            return jsonify({'resultados': resultados_rolagem, 'estilo': estilo})
        else:
            return jsonify({"error": "Estilo de atributo inválido."}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/distribuir_livre', methods=['POST'])
def distribuir_livre():
    try:
        data = request.json
        raca_nome = data['raca'].lower()
        classe_nome = data['classe'].lower()
        atributos_distribuidos = data['atributos']

        raca_escolhida = racas_disponiveis.get(raca_nome)
        classe_escolhida = classes_disponiveis.get(classe_nome)

        if not raca_escolhida or not classe_escolhida:
            return jsonify({"error": "Dados de raça ou classe inválidos."}), 400

        personagem = Personagem(raca_escolhida, classe_escolhida, **atributos_distribuidos)
        return jsonify(personagem.to_dict())

    except Exception as e:
        return jsonify({"error": str(e)}), 500