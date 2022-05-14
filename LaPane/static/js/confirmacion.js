//pregunta de aceptar para eliminar 
$(document).on('click', '.btn-danger', function(){
    $(document).on('submit','form', function canEvt(event){
        const ops = confirm('Esta seguro de hacer esta acción?');
        if(ops==false){
            event.preventDefault();
            location.reload()
        }
    });
});

// confirmar registro 


