# -*- coding: iso-8859-1 -*-

en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
de_fr = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}
print en_de
print en_de["red"]
print "The French word for red is: " + de_fr[en_de["red"]]

dictionaries = {"en_de" : en_de, "de_fr" : de_fr }
print dictionaries["de_fr"]["blau"]

dic = { (1,2,3):"abc", 3.1415:"abc"}

print dic

for key in en_de.iterkeys():
    print key

#from list to dictionaries

countries = ["Italy", "Germany", "Spain", "USA", "Switzerland"]
dishes = ["pizza", "sauerkraut", "paella", "Hamburger"]

country_specialities = zip(countries,dishes)
print country_specialities
country_specialities_dict = dict(country_specialities)
print country_specialities_dict
