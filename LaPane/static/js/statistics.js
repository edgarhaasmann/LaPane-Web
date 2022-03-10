
$(document).ready(function(){
let products = $('.nombres').text().split(',')
let votos = $('.votos').text().split(',')
let colores = []
let optColores = ['rgba(139,0,139)', 'rgba(0,0,255)', 'rgba(210,105,30)', 'rgba(105,105,105)', 'rgba(85,107,47)', 'rgba(50,205, 59)']
let colorRam = 0 
const random=(min, max)=>{
    return Math.floor(Math.random()*(max- min +1)+min);    
}
for(let i = 0; i<products.length; i++){
    colores.push(optColores[random(0,5)])    

}
const ctx = document.getElementById('Estadisticas').getContext('2d');
const myChart = new Chart(ctx, {
    //grafica de pastel 'doughnut'
    //grafica de barras 'bar'
    type: 'bar',
    data: {
        labels: products,
        datasets: [{
            label: 'cantidad de ventas',
            data: votos,
            backgroundColor: colores ,
            borderColor:colores ,
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});


});
