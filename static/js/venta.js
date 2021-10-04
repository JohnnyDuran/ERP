var BusquedaAjax = (url)=>{
    ajax = {
        url:url,
        dataType:'json',
        type:'GET',
        data:function (params) {
            var queryParameters = {
                search : params.term
            }
            return queryParameters;
        },
        processResults: function (data) {

            return{
                results:$.map(data.data,function (item) {
                    return{
                        text: item.value,
                        id:item.id,
                        precio :item.precio
                    }
                })
            }
        }
    }
    return ajax;
}
var languajeBusqueda ={
        noResults:function () {
            return "No hay resultado";
        },
        searching: function () {
            return "Buscando..";
        },

        escapeMarkup:function (markup) {
            return markup;
        }
    }

$('#productos').select2({
    placeholder: 'Seleccione Producto',
    allowClear: true,
    //theme: 'bootstrap4',
    language: languajeBusqueda,
    ajax: BusquedaAjax('/productos/')
});
$('#productos').change(function () {
    data = $(this).select2('data')[0];
    console.log(data);
    const tr= `<tr id_producto = ${data.id}>
    <th scope="col"><button type="button" class="btn btn-danger btn_eliminar">X</button></th>
    <th scope="col">${data.text}</th>
    <th scope="col"><input type="number" name="precio" class=" form-control inp-precio" value="1"></th>
    <th scope="col">${data.precio}</th>
    <th scope="col">${data.precio}</th>
  </tr>`
  $('#table_detalle tbody').append(tr)
    
})
$(document).on('click','.btn_eliminar',function () {
    $(this).parent().parent().remove()
})

$(document).on('change','.inp-precio',function () {
    $(this).val()
    total = 0;
    $('#table_detalle tbody tr').each(function (index,elemento) {
        console.log(index,elemento);
        total = parseFloat( $($(elemento).find('td')[3]).text()) * parseInt( $(this).val())
        console.log(total)
        $($(elemento).find('td')[4]).text(total)
    })
})
