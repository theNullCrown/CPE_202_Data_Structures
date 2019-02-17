

## Allie Blaising 
## CPE 202


# Given weight on earth and string representing planet, return weight on planet
# If string does not match a planet, raise ValueError
def weight_on_planets(earth_weight, planet):
   if planet == "Mars": 
        pounds = 0.38*earth_weight
        return pounds
   elif planet == "Jupiter": 
        pounds = 2.34*earth_weight
        return pounds
   elif planet == "Venus": 
        pounds = 0.91*earth_weight
   else: 
        raise ValueError
   return pounds 


if __name__ == '__main__':
    pounds = float(input("What do you weigh on earth? "))
    print("\nOn Mars you would weigh", weight_on_planets(pounds, 'Mars'), "pounds.\n" +
          "On Jupiter you would weigh", weight_on_planets(pounds, 'Jupiter'), "pounds.")