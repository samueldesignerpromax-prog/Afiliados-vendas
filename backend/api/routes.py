from flask import Flask, request, jsonify, session
from flask_cors import CORS
import uuid

app = Flask(__name__)
app.secret_key = "sua-chave-secreta-aqui"
CORS(app)

# Importar serviços
from services import ChatbotIA, PagamentoService, AfiliadoService
from models import Usuario, Curso, Venda

# Inicializar serviços
chatbot = ChatbotIA()
pagamento_service = PagamentoService()
afiliado_service = AfiliadoService()

# Banco de dados em memória
usuarios = {}
cursos = {}
vendas = {}
next_usuario_id = 1
next_venda_id = 1

# Cadastrar cursos iniciais
cursos[1] = Curso(1, "Curso de Marketing Digital", 497.00, "Aprenda as melhores estratégias de marketing digital", "link-afiliado-1")
cursos[2] = Curso(2, "Curso de Programação Python", 397.00, "Do zero ao avançado em Python", "link-afiliado-2")
cursos[3] = Curso(3, "Curso de IA para Negócios", 597.00, "Aplique inteligência artificial no seu negócio", "link-afiliado-3")

# Cadastrar afiliados de exemplo
afiliado_service.cadastrar_afiliado("João Silva", 30)
afiliado_service.cadastrar_afiliado("Maria Santos", 35)

@app.route('/')
def index():
    return jsonify({"message": "Plataforma de Cursos com Afiliados - API", "status": "online"})

@app.route('/api/chatbot', methods=['POST'])
def chatbot_message():
    data = request.json
    mensagem = data.get('mensagem', '')
    
    resposta = chatbot.responder(mensagem)
    
    return jsonify({
        "resposta": resposta,
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/cursos', methods=['GET'])
def listar_cursos():
    cursos_list = [curso.to_dict() for curso in cursos.values()]
    return jsonify(cursos_list)

@app.route('/api/cursos/<int:curso_id>', methods=['GET'])
def get_curso(curso_id):
    curso = cursos.get(curso_id)
    if not curso:
        return jsonify({"error": "Curso não encontrado"}), 404
    
    return jsonify(curso.to_dict())

@app.route('/api/cursos/<int:curso_id>/link-afiliado', methods=['POST'])
def gerar_link_afiliado(curso_id):
    data = request.json
    afiliado_id = data.get('afiliado_id')
    
    curso = cursos.get(curso_id)
    if not curso:
        return jsonify({"error": "Curso não encontrado"}), 404
    
    link = chatbot.gerar_link_afiliado(curso_id, afiliado_id)
    
    return jsonify({
        "link": link,
        "curso": curso.nome,
        "afiliado_id": afiliado_id
    })

@app.route('/api/comprar', methods=['POST'])
def comprar_curso():
    global next_usuario_id, next_venda_id
    
    data = request.json
    curso_id = data.get('curso_id')
    usuario_nome = data.get('usuario_nome')
    usuario_email = data.get('usuario_email')
    afiliado_id = data.get('afiliado_id')
    
    # Verificar curso
    curso = cursos.get(curso_id)
    if not curso:
        return jsonify({"error": "Curso não encontrado"}), 404
    
    # Criar ou buscar usuário
    usuario = None
    for u in usuarios.values():
        if u.email == usuario_email:
            usuario = u
            break
    
    if not usuario:
        usuario = Usuario(next_usuario_id, usuario_nome, usuario_email)
        usuarios[next_usuario_id] = usuario
        next_usuario_id += 1
    
    # Verificar se já comprou o curso
    if curso_id in usuario.cursos_comprados:
        return jsonify({"error": "Usuário já possui este curso"}), 400
    
    # Buscar afiliado
    afiliado = None
    if afiliado_id:
        afiliado = afiliado_service.get_afiliado(afiliado_id)
    
    # Criar venda
    venda = Venda(next_venda_id, usuario, curso, afiliado)
    vendas[next_venda_id] = venda
    next_venda_id += 1
    
    # Processar pagamento
    pagamento_aprovado = pagamento_service.processar_pagamento(venda)
    
    if pagamento_aprovado:
        return jsonify({
            "status": "success",
            "message": "Compra realizada com sucesso!",
            "venda_id": venda.id,
            "curso": curso.nome,
            "valor": curso.preco,
            "acesso_liberado": True,
            "afiliado": afiliado.nome if afiliado else None,
            "comissao": afiliado.saldo if afiliado else 0
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Pagamento não aprovado. Tente novamente."
        }), 400

@app.route('/api/afiliados', methods=['GET'])
def listar_afiliados():
    afiliados_list = [a.to_dict() for a in afiliado_service.listar_afiliados()]
    return jsonify(afiliados_list)

@app.route('/api/afiliados/<int:afiliado_id>/saldo', methods=['GET'])
def get_saldo_afiliado(afiliado_id):
    afiliado = afiliado_service.get_afiliado(afiliado_id)
    if not afiliado:
        return jsonify({"error": "Afiliado não encontrado"}), 404
    
    return jsonify({
        "nome": afiliado.nome,
        "saldo": afiliado.saldo,
        "total_vendas": afiliado.total_vendas,
        "comissao_percentual": afiliado.comissao_percentual
    })

@app.route('/api/vendas', methods=['GET'])
def listar_vendas():
    vendas_list = [venda.to_dict() for venda in vendas.values()]
    return jsonify(vendas_list)

from datetime import datetime
