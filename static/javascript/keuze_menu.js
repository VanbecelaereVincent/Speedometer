/**
 * Created by vincent on 11/06/2017.
 */


 /** var button1 = document.getElementsByName("submit1")[0]; */

var button3 = document.getElementsByName("submit3")[0];

/** button1.onclick = function() { ophalen()};


 */

button3.onclick = function() {verificatie()};


function verificatie() {

   console.write("Uw gegevens werden correct verstuurd.")


}


function ophalen(){

    input_naam = document.getElementsByName('naam')[0];
    naam = input_naam.value;

    input_voornaam = document.getElementsByName('voornaam')[0];
    voornaam = input_voornaam.value;

    input_leeftijd = document.getElementsByName('leeftijd')[0];
    leeftijd = input_leeftijd.value;

    input_wiel = document.getElementsByName('diameter wiel')[0];
    wiel = input_wiel.value;


    arr_input = [];
    arr_input.append(naam);
    arr_input.append(voornaam);
    arr_input.append(leeftijd);
    arr_input.append(wiel);

    window.alert("De data werd correct verstuurd");

}