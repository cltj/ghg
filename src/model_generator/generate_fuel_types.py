import pandas as pd
import os

fuel_used = [
    'Sub Bitumious Coal', 
    'Jet Kerosene', 
    'Aviation Gasoline', 
    'Petrol (100% mineral petrol) (Motor Gasoline)', #assuming this is the same as 'Motor Petrol/Gasoline'
    'Diesel (100% mineral diesel)', #assuming this is the same as 'On-Road Diesel Fuel'
    'Recidual Fuel',
    'Hybrid', # not originally in the list, but added for completeness
    'Liquefied Petrolium Gases (LPG)',
    'Compressed Natural Gas (CNG)'
    ]


fuel_df = pd.DataFrame({
    "id": range(1, len(fuel_used) + 1),  # Generating IDs starting from 1
    "fuel_used": fuel_used
})


output_dir = 'src/model_generator/outputs'
output_path = os.path.join(output_dir, 'fuel_used_dim.csv')
os.makedirs(output_dir, exist_ok=True)
fuel_df.to_csv(output_path, index=False)
print(f"CSV file 'fuel_used_dim.csv' created successfully at {output_path}.")
