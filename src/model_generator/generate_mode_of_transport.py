import pandas as pd
import os

# Define the mode of transport list
mode_of_transport = ['Road', 'Rail', 'Water', 'Aircraft', 'Offroad']

# Create a DataFrame with an ID column
transport_df = pd.DataFrame({
    "id": range(1, len(mode_of_transport) + 1),  # Generating IDs starting from 1
    "mode_of_transport": mode_of_transport
})

# Define the output path
output_dir = 'src/model_generator/outputs'
output_path = os.path.join(output_dir, 'mode_of_transport_dim.csv')

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Save the DataFrame to CSV
transport_df.to_csv(output_path, index=False)
print(f"CSV file 'mode_of_transport_dim.csv' created successfully at {output_path}.")
