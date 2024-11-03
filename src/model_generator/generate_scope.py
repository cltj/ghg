import pandas as pd
import os

scope = [(1, "Scope 1"), (2, "Scope 2"), (3, "Scope 3")]

scope_data = [{"id": id, "scope": name} for id, name in scope]
scope_df = pd.DataFrame(scope_data)

output_dir = 'src/model_generator/outputs'
output_path = os.path.join(output_dir, 'scope_dim.csv')
os.makedirs(output_dir, exist_ok=True)
scope_df.to_csv(output_path, index=False)
print(f"CSV file 'scope_dim.csv' created successfully at {output_path}.")