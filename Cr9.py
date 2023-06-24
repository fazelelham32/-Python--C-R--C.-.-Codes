Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> b=1
>>> b
1
>>> while b<=10:
	print('b')
	b+=1

	
b
b
b
b
b
b
b
b
b
b
>>> b=1
>>> b
1
>>> while b<=10:
	print(b)
	b+=1

	
1
2
3
4
5
6
7
8
9
10
>>> g1=['bread', 'milk', 'meat', 'beef']
>>> g1
['bread', 'milk', 'meat', 'beef']
>>> for food in g1:
	print('I want' + food)

	
I wantbread
I wantmilk
I wantmeat
I wantbeef
>>> ages={'dad':42, 'mom':48, 'lisa':7}
>>> ages
{'dad': 42, 'mom': 48, 'lisa': 7}
>>> for item in ages:
	print(item)

	
dad
mom
lisa
>>> for item in ages:
	print(item, ages[item])

	
dad 42
mom 48
lisa 7
>>> while 1:
	name = input('Enter name: ')
	if name == 'quit': break

	
Enter name: greg
Enter name: tom
Enter name: lisa
Enter name: bucky
Enter name: quit
>>> def whatsup(x):
	return 'whats up' + x
print whatsup('tony')
SyntaxError: invalid syntax
>>> print(whatsup('tony'))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(whatsup('tony'))
NameError: name 'whatsup' is not defined
>>> def whatsup(x):
	return 'whats up' + x
print(whatsup('tony'))
SyntaxError: invalid syntax
>>> print('whatsup('tony')')
SyntaxError: invalid syntax
>>> print('whatsup(tony)')
whatsup(tony)
>>> print('whatsup(noob)')
whatsup(noob)
>>> print ('whats up noob')
whats up noob
>>> def plusten(y):
	return y+10
print('plusten 44')
SyntaxError: invalid syntax
>>> print("plusten"+44)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print("plusten"+44)
TypeError: can only concatenate str (not "int") to str
>>> print('plusten + 44')
plusten + 44
>>> print(plusten(44))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(plusten(44))
NameError: name 'plusten' is not defined
>>> print('plusten(44)')
plusten(44)
>>> def plusten(y):
	return y+10
print(plusten44)
SyntaxError: invalid syntax
>>> print('plusten'(44))
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print('plusten'(44))
TypeError: 'str' object is not callable
>>> 