import pandas as pd
import glob
import os

# Step 1: Load all CSV files from data/ folder
csv_files = glob.glob(os.path.join('data', '*.csv'))

# Step 2: Read and process each CSV
data_frames = []

for file in csv_files:
    df = pd.read_csv(file)
    
    # Step 3: Filter for Pink Morsel
    df = df[df['product'] == 'pink morsel']
    
    # Step 4: Calculate 'sales' column
    df['sales'] = df['quantity'] * df['price']
    
    # Step 5: Keep only 'sales', 'date', 'region'
    df = df[['sales', 'date', 'region']]
    
    data_frames.append(df)

# Step 6: Combine all into one DataFrame
combined_df = pd.concat(data_frames)

# Step 7: Export to CSV
combined_df.to_csv('processed_data.csv', index=False)

print("✅ Data processed and saved to processed_data.csv")
