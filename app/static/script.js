const atributosMap = {
    forca: 'forca_select',
    destreza: 'destreza_select',
    constituicao: 'constituicao_select',
    inteligencia: 'inteligencia_select',
    sabedoria: 'sabedoria_select',
    carisma: 'carisma_select'
};

let pontosRolados = [];

function iniciarGeracao() {
    const estilo = document.getElementById('estilo_select').value;
    const raca_nome = document.getElementById('raca_select').value;
    const classe_nome = document.getElementById('classe_select').value;

    fetch('/gerar_personagem', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({estilo: estilo, raca: raca_nome, classe: classe_nome})
    })
    .then(response => response.json())
    .then(data => {
        if(data.estilo) {
            pontosRolados = data.resultados;
            document.getElementById('resultados-rolagem').innerText = pontosRolados.join(', ');
            popularSelects();
            document.getElementById('selecao').style.display = 'none';
            document.getElementById('distribuicao-livre').style.display = 'block';
        } else if(data.raca && data.classe) {
            document.getElementById('selecao').style.display = 'none';
            exibirFicha(data);
        } else if(data.error) {
             alert("Erro: " + data.error);
        }
    })
    .catch(error => {
        alert("Ocorreu um erro ao rolar os dados. Tente novamente.");
        console.error('Error:', error);
    });
}

// Função principal que atualiza os dropdowns
function atualizarSelects() {
    const selects = document.querySelectorAll('.attribute-list select');
    const valoresSelecionados = Array.from(selects).map(s => s.value).filter(v => v !== '');

    selects.forEach(select => {
        const valorAtual = select.value;
        select.innerHTML = '';
        
        const placeholderOption = document.createElement('option');
        placeholderOption.value = '';
        placeholderOption.innerText = 'Escolha um valor';
        placeholderOption.disabled = true;
        if (!valorAtual) {
            placeholderOption.selected = true;
        }
        select.appendChild(placeholderOption);

        const pontosDisponiveis = [...pontosRolados];
        valoresSelecionados.forEach(v => {
            const index = pontosDisponiveis.indexOf(parseInt(v));
            if (index > -1 && String(v) !== valorAtual) {
                pontosDisponiveis.splice(index, 1);
            }
        });

        const sortedPontos = [...pontosDisponiveis].sort((a, b) => b - a);

        sortedPontos.forEach(ponto => {
            const option = document.createElement('option');
            option.value = ponto;
            option.innerText = ponto;
            select.appendChild(option);
        });
        
        if (valorAtual) {
            select.value = valorAtual;
        }
    });
    validarValores();
}

function popularSelects() {
    const selects = document.querySelectorAll('.attribute-list select');
    const sortedPontos = [...pontosRolados].sort((a, b) => b - a);
    
    selects.forEach(select => {
        select.innerHTML = '';
        const placeholderOption = document.createElement('option');
        placeholderOption.value = '';
        placeholderOption.innerText = 'Escolha um valor';
        placeholderOption.disabled = true;
        placeholderOption.selected = true;
        select.appendChild(placeholderOption);

        sortedPontos.forEach(ponto => {
            const option = document.createElement('option');
            option.value = ponto;
            option.innerText = ponto;
            select.appendChild(option);
        });
    });
    validarValores();
}

function validarValores() {
    const selects = document.querySelectorAll('.attribute-list select');
    const valoresSelecionados = Array.from(selects).map(s => parseInt(s.value)).filter(v => !isNaN(v));
    const feedback = document.getElementById('feedback-erro');
    const btn = document.getElementById('btn-distribuir');
    
    if (valoresSelecionados.length !== 6) {
        feedback.innerText = "Por favor, preencha todos os atributos.";
        feedback.style.display = 'block';
        btn.disabled = true;
        return;
    }

    const valoresSelecionadosSorted = [...valoresSelecionados].sort((a,b) => a-b);
    const pontosRoladosSorted = [...pontosRolados].sort((a,b) => a-b);
    
    const saoIguais = JSON.stringify(valoresSelecionadosSorted) === JSON.stringify(pontosRoladosSorted);

    if (!saoIguais) {
        feedback.innerText = "Os valores selecionados não correspondem aos valores rolados.";
        feedback.style.display = 'block';
        btn.disabled = true;
    } else {
        feedback.style.display = 'none';
        btn.disabled = false;
    }
}

function distribuirAtributos() {
    const raca_nome = document.getElementById('raca_select').value;
    const classe_nome = document.getElementById('classe_select').value;
    const atributos = {};
    
    for (const key in atributosMap) {
        const selectId = atributosMap[key];
        const valor = document.getElementById(selectId).value;
        atributos[key] = parseInt(valor);
    }

    fetch('/distribuir_livre', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({raca: raca_nome, classe: classe_nome, atributos: atributos})
    })
    .then(response => response.json())
    .then(data => {
        if(data.raca && data.classe) {
            document.getElementById('distribuicao-livre').style.display = 'none';
            exibirFicha(data);
        } else if(data.error) {
            alert("Erro: " + data.error);
        }
    })
    .catch(error => {
        alert("Ocorreu um erro ao distribuir os atributos. Tente novamente.");
        console.error('Error:', error);
    });
}

function exibirFicha(personagem) {
    let fichaHtml = `
        <div class="ficha">
            <h2>Ficha do Personagem</h2>
            <table>
                <thead>
                    <tr><th colspan="2">Informações Básicas</th></tr>
                </thead>
                <tbody>
                    <tr><td><strong>Raça:</strong></td><td>${personagem.raca.nome}</td></tr>
                    <tr><td><strong>Classe:</strong></td><td>${personagem.classe.nome}</td></tr>
                    <tr><td><strong>Alinhamento:</strong></td><td>${personagem.raca.alinhamento}</td></tr>
                    <tr><td><strong>Movimento:</strong></td><td>${personagem.raca.movimento}m</td></tr>
                    <tr><td><strong>Infravisão:</strong></td><td>${personagem.raca.infravisao}</td></tr>
                </tbody>
            </table>

            <table>
                <thead>
                    <tr><th colspan="2">Atributos</th></tr>
                </thead>
                <tbody>
                    <tr><td><strong>Força:</strong></td><td>${personagem.forca} (Mod: ${Math.floor((personagem.forca - 10) / 2)})</td></tr>
                    <tr><td><strong>Destreza:</strong></td><td>${personagem.destreza} (Mod: ${Math.floor((personagem.destreza - 10) / 2)})</td></tr>
                    <tr><td><strong>Constituição:</strong></td><td>${personagem.constituicao} (Mod: ${Math.floor((personagem.constituicao - 10) / 2)})</td></tr>
                    <tr><td><strong>Inteligência:</strong></td><td>${personagem.inteligencia} (Mod: ${Math.floor((personagem.inteligencia - 10) / 2)})</td></tr>
                    <tr><td><strong>Sabedoria:</strong></td><td>${personagem.sabedoria} (Mod: ${Math.floor((personagem.sabedoria - 10) / 2)})</td></tr>
                    <tr><td><strong>Carisma:</strong></td><td>${personagem.carisma} (Mod: ${Math.floor((personagem.carisma - 10) / 2)})</td></tr>
                </tbody>
            </table>

            <table>
                <thead>
                    <tr><th colspan="2">Habilidades & Proficiências</th></tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Habilidades de Raça:</strong></td>
                        <td><ul><li>${personagem.raca.habilidades.join('</li><li>')}</li></ul></td>
                    </tr>
                    <tr>
                        <td><strong>PV Inicial da Classe:</strong></td>
                        <td>${personagem.classe.pv_inicial} + mod. CON</td>
                    </tr>
                    <tr>
                        <td><strong>Proficiências de Classe:</strong></td>
                        <td>${personagem.classe.proficiencias.join(', ')}</td>
                    </tr>
                    <tr>
                        <td><strong>Habilidades de Classe:</strong></td>
                        <td><ul><li>${personagem.classe.habilidades.join('</li><li>')}</li></ul></td>
                    </tr>
                </tbody>
            </table>
        </div>
    `;
    document.getElementById('ficha-conteudo').innerHTML = fichaHtml;
    document.getElementById('ficha-personagem').style.display = 'block';
}