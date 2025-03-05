let nombre = "Tanjiro";
let anime = "demon slayer";
let edad = 16;

let personaje = {
    nombre: "Tanjiro";
    anime: "Demon Slayer",
    edad: 16,
}; //objeto literal
console.log(personaje);
console.log(personaje.nombre);
console.log(personaje["anime"]);

//da error porque la edad en realidad es 16
personaje.edad = 13;

let llave = "edad";
personaje[llave] = 16;

delete personaje.anime;

console.log(personaje);