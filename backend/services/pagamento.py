import random

class PagamentoService:
    def __init__(self):
        self.pagamentos_aprovados = True
    
    def processar_pagamento(self, venda) -> bool:
        """Simula processamento de pagamento"""
        print(f"🔄 Processando pagamento de R$ {venda.valor_total:.2f}...")
        
        # Simulação de aprovação (90% de chance)
        aprovado = random.random() > 0.1
        
        if aprovado:
            comissao = venda.aprovar_pagamento()
            print(f"✅ Pagamento aprovado!")
            if venda.afiliado:
                print(f"💰 Comissão paga para {venda.afiliado.nome}: R$ {comissao:.2f}")
            return True
        else:
            print(f"❌ Pagamento reprovado!")
            return False
