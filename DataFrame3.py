import pandas as pd

bond=pd.read_csv("pandas/jamesbond.csv")

# print(bond.head(3).to_string())

bond.set_index(keys="Film",inplace=True)
# print(bond.head(3).to_string())

# bond.reset_index()
# bond.reset_index(drop=False,inplace=True)
# print(bond.head(3).to_string())

# Use reset index before setting index to new column
# bond.reset_index(inplace=True)
# bond.set_index("Year",inplace=True)
# print(bond.head(3).to_string())


# retrieve rows by index label with .loc[]

# bond=pd.read_csv("pandas/jamesbond.csv",index_col="Film")

bond.sort_index(inplace=True)
# print(bond.head(3).to_string())

# print()
# print(bond.loc["Goldfinger"])
# print(bond.loc["GoldenEye"])
# print(bond.loc["Casino Royale"])

# print(bond.loc["Diamonds Are Forever":"From Russia with Love" ])
# skip/jump by 2
# print(bond.loc["Diamonds Are Forever":"From Russia with Love":2 ])
#Skip
# print(bond.loc[:"From Russia with Love"])
# print(bond.loc[["Die Another Day","Octopussy"]])
# print(bond.loc[["Octopussy","Die Another Day"]])

print( "Gold Bond" in bond.index)

# iloc
bond.reset_index(inplace=True)
# print(bond.iloc[0])
# print(bond.iloc[15])
# print(bond.iloc[15:20])
#
# print(bond.iloc[4:8])
# print(bond.iloc[:4])

bond.sort_index(inplace=True)
bond.set_index(keys="Film",inplace=True)
# print(bond.iloc[0])
# print(bond.iloc[15])
# print(bond.iloc[15:20])
#
# print(bond.iloc[4:8])
# print(bond.iloc[:4])



# bond.reset_index(inplace=True)
bond=pd.read_csv("pandas/jamesbond.csv",index_col="Film")
bond.sort_index(inplace=True)

# print(bond.loc["Moonraker","Actor"])
# print(bond.loc["Moonraker","Director"])
# print(bond.loc["Moonraker",["Director","Box Office"]])
# print(bond.loc[["Moonraker","A View to a Kill"], ["Director","Box Office"]])
# print(bond.loc["Moonraker","Director":"Budget"])
# print(bond.loc["Moonraker":"Thunderball","Director":"Budget"])
# print(bond.loc["Moonraker","Director":])
# print(bond.loc[:"Moonraker","Director":])
#
# print(bond.iloc[14,2:5])
# print(bond.iloc[[14,17],2:5])
# print(bond.iloc[:7,[2,5]])

# Set new value to a cell
print(bond.loc["Dr. No","Actor"])
bond.loc["Dr. No","Actor"]="Sir Sean Connery"
print(bond.loc["Dr. No","Actor"])

print(bond.loc["Dr. No",["Box Office","Budget","Bond Actor Salary"]])
bond.loc["Dr. No",["Box Office","Budget","Bond Actor Salary"]]=[448000000,7000000,600000]
print(bond.loc["Dr. No",["Box Office","Budget","Bond Actor Salary"]])


