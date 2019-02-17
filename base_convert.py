# Project 1: Name: Allie Blaising 

## Base convert function 

def convert(num, b):
   convert_string = "0123456789ABCDEF" 
   if num < b: # base case, when num < b, then we can grab the character at string index num 
   # and send back to recursively add character associated with index 
   # num // b 
      return convert_string[num] # base case that once met feeds back into recursive call below
   else:
      return convert(num // b, b) + convert_string[num % b] # recursively call convert and concatinate return value with remainder index


"""Recursive function that returns a string representing num in the base b"""

