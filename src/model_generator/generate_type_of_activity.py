import pandas as pd
import os

# Define the mode of transport list
type_of_activity = [
    'Fuel Use',
    'Fuel Use and Vehicle Distance', 
    'Vehicle Distance (e.g. Road Transport)', 
    'Custom fuel', 
    'Custom vehicle']

# Create a DataFrame with an ID column
transport_df = pd.DataFrame({
    "id": range(1, len(type_of_activity) + 1),  # Generating IDs starting from 1
    "type_of_activity": type_of_activity
})

# Define the output path
output_dir = 'src/model_generator/outputs'
output_path = os.path.join(output_dir, 'type_of_activity_dim.csv')

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Save the DataFrame to CSV
transport_df.to_csv(output_path, index=False)
print(f"CSV file 'type_of_activity_dim.csv' created successfully at {output_path}.")