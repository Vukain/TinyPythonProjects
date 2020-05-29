import re

"""Small regex bible"""

r"""
\d - digit - [0-9]
\D - non-digit
\w - word character - letter, digit, underscore - [A-Za-z0-9_]
\W - non-word character
\s - whitespace character - 
\S - non-whitespace
\ - escape character
{x,y} - from x to y repetitions | {x,y}? non-greedy match, shortest possible | {x,} - at least x repetitions
? - once or zero
* - zero or more
+ - once or more
^ - starts with
$ - ends with
() - grouping
[x-y] - one character from x to z | [xyz] - one character from xyz | [^x] - not x character
re.DOTALL, re.I - flags for compile (dot also counts as new line, ignore case sensitivity)
re.VERBOSE - flag to use triple quote and create multi layer regex pattern
"""

"""Basic phone finding"""
# Creating pattern and string - can be used directly
phone = "Call me at 123-456-7890 or at 098-765-4321!"
pat = r'\d\d\d-\d\d\d-\d\d\d\d'  # or r'\d{3}-\d{3}-\d{4}'
# Creating a regex object (adding a pattern into object)
phone_num_regex = re.compile(pat)
pn1 = phone_num_regex.findall(phone)
# Alternative - calling with a pattern
pn2 = re.findall(pat, phone)
# Getting raw content (group extracts result from a match object)
pn3 = re.search(pat, phone).group()
# Extracting groups
pn4 = re.search(r'((\d\d\d).(\d\d\d-\d\d\d\d))', phone).group(2)
# Pattern with VERBOSE
verbose_num_regex = re.compile(r'''
(((\d\d\d)|(\(\d\d\d\)))?               # optional area code XXX or (xxx)
(-|\s)?                                 # separator - or whitespace
\d\d\d                                  # first 3 digits
-                                       # separator
\d\d\d\d)                               # last 4 digits
''', re.VERBOSE)
pn5 = [num[0] for num in verbose_num_regex.findall(phone)]  # returns all groups, we want first
print(pn1, pn2, pn3, pn4, pn5, sep='---')

"""Words starting with"""
# Predefined options
bt1 = re.search(r'Bat(man|mobile|copter|bat)', 'Batmobile lost a wheel').group()
# Any letters till special sign
bt2 = re.search(r'Bat\w*', 'Batmobile lost a wheel').group()
# Optional part (once or zero), we can use * for (zero or more)
bt3 = re.search(r'Bat(wo)?man', 'Batwoman lost a wheel').group()
# Optional part (once or zero), we can use * for (zero or more)
bt4 = re.search(r'^Bat\w*', 'Batwoman lost a wheel').group()
print(bt1, bt2, bt3, bt4, sep='---')

"""Replacing a substring"""
# Replacing with groups - \1, \2 groups
ag1 = re.sub(r'Agent (\w)\w*', r'Ag. \1***', 'Agent Adam gave Agent Tim secret files.')

print(ag1)
