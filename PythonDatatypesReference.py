# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 10:46:35 2018

@author: clyma
"""

# Python data types reference
'''-----Numbers-----
Numbers are immutable data types 
Delete using del:
    x = 3
    del x
    *** Can do multiple deletions in a line using comma separation
Python supports 4 numerical data types:
    1. int (signed ints)
    2. long - written like ints but followed with upper or lower-case "L" 
        (upper case recommended)
    3. float - can be in scientific notation
    4. complex - a+bj or a+bJ
        To cast to complex use complex(x) -> x+0J
        Or use complex(x,y) -> x+yJ
'''

'''-----Strings-----
Single and double quotes treated the same for strings
string = "Hello, world!" == string = 'Hello, world!' != string = 'Hello, world!"
There is no Python character type; characters are just strings of length 1
Strings are immutable data types
Strings in Python stored as 8-bit ASCII
Unicode strings stored as 16-bit Unicode
    Create unicode string with u before quotes
    thing = u'Hello world!'
'''

'''-----Lists-----
Items in a list need not be of the same type
'''

'''-----Tuples-----
Like lists, but tuples are immutable
'''

'''-----Dictionary-----
Keys are unique while values may not be
Values can be of any type
Keys must be of an immutable data type
If duplicate keys are encountered, the last assignment wins
Can cast a dict to a string using str(dict)
'''



    