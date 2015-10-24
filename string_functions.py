from string import maketrans
#capitalize()
print "capitalize function"
str = "this is String Example....wow!!!";
print "str.capitalize() : ", str.capitalize()

#center()
print"------------------------------------------"
print "center function"
print len(str)
print "str.center(40, 'a') : ", str.center(40, 'a')
print "str.center(40, 'a') : ", str.center(50, 'a')

#count()
print"------------------------------------------"
print "count function"
sub = "i";
print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)
sub = "wow";
print "str.count(sub) : ", str.count(sub)

#encode()
print"------------------------------------------"
print "encode function"
print "Encoded String: " + str.encode('base64','strict')

#endswith()
print"------------------------------------------"
print "endswith function"
suffix = "wow!!!";
print str.endswith(suffix);
print str.endswith(suffix,20);
suffix = "is";
print str.endswith(suffix, 2, 4);
print str.endswith(suffix, 2, 6);

#expandtabs()
print"------------------------------------------"
print "expandtabs function"
str = "this is\tstring example....wow!!!";
print "Original string: " + str;
print "Defualt exapanded tab: " +  str.expandtabs();
print "Double exapanded tab: " +  str.expandtabs(16);

#find and rfind()
print"------------------------------------------"
print "find and rfind function"
str1 = "this is string example....wow!!!";
str2 = "exam";
print str1.find(str2);
print str1.find(str2, 10);
print str1.find(str2, 40);
print str1.rfind(str2);

#index()
print"------------------------------------------"
print "index and rindex function"
print str1.index(str2);
print str1.index(str2, 10);
#print str1.index(str2, 40);
print str1.rindex(str2);

#join()
print"------------------------------------------"
print "join function"
str = "-";
seq = ("a", "b", "c"); # This is sequence of strings.
print str.join( seq );

#lstrip()
print"------------------------------------------"
print "lstrip function"
str = "     this is string example....wow!!!     ";
print str.lstrip();
str = "88888888this is string example....wow!!!8888888";
print str.lstrip('8');

#maketrans()
print"------------------------------------------"
print "maketrans function"
intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)
str = "this is string example....wow!!!";
print str.translate(trantab);

#max()
print"------------------------------------------"
print "max function"
str = "this is really a string example....wow!!!";
print "Max character: " + max(str);
str = "this is a string example....wow!!!";
print "Max character: " + max(str);

#min()
print"------------------------------------------"
print "min function"
str = "this-is-real-string-example....wow!!!";
print "Min character: " + min(str);
str = "this-is-a-string-example....wow!!!";
print "Min character: " + min(str);

#replace()
print"------------------------------------------"
print "replace function"
str = "this is string example....wow!!! this is really string";
print str.replace("is", "was");
print str.replace("is", "was", 3);

#rfind()
print"------------------------------------------"
print "rfind function"
str1 = "this is really a string example....wow!!!";
str2 = "is";
print str1.rfind(str2);
print str1.rfind(str2, 0, 10);
print str1.rfind(str2, 10, 0);

#rindex()
print"------------------------------------------"
print "rindex function"
print str1.rindex(str2);
print str1.index(str2);

#splitlines()
print"------------------------------------------"
print "splitlines function"
str = "Line1-a b c d e f\nLine2- a b c\n\nLine4- a b c d";
print str.splitlines( );
print str.splitlines( 0 );
print str.splitlines( 3 );
print str.splitlines( 4 );
print str.splitlines( 5 );

#zfill()
print"------------------------------------------"
print "zfill function"
str = "this is string example....wow!!!";
print str.zfill(40);
print str.zfill(50);


#isdecimal()
print"------------------------------------------"
print "isdecimal function"
str = u"this2009";  
print str.isdecimal();
str = u"23443434";
print str.isdecimal();


