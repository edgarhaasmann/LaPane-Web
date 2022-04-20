function entregarPedido(i, cli){
    let ops = confirm(`Esta seguro de cambiar el estado del producto para el cliente ${cli}?`)
    console.log(ops, i, cli);
    if(ops== true){
        $.ajax({
            url:'',
            type:'GET',
            data:{'estado':i}
        })
    }else{
        alert('No se realizaron cambios')
    }
} 

//Funcion para pedido modulo admin
$(document).ready(function(){
    $('.btn-buscar').on('click', function(){
        let inputBuscar = document.querySelector('.inputBuscar').value;
        if(inputBuscar && inputBuscar!=' '){
            $.ajax({
                url:'',
                type:'GET',
                data: {inputBuscar},
                dataType:'JSON',
                success: function(res){
                    console.log(res);
                    const tbody = document.querySelector('.tbody');
                    if(res.length>0){
                        let content = ''
                        for(let r=0; r<res.length; r++){
                            console.log('enctro primero', r);
                            // for(c in res[r]){
                            //     console.log('segundo', c[1]);
                            // }
                            let nombre = $(`#nom${res[r].id_pedido}`).text(),
                                estado = $(`#est${res[r].id_pedido}`).text(),
                                estadoEn = $(`#estEn${res[r].id_pedido}`).text(),
                                e = estado.split(' '),
                                eEn = estadoEn.split(' ');
                                console.log(e, eEn);
                            content += `
                            <tr>
                                <td class='text'>${res[r].nombrecliente}</td>
                                <td class='text'>${res[r].descripcionpedido}</td>
                                <td class='text'>${nombre}</td>
                                <td class='text ${e[1] === 'No'?'text-warning':'text-success'}'>${estado}</td>
                                <td class='text'>${res[r].fEntrega}</td>
                                <td class='text ${eEn[1] === 'No'?'text-warning':'text-success'}'>${estadoEn}</td>
                                <td><button onclick= entregarPedido(${res[r].id_pedido}) class="btn btn-success form-control">Entregar</button></td>
                            </tr>
                            
                            `
                        }
                        tbody.innerHTML = content
                    }else{
                        alert('No se encontraron coincidencias!')
                    }
                },
                error:function(res){
                    console.log(res.error)
                }
            });
        }else{
            location.reload()
        }
    });
    
});
//FUncion busqueda de pedidos en plaza
$(document).ready(function(){
    $('.btn-buscarNPlaza').on('click', function(){
        const inputBuscar = document.querySelector('.inputBuscar2').value;
        if(inputBuscar&& inputBuscar!=' '){
            $.ajax({
                url:'',
                type:'GET',
                data:{inputBuscar},
                dataType:'JSON',
                success: function(res){
                    const tbody = document.querySelector('.tbody');
                    if(res.length>0){
                        for(let r=0; r<res.length; r++){
                            console.log(res[r].id_pedido , res[r].nombrecliente);
                            let nombre = res[r].nombrecliente
                            let content = `
                            <tr>
                                <td class='text'>${res[r].nombrecliente}</td>
                                <td class='text'>${res[r].descripcionpedido}</td>
                                <td class='${res[r].estadoPreparacion==true? 'text-success':'text-warning'}'>${res[r].estadoPreparacion==true? 'Diponible':'No disponible'}</td>
                                <form action='' method="get">
                                    <td ${res[r].estadoPreparacion == true?'':'hidden'} ><button type='button' onclick= entregarPedido(${res[r].id_pedido}) class="btn btn-success form-control">Entregar</button></td>
                                </form>
                            </tr>
                            `
                        tbody.innerHTML = content
                        }
                    }else{
                        alert('No se han encontrado coincidencias!')
                    }
                },
                error: function(res){
                    document.write(`Ha ocurrido un error ${res.error}`)
                }
            });
        }else{
            location.reload()
        }
    });
});


