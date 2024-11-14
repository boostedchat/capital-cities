import json

# Load the capital-cities.json file
with open('capital-cities.json', 'r', encoding='utf-8') as f:
    countries_data = json.load(f)

# Initialize dictionaries for countries and timezones
countries_brief = {}
# timezones = []
timezones = set() 

# Loop through each country in the data
for country in countries_data:
    iso2 = country.get("iso2")
    name = country.get("name")
    currency = country.get("currency")
    currency_name = country.get("currency_name")
    currency_symbol = country.get("currency_symbol")
    
    # Extract the first timezone (if it exists)
    timezone = None
    if country.get("timezones"):
        timezone = country["timezones"][0]["gmtOffsetName"]


    if country.get("timezones"):
        for tz in country["timezones"]:
            gmt_offset = tz.get("gmtOffset")
            tz_name = tz.get("tzName")
            zoneName = tz.get("zoneName")
            if gmt_offset is not None and tz_name:
                # Format the GMT offset correctly (example: GMT+4:30)
                sign = "+" if gmt_offset >= 0 else "-"
                hours = abs(gmt_offset) // 3600
                minutes = (abs(gmt_offset) % 3600) // 60
                formatted_offset = f"(GMT{sign}{hours:02}:{minutes:02})"
                timezone = f"{formatted_offset} {zoneName}"
                timezones.add(f"{formatted_offset} {zoneName}")
    # Add country data to countries_brief dictionary
    countries_brief[iso2] = {
        "name": name,
        "currency": currency,
        "currency_name": currency_name,
        "currency_symbol": currency_symbol,
        "timezone": timezone
    }

    # Collect timezones in the format (GMT+offset) city
    

# Save the countries_brief data to countries_brief.json
with open('countries_brief.json', 'w', encoding='utf-8') as f:
    json.dump(countries_brief, f, ensure_ascii=False, indent=4)

# Save the timezones data to timezones.json
sorted_timezones = sorted(timezones, key=lambda x: x.split()[0])

with open('timezones.json', 'w', encoding='utf-8') as f:
    json.dump(sorted_timezones, f, ensure_ascii=False, indent=4)

print("Data has been saved to 'countries_brief.json' and 'timezones.json'.")
