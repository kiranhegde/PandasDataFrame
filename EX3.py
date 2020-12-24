###############################################################
# DO NOT DELETE THIS CODE. IT IS NEEDED FOR THE TESTS TO RUN. #
# from ignore import pd                                         #
###############################################################

# Assume pandas ha salready been imported and assigned to the alias "pd".

flavors = ["Spicy Sweet Chili", "Cool Ranch", "Nacho Cheese", "Salsa Verde"]

# Create a new Series object, passing in the flavors list defined above
# Assign it to a 'doritos' variable. The resulting Series should look like this:
#
#
#   0    Spicy Sweet Chili
#   1           Cool Ranch
#   2         Nacho Cheese
#   3          Salsa Verde
#   dtype: object

# Below, sort the doritos Series in descending order.
# Make sure the operation is permanent.
# The Series should like this afterwards:
#
#   0    Spicy Sweet Chili
#   3          Salsa Verde
#   2         Nacho Cheese
#   1           Cool Ranch
#   dtype: object

# Below, sort the doritos Series index in descending order.
# Make sure the operation is permanent.
# The Series should like this afterwards:
#
#   3          Salsa Verde
#   2         Nacho Cheese
#   1           Cool Ranch
#   0    Spicy Sweet Chili
#   dtype: object
import pandas as pd

doritos=pd.Series(flavors)
doritos.sort_values(ascending=False,inplace=True)
# print(doritos)
doritos.sort_index(ascending=False,inplace=True)
# print(doritos)


