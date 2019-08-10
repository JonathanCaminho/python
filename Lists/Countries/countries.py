# Testing all functions of chapter 3
countries = ['Norway', 'Albania', 'Trindad e Tobago',
             "Côte d'Ivoire", 'Switzerland',
             'Myanmar', 'South Africa', 'Mozambique',
             'France', 'Caledonia', 'Wales']

print(countries[1])
print(countries[3])
message = "The Fourth country is " + countries[3].title() + "."
print(message)
countries[5] = "Brazil"
countries.append("USA")
print(countries)
countries.insert(3,'Canada')
print(countries)
del countries[5]
print(countries)
countries.pop(7)
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)
print(sorted(countries))
print(sorted(countries,reverse=True))
countries.reverse()
print(countries)
countries.reverse()
print(countries)
print(str(len(countries)) + " Countries ")