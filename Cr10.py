Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def name(first, last):
	print('%s %s' % (first, last))

	
>>> name('bucky', 'roberts')
bucky roberts
>>> def name(first='tom', last='smith'):
	print('%s %s' %(first, last))

	
>>> name()
tom smith
>>> name('bucky', 'roberts')
bucky roberts
>>> name('bucky')
bucky smith
>>> name(last='roberts')
tom roberts
>>> def list(*food):
	print(food)

	
>>> list('apples')
('apples',)
>>> list('apples', 'peaches', 'beef')
('apples', 'peaches', 'beef')
>>> def profile(name, *ages):
	print(name)
	print(ages)

	
>>> profile('bucky', 42, 43, 76, 54, 98)
bucky
(42, 43, 76, 54, 98)
>>> def cart(**items):
	print(items)

	
>>> cart(apples=4,peaches=6, beef=60)
{'apples': 4, 'peaches': 6, 'beef': 60}
>>> def profile(first, last, *ages, **items)
SyntaxError: invalid syntax
>>> def profile(first, last, *ages, **items):
	print(first, last)
	print(ages)
	print(items)

	
>>> profile('bucky', 'roberts', 32, 43, 76, 65, 76, bacon=4, saus=64)
bucky roberts
(32, 43, 76, 65, 76)
{'bacon': 4, 'saus': 64}
>>> def example(a,b,c):
	return a+b*c
tuna=(5,7,3)
SyntaxError: invalid syntax
>>> def example(a,b,c):
	return a+b*c

>>> tuna=(5,7,3)
>>> example(*tuna)
26
>>> def example2(**this):
	print(this)

	
>>> bacon={'mom':32, 'dad':54}
>>> example2(**bacon)
{'mom': 32, 'dad': 54}
>>> class exampleClass:
	eyes="blue"
	age=22
	def thisMethod(self):
		return 'hey this method worked'

	
>>> exampleClass
<class '__main__.exampleClass'>
>>> exampleObject=exampleClass()
>>> exampleObject.eyes
'blue'
>>> exampleObject.age
22
>>> exampleObject.thisMethod()
'hey this method worked'
>>> class className:
	def createName(self, name):
		self.name=name
	def displayName(self):
		return self.name
	def saying(self):
		print("hello %s" % self.name)

		
>>> className
<class '__main__.className'>
>>> first=className()
>>> second=className()
>>> first.createName('bucky')
>>> second.createname('tony')
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    second.createname('tony')
AttributeError: 'className' object has no attribute 'createname'
>>> second.createName('tony')
>>> first.displayName()
'bucky'
>>> first.saying()
hello bucky
>>> first.name
'bucky'
>>> class parentClass:
	var1="i am var1"
	var2="i am var2"

	
>>> class childClass(parentClass):
	pass

>>> parentObject=parentClass()
>>> parentObject.var1
'i am var1'
>>> childObject=childClass()
>>> childObject.var1
'i am var1'
>>> childObject.var2
'i am var2'
>>> class parent:
	var1="bacon"
	var2="snausage"

	
>>> class child
SyntaxError: invalid syntax
>>> class child(parent):
	var2="toast"

	
>>> pob=parent()
>>> cob=child()
>>> pop.var1
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    pop.var1
NameError: name 'pop' is not defined
>>> pob.var1
'bacon'
>>> cob.var1
'bacon'
>>> cob.var2
'toast'
>>> class Mom:
	var1="hey im mom"

	
>>> class Dad:
	var2="hey there son im adad"

	
>>> class child(Mom, Dad):
	var3='im a new varibale'

	
>>> childObject=child()
>>> childObject.var1
'hey im mom'
>>> childObject.var2
'hey there son im adad'
>>> 