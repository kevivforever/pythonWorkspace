capital_country = {"United States" : "Washington", 
                   "US" : "Washington", 
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}

print("Countries and their capitals:")
print
for c in capital_country:
    print("{country}: {capital}".format(country=c, capital=capital_country[c]))

print "************************"

capital_country = {"United States" : "Washington", 
                   "US" : "Washington", 
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}

print("Countries and their capitals:")
print
for c in capital_country:
    format_string = c + ": {" + c + "}" 
    print(format_string.format(**capital_country))
