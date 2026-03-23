from models import Afiliado

class AfiliadoService:
    def __init__(self):
        self.afiliados = {}
        self.proximo_id = 1
    
    def cadastrar_afiliado(self, nome: str, comissao: float = 30.0):
        afiliado = Afiliado(self.proximo_id, nome, comissao)
        self.afiliados[afiliado.id] = afiliado
        self.proximo_id += 1
        return afiliado
    
    def get_afiliado(self, id: int):
        return self.afiliados.get(id)
    
    def listar_afiliados(self):
        return list(self.afiliados.values())
    
    def calcular_comissao(self, valor_venda: float, comissao_percentual: float) -> float:
        return valor_venda * (comissao_percentual / 100)
