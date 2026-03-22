import random

class ChatbotIA:
    def __init__(self):
        self.perguntas_respostas = {
            "preco": "💰 O curso custa R$ 497,00 com acesso vitalício!",
            "valor": "💰 O curso custa R$ 497,00 com acesso vitalício!",
            "certificado": "🎓 Sim! Ao concluir o curso você recebe um certificado reconhecido internacionalmente.",
            "tempo": "⏱️ O curso tem 40 horas de conteúdo completo + bônus exclusivos!",
            "duracao": "⏱️ O curso tem 40 horas de conteúdo completo + bônus exclusivos!",
            "acesso": "🔓 Após a compra aprovada, você recebe acesso imediato por e-mail em até 5 minutos.",
            "como acessar": "🔓 Após a compra aprovada, você recebe acesso imediato por e-mail em até 5 minutos.",
            "suporte": "💬 Temos suporte 24/7 pelo WhatsApp e e-mail!",
            "garantia": "✅ Garantia de 7 dias! Se não gostar, devolvemos 100% do seu dinheiro.",
            "parcelamento": "💳 Parcelamos em até 12x sem juros no cartão de crédito!",
            "afiliado": "🤝 Temos programa de afiliados com 30% de comissão!",
            "indicacao": "🤝 Temos programa de afiliados com 30% de comissão!",
            "bonus": "🎁 Bônus exclusivos: Planilhas, Templates e Grupo VIP no Telegram!"
        }
        
        self.respostas_genericas = [
            "📚 Posso ajudar com informações sobre preço, conteúdo e forma de acesso!",
            "🎯 O curso é completo e prático. Quer saber sobre o conteúdo programático?",
            "💡 Tem alguma dúvida específica sobre o curso? Posso te ajudar!",
            "🚀 Aproveite que hoje tem desconto especial! Quer saber mais?"
        ]
    
    def responder(self, mensagem: str) -> str:
        mensagem_lower = mensagem.lower()
        
        for palavra, resposta in self.perguntas_respostas.items():
            if palavra in mensagem_lower:
                return resposta
        
        return random.choice(self.respostas_genericas)
    
    def gerar_link_afiliado(self, curso_id: int, afiliado_id: int) -> str:
        return f"https://plataforma-cursos.com/curso/{curso_id}?ref={afiliado_id}"
