function toggleFAQ(el){
const answer = el.nextElementSibling;
answer.style.display =
answer.style.display === 'block'
? 'none'
: 'block';
}

function calcularFinanciamento(){

const valor =
parseFloat(document.getElementById('valor').value);

const juros =
parseFloat(document.getElementById('juros').value)/100;

const meses =
parseInt(document.getElementById('meses').value);

const parcela =
(valor*juros)/
(1-Math.pow(1+juros,-meses));

if(!isNaN(parcela)){
document.getElementById('resultado').innerHTML =
'Parcela estimada: R$ '+
parcela.toFixed(2);
}
}
