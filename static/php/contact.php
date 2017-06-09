<?php
$naar = 'vincent.vanbecelaere@student.howest.be';
$onderwerp = 'Contactformulier';


$headers = "MIME-version: 1.0\r\n";
$headers .= "content-type: text/html;charset=utf-8\r\n";

if(isset($_POST['versturen']))
{
    $voornaam = trim($_POST['voornaam']);
    $familienaam = trim($_POST['familienaam']);
    $email = trim($_POST['email']);
    $bericht = trim($_POST['bericht']);
    $fout = false;

    if(empty($voornaam))
    {
        print '<p>Helaas, het voornaam veld is verplicht maar is nu niet ingevuld!</p>';
        $fout = true;
    }
    if(empty($familienaam))
    {
        print '<p>Helaas, het achternaam veld is verplicht maar is nu niet ingevuld!</p>';
        $fout = true;
    }
    if(empty($email))
    {
        print '<p>Helaas, het email veld is verplicht maar is nu niet ingevuld!</p>';
        $fout = true;
    }
    if(!filter_var($email, FILTER_VALIDATE_EMAIL))
    {
        print '<p>Helaas, het email adres is niet correct!</p>';
        $fout = true;
    }
    if(empty($bericht))
    {
        print '<p>Helaas, het bericht veld is verplicht maar is nu niet ingvuld!</p>';
        $fout = true;
    }

    if($fout == false)
    {
        $headers .= 'From: ' . $voornaam . ' ' . $familienaam . '<' . $email . '>';

        if(mail($naar, $onderwerp, nl2br($bericht), $headers))
        {
            print '<p>Het bericht is succesvol verzonden!</p>';
        }
        else
        {
            print '<p>Helaas, er is wat fout gegaan tijdens het verzenden van het formulier.</p>';
        }
    }
}
?>