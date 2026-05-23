function calculateSalary(){

let salary = parseFloat(document.getElementById("salary").value);

if(isNaN(salary) || salary <= 0){
alert("Enter a valid salary");
return;
}

let essentials = (salary * 0.50).toFixed(2);
let personal = (salary * 0.30).toFixed(2);
let savings = (salary * 0.20).toFixed(2);

document.getElementById("essentials").innerText = essentials;
document.getElementById("personal").innerText = personal;
document.getElementById("savings").innerText = savings;

document.getElementById("result").style.display = "block";

}
