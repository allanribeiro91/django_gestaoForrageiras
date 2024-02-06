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

function sweetAlert(title, icon, iconColor='black', position='center', timer=2000) {
  Swal.fire({
      position: position,
      icon: icon,
      title: title,
      showConfirmButton: false,
      timer: timer,
      iconColor: iconColor,
      backdrop: false,
  });
}

function sweetAlertPreenchimento(html){
  Swal.fire({
      title: 'Atenção!',
      html: html,
      icon: 'warning',
      iconColor: 'red',
      confirmButtonText: 'Ok',
      confirmButtonColor: 'green',
  });
}

function sweetAlertDelete(mensagem, url_delete, csrfToken, url_apos_delete) {
Swal.fire({
  title: "Você tem certeza?",
  text: mensagem,
  icon: "warning",
  iconColor: 'red',
  showCancelButton: true,
  confirmButtonColor: "#d33",
  cancelButtonColor: "#3085d6",
  confirmButtonText: "Sim, deletar!"
}).then((result) => {
  if (result.isConfirmed) {
    $.ajax({
      url: url_delete,
      method: 'POST',
      headers: {
          'X-CSRFToken': csrfToken
      },
      success: function(response) {
          Swal.fire({
            title: "Deletado!",
            text: "Registro deletado com sucesso!",
            icon: "success",
            confirmButtonColor: 'green',
          });
          setTimeout(function() {
            window.location.href = url_apos_delete;
          }, 1500);
      },
      error: function(error) {
          alert('Ocorreu um erro ao tentar deletar. Por favor, tente novamente.');
      }
  });


    
  }
});
}


function sweetAlertGenerico(title='Atenção!', html, icon='warning', iconColor='red', confirmButtonText='Ok', confirmButtonColor='green', onConfirm){
Swal.fire({
    title: title,
    html: html,
    icon: icon,
    iconColor: iconColor,
    confirmButtonText: confirmButtonText,
    confirmButtonColor: confirmButtonColor,
}).then((result) => {
    if (result.isConfirmed && onConfirm) {
        onConfirm();
    }
});
}

