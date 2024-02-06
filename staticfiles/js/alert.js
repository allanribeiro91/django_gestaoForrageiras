document.addEventListener("DOMContentLoaded", function() {
    // Seleciona todos os elementos com a classe 'alert'
    const alertElements = document.querySelectorAll('.alert');
  
    // Para cada elemento de alerta, faz com que desapareça após 3 segundos
    alertElements.forEach(function(element) {
      setTimeout(function() {
        element.style.opacity = '0';  // Faz o elemento ficar transparente
  
        // Após a transição, remove o elemento do DOM
        setTimeout(function() {
          element.style.display = 'none';
        }, 1000);  // 1000ms = 1s, o tempo da transição
      }, 2000);  // 2000ms = 2s
    });
  });
  