import pandas as pd

nba=pd.read_csv("pandas/nba.csv")

# print(nba.to_string())
# print(nba.columns)
# print(nba.axes)
# print(nba.info())



# as type method
# print(nba.info())
# print(nba.head().to_string())
# nba["Salary"].fillna(0,inplace=True)
# nba["Number"].fillna(0,inplace=True)
# nba["Age"].fillna(0,inplace=True)
# nba["College"].fillna("None",inplace=True)
# print(nba.head().to_string())
#
# print(nba.dtypes)
# print(nba.info())
#
# print(nba["Salary"])
# nba["Salary"]=nba["Salary"].astype("int")
# print(nba["Salary"])
#
# print(nba["Number"])
# nba["Number"]=nba["Number"].astype("int")
# print(nba["Number"])
#
# print(nba["Age"])
# nba["Age"]=nba["Age"].astype("float")
# print(nba["Age"])
#
# print(nba["Position"].nunique())
# nba["Position"]=nba["Position"].astype("category")
# print(nba.dtypes)
# print(nba.info())
#
# print(nba["Team"].nunique())
# nba["Team"]=nba["Team"].astype("category")
# print(nba.dtypes)
# print(nba.info())

#  Sort a dataframe
# print(nba.sort_values("Name",ascending=False))
# nba.sort_values("Salary",ascending=False,inplace=True,na_position="first" )
# print(nba.head())

# Rank Series and rank method
# nba=nba.dropna(how="all")
# nba["Salary"] = nba["Salary"].fillna(0).astype("int")
# nba["Salary Rank"]= nba["Salary"].rank(ascending=False).astype("int")
# print(nba.sort_values(by= "Salary",ascending=False))
# print(nba.head(5))
#




