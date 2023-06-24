Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class swine:
	def apples(self):
		print("beef pie")

		
>>> obj=swine()
>>> obj.apples()
beef pie
>>> class new:
	def __init__(self):
		print "this is a constructor"
		
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("this is a constructor")?
>>> print("this is a constructor")
this is a constructor
>>> print("this also print out")
this also print out
>>> 
>>> newobj=new()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    newobj=new()
NameError: name 'new' is not defined
>>> obj=swine()
>>> obj.apples()
beef pie
>>> class new:
	def __init__(self):
		print("this is a constructor")
		print("this also print out")

		
>>> newobj=new()
this is a constructor
this also print out
>>> 