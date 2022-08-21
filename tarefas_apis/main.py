import json

from flask import Flask, jsonify, request

app = Flask(__name__)

lista_tarefas = [
    {
        'id': 0,
        'responsavel': 'Pedro',
        'tarefa': 'Desenvolver metodo GET',
        'status': 'concluida'
    },
    {
        'id': 1,
        'responsavel': 'Jose',
        'tarefa': 'Desenvolver metodo PUT',
        'status': 'pendente'
    },
{
        'id': 2,
        'responsavel': 'Guilherme',
        'tarefa': 'Desenvolver metodo DELETE',
        'status': 'concluida'
    },
    {
        'id': 3,
        'responsavel': 'Antonio',
        'tarefa': 'Desenvolver metodo POST',
        'status': 'pendente'
    }
]


@app.route('/tarefa/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def tarefas(id):
    if request.method == 'GET':
        try:
            response = lista_tarefas[id]
        except IndexError:
            mensagem = 'Tarefa de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        dados['id'] = id
        lista_tarefas[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        lista_tarefas.pop(id)
        for i in range(len(lista_tarefas)):
            lista_tarefas[i]['id'] = i
        return jsonify({'status': 'sucesso', 'mensagem': 'Tarefa excluida'})


#Listar e adicionar tarefas
@app.route('/tarefas/', methods=['GET', 'POST'])
def listar_tarefas():
    if request.method == 'GET':
        return jsonify(lista_tarefas)
    elif request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(lista_tarefas)
        dados['id'] = posicao
        lista_tarefas.append(dados)
        return jsonify(lista_tarefas[posicao])

if __name__ == '__main__':
    app.run(debug=True)
