x = set("A Python Tutorial")
print (type(x))
print (x)

y = set(["Perl", "Python", "Java"])
print (y)

cities = set(("Paris", "Lyon", "London","Berlin","Paris","Birmingham"))
print (cities)

cities.add("Strasbourg")
print (cities)

cities = frozenset(["Frankfurt", "Basel","Freiburg"])
#frozensets cant be changed
#following address will give error
#cities.add("Strasbourg")

adjectives = {"cheap","expensive","inexpensive","economical"}
print (adjectives)

adjectives_backup = adjectives.copy()
print (adjectives_backup)

adjectives.clear()
print (adjectives)

a = {"a","b","c","d","e"}
b = {"b","c"}
c = {"c","d"}
print (a.difference(b))
print (a.difference(b).difference(c))

#another of doing difference
print (a - b)
print (a - b - c)

a.difference_update(b)
print (a)

a.discard("a")
print (a)

#will not give error if elemet is not present in set
a.discard("z")
print (a)

a.remove("e")
print (a)
#remove will give error if tried to remove an element which is not present

print (b.intersection(c))
print (b & c)

print (a.issubset(c))
print (a < c)
print (c.issuperset(a))
print (c > a)

letters = {"a","b","c","d","e"}
print (letters.pop())
print (letters)
print (letters.pop())
print (letters)


