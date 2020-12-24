import pandas as pd
import matplotlib.pyplot as plt
# DF to Series format
pokemon=pd.read_csv('pandas/pokemon.csv',usecols=['Pokemon'],squeeze=True)
# print(pokemon)

google_stock=pd.read_csv('pandas/google_stock_price.csv', usecols=['Stock Price'], squeeze=True)
# print(google_stock)
# print(google_stock.head(9))
# print(google_stock.tail())
# google_stock.plot()
# plt.show()

# print(dir(google_stock))

# print(pokemon.shape)
# print(pokemon.name)
# print(pokemon.sort_values(ascending=True))

google=google_stock.sort_values()
# inplace make modificcation to original series
google.sort_values(ascending=False,inplace=True)
# print(google)
# print(google.head())

# index position
pokemon.sort_values(ascending=True,inplace=True )
# print(pokemon)
pokemon.sort_index(ascending=True,inplace=True )
# print(pokemon)


# in keyword
# print(pokemon)
# print("Bulbasaur" in pokemon.values)

# index position
# print(pokemon[100])
# print(pokemon[[100,200,300]])
# print(pokemon[50:101])


# index labeling
pokemons=pd.read_csv('pandas/pokemon.csv',index_col='Pokemon',squeeze=True)
# print(pokemons)
# print(pokemons[0])
# print(pokemons[[100,134]])
#
# print(pokemons['Bulbasaur'])
# print(pokemons['Ditto'])
# print(pokemons[["Charizard",'Jolteon']])
# print(pokemons["Charmander":'Weedle':2])

# print(pokemons["kiran"])


# print(pokemons.reindex(index=['Pikachu','Digimon']))


# get method
pokemons.sort_index(inplace=True)
print(pokemons.head(3))
print(pokemons.get(0))
print(pokemons.get("Moltres"))
print(pokemons.get(["Moltres","Meowth"]))
# default message
print(pokemons.get(key="kiran",default="THis is not a Pokemon" ))
print(pokemons.get(key=[0,5,10,3000],default="This is not a Pokemon" ))



















