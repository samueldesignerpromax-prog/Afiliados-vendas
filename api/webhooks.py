from flask import Blueprint, request, jsonify

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/webhook/pagamento', methods=['POST'])
def webhook_pagamento():
    data = request.json
    
    # Processar webhook de pagamento
    venda_id = data.get('venda_id')
    status = data.get('status')
    
    # Atualizar status da venda
    # Isso seria implementado com integração real (Stripe, Hotmart, etc)
    
    return jsonify({"status": "received"})

@webhook_bp.route('/webhook/afiliado', methods=['POST'])
def webhook_afiliado():
    data = request.json
    
    # Processar webhook de afiliado
    # Registrar clique, venda, etc
    
    return jsonify({"status": "received"})
