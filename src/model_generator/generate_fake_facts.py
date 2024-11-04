
import faker
import random
import os
from datetime import datetime
import pandas as pd


# What i need to generate
# 1. id
# 2. date - ranom date between 2022 and 2024
# 3. fuel_used_id - random number between 1 and 9
# 4. type_of_activity_id - random number between 1 and 5
# 5. mode_of_transport_id - random number between 1 and 5
# 6. scope_id - random number between 1 and 3
# 7. distance_travelled - random number between 1 and 1000
# 8. fuel_used -
# 9. vehicle_type - random number between 1 and 4
# 10. engine_size
# 11. weight_class
# 12. source_description - random sentence (5-10 words)
# 13. region - random region from the list
# 14. country - random country from the list

# Create a Faker instance
fake = faker.Faker()

# Define the number of fake facts to generate
NUM_FAKE_FACTS = 1000

# Define the output directory
output_dir = 'src/model_generator/outputs'
os.makedirs(output_dir, exist_ok=True)
# Define the list of regions and their respective countries
regions_countries = {
    'UK': ["United Kingdom"],
    'EU': ["France", "Germany", "Spain", "Italy", "Netherlands", "Sweden", "Norway", "Finland", "Poland", "Belgium", "Denmark", "Switzerland"],
    'AS': ["Japan", "China", "India"],
    'NA': ["United States", "Canada"],
    'OC': ["Australia", "New Zealand"]
}

# Generate the fake facts
data = []

for unique_id in range(1, NUM_FAKE_FACTS + 1):
    region = random.choice(list(regions_countries.keys()))
    country = random.choice(regions_countries[region])
    
    row = {
        "id": unique_id,
        "date": fake.date_time_between_dates(datetime_start=datetime(2022, 1, 1), datetime_end=datetime(2024, 12, 31)).strftime('%Y-%m-%d'),
        "fuel_used": random.choice([
            "Petrol (100% mineral petrol) (Motor Gasoline)",
            "Diesel (100% mineral diesel)",
            "Hybrid",
            "Liquefied Petrolium Gases (LPG)",
            "Compressed Natural Gas (CNG)"
        ]),
        "type_of_activity": random.choice(["Fuel Use","Fuel Use and Vehicle Distance", "Vehicle Distance (e.g. Road Transport)", "Custom fuel", "Custom vehicle"]),
        "mode_of_transport": "Road", # ['Road', 'Rail', 'Water', 'Aircraft', 'Offroad']
        "scope_id": random.choice([1, 3]),
        "distance_travelled": random.randint(400, 1000),
        "fuel_used": random.choice([
            "Petrol (100% mineral petrol) (Motor Gasoline)",
            "Diesel (100% mineral diesel)",
            "Hybrid",
            "Liquefied Petrolium Gases (LPG)",
            "Compressed Natural Gas (CNG)"
        ]),
        "vehicle_type": random.choice(["Passenger car", "Vans"]),
        "engine_size": random.choice([1.3, 1.8, 2.0, 2.4, 3.0]),
        "weight_class": random.choice([random.randint(1000, 1300), random.randint(1300, 1740), random.randint(1740, 7500)]),
        "source_description": fake.sentence(nb_words=random.randint(3, 5)),
        "region": region,
        "country": country
    }
    data.append(row)

# Create a DataFrame and save it as a CSV file
df = pd.DataFrame(data)
output_file = os.path.join(output_dir, 'fake_facts.csv')
df.to_csv(output_file, index=False)

print(f"Generated {NUM_FAKE_FACTS} rows of data and saved to {output_file}")