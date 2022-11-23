import re

pattern = r'07[0-9][0-9]{7}'
phoneNumber = '0794188755'
result = re.match(pattern, phoneNumber, re.I)
if(result):
    print('Matched => ',result)
else:
    print('Not matched!')

string = 'He is 23 years old.'

reObj = re.match(r'.*? .*?', string, re.M|re.I)
if reObj:
    print('reObj.group(): ', reObj.group())
    print('reObj.groups(): ', reObj.groups())
else:
    print('No match!')


print()

str2 = 'I was born in 2000.....'

reObj2 = re.search(r'.? [a-z]* born', str2, re.I)
if reObj:
    print('reObj2.group(): ', reObj2.group())
    print('reObj2.group(1): ', reObj2.groups())
else:
    print('No match!')
    
    
reObj2 = re.search(r'.? [a-z]* born in [0-3]*.*', str2, re.I)
if reObj:
    print('reObj2.group(): ', reObj2.group())
    print('reObj2.group(1): ', reObj2.groups())
else:
    print('No match!')


string = "Python regex"
matches = re.match("^Python", string, re.I)
print(matches)      # prints match = 'Python'
print(re.match("$Pyhton", string, re.I))    # prints None

