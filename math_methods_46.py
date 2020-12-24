import pandas as pd

google=pd.read_csv("pandas/google_stock_price.csv",squeeze=True)

# print(google.head(3))
# print(google.sum())
# print(google.mean())
# print(google.sum()/google.count())
# print(google.count())
# print(len(google))
# print(google.max())
# print(google.min())
# print(google.median())
# print(google.mode())
# print(google.describe())


# idxmax, idxmin
# print(google.max())
# print(google.min())
# print(google.idxmin())
# print(google.idxmax())
# print(google[google.idxmin()])

# value count method

pokemons=pd.read_csv('pandas/pokemon.csv',index_col='Pokemon',squeeze=True)

# print(pokemons.value_counts())
# print(pokemons.value_counts().sum())
# print(pokemons.count())
# print(pokemons.value_counts(ascending=True))

# apply
# print(google.head(6))

def classify_performance(number):
    if  number < 300:
        return "OK"
    elif number >=300 and number <650:
        return "Satisfacory"
    else:
        return "Incredible"

# print(google.apply(classify_performance).tail())
#
# print(google.apply(lambda stock_price : stock_price+1))


#  map

pokemon_names=pd.read_csv('pandas/pokemon.csv',usecols=['Pokemon'],squeeze=True)
print(pokemon_names.head(3))

pokemon_types=pd.read_csv('pandas/pokemon.csv',index_col='Pokemon',squeeze=True)
print(pokemon_types.head(3))

print(pokemon_names.map(pokemon_types))

