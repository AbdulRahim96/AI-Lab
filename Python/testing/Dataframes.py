# creating Dataframes
import pandas as pd

# make a data variable for Dataframe contructor
data = {
    'Name': ['John', 'Anna', 'Peter', 'ars'],
    'Age': [28, 24, 33, 27],
    'City': ['New York', 'Los Angeles', 'Chicago', 'pak']
}




# creating a Dataframe
df = pd.DataFrame(data)

# printing the Dataframe
print(df,"\n")

# printing the Dataframe
print(df.head(),"\n")

# printing the Dataframe

print(df.tail(),"\n")

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
