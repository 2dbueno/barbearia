// Arquivo JavaScript principal para o sistema de barbearia

document.addEventListener('DOMContentLoaded', function() {
    // Inicializar tooltips do Bootstrap
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });

    // Função para verificar disponibilidade de horários
    function verificarDisponibilidade() {
        const dataInput = document.getElementById('id_data');
        const barbeiroInput = document.getElementById('id_barbeiro');
        const horarioSelect = document.getElementById('id_horario');
        
        if (!dataInput || !barbeiroInput || !horarioSelect) return;
        
        dataInput.addEventListener('change', atualizarHorarios);
        barbeiroInput.addEventListener('change', atualizarHorarios);
        
        function atualizarHorarios() {
            const data = dataInput.value;
            const barbeiroId = barbeiroInput.value;
            
            if (!data || !barbeiroId) return;
            
            // Aqui seria feita uma requisição AJAX para verificar horários disponíveis
            // Por enquanto, vamos apenas simular com uma mensagem
            const mensagemDisponibilidade = document.getElementById('mensagem-disponibilidade');
            if (mensagemDisponibilidade) {
                mensagemDisponibilidade.textContent = 'Verificando horários disponíveis...';
                mensagemDisponibilidade.classList.remove('d-none');
                
                // Simulação de resposta após 1 segundo
                setTimeout(() => {
                    mensagemDisponibilidade.textContent = 'Horários atualizados conforme disponibilidade.';
                    mensagemDisponibilidade.classList.add('text-success');
                }, 1000);
            }
        }
    }
    
    // Inicializar verificação de disponibilidade
    verificarDisponibilidade();
    
    // Validação de formulários
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
    
    // Animações de entrada
    const fadeElements = document.querySelectorAll('.fade-in');
    fadeElements.forEach(element => {
        element.classList.add('show');
    });
    
    // Confirmação para cancelamento de agendamentos
    const btnsCancelar = document.querySelectorAll('.btn-cancelar-agendamento');
    btnsCancelar.forEach(btn => {
        btn.addEventListener('click', function(e) {
            if (!confirm('Tem certeza que deseja cancelar este agendamento?')) {
                e.preventDefault();
            }
        });
    });
});
