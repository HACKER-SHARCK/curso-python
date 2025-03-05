// dentro del {} son parametros
function suma(a, b) {
    console.log(arguments);
    return a + b;
}
//dentro del ()argumentos
let resultado = suma(5, 6, 1, 2, 3);
console.log(resultado);
console.log(typeof suma);