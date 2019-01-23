#! python3

import re, pyperclip

#Create regex object for phone numbers
phoneRegex = re.compile(r'''
#Can read in: 415-555-0000, 555-0098, (830) 332-9876, 210-9876 ext 12345, ext.12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?    #area code (optional)
(\s|-)                      #first seperator
\d\d\d                      #first 3 digits
-                           #seperator
\d\d\d\d                    #last 4 digits
(((ext(\.)?\s)|x)            #extension word-part (optional)
(\d{2,5}))?                 #extension digits (optional)
)
''', re.VERBOSE)

#Create regex for email addresses
emailRegex = re.compile(r'''
#some.+_thing@something.com

[a-zA-Z0-9_.+]+         #name part, a-Z, digits, underscore, dots, plus sign one or more times
@                       #@ symbol
[a-zA-Z0-9_.+]+         #domain name part
''', re.VERBOSE)
#Get the text off clipboard

#text = pyperclip.paste

#Get text from variable, pyperclip not working :(
text = '''Abbo, Teri Ann
Director IT Services Alliance University Technology
(248) 370-2151
abbo@oakland.edu
216 DH
118 Library Drive
Rochester, MI 48309-4401
Abbott, Christine M
Spec Instr Education SEHS/Organizational
(248) 370-2636
cabbott@oakland.edu
480A Pawley Hall
456 Pioneer Dr.
Rochester, MI 48309-4482 '''
#Extract the email/phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#print(allPhoneNumbers)
#print(extractedPhone)
#print(extractedEmail)
# Copy the extracted emai/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
print(results)
#pyperclip.copy(results)
