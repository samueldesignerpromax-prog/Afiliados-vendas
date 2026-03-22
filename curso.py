class Curso:
    def __init__(self, id: int, nome: str, preco: float, descricao: str, link_afiliado: str = None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self.link_afiliado = link_afiliado
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "descricao": self.descricao,
            "link_afiliado": self.link_afiliado
        }
