let cursos = [];

async function loadCursos() {
    try {
        cursos = await API.getCursos();
        displayCursos(cursos);
    } catch (error) {
        console.error('Erro ao carregar cursos:', error);
    }
}

function displayCursos(cursos) {
    const grid = document.getElementById('cursos-grid');
    grid.innerHTML = cursos.map(curso => `
        <div class="curso-card" onclick="mostrarModalCompra(${curso.id})">
            <div class="card-content">
                <h3>${curso.nome}</h3>
                <div class="preco">
                    R$ ${curso.preco.toFixed(2)} <small>à vista</small>
                </div>
                <p class="descricao">${curso.descricao}</p>
                <button class="btn-comprar">Comprar Agora</button>
            </div>
        </div>
    `).join('');
}

function mostrarModalCompra(cursoId) {
    const curso = cursos.find(c => c.id === cursoId);
    const nome = prompt('Digite seu nome completo:');
    const email = prompt('Digite seu e-mail:');
    
    if (nome && email) {
        realizarCompra(cursoId, nome, email);
    }
}

async function realizarCompra(cursoId, nome, email) {
    // Pegar afiliado da URL se existir
    const urlParams = new URLSearchParams(window.location.search);
    const afiliadoId = urlParams.get('ref');
    
    try {
        const result = await API.comprarCurso(cursoId, nome, email, afiliadoId);
        
        if (result.status === 'success') {
            alert(`✅ ${result.message}\n\nCurso: ${result.curso}\nValor: R$ ${result.valor}\n\nAcesse seu e-mail para mais informações!`);
            
            if (result.afiliado) {
                console.log(`Venda registrada para afiliado: ${result.afiliado}`);
            }
        } else {
            alert(`❌ ${result.message}`);
        }
    } catch (error) {
        alert('Erro ao processar compra. Tente novamente.');
    }
}

function scrollToCursos() {
    document.getElementById('cursos').scrollIntoView({ behavior: 'smooth' });
}

// Carregar cursos ao iniciar
document.addEventListener('DOMContentLoaded', () => {
    loadCursos();
});
