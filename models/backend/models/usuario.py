from typing import List, Dict

class Usuario:
    def __init__(self, id: int, nome: str, email: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.cursos_comprados: List[int] = []
        self.historico_compras: List[Dict] = []
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "cursos_comprados": self.cursos_comprados,
            "historico_compras": self.historico_compras
        }
