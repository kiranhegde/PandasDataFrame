import pandas as pd

df=pd.read_csv("pandas/employees.csv")


# Memory optimisation
# # check data types in info, if they are correct
# print(df.info())
# df["Start Date"]=pd.to_datetime(df["Start Date"])
# df["Last Login Time"]=pd.to_datetime(df["Last Login Time"])
# df["Senior Management"]=df["Senior Management"].astype("bool")
# df["Gender"]=df["Gender"].astype("category")
# print(df.head().to_string())
# print(df.info())
#
#
# # 2nd method
df=pd.read_csv("pandas/employees.csv",parse_dates=["Start Date","Last Login Time"])
# df["Start Date"]=pd.to_datetime(df["Start Date"])
# df["Last Login Time"]=pd.to_datetime(df["Last Login Time"])
df["Senior Management"]=df["Senior Management"].astype("bool")
df["Gender"]=df["Gender"].astype("category")
# print(df.head().to_string())
# print(df.info())

# # prints True/False
# print(df["Gender"] == "Male")
# # prints only Male
# print(df[df["Gender"] == "Male"])
#
# mask=df["Team"] == "Finance"
# print(df[mask])

# printing boolian
# df.dropna(inplace=True)
# print(df[df["Senior Management"]])
# mask=df["Team"] != "Marketting"
# mask=df["Salary"] > 11000
# mask=df["Bonus %"] < 1.5
# mask=df["Start Date"] < "1985-01-01"
# print(df[mask].to_string())

# Filter more than one condition
mask1= df["Gender"] == "Male"
mask2= df["Team"] == "Marketing"
# print(df[mask1 & mask2 ])

mask1= df["Senior Management"]
mask2=df["Start Date"] < "1990-01-01"

# print(df[mask1 | mask2 ])

mask1=df["First Name"] == "Robert"
mask2=df["Team"] == "Client Services"
mask3=df["Start Date"] > "2016-06-01"

# print(df[ (mask1 & mask2) | mask3])

# isin method

mask1=df["Team"] == "Legal"
mask2=df["Team"] == "Sales"
mask3=df["Team"] == "Product"
# print(df[mask1 | mask2 | mask3])

mask0=df["Team"].isin(["Legal","Sales","Product"])
# print(mask0)


# isnull,notnull
mask0=df["Team"].isnull()
mask1=df["Gender"].notnull()
# print(mask1)
# print(mask1)

# between
mask1=df["Salary"].between(60000,70000)
mask2=df["Bonus %"].between(2.0,5.0)
mask3=df["Start Date"].between("1991-01-01","1992-01-01")
# print(mask3)
# print(df[mask3])

# print(df[mask].to_string())

# duplicate method
df.sort_values("First Name",inplace=True)
mask1=~df["First Name"].duplicated(keep='last')
# print(df[mask1])

# drop duplicated
# print(len(df))
# print(len(df.drop_duplicates()))
mask1=df.drop_duplicates(subset=["First Name"],keep="first" )
mask2=df.drop_duplicates(subset=["First Name"],keep=False )

# print(mask1)
# print(mask2)

mask3=df.drop_duplicates(subset=["First Name","Team"],keep=False )
# print(mask3)

# unique, nunique
mask1=df["Gender"].unique()
mask2=df["Team"].unique()
mask3=df["Team"].nunique(dropna=False)

print(mask1)
print(mask2)
print(mask3)

