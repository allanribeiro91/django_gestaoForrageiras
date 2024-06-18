$(document).ready(function() {  

    // Adiciona evento de clique a todos os itens ciclo
    document.querySelectorAll('.item_ciclo').forEach(item => {
        item.addEventListener('click', function() {
            const id = this.getAttribute('data-id');
            
            window.location.href = '/urts/ficha/ciclo/ficha/'
        });
    });

    // Adiciona evento de clique a todos os botões cicloRelatorio
    document.querySelectorAll('.cicloRelatorio').forEach(button => {
        button.addEventListener('click', function(event) {
            event.stopPropagation(); // Impede a propagação do evento de clique
            const id = this.getAttribute('data-id');
            alert('Relatório ' + id);
        });
    });


            
});