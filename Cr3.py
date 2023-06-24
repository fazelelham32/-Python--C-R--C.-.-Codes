Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> "hey now"
'hey now'
>>> 'hey now'
'hey now'
>>> "he's a jerk"
"he's a jerk"
>>> "he\'s a jerk"
"he's a jerk"
>>> "bucky said, \"hey now\" to me "
'bucky said, "hey now" to me '
>>> 'let\'s go fishing'
"let's go fishing"
>>> a = "bucky"
>>> b = "roberts"
>>> a+b
'buckyroberts'
>>> a, b
('bucky', 'roberts')
>>> a = "bucky"
>>> a + b
'buckyroberts'
>>> a="bucky "
>>> a + b
'bucky roberts'
>>> "hey now"
'hey now'
>>> print("hey now")
hey now
>>> num = 18
>>> num+18
36
>>> print("BUcky id")
BUcky id
>>> num = str(18)
>>> print("bucky is") + num
bucky is
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print("bucky is") + num
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
>>> print("BUcky is + num")
BUcky is + num
>>> num = str(18)
>>> print("BUcky is" + num)
BUcky is18
>>> num2 = 32
>>> print("my mum is" + num2)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print("my mum is" + num2)
TypeError: can only concatenate str (not "int") to str
>>> print("my name is" + 'num2')
my name isnum2
>>> num2=32
>>>  print("my name is" + 'num2')
 
SyntaxError: unexpected indent
>>> print("my name is" + 'num2')
my name isnum2
>>> num2=32
>>> print("my name is" + 'num2')
my name isnum2
>>> num34
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    num34
NameError: name 'num34' is not defined
>>> num2=34
>>>  print("my name is" + num2)
 
SyntaxError: unexpected indent
>>> num2=87
>>> print("my name is" + num2)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print("my name is" + num2)
TypeError: can only concatenate str (not "int") to str
>>> num2=56
>>> print("my name is" + 'num2')
my name isnum2
>>>  print("my name is" +  'num2')
 
SyntaxError: unexpected indent
>>> print("my name is" +  'num2')
my name isnum2
>>>  print("my name is + num2")
 
SyntaxError: unexpected indent
>>> print("my name is + num2")
my name is + num2
>>> buck=input("Enter name: ")
Enter name: bucky
>>> 