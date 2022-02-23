$(document).ready(function(){
let products = $('.nombres').text().split(',')
let votos = $('.votos').text().split(',')
let colores = []
const random=(min, max)=>{
    return Math.floor(Math.random()*(max- min +1)+min);    
}

let pos1= random(1,255) , pos2 = random(99,255) , pos3 = random(80,255)  , pos4 = 0.2
for(let i = 0; i<products.length; i++){
    
    console.log(colores.push(`rgba(${pos1}, ${pos2}, ${pos3}, ${pos4})`) in colores) 
}
console.log(colores)
console.log(products, votos)
const ctx = document.getElementById('Estadisticas').getContext('2d');
const myChart = new Chart(ctx, {
    //grafica de pastel 'doughnut'
    type: 'bar',
    data: {
        labels: products,
        datasets: [{
            label: '# of Votes',
            data: votos,
            backgroundColor: colores 
            // [
            //     'rgba(255, 99, 132, 0.2)',
            //     'rgba(54, 162, 235, 0.2)',
            //     'rgba(255, 206, 86, 0.2)',
            //     'rgba(75, 192, 192, 0.2)',
            //     'rgba(153, 102, 255, 0.2)',
            //     'rgba(255, 159, 64, 0.2)'
            // ]
            ,
            borderColor:colores 
            // [
            //     'rgba(255, 99, 132, 1)',
            //     'rgba(54, 162, 235, 1)',
            //     'rgba(255, 206, 86, 1)',
            //     'rgba(75, 192, 192, 1)',
            //     'rgba(153, 102, 255, 1)',
            //     'rgba(255, 159, 64, 1)'
            // ]
            ,
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
