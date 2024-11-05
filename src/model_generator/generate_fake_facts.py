
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

# Generate the fake facts
data = []

for unique_id in range(1, NUM_FAKE_FACTS + 1):
    row = {
        "id": unique_id,
        "date": fake.date_time_between_dates(datetime_start=datetime(2022, 1, 1), datetime_end=datetime(2024, 12, 31)).strftime('%Y%m%d'),
        "fuel_used_id": random.randint(4,9),
        "type_of_activity_id": random.randint(1,5),
        "mode_of_transport_id": random.randint(1,5),
        "scope_id": random.choice([1, 3]),
        "distance_travelled": random.randint(400, 1000),
        "vehicle_class": random.randint(1, 51),
        "engine_size": round(random.uniform(1, 10), 1),
        "weight_class": random.randint(1000, 50000),
        "source_description": fake.sentence(nb_words=random.randint(3, 5)),
        "country_id": random.randint(1,20),
    }
    data.append(row)

# Create a DataFrame and save it as a CSV file
df = pd.DataFrame(data)
output_file = os.path.join(output_dir, 'fake_facts.csv')
df.to_csv(output_file, index=False)

print(f"Generated {NUM_FAKE_FACTS} rows of data and saved to {output_file}")