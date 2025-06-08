from flask import Flask, jsonify

app = Flask(__name__)

# Lista simulada de filmes
filmes = [
    {
        "id": 1,
        "titulo": "Batman: O Cavaleiro das Trevas",
        "diretor": "Christopher Nolan",
        "ano": 2008,
        "genero": "Ação, Crime, Drama",
        "nota": 9.0,
        "sinopse": "Com a ajuda do tenente Jim Gordon e do promotor Harvey Dent, Batman enfrenta o Coringa, um criminoso anarquista que causa o caos em Gotham."
    },
    {
        "id": 2,
        "titulo": "Harry Potter e o Prisioneiro de Azkaban",
        "diretor": "Alfonso Cuarón",
        "ano": 2004,
        "genero": "Fantasia, Aventura",
        "nota": 7.9,
        "sinopse": "Harry descobre mais sobre seu passado enquanto um perigoso prisioneiro, Sirius Black, escapa de Azkaban e vai atrás dele."
    },
    {
        "id": 3,
        "titulo": "Closer: Perto Demais",
        "diretor": "Mike Nichols",
        "ano": 2004,
        "genero": "Drama, Romance",
        "nota": 7.2,
        "sinopse": "Dois casais se entrelaçam em um jogo de amor, traição e desejo numa Londres moderna e emocionalmente conturbada."
    },
    {
        "id": 4,
        "titulo": "A Pior Pessoa do Mundo",
        "diretor": "Joachim Trier",
        "ano": 2021,
        "genero": "Drama, Romance, Comédia",
        "nota": 8.1,
        "sinopse": "Julie é uma jovem em busca de si mesma enquanto lida com relacionamentos amorosos, carreira e crises existenciais em Oslo."
    },
    {
        "id": 5,
        "titulo": "Whiplash: Em Busca da Perfeição",
        "diretor": "Damien Chazelle",
        "ano": 2014,
        "genero": "Drama, Música",
        "nota": 8.5,
        "sinopse": "Um jovem baterista ambicioso entra em uma escola de música de elite e é desafiado ao limite por um instrutor implacável."
    },
    {
        "id": 6,
        "titulo": "Donnie Darko",
        "diretor": "Richard Kelly",
        "ano": 2001,
        "genero": "Drama, Ficção Científica, Suspense",
        "nota": 8.0,
        "sinopse": "Após sobreviver a um estranho acidente, um adolescente perturbado começa a ter visões de um homem fantasiado de coelho que o leva a questionar a realidade."
    }
]

# Rota para todos os filmes
@app.route('/filmes', methods=['GET'])
def listar_filmes():
    return jsonify(filmes)

# Rota para filme por ID
@app.route('/filmes/<int:filme_id>', methods=['GET'])
def buscar_filme(filme_id):
    filme = next((f for f in filmes if f["id"] == filme_id), None)
    if filme:
        return jsonify(filme)
    return jsonify({"erro": "Filme não encontrado"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
