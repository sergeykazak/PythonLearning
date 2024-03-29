# https://www.w3schools.com/python/python_regex.asp

# https://docs.python.org/3/library/re.html

import re

text = ('Use our game-changing fully managed development environment Vertex AI Vision to create your own computer vision'
'applications or derive insights from images and videos with pre-trained APIs,  AutoML, or c3ustom models.'
'Easily build, deploy and manage computer vision applications for your unique business nee5ds with pre-trained APIs,'
'AutoML and custom models. Whether you need plug and play ana9ytics via AP7s or the abi6ity to use custom ML models'
'or an end to end development environment, our vis8ion portfolio has a solution. Benefit from Google\'s investments'
 ' in vision across our portfolio. Google5\'s vision offerings have received the highest ratings from several analyst firms.')

# Main 4 methods:
# Function	Description
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

pattern = 'Google\'s'

x = re.findall(pattern, text, flags=re.IGNORECASE)
print(x)

pattern = 'Gogle\'s'
x = re.findall(pattern, text, flags=re.IGNORECASE)
print(x)

pattern = 'ml'
x = re.findall(pattern,text,flags=re.IGNORECASE)
print(x)


pattern1 = r'\d' #r before a string literal, such as r'\d', indicates a raw string literal. A raw string
# literal treats backslashes (\) as literal characters and not as escape characters. This means that backslashes
# are not used to escape characters like they are in regular string literals.

a = re.findall(pattern1, text, flags=re.IGNORECASE)
print(a) #['3', '5', '9', '7', '6', '8']

pattern2 = r'[0-9]'
b = re.findall(pattern2,text, flags=re.IGNORECASE)
print(b) #['3', '5', '9', '7', '6', '8']

pattern3 = r'[^0-9]' #all characters except digits

pattern4 = r'G..{3,5}\'s'
c = re.findall(pattern4,text,flags=re.IGNORECASE)
print(c) # ["Google's", "Google's"]

pattern5 = r'G..{4}\d?\'s' # \d? - means digit is either presented or not
d = re.findall(pattern5,text, flags=re.IGNORECASE)
print(d) # ["Google's", "Google5's"]

e = re.search(pattern5,text,flags=re.IGNORECASE) # will find 1st match for pattern5 in text
print(e) # <re.Match object; span=(538, 546), match="Google's">
print(e.start()) #538 - character from which string Google's begins
print(e.end()) # 546
print(e.group()) # Google's
print(e.span()) #(538, 546)

pattern6 = r'G..{3}\d?\'s'
f = re.search(pattern6,text,flags=re.IGNORECASE)
print(f) #None


g = re.split(pattern5, text, flags=re.IGNORECASE)
print(g) # list with 3 strings splitted by string pattern5
print(len(x)) #3


f = re.split(pattern2, text, flags=re.IGNORECASE)
print(f) # list with 3 strings splitted by string pattern5
print(len(f)) #8

h = re.sub(pattern4, "News", text, flags=re.IGNORECASE) # we replace matched pattern5 strings with 'News'
print(h)
pattern7 = 'News'
i = re.findall(pattern7, h, flags=re.IGNORECASE)
print(i)

