import pandas as pd
import os

fuel_economy_data = {
    "Petrol (100% mineral petrol) (Motor Gasoline)": {
        "Passenger Car": {
            "Small car, <1.4 litre": {"mpg": 39.1, "km/L": 16.6},
            "Medium car, 1.4 - 2.0 litres": {"mpg": 30.9, "km/L": 13.1},
            "Large car, >2.0 litres": {"mpg": 20.2, "km/L": 8.6},
            "Average car": {"mpg": 33.6, "km/L": 14.3},
        },
        "Vans": {
            "Class I, ≤1.305 tonnes": {"mpg": 30.2, "km/L": 12.8},
            "Class II, >1.305 to ≤1.74 tonnes": {"mpg": 28.1, "km/L": 11.9},
            "Class III, >1.74 to ≤3.5 tonnes": {"mpg": 17.5, "km/L": 7.4},
            "Average (up to 3.5 tonnes)": {"mpg": 27.3, "km/L": 11.6},
        },
        "Motorbike": {
            "Small, ≤125 cc": {"mpg": 67.7, "km/L": 28.8},
            "Medium, >125 and ≤500 cc": {"mpg": 55.8, "km/L": 23.7},
            "Large, >500 cc": {"mpg": 41.9, "km/L": 17.8},
            "Average": {"mpg": 49.2, "km/L": 20.9},
        }
    },
    "Diesel (100% mineral diesel)": {
        "Passenger Car": {
            "Small car, <1.7 litre": {"mpg": 44.9, "km/L": 19.1},
            "Medium car, 1.7 - 2.0 litres": {"mpg": 37.3, "km/L": 15.9},
            "Large car, >2.0 litres": {"mpg": 29.9, "km/L": 12.7},
            "Average car": {"mpg": 36.7, "km/L": 15.6},
        },
        "Vans": {
            "Average (up to 3.5 tonnes)": {"mpg": 26.9, "km/L": 11.4},
        },
        "HGV": {
            "Rigid - 3.5 - 7.5 tonnes - 0% Weight Laden": {"mpg": 13.8, "km/L": 5.9},
            "Rigid - 3.5 - 7.5 tonnes - 50% Weight Laden": {"mpg": 12.7, "km/L": 5.4},
            "Rigid - 3.5 - 7.5 tonnes - 100% Weight Laden": {"mpg": 11.8, "km/L": 5.0},
            "Rigid - 3.5 - 7.5 tonnes - Average Laden": {"mpg": 12.9, "km/L": 5.5},
            "Rigid - 7.5 - 17 tonnes - 0% Weight Laden": {"mpg": 11.6, "km/L": 4.9},
            "Rigid - 7.5 - 17 tonnes - 50% Weight Laden": {"mpg": 10.1, "km/L": 4.3},
            "Rigid - 7.5 - 17 tonnes - 100% Weight Laden": {"mpg": 9.0, "km/L": 3.8},
            "Rigid - 7.5 - 17 tonnes - Average Laden": {"mpg": 10.5, "km/L": 4.5},
            "Rigid - >17 tonnes - 0% Weight Laden": {"mpg": 8.4, "km/L": 3.6},
            "Rigid - >17 tonnes - 50% Weight Laden": {"mpg": 6.9, "km/L": 2.9},
            "Rigid - >17 tonnes - 100% Weight Laden": {"mpg": 5.8, "km/L": 2.5},
            "Rigid - >17 tonnes - Average Laden": {"mpg": 6.4, "km/L": 2.7},
            "Rigid - Average - Average Laden": {"mpg": 7.6, "km/L": 3.2},
            "Articulated - 3.5 - 33 tonnes - 0% Weight Laden": {"mpg": 10.2, "km/L": 4.4},
            "Articulated - 3.5 - 33 tonnes - 50% Weight Laden": {"mpg": 8.2, "km/L": 3.5},
            "Articulated - 3.5 - 33 tonnes - 100% Weight Laden": {"mpg": 6.8, "km/L": 2.9},
            "Articulated - 3.5 - 33 tonnes - Average Laden": {"mpg": 8.2, "km/L": 3.5},
            "Articulated - >33 tonnes - 0% Weight Laden": {"mpg": 10.0, "km/L": 4.2},
            "Articulated - >33 tonnes - 50% Weight Laden": {"mpg": 7.5, "km/L": 3.2},
            "Articulated - >33 tonnes - 100% Weight Laden": {"mpg": 6.0, "km/L": 2.5},
            "Articulated - >33 tonnes - Average Laden": {"mpg": 6.9, "km/L": 2.9},
            "Articulated - Average - Average Laden": {"mpg": 6.9, "km/L": 2.9},
            "Type Unknown - Average - Average Laden": {"mpg": 7.2, "km/L": 3.1},
        }
    },
    "Hybrid": {
        "Passenger Car": {
            "Small car, <1.4 litre": {"mpg": 54.6, "km/L": 23.2},
            "Medium car, 1.4 - 2.0 litres": {"mpg": 50.8, "km/L": 21.6},
            "Large car, >2.0 litres": {"mpg": 36.3, "km/L": 15.4},
            "Average car": {"mpg": 46.5, "km/L": 19.8}
        }
    },
    "Compressed Natural Gas (CNG)": {
        "Passenger Car": {
            "Medium car, 1.4 - 2.0 litres": {"mpg": 38.4, "km/L": 16.3},
            "Large car, >2.0 litres": {"mpg": 25.1, "km/L": 10.7},
            "Average car": {"mpg": 34.3, "km/L": 14.6}
        },
        "Vans": {
            "Average (up to 3.5 tonnes)": {"mpg": 25.7, "km/L": 10.9}
        }
    },
    "Liquefied Petroleum Gases (LPG)": {
        "Passenger Car": {
            "Medium car, 1.4 - 2.0 litres": {"mpg": 42.3, "km/L": 18.0},
            "Large car, >2.0 litres": {"mpg": 27.7, "km/L": 11.8},
            "Average car": {"mpg": 37.8, "km/L": 16.1}
        },
        "Vans": {
            "Average (up to 3.5 tonnes)": {"mpg": 29.2, "km/L": 12.4}
        }
    }
}


rows = []
unique_id = 1  
for fuel_type, vehicle_data in fuel_economy_data.items():
    for vehicle_class, engine_data in vehicle_data.items():
        for engine_size, fuel_stats in engine_data.items():
            row = {
                "id": unique_id,
                "Fuel Type": fuel_type,
                "Vehicle Class": vehicle_class,
                "Engine Size/Weight Class": engine_size,
                "MPG": fuel_stats["mpg"],
                "KM/L": fuel_stats["km/L"],
                "fk_mode_of_transport": "road"  # Adding the 'road' foreign key
            }
            rows.append(row)
            unique_id += 1  

fuel_df = pd.DataFrame(rows)

output_dir = 'src/model_generator/outputs'
output_path = os.path.join(output_dir, 'fuel_economy_dim.csv')
os.makedirs(output_dir, exist_ok=True)
fuel_df.to_csv(output_path, index=False)
print(f"CSV file 'fuel_economy_dim.csv' created successfully at {output_path}.")
