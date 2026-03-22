class Afiliado:
    def __init__(self, id: int, nome: str, comissao_percentual: float = 30.0):
        self.id = id
        self.nome = nome
        self.comissao_percentual = comissao_percentual
        self.saldo = 0.0
        self.total_vendas = 0
    
    def receber_comissao(self, valor_venda: float) -> float:
        comissao = valor_venda * (self.comissao_percentual / 100)
        self.saldo += comissao
        self.total_vendas += 1
        return comissao
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "comissao_percentual": self.comissao_percentual,
            "saldo": self.saldo,
            "total_vendas": self.total_vendas
        }
