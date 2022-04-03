$('.btn-buscar').on('click', function(){
    let inputBuscar = document.querySelector('.inputBuscar').value;

    if(inputBuscar && inputBuscar!=' '){
        $.ajax({
            url:'pedidos',
            type:'GET',
            data: {inputBuscar},
            dataType:'JSON',
            success: function(res){
                console.log(res);
                const tbody = document.querySelector('.tbody');
                if(res.length>0)
                for(let r=0; r<res.length; r++){
                    let nombre = $(`#nom${res[r].id_pedido}`).text(),
                        estado = $(`#est${res[r].id_pedido}`).text(),
                        e = estado.split(' ');

                    content = `
                    <tr>
                        <td class='text'>${res[r].nombrecliente}</td>
                        <td class='text'>${res[r].descripcionpedido}</td>
                        <td class='text'>${nombre}</td>
                        <td class='text ${e[1] === 'No'?'text-warning':'text-success'}'>${estado}</td>
                        <td class='text'>${res[r].fEntrega}</td>
                        <td><form method="get"><input type='text' name='idPedido' value='${res[r].id_pedido}' hidden>  <button type="submit" class="btn btn-success form-control">Entregar</button></form> </td>
                    </tr>
                    
                    `
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


// $(document).ready(function(){
//     function addToHtml(nc, dp, pl,ep ,fe ){
//         let row = $(this).closest('tr'),
//             nombre = row.find(nc)
//             res = `
//                 <tr>
//                     <td class='text'>${nc}</td>
//                     <td class='text'>${dp}</td>
//                     <td class='text'>${pl}</td>
//                     <td class='text'>${ep}</td>
//                     <td class='text'>${fe}</td>
//                     <td><form action="{url 'pedidosAdminList'}" method="post"> <button type="submit" class="btn btn-success form-control">Entregar</button></form> </td>
//                 </tr>
//                     `
//         return res
//     }
//     const btnSearch = document.querySelector('.btn-buscar');
//     let b = btnSearch.addEventListener('click', addToHtml)
//     $('.btn-buscar').on('click', function(){

//     //     const inputBuscar = document.querySelector('.inputBuscar');
//     //     const tbody = document.querySelector('.tbody')
//     //     let item = document.querySelectorAll('.item');
//     //     let res=''
//     //     try{
//     //         item.forEach((i)=>{
//     //             let nc = i.querySelector('.nombreCliente').textContent,
//     //                 dp = i.querySelector('.descripcionPedido').textContent,
//     //                 pl = i.querySelector('.plaza').textContent,
//     //                 ep = i.querySelector('.estado').textContent,
//     //                 fe = i.querySelector('.fentrega').textContent;
//     //                 if(nc === inputBuscar.value){
//     //                     res += addToHtml(nc, dp, pl,ep ,fe)
//     //                     throw BreakException        
//     //                 }else if(dp.search(inputBuscar.value)){
//     //                     res +=addToHtml(nc, dp, pl,ep ,fe)
//     //                     throw BreakException        
                        
//     //                 }else{
//     //                     alert('No se encontraron coincidencias')
//     //                 }
                    
//     //         });
//     //     }catch(error){
//     //         if(inputBuscar.value!=''){
//     //             tbody.innerHTML = res
//     //         }else{
//     //             location.reload()
//     //         }
//     //     }
//     // });

//     });
// });
// const btnSearch = document.querySelector('.btn-buscar');
// function addToHtml(){
//     let row = $(this).closest('tr'),
//         pc = row.find('.nombreCliente').val()

//         return pc
// }

// btnSearch.addEventListener('click', addToHtml)

// $(document).on('click', '.btn-buscar', function(){
//     // const row = $(this).closest('tr'),
//     //     inputBuscar = document.querySelector('.inputBuscar').value;
//     // let nombre = document.querySelector('')
//     // nombre.search(inputBuscar)
//     // console.log(inputBuscar.value)
// })