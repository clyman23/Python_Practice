# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 10:15:10 2018

@author: clyman
"""

# Python commands reference

'''-----Numbers-----
abs(x) - absolute value of x
ceil(x) - round up to nearest int
cmp(x,y)
    -1 if x<y
    0 if x==y
    1 if x>y
exp(x) - e^x
fabs(x) - absolute value of x as a float
    import math
    math.fabs(x)
floor(x) - round down to nearest int
log(x) - natural log of x for x>0
log10(x) - base 10 log of x for x>0
max(x1, x2, ...) - duh
min(x1, x2, ...) - also duh
modf(x)
    Returns tuple containing (fractional part, integer part) of x
    Both items in tuple of type float
    math.modf(x)
pow(x,y) - returns x^y (which is x**y in python)
round(x, n)
    x rounded to n digits from decimal point
    n is optional (default to 0)
    Python rounds away from 0 as a tie-breaker (this might not be true...)
    round(0.5) -> 1
    round(-0.5) -> -1
sqrt(x) - square root of x for x > 0
'''

'''-----Random Number Functions-----
choice(seq)
    Choose a random entry from a list, tuple, or string
    random.choice(seq)
randrange(start, stop, step)
    random.randrange(start, stop, step)
    start is optional - defaults to 0
    step is optional - defaults to 1
    stop is exclusive
random()
    returns random float between in range [0,1)
    (inclusive 0, exclusive 1)
    random.random()
seed(x)
    random.seed(x)
    x is the seed int for the beginning of the random number function
    Should be called first before calling a random number
    If omitted, the seed value is the system time
shuffle(list)
    random.shuffle(list)
    returns randomly shuffled list, changing the original
uniform(x,y)
    random.uniform(x,y)
    returns random float in range [x,y)
'''

'''-----Trig Functions-----
acos(x)
    math.acos(x)
    returns acos of x in rads
asin(x)
    math.asin(x)
    returns asin of x in rads
atan(x)
    math.atan(x)
    returns atan of x in rads
atan2(y,x)
    math.atan2(y,x)
    returns atan(y/x) in rads
cos(x)
    math.cos(x)
    returns cos(x) in rads
sin(x)
    math.sin(x)
    returns sin(x) in rads
tan(x)
    math.tan(x)
    returns tan(x) in rads
hypot(x,y)
    math.hypot(x,y)
    returns Euclidean norm 
    same as sqrt(x^2 + y^2)
degrees(x)
    math.degrees(x)
    returns x in rads as x in degs
radians(x)
    math.radians(x)
    returns x in degs as x in rads
'''

'''-----String Escape Characters-----
\a = bell or alert
\b = backspace
\cx = Control-x
\Cx = Control-x
\e = escape
\f = formfeed
\M-\C-x = Meta-Control-x
\n = newline
\nnn = octal notation
\r = carriage return
\s = space
\t = tab
\v = vertical tab
\x = Character x
\xnn = hexadecimal notation
'''

'''-----String Special Operations-----
let a = 'Hello'
and b = 'Python'
a+b => 'HelloPython'
a*2 => 'HelloHello'
a[1] => 'e'
a[1:4] => 'ell'
'H' in a => True
'M' not in a => True
r'Hello\n' or R'Hello\n' will print as 'Hello\n'
'''

'''-----String Formatting Operator-----
%c = character
%s = string conversion via str() prior to formatting
%i = signed decimal integer
%d = signed decimal integer
%u = unsigned decimal integer
%o = octal integer
%x = hexadecimal int (lowercase letters)
%X = hex in (uppercase letters)
%e = exponential notation w/ lowercase e
%E = exponential notation w/ uppercase E
%f = floating point real number
%g = shorter of %f and %e
%G = shorter of %f and %E
'''

'''-----String Format Methods-----'''
'''.capitalize()''' #capitalize first character in string
'''.lower()''' #makes all characters in string lowercase
'''.upper()''' #makes all chracters in string uppercase
'''.swapcase()''' #switches case of all characters in string
'''.title()''' #capitalizes first letter of every word in string 
'''len('string')''' #NOTE: NO '.'; returns length of string
'''.count('charcater or substring')''' #Returns number of times a character or sub-string appears 
'''.find('charcter or substing')''' #Returns index of first character or sub-string match; -1 if no match


'''-----List Methods-----'''
'''cmp(lis1, list2)''' #Compares elements of both lists
'''len(list)''' #Returns length of list
'''max(list)'''
'''min(list)'''
'''list(seq)''' #Casts tuple to list
'''.append(input)''' #adds item to end of list
'''.insert(index, input)''' #inserts item into list at input; increases all other indices at and above index by 1
'''del list[index]''' #deletes a list index
'''.pop(index)''' #returns and deletes item from list at index
'''.remove(input)''' #removes first item from list that matches input
'''.extend(list2)''' #rewrites list by adding input (list2) to end of list
'''list1 + list2''' #adds list2 to end of list1 and creates a new list [list1,list2]
'''.reverse()''' #reverses a list
'''.sort()''' #orders a list
'''sorted(list)''' #returns list sorted
'''.split('input')''' #splits string into list; splits at " " by default
'''string1.join(list)''' #joins list elements into a new string separated by string1
'''list.count(obj)''' #Returns count of how many times obj occurs in list

'''-----Dictionary Methods-----
dict.clear() - remove all elements
dict.copy() - returns shallow copy of dict
dict.fromkeys(seq, value)
    Creates new dict with keys from seq and values set ot value
    seq - list of values for keys
    value - optional; each key maps to value
dict.get(key, default=None)
    returns value at key
    if key not in dict, returns default
dict.has_key(key)
    obvious
dict.items()
    returns list of dict's (key, value) tuple pairs
dict.keys()
    returns list of dict's keys
dict.setdefault(key, default=None)
    similar to get(), but if key not in dictionary, it creates the key and 
    assigns the value default to it
dict.update(dict2)
    adds dict2's key-value pairs to dict
dict.values()
    returns list of dict's values
'''

'''-----Date and time-----
import time
time.time() 
    Returns number of seconds as float since 12:00 am, Jan 1, 1970 (the epoch)
    Dates before the epoch cannot be expressed this way
    Also, dates in the far future cannot be expressed in this way
    Cutoff for UNIX and Windows systems is sometime in 2038
time.clock()
    Returns CPU time as float
    More useful than time.time() for determining computational costs of two
    different approaches
    Time begins from the first call to time.clock()
'''


'''-----File import/read/write/etc-----'''
'''!curl "url" -o output.txt''' #to grab file from internet





