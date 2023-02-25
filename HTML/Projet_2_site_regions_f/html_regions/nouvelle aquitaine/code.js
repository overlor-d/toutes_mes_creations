//________________________________________________xxx______________________________________________//


//selectionne le span qui contient la température 
let temperature = document.getElementById('temperature');

//selectionne le span qui contient la description 
let description = document.getElementById('description');



//déclaration de la clé d API nécessaire à l obtention des informations météorologiques
const APIKEY = "a78ba88339c7f2f2ce1f44a8ae1f2cf8";

//url sur laquelle on chercher la météo
// site openweathermap, en parametres exemple: ville : Rennes, clé d'API, le systeme métrique puis la langue
let url_Bretagne = "https://api.openweathermap.org/data/2.5/weather?q=Bordeaux&appid=a78ba88339c7f2f2ce1f44a8ae1f2cf8&units=metric&lang=fr";


//requete sur l url définie précedemment
//convertit la réponse en format json puis utilise les donnees collectées pour les afficher
fetch(url_Bretagne).then(response=> response.json().then(data =>{
    console.log(data);
    temperature.innerHTML = data.main.temp+"°C"
    description.innerHTML = data.weather[0].description

}));
