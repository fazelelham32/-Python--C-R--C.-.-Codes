Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> say=['hey', 'now', 'brown', 'cow']
>>> say
['hey', 'now', 'brown', 'cow']
>>> say.index('brown')
2
>>> say.insert(2, 'hoss')
>>> say
['hey', 'now', 'hoss', 'brown', 'cow']
>>> say.pop(1)
'now'
>>> say
['hey', 'hoss', 'brown', 'cow']
>>> say.remove('brown')
>>> say
['hey', 'hoss', 'cow']
>>> say.reverse()
>>> say
['cow', 'hoss', 'hey']
>>> new=[32,54,22,7,98,1]
>>> new
[32, 54, 22, 7, 98, 1]
>>> new.sort()
>>> new
[1, 7, 22, 32, 54, 98]
>>> sorted('Easyhoss')
['E', 'a', 'h', 'o', 's', 's', 's', 'y']
>>> 41,42,32,54
(41, 42, 32, 54)
>>> bucky=(32,32,43,54)
>>> bucky
(32, 32, 43, 54)
>>> bucky[2]
43
>>> bucky="Hey there %s, hows your %s"
>>> varb=('bukky', 'foot')
>>> print bucky % varb
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(bucky % varb)?
>>> prnit("bucky % varb")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    prnit("bucky % varb")
NameError: name 'prnit' is not defined
>>> prnit(bucky % varb)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    prnit(bucky % varb)
NameError: name 'prnit' is not defined
>>> print('bucky % varb')
bucky % varb
>>> bucky="Hey there %s, hows your %s"
>>> varb=('betty', 'foot')
>>> print ('bucky % varb')
bucky % varb
>>> bucky="Hey there %s, hows your %s"
>>> varb=('betty', 'foot')
>>> print (bucky % varb)
Hey there betty, hows your foot
>>> varc=('tuna', 'fit')
>>> print (tuna % fit)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print (tuna % fit)
NameError: name 'tuna' is not defined
>>> print (tuna % varc)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print (tuna % varc)
NameError: name 'tuna' is not defined
>>> varc=('tuna', 'fin')
>>> print (bucky % varc)
Hey there tuna, hows your fin
>>> example="Hey now bessie nice chops"
>>> example
'Hey now bessie nice chops'
>>> example.find('bessie')
8
>>> example.find('chops')
20
>>> seperator='hoss'
>>> sequence=['hey', 'there', 'bessie', 'hoss']
>>> sequence
['hey', 'there', 'bessie', 'hoss']
>>> glue='hoss'
>>> glue.join(sequence)
'heyhosstherehossbessiehosshoss'
>>> randstr="I wish i had NO sausage"
>>> randstr
'I wish i had NO sausage'
>>> randstr.lower()
'i wish i had no sausage'
>>> truth="I love old women"
>>> truth
'I love old women'
>>> truth.replace('women', 'men')
'I love old men'
>>> book={'Dad':'Bob', 'Mom':'Lisa', 'Bro':'Joe'}
>>> book
{'Dad': 'Bob', 'Mom': 'Lisa', 'Bro': 'Joe'}
>>> book['Dad']
'Bob'
>>> book['Mom']
'Lisa'
>>> ages={'Dad': '42', 'Mom': '87'}
>>> ages
{'Dad': '42', 'Mom': '87'}
>>> ages['Dad']
'42'
>>> book.clear()
>>> book
{}
>>> tuna=ages.copy()
>>> tuna
{'Dad': '42', 'Mom': '87'}
>>> tuna.has_key('Mom')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    tuna.has_key('Mom')
AttributeError: 'dict' object has no attribute 'has_key'
>>> 