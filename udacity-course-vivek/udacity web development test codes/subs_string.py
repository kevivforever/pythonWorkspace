given_string = "I think %s is a perfectly normal thing to do in public."
def sub1(s):
    #return given_string.replace("%s",s)
    return given_string % s

given_string2 = "I think %s and %s are perfectly normal things to do in public."
def sub2(s1, s2):
    return given_string2 % (s1,s2)

given_string3 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."
def sub_m(name, nickname):
    return given_string3 % {"nickname":nickname,"name":name}
    #return given_string3 % {'nickname':nickname,'name':name} cal also use single quotes

print sub1("it")
print sub2("sleeping","running")
print sub_m("vivek","naik")
