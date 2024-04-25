# creating Dataframes
import pandas as pd

# make a data variable for Dataframe contructor
data = {
    'Name': ['John', 'Anna', 'Peter'],
    'Age': [28, 24, 33],
    'City': ['New York', 'Los Angeles', 'Chicago']
}




# creating a Dataframe
df = pd.DataFrame(data)

# printing the Dataframe
print(df)

# printing the Dataframe
print(df.head())

# printing the Dataframe

print(df.tail())

# printing the Dataframe
print(df.shape)

# printing the Dataframe
print(df.info())

# printing the Dataframe
print(df.describe())
# printing the Dataframe
print(df.columns)

# printing the Dataframe
print(df.index)

# printing the Dataframe
print(df.values)

# printing the Dataframe
print(df.dtypes)

# printing the Dataframe
