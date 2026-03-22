import json
import os

class Database:
    def __init__(self):
        self.usuarios = {}
        self.cursos = {}
        self.vendas = {}
        self.proximo_usuario = 1
        self.proximo_curso = 1
        self.proximo_venda = 1
    
    def salvar_em_json(self, arquivo: str = "database.json"):
        dados = {
            "usuarios": {k: v.to_dict() for k, v in self.usuarios.items()},
            "cursos": {k: v.to_dict() for k, v in self.cursos.items()},
            "vendas": {k: v.to_dict() for k, v in self.vendas.items()},
            "proximo_usuario": self.proximo_usuario,
            "proximo_curso": self.proximo_curso,
            "proximo_venda": self.proximo_venda
        }
        
        with open(arquivo, 'w') as f:
            json.dump(dados, f, indent=2)
    
    def carregar_de_json(self, arquivo: str = "database.json"):
        if os.path.exists(arquivo):
            with open(arquivo, 'r') as f:
                dados = json.load(f)
                # Recriar objetos a partir do JSON
                # Implementar recriação conforme necessidade
                pass
