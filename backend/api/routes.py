from flask import request, jsonify
from services import ChatbotIA, PagamentoService, AfiliadoService
from models import Usuario, Curso, Venda
from datetime import datetime

# Inicializar serviços
chatbot = ChatbotIA()
pagamento_service = PagamentoService()
afiliado_service = AfiliadoService()

# Banco de dados em memória
usuarios = {}
cursos = {
    1: Curso(1, "Marketing Digital", 497.00, "Aprenda as melhores estratégias de marketing digital", "link-1"),
    2: Curso(2, "Python Programação", 397.00, "Do zero ao avançado em Python", "link-2"),
    3: Curso(3, "IA para Negócios", 597.00, "Aplique inteligência artificial no seu negócio", "link-3")
}
vendas = {}
next_usuario_id = 1
next_venda_id = 1

# Cadastrar afiliados de exemplo
afiliado_service.cadastrar_afiliado("João Silva", 30)
afiliado_service.cadastrar_afiliado("Maria Santos", 35)

@app.route('/api/cursos', methods=['GET'])
def listar_cursos():
    """Lista todos os cursos disponíveis"""
    return jsonify([curso.to_dict() for curso in cursos.values()])

@app.route('/api/cursos/<int:curso_id>', methods=['GET'])
def get_curso(curso_id):
    """Obtém detalhes de um curso específico"""
    curso = cursos.get(curso_id)
    if not curso:
        return jsonify({"error": "Curso não encontrado"}), 404
    return jsonify(curso.to_dict())

@app.route('/api/cursos/<int:curso_id>/link-afiliado', methods=['POST'])
def gerar_link_afiliado(curso_id):
    """Gera link de afiliado para um curso"""
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

@app.route('/api/chatbot', methods=['POST'])
def chatbot_message():
    """Processa mensagens do chatbot"""
    data = request.json
    mensagem = data.get('mensagem', '')
    resposta = chatbot.responder(mensagem)
    return jsonify({"resposta": resposta})

@app.route('/api/comprar', methods=['POST'])
def comprar_curso():
    """Processa a compra de um curso"""
    global next_usuario_id, next_venda_id
    
    data = request.json
    curso_id = data.get('curso_id')
    usuario_nome = data.get('usuario_nome')
    usuario_email = data.get('usuario_email')
    afiliado_id = data.get('afiliado_id')
    
    curso = cursos.get(curso_id)
    if not curso:
        return jsonify({"error": "Curso não encontrado"}), 404
    
    # Buscar ou criar usuário
    usuario = None
    for u in usuarios.values():
        if u.email == usuario_email:
            usuario = u
            break
    
    if not usuario:
        usuario = Usuario(next_usuario_id, usuario_nome, usuario_email)
        usuarios[next_usuario_id] = usuario
        next_usuario_id += 1
    
    # Verificar se já possui o curso
    if curso_id in usuario.cursos_comprados:
        return jsonify({"error": "Usuário já possui este curso"}), 400
    
    # Buscar afiliado
    afiliado = afiliado_service.get_afiliado(afiliado_id) if afiliado_id else None
    
    # Criar venda
    venda = Venda(next_venda_id, usuario, curso, afiliado)
    vendas[next_venda_id] = venda
    next_venda_id += 1
    
    # Processar pagamento
    if pagamento_service.processar_pagamento(venda):
        return jsonify({
            "status": "success",
            "message": "Compra realizada com sucesso!",
            "venda_id": venda.id,
            "curso": curso.nome,
            "valor": curso.preco,
            "acesso_liberado": True,
            "afiliado": afiliado.nome if afiliado else None
        })
    else:
        return jsonify({"status": "error", "message": "Pagamento não aprovado"}), 400

@app.route('/api/afiliados', methods=['GET'])
def listar_afiliados():
    """Lista todos os afiliados"""
    return jsonify([a.to_dict() for a in afiliado_service.listar_afiliados()])

@app.route('/api/afiliados/<int:afiliado_id>/saldo', methods=['GET'])
def get_saldo_afiliado(afiliado_id):
    """Obtém saldo de um afiliado"""
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
    """Lista todas as vendas"""
    return jsonify([venda.to_dict() for venda in vendas.values()])
