$(function name(params) {
    $('.btn-eliminar').click(function name(params) {
        data_info = $(this).data('json')
        Swal.fire({
            title: 'Información?',
            html: `Estas Seguro deseas Elimianar  El  Resgistro!${data_info.name} `,
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Si',
            cancelButtonText: 'No'
          }).then((result) => {
            if (result.isConfirmed) {
                data_info.csrfmiddlewaretoken = $('input[name="csrfmiddlewaretoken"]').val();
            
                $.post(data_info.url,data_info).done(function(data){
                    if(data.status){
                        Swal.fire(
                            'Eliminado!',
                            data.message,
                            'success'
                          )
                          window.location.href = '.';
                    }else{
                        Swal.fire(
                            'No se Elimino!',
                            data.message,
                            'error'
                          )
                    }
                })
            }
          })
    });
});