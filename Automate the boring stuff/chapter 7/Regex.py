import re
#*******************************************
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print (mo.group(0))
print (mo.group(1))
print (mo.group(2))
print (mo.group())

areaCode, mainNumber = mo.groups()
print (areaCode + " " + mainNumber)

#*******************************************
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print (mo1.group())
mo2 = phoneRegex.search('My number is 555-4242')
print (mo2.group())

#*******************************************
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print (mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
print (mo2.group())

#*******************************************
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print (mo.group())
print (mo.group(1))

#*******************************************
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print (mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print (mo2.group())

#*******************************************
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print (mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print (mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print (mo3.group())

#*******************************************
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
print (mo1)
print (type(mo1))
mo2 = batRegex.search('The Adventures of Batwoman')
print (mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print (mo3.group())
print (type(mo3))

#*******************************************
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print (mo1.group())

#Greedy 
haRegex = re.compile(r'(Ha){3,5}')
mo1 = haRegex.search('HaHaHa')
print (mo1.group())
mo2 = haRegex.search('HaHaHaHa')
print (mo2.group())
mo3 = haRegex.search('HaHaHaHaHa')
print (mo3.group())

haRegex = re.compile(r'(Ha){,5}')
mo1 = haRegex.search('HaHaHa')
print (mo1.group())
mo2 = haRegex.search('HaHaHaHa')
print (mo2.group())
mo3 = haRegex.search('HaHaHaHaHa')
print (mo3.group())

nongreedyRegex = re.compile(r'<.*>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

#Non Greedy
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print (mo2.group())

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

#*******************************************
#findal() method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())
print (phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

#*******************************************
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, pipers, 10 lords, ladies, 8 maids,swans, 6 geese,rings, 4 birds,hens, 2 doves,partridge'))


vowelRegex = re.compile(r'[aeiouAEIOU]')
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.'))
print(consonantRegex.findall('Robocop eats baby food. BABY FOOD.'))


atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))


noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

#*******************************************
#sub() method

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

                            
