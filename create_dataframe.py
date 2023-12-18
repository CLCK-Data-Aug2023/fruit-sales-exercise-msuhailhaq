import pandas as pd

# Create a Pandas DataFrame
data = {
    'Apples': [35, 41],
    'Bananas': [21, 34],
}

df = pd.DataFrame(data, index=['2017 Sales', '2018 Sales'])

# Write the DataFrame to a CSV file
df.to_csv('fruit.csv')

# Print the DataFrame
print(df)