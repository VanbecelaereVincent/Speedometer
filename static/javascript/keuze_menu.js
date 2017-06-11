/**
 * Created by vincent on 11/06/2017.
 */


var button = document.getElementsByName("submit1")[0];
button.onclick = function() {ophalen()};


function ophalen(){

    input_naam = document.getElementsByName('naam')[0];
    naam = input_naam.value;

    input_voornaam = document.getElementsByName('voornaam')[0];
    voornaam = input_voornaam.value;

    input_leeftijd = document.getElementsByName('leeftijd')[0];
    leeftijd = input_leeftijd.value;

    input_wiel = document.getElementsByName('diamter wiel')[0];
    wiel = input_wiel.value;




}