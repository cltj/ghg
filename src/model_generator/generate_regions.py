import pandas as pd

regions_data = {
    "US": {
        "country_code": "US",
        "countries": ["United States"],
        "units": {
            "distance": "miles",
            "fuel": "gallons",
            "temperature": "Fahrenheit"
        },
        "currency": "USD",
    },
    "UK": {
        "country_code": "GB",
        "countries": ["United Kingdom"],
        "units": {
            "distance": "miles",
            "fuel": "litres",
            "temperature": "Celsius"
        },
        "currency": "GBP",
    },
    "Europe": {
        "country_code": "EU",
        "countries": ["France", "Germany", "Spain", "Italy", "Netherlands", "Sweden", "Norway", "Finland", "Poland", "Belgium"],
        "units": {
            "distance": "kilometers",
            "fuel": "litres",
            "temperature": "Celsius"
        },
        "currency": "EUR",
    }
}


region_rows = []
for region, details in regions_data.items():
    row = {
        "Region": region,
        "Country Code": details["country_code"],
        "Countries": ", ".join(details["countries"]),
        "Distance Unit": details["units_distance"],
        "Fuel Unit": details["units_fuel"],
        "Temperature Unit": details["units_temperature"],
        "Currency": details["currency"]
    }
    region_rows.append(row)

# Create a DataFrame
regions_df = pd.DataFrame(region_rows)

# Save to CSV
regions_df.to_csv('outputs/regions_data.csv', index=True)
print("CSV file 'regions_data.csv' created successfully.")