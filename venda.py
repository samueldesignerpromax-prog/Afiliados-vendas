from datetime import datetime
from typing import Optional

class Venda:
    def __init__(self, id: int, usuario, curso, afiliado=None):
        self.id = id
        self.usuario = usuario
        self.curso = curso
        self.afiliado = afiliado
        self.valor_total = curso.preco
        self.data = datetime.now()
        self.status = "pendente"
        
    def aprovar_pagamento(self):
        self.status = "aprovada"
        self.usuario.cursos_comprados.append(self.curso.id)
        self.usuario.historico_compras.append({
            "curso_id": self.curso.id,
            "curso_nome": self.curso.nome,
            "valor": self.valor_total,
            "data": self.data.strftime("%Y-%m-%d %H:%M:%S")
        })
        
        if self.afiliado:
            comissao = self.afiliado.receber_comissao(self.valor_total)
            return comissao
        return 0.0
    
    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario.id,
            "curso_id": self.curso.id,
            "afiliado_id": self.afiliado.id if self.afiliado else None,
            "valor_total": self.valor_total,
            "data": self.data.strftime("%Y-%m-%d %H:%M:%S"),
            "status": self.status
        }
