const API_URL = '/api';

class API {
    static async getCursos() {
        const response = await fetch(`${API_URL}/cursos`);
        return await response.json();
    }
    
    static async enviarMensagemChatbot(mensagem) {
        const response = await fetch(`${API_URL}/chatbot`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ mensagem })
        });
        return await response.json();
    }
    
    static async comprarCurso(cursoId, usuarioNome, usuarioEmail, afiliadoId = null) {
        const response = await fetch(`${API_URL}/comprar`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                curso_id: cursoId,
                usuario_nome: usuarioNome,
                usuario_email: usuarioEmail,
                afiliado_id: afiliadoId
            })
        });
        return await response.json();
    }
}
