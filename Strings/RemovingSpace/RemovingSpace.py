# Jonathan - 08/03/2019

# Insert of the name
favorite_language = 'python '
# Printing the Name as original
print(favorite_language + "||")
# Printing the Result of rstrip() method
print(favorite_language.rstrip() + "||")
# Changing permanently to the without right space version
favorite_language = favorite_language.rstrip()
# Printing the New Name
print(favorite_language+"|")
favorite_language = ' python '
print(' |' + favorite_language + '| ')
print(' |' + favorite_language.rstrip() + '| ')
print(' |' + favorite_language.lstrip() + '| ')
print(' |' + favorite_language.strip() + "|")