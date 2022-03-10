

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
      addCanasta(itemIdProducto, itemNombreProducto, itemPrecioProducto, itemCantidadProducto);
   }
   
   
   function addCanasta(itemIdProducto, itemNombreProducto, itemPrecioProducto, itemCantidadProducto){
         const productoEnCanastaFila = document.createElement('tr');
         productoEnCanastaFila.className = 'item-Producto'
         const productoEnCanastaItem =  `
            <td hidden><input class='id' type='text' value='${itemIdProducto}' name='id_producto' hidden></td>
            <td><div class='nombreP'>${itemNombreProducto} </div></td>
            <td> <input  class='cantidadP' type='number' value='1' name='cantidad' min='1' max='${parseInt(itemCantidadProducto)}'> </td>
            <td> <input class='precioP' type='number' value='${itemPrecioProducto}' hidden> ${itemPrecioProducto} </div></td>
            <td><input type='button' class='btn btn-danger buttonDelete' value='x'></td>
            <td hidden> <input id='${itemIdProducto}' class='totalP' type='number' name='valorTotal' > </td>
      `;
      productoEnCanastaFila.innerHTML = productoEnCanastaItem;
      tbody.append(productoEnCanastaFila);
      
      productoEnCanastaFila.querySelector('.buttonDelete').addEventListener('click',removeItemDeCanasta);
      productoEnCanastaFila.querySelector('.cantidadP').addEventListener('change',changeItemCantidad);
      actualizarTotalGeneral();
   } 

   function actualizarTotalGeneral(){
      let total = 0
      const totalLabel = document.querySelector('#total');
      const item = document.querySelectorAll('.item-Producto');
      item.forEach((i)=>{
         let precio =  Number(i.querySelector('.precioP').value);
         let cantidad = Number(i.querySelector('.cantidadP').value);
         
         total= total+ precio* cantidad;
      });
   totalLabel.innerHTML = `${total.toFixed(2)}`
   }
   function removeItemDeCanasta(evt){
      const buttonDelete = evt.target;
      buttonDelete.closest('.item-Producto').remove();
      actualizarTotalGeneral();
   }

   function changeItemCantidad(evt){
      let cantidadInput =evt.target;
      if(cantidadInput.value <= 0){
         cantidadInput.value = 1;
      }
      actualizarTotalGeneral()

   }



   
   

});


