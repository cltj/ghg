import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Predefined list of addresses and customer names
addresses = [fake.address() for _ in range(30)]
customer_names = [fake.name() for _ in range(30)]

def generate_electric_data(id):
    billing_period_start = fake.date_time_between(start_date=datetime(2023, 1, 1), end_date=datetime.today() - timedelta(days=30))
    billing_period_end = billing_period_start + timedelta(days=30)
    previous_reading = round(random.uniform(1000, 5000), 2)
    current_reading = previous_reading + round(random.uniform(100, 500), 2)
    usage_kwh = current_reading - previous_reading
    energy_charge = round(usage_kwh * random.uniform(0.1, 0.2), 2)
    service_charge = round(random.uniform(10, 20), 2)
    taxes = round((energy_charge + service_charge) * 0.1, 2)
    total_cost = energy_charge + service_charge + taxes

    return {
        "id": id,
        "customer_name": random.choice(customer_names),
        "account_number": fake.unique.random_number(digits=10),
        "billing_address": random.choice(addresses),
        "billing_period_start": billing_period_start.strftime("%Y-%m-%d"),
        "billing_period_end": billing_period_end.strftime("%Y-%m-%d"),
        "due_date": (billing_period_end + timedelta(days=15)).strftime("%Y-%m-%d"),
        "previous_reading": previous_reading,
        "current_reading": current_reading,
        "usage_kwh": usage_kwh,
        "energy_charge": energy_charge,
        "service_charge": service_charge,
        "taxes": taxes,
        "total_cost": total_cost,
        "street_address": random.choice(addresses)
    }

def write_electric_data_to_csv(filename, num_rows):
    fieldnames = [
        "id", "customer_name", "account_number", "billing_address", "billing_period_start",
        "billing_period_end", "due_date", "previous_reading", "current_reading", "usage_kwh",
        "energy_charge", "service_charge", "taxes", "total_cost", "street_address"
    ]
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(1, num_rows + 1):
            data = generate_electric_data(i)
            print(data)  # Debugging: Print the generated data
            writer.writerow(data)

# Define the number of rows you want to generate
num_rows = 100
write_electric_data_to_csv('dummy_electric_data.csv', num_rows)

# Function to generate dummy fleet data
def generate_fleet_data(id):
    fuel_types = ['diesel', 'gasoline', 'gas', 'hybrid', 'electric']
    distance_traveled = round(random.uniform(1000, 50000), 2)
    departure_time = fake.date_time_between(start_date='-1y', end_date='now')
    arrival_time = departure_time + timedelta(hours=random.uniform(1, 12))
    
    return {
        "truck_id": id,
        "fuel_type": random.choice(fuel_types),
        "distance_traveled": distance_traveled,
        "from_location": fake.city(),
        "to_location": fake.city(),
        "departure_time": departure_time.strftime("%Y-%m-%d %H:%M:%S"),
        "arrival_time": arrival_time.strftime("%Y-%m-%d %H:%M:%S")
    }

def write_fleet_data_to_csv(filename, num_rows):
    fieldnames = ["truck_id", "fuel_type", "distance_traveled", "from_location", "to_location", "departure_time", "arrival_time"]
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(1, num_rows + 1):
            data = generate_fleet_data(i)
            print(data)  # Debugging: Print the generated data
            writer.writerow(data)

# Define the number of rows you want to generate for fleet data
num_rows_fleet = 200
write_fleet_data_to_csv('dummy_fleet_data.csv', num_rows_fleet)