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

'''-----Anonymous Functions-----
Created using lambda keyword
Can take any number of arguments but return just one value as an expression
Cannot contain commands or multiple expressions
Cannot be a direct call to print because it requires an expression
Have their own local namespace
    Cannot access variables other than those in their parameter list and the 
    global namespace
Not equivalent to inline statements in C/C++

Syntax:
    lambda [arg1 [,arg2, ... argn]]:expression
    
Ex:
    sum = lambda arg1, arg2: arg1+arg2
    print("Value of total is: " + sum(10,20))
Output is "Value of total is: 30"
'''

'''-----Modules-----
Python searches for a module in the following order:
    - The current directory
    - Each directory in PYTHONPATH
    - Each directory in the default path
    Search path is stored in variable sys.path
dir(module) returns a sorted list of all the modules, variables, and functions in module
globals() and locals() returns all the variables in global and local namespace
    returned as dict
    if locals() called within a function, it will return all the names that can be accessed 
    locally from that function
    if globals() called within a function, it will return all the names that can be accessed
    globally from that function 
reload(module) re-imports the module
'''

'''-----Files I/O-----
In Python 2, there is a difference between input() and raw_input()
This difference has been removed in Python 3 and both store the input as a string
In Python 2, input() treats the input as a valid Python expression
Different modes for opening a file:
    r - read; file pointer at beginning of file
    rb - reading in binary format; file pointer at beginning of file
    r+ - reading and writing; file pointer at beginning
    rb+ - reading and writing binary; file pointer at beginning
    w - writing; overwrites file if it exists
    wb - writing binary
    w+ - writing and reading
    wb+ - writing and reading binary
    a - appending; file pointer at end of file; creates new file if file DNE
    ab - appending binary
    a+ - appending and reading
    ab+ - appending and reading binary
Attributes of file object:
    file.closed - true if file is closed
    file.mode - returns access mode with which file was opened
    file.name - returns name of file
    file.softspace - false if space explicity required with print
tell() 
    method returns the current position within the file
seek(offset[,from])
    changes position within file
    offset = number of bytes to move
    from = reference position to move from
        0 = beginning of file
        1 = current position
        2 = end of file
os.rename(old_filename, new_filename)
    self-explanatory
os.remove(filename)
    also self-explanatory
os.mkdir(blah)
os.chdir(blah)
os.getcwd()
os.rmdir(blah)

!curl "url" -o output.txt
    grab file from internet
''' 

'''-----Exceptions-----
Handles unexpected errors in program; adds debugging capability
Standard exceptions:
    Exception - base class for all exceptions
    StopIteration - Raised when the next() method of iterator does not point to any object
    SystemExit - Raised by the sys.exit() function
    StandardError - Base class for all built-in exceptions except StopIteration and SystemExit
    ArithmeticError - Base class for all errors that occur for numeric calculation
    OverflowError - Raised when a calculation exceeds max limit for a numeric type
    FloatingPointError - Raised when a floating point calc fails
    ZeroDivisionError - Raised when div or modulo by 0 takes place for all numeric types
    AssertionError - Raised in case of failure of the Assert statement
    AttributeError - Raise in case of failure of attribute reference or assignment
    EOFError - Raised when there is no input from raw_input() or input() and the end of file is reached
    ImportError - Raised when an import statement fails
    KeyboardInterrupt - Raised when user interrupts program execution (usually with ctrl+c)
    LookupError - Base class for all lookup errors
    IndexError - Raised when index not found in sequence
    KeyError - Raised when specified key not found in dict
    NameError - Raised when identified is not found in local or global namespace
    UnboundLocalError - Raised when trying to access local var in a func or method but no value assigned to it
    EnvironmentError - Base class for all exceptions that occur outside the Python environment
    IOError - Raised when input/output operation fails, such as print statement or the open() function
    when trying to open a file that does not exist
    SyntaxError - Raised when error in Python syntax
    IndentationError - Raised when indentation not specified properly
    SystemError - Riased when interpreter finds internal problem; when this error encountered
    Python interpreter does not exit
    SystemExit - Raised when Python interpreter is quit by using the sys.exit() func; if not
    handled in the code, causes the interpreter to exit
    TypeError - Raised when operation or func is attempted that is invalid for the specified data type
    ValueError - Raised when built-in func for a data type has the valid type of arguments, 
    but the argurments have invalid values specified
    RuntimeError - Raised when a generated error does not fall into a category
    NotImplementedError - Raised when an abstract method that needs to be implemented in an
    inherited class is not actually implemented

Assertion:
    Sanity-check that can be turned on or off while testing a program
    Often placed at the start of a func to check for valid input and after a func call
    to check for valid output
    
    assert Expression[, Arguments]
    
    Python evaluates expression and raises AssertionError if Expression is False
    Arguments is used as the argument for the AssertionError

Exceptions:
try...except...else
A try statement can have multiple except statements
Code is else block runs if code in try block does not raise an exception
    Therefore, the else block is good for code that does not need "protection" from try
Can use except block without defining which exception but is bad practice
Can also use except block with multiple exceptions at once
finally block:
    place to put any code that must execute whether try raises exception or not
Can use:
    except ExceptionType, Argument:
        This will store info about the exception in Argument

Raising Exceptions:
raise [Exception [, args [, traceback]]]
    Exception - type of exception
    args - value for exception argument
    traceback - traceback object for the exception (rarely used)

'''

'''-----Classes-----
Accessing attributes
    getattr(object, name)
    hasattr(object, name) - check if attribute exist or not
    setattr(object, name, value)
    delattr(object, name)
    
Built-in class attributes
    __dict__ - dictionary containing class's namespace
    __doc__ - class documentation string or none, if undefined
        The doc string is the comments directly after the class line in code
    __name__ - class name
        Python 3: call as __class__.__name__
    __module__ - module name in which the class is defined
    __bases__ - possibly empty tuple containing base classes in the order
    of their occurence in the base class list
    
Garbage Collection
    Python deletes unneeded objects automatically to free up space
    Garbage collection - process by which Python periodically reclaims blocks
    of memory that no longer are in use
    Triggered when object's reference count reaches 0
    Reference count increases when it is assigned a new name or placed in a container
    (list, tuple, dict)
    Reference count decreases when it's deleted with del, reference is reassigned, 
    or its reference goes out of scope
    Class can invoke __del__(), called a destructor, that is invoked when instance
    is about to be destroyed
    
Class Inheritance
    Child class inherits attributes of parent class
    Can use those attributes as if they were defined in child class
    Child class can also override data members and methods from parent
    issubclass(sub, sup)
        True if sub is a subclass of sup
    isinstance(obj, Class) 
        True if obj is instance of Class or is instance of subclass of Class
        
Overloading Operators
    Can define an __add__() function so that you can add two instances of a class
    
Data Hiding
    if an attribute is named with a leading __ (double _), then it cannot be viewed
    Can only be accessed by object._className__attributeName
'''

'''-----Iterators-----
Lists, tuples, dictionaries, strings, and sets are all iterable objects
Can get an iterator by using:
    thing = iter(object)
Can then get the next value of the iterator by using:
    next(thing)
    next(thing)
    ...
Can get each value using:
    for x in thing:
        print(thing)

Can create an object/class as an iterator, must implement methods:
    __iter__() - must return the iterator object itself
    __next__() - must return the next item in the sequence
    
Example - will return 1,2,3,4,5,...
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

Can use if self.a <= some_number
and else: raise StopIteration
to prevent next() from returning a new value "forever"
'''


'''-----Regular Expressions-----
Special sequence of characters that helps you match or find other strings or
sets of strings, using a special syntax held in a pattern
Regular expressions are widely used in UNIX world
Module re provides full support for Perl-like regular expressions in Python
re module raises exception re.error if error occurs

Match function
Function attempts to match RE pattern to string with optional flages
re.match(pattern, string, flags = 0)
pattern - regular expression to be matched
string - string that would be searched to match pattern
flags - can specify different flags using bitwise OR

Ex:
import re
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")
    
re.match() check for match at beginning of string while re.search() checks for 
match anywhere in string

Can search and replace using
re.sub(pattern, replace, string, max=0)

More references at: https://www.tutorialspoint.com/python/python_reg_expressions.htm
'''

'''-----CGI: Common Gateway Interface-----
Set of standards that define how information is exchanged b/w the web server
and a custom script


'''

