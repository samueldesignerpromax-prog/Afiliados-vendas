from flask import Blueprint, request, jsonify

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/webhook/pagamento', methods=['POST'])
def webhook_pagamento():
    """Webhook para receber confirmação de pagamento"""
    data = request.json
    # Processar confirmação de pagamento
    return jsonify({"status": "received", "message": "Webhook processado"})

@webhook_bp.route('/webhook/afiliado', methods=['POST'])
def webhook_afiliado():
    """Webhook para registrar cliques de afiliados"""
    data = request.json
    # Registrar clique ou venda de afiliado
    return jsonify({"status": "received", "message": "Clique registrado"})
