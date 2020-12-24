import pandas as pd

print("Hello Pandas")

# 1D array
ice_cream=["Chocolate",'Vanilla','Strawberry','Rum Raisin']
# print(pd.Series(ice_cream))

lottery=[4,8,15,16,23,42]
# print(pd.Series(lottery))

registrations=[True,False,True,False,False,True]
# print(pd.Series(registrations))

webster={"Cat":'animal' , 'Banana':'fruit','Cyan':'color','1':'integer' }
# print(pd.Series(webster))

about_me=['smart','handsome','charming','brilliant','humble']
s=pd.Series(about_me)
# print(s)
# print(s.values)
# print(s.index)
# print(s.dtype)

prices=[2.99,4.45,1.36]
s=pd.Series(prices)
# print(s.sum())
# print(s.product())
# print(s.mean())








