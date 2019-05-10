# Exercise 2

# Satellites:
sat_database = {"METEOSAT" : 3000,
                "LANDSAT"  : 30,
                "MODIS"    : 500
                }

# The dictionary above contains the names and spatial resolutions of some satellite systems.

# 1) Add the "GOES" and "worldview" satellites with their 2000/0.31m resolution to the dictionary [2P]
sat_database["GOES"] = 2000
sat_database["worldview"] = 0.31

print("I have the following satellites in my database:")

# 2) print out all satellite names contained in the dictionary [2P]
print(sat_database.keys())

# 3) Ask the user to enter the satellite name from which she/he would like to know the resolution [2P]
answer = input("Which satellite you would like to know the resolution of? Please enter its name: ")
 

# 4) Check, if the satellite is in the database and inform the user, if it is not [2P]
tempvar = answer in sat_database
if tempvar == True:
    print("Your entered satellite is part of our database.")
else:
    print("Unfortunately your entered satellite is not part of our database.")

# 5) If the satellite name is in the database, print a meaningful message containing the satellite's name and its resolution [2P] 
for key, val in sat_database.items():
    if answer == key:
        print("The satellite {} has the resolution {}.".format(key, val))
        break

