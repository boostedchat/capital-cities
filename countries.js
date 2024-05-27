// count number of items in capital cities.json

const fs = require('fs');
const path = require('path');
const capitalCities = require('./capital-cities.json');

let count = 0;
let countries = [];
let iso2s = [];
let iso3s = [];
for(let city of capitalCities) {
    let {iso2, iso3, capital} = city;
    iso2s.push(iso2)
    iso3s.push(iso3)

    
   
    // console.log(count++)
}

// fs.mkdirSync(path.join(__dirname, "countries", "iso2"), {recursive: true});
// fs.mkdirSync(path.join(__dirname, "countries", "iso3"), {recursive: true});
fs.writeFileSync(path.join(__dirname, "countries",  `iso2.html`), JSON.stringify(iso2s, null, 2));
fs.writeFileSync(path.join(__dirname, "countries",  `iso3.html`), JSON.stringify(iso3s, null, 2));
