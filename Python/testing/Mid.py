import pandas as pd

df = pd.read_csv('supermarket_sales - Sheet1.csv')

# Check for empty data in a specific column (e.g. 'column_name')
df['Gender'].fillna('Unknown', inplace=True)

print(df)