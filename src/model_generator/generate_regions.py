import pandas as pd

regions_data = {
    "UK": {
        "country_code": "GB",
        "countries": [{"name": "United Kingdom", "currency_code": "GBP"}],
        "units": {
            "distance": "miles",
            "fuel": "litres",
            "temperature": "Celsius"
        },
    },
    "Europe": {
        "country_code": "EU",
        "countries": [
            {"name": "France", "currency_code": "EUR"},
            {"name": "Germany", "currency_code": "EUR"},
            {"name": "Spain", "currency_code": "EUR"},
            {"name": "Italy", "currency_code": "EUR"},
            {"name": "Netherlands", "currency_code": "EUR"},
            {"name": "Sweden", "currency_code": "SEK"},
            {"name": "Norway", "currency_code": "NOK"},
            {"name": "Finland", "currency_code": "EUR"},
            {"name": "Poland", "currency_code": "PLN"},
            {"name": "Belgium", "currency_code": "EUR"},
            {"name": "Denmark", "currency_code": "DKK"},
            {"name": "Switzerland", "currency_code": "CHF"}
        ],
        "units": {
            "distance": "kilometers",
            "fuel": "litres",
            "temperature": "Celsius"
        },
    },
    "Asia": {
        "country_code": "AS",
        "countries": [
            {"name": "Japan", "currency_code": "JPY"},
            {"name": "China", "currency_code": "CNY"},
            {"name": "India", "currency_code": "INR"}
        ],
        "units": {
            "distance": "kilometers",
            "fuel": "litres",
            "temperature": "Celsius"
        },
    },
    "North America": {
        "country_code": "NA",
        "countries": [
            {"name": "United States", "currency_code": "USD"},
            {"name": "Canada", "currency_code": "CAD"}
        ],
        "units": {
            "distance": "miles",
            "fuel": "gallons",
            "temperature": "Fahrenheit"
        },
    },
    "Oceania": {
        "country_code": "OC",
        "countries": [
            {"name": "Australia", "currency_code": "AUD"},
            {"name": "New Zealand", "currency_code": "NZD"}
        ],
        "units": {
            "distance": "kilometers",
            "fuel": "litres",
            "temperature": "Celsius"
        },
    }
}

# Convert regions_data dictionary to a list of rows with each country as a separate row
region_rows = []
unique_id = 1  # Initialize unique ID

for region, details in regions_data.items():
    for country in details["countries"]:
        country_name = country["name"]
        currency_code = country["currency_code"]
        
        row = {
            "id": unique_id,
            "Region": region,
            "Country Code": details["country_code"],
            "Country": country_name,
            "Distance Unit": details["units"]["distance"],
            "Fuel Unit": details["units"]["fuel"],
            "Temperature Unit": details["units"]["temperature"],
            "Currency Code": currency_code
        }
        region_rows.append(row)
        unique_id += 1  # Increment unique ID for each row

# Create a DataFrame
regions_df = pd.DataFrame(region_rows)

# Save to CSV
regions_df.to_csv('src/model_generator/outputs/regions_dim.csv', index=False)
print("CSV file 'regions_dim.csv' created successfully.")
