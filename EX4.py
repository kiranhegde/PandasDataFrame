###############################################################
# DO NOT DELETE THIS CODE. IT IS NEEDED FOR THE TESTS TO RUN. #
# from ignore import pd
import pandas as pd
###############################################################

# Let's say I have a dictionary that maps guitar types
# to their colors
guitars_dict = {
    "Fender Telecaster": "Baby Blue",
    "Gibson Les Paul": "Sunburst",
    "ESP Eclipse": "Dark Green"
}

# Create a new Series object, passing in the guitars_dict dictionary as the data source.
# Assign the resulting Series to a "guitars" variable.


# Access the value for the index position of 0 within the "guitars" Series.
# Assign the value to a "fender_color" variable.


# Access the value for the index label of "Gibson Les Paul" in the "guitars" Series.
# Assign the value to a "gibson_color" variable.


# Access the value for the index label of "ESP Eclipse" in the "guitars" Series.
# Assign the value to a "esp_color" variable.

guitars=pd.Series(guitars_dict)
print(guitars)
guitars=pd.Series(guitars_dict)
fender_color=guitars[0]
gibson_color=guitars["Gibson Les Paul"]
esp_color=guitars["ESP Eclipse"]

print(fender_color,gibson_color,esp_color)
