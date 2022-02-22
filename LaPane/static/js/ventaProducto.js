$(document).ready(function(){
   //agregar productos a la venta 
   $(document).on('click', '#btn-agregarProducto', function(){
      let contador = 1;
      let row = $(this).closest('tr')
      let id = row.find('.nombre').text()
      let precio = row.find('.precio').text()
      let data = ''
      let table = document.querySelector('.tbody')
      for(let i=0; i<contador;i++){
         data+=`
            <tr>
               <td>${id}</td>
               <td> <input  class='cantidadP' type='number' placeholder='Cantidad producto' name='cantidad' min='0'> </td>
               <td class='precioP'> ${precio}</td>
            </tr>
         `
         
         table.innerHTML = data
      }
      
   });
   //total de todos los productos
   $(document).on('change', '.cantidadP', function(){
      let row = $(this).closest('tr')
      let precio = row.find('.precioP').text() 
      let cantidad = row.find('.cantidadP').val()
      let total = parseFloat(precio) * parseInt(cantidad)
      let data = ''
      let label = document.querySelector('.total')
      data+=`${total}`

      label.innerHTML = data
   });


});