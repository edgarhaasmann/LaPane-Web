$(document).ready(function(){
   const tbody = document.querySelector('.tbody');

   const buttonAdd= document.querySelectorAll('#btn-agregarProducto');
   buttonAdd.forEach(addVenta=>{
      addVenta.addEventListener('click', addVentaClicked);
   });
   
   
   function addVentaClicked(event){
      const button = event.target;
      const item =  button.closest('.producto');
      let itemIdProducto = item.querySelector('.id_producto').textContent;
      let itemNombreProducto = item.querySelector('.nombre').textContent;
      let itemCantidadProducto = item.querySelector('.cantidad').textContent.replace('piezas','');
      let itemPrecioProducto = item.querySelector('.precio').textContent;
      let idPlaza = item.querySelector('.id_plaza').textContent;
      addCanasta(itemIdProducto, itemNombreProducto, itemPrecioProducto, itemCantidadProducto, idPlaza);
   }
   
   
   function addCanasta(itemIdProducto, itemNombreProducto, itemPrecioProducto, itemCantidadProducto, idPlaza){
         const productoEnCanastaFila = document.createElement('tr');
         productoEnCanastaFila.className = 'item-Producto'
         const productoEnCanastaItem =  `
            <td hidden><input class='id' type='text' value='${itemIdProducto}' name='id_producto' ></td>
            <td hidden><input class='id_plaza' type='text' value='${idPlaza}' name='id_plaza' ></td>
            <td><div class=' text nombreP'>${itemNombreProducto} </div></td>
            <td> <input  class='cantidadP' type='number' placeholder='Ingrese cantidad' name='cantidad' min='1' max='${parseInt(itemCantidadProducto)}'> </td>
            <td class='text'> <input class=' precioP' type='number' value='${itemPrecioProducto}' hidden> ${itemPrecioProducto} </div></td>
            <td><input type='button' class='btn btn-danger buttonDelete' value='x'></td>
            <td><input hidden type='text' id='Product${itemIdProducto}' class='totlp' > </td>

      `;
      
      productoEnCanastaFila.innerHTML = productoEnCanastaItem;
      tbody.append(productoEnCanastaFila);
      
      productoEnCanastaFila.querySelector('.buttonDelete').addEventListener('click',removeItemDeCanasta);
      productoEnCanastaFila.querySelector('.cantidadP').addEventListener('change',changeItemCantidad);
      
      actualizarTotalGeneral();
   
      
      
      
   } 
   $(document).on('change', '.cantidadP', function(){
      let row = $(this).closest('tr');
      let id = row.find('.id').val();
      let precio = row.find('.precioP').val(); 
      let cantidad = row.find('.cantidadP').val();
      let totalProduct = parseFloat(precio)*parseInt(cantidad);
      let totalP = document.getElementById(`Product${id}`).value =totalProduct; 
   });
   
   $(document).on('click','#btn-vender', function(){
      const item = document.querySelectorAll('.item-Producto');
      item.forEach((i)=>{
         let id_producto = i.querySelector('.id').value,
             total_producto = i.querySelector('.totlp').value,
             id_plaza = i.querySelector('.id_plaza').value,
             cantidad = i.querySelector('.cantidadP').value;
         
         if (cantidad ===''){
            alert('la cantidad no puede quedar vacia')
         }else if (cantidad==='0'){
            alert('La cantidad no puede ser cero')
         }else{

            $.ajax({
               url:'Venta',
               type:'GET',
               data:{
                  id_producto,
                  total_producto,
                  id_plaza,
                  cantidad
               },
               dataType:'json',
               success:function(data){
                  let message = data.content.message;
                  console.log('false');
                  location.reload( );
               },error:function(data){
                  let message = data.content.message;
                  console.log(message);
                  // alert(message.status);
                  // console.log(message.content.status, message.content.message);
                  // location.reload();
               }
   
            });
         }
      });
   });
   
   
   
   function actualizarTotalGeneral(){
      let total = 0;
      const totalLabel = document.querySelector('#total');
      const item = document.querySelectorAll('.item-Producto');
      item.forEach((i)=>{
         let precio =  Number(i.querySelector('.precioP').value);
         let cantidad = Number(i.querySelector('.cantidadP').value);
         
         total= total+ precio* cantidad;
      });
   totalLabel.innerHTML = `${total.toFixed(2)}`;
   }
   function removeItemDeCanasta(evt){
      const buttonDelete = evt.target;
      buttonDelete.closest('.item-Producto').remove();
      actualizarTotalGeneral();
   }

   function changeItemCantidad(evt){
      let cantidadInput =evt.target;
      if(cantidadInput.value <= 0){
         cantidadInput.value = 0;
      }
      actualizarTotalGeneral()

   }



   
   

});



