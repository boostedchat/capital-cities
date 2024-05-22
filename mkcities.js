// count number of items in capital cities.json

const fs = require('fs');
const path = require('path');
const capitalCities = require('./capital-cities.json');

let count = 0;
for(let city of capitalCities) {
    let {iso2, iso3, capital} = city;
    if(!capital)
        continue;
    fs.writeFileSync(path.join(__dirname, "iso2", `${iso2}.html`), JSON.stringify(city, null, 2));
    fs.writeFileSync(path.join(__dirname, "iso3", `${iso3}.html`), JSON.stringify(city, null, 2));
    console.log(count++)
}
