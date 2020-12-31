import pandas as pd

bond=pd.read_csv("pandas/jamesbond.csv")

# print(bond.head(3).to_string())

bond.set_index(keys="Film",inplace=True)
# print(bond.head(3).to_string())

# bond.reset_index()
# bond.reset_index(drop=False,inplace=True)
# print(bond.head(3).to_string())

# Use reset index before setting index to new column
bond.reset_index(inplace=True)
bond.set_index("Year",inplace=True)

print(bond.head(3).to_string())



