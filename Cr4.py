Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> family = ['mom', 'dad', 'bro', 'sis', 'dog']
>>> family[3]
'sis'
>>> family[-2]
'sis'
>>> 'bucky'[3]
'k'
>>> example=[0,1,2,3,4,5,6,7,8,9]
>>> example[4:8]
[4, 5, 6, 7]
>>> example[4:9]
[4, 5, 6, 7, 8]
>>> example[4:10]
[4, 5, 6, 7, 8, 9]
>>> example[-5:-1]
[5, 6, 7, 8]
>>> example[-5:0]
[]
>>> example[-5:]
[5, 6, 7, 8, 9]
>>> example[3]
3
>>> example[:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> example[1:8:2]
[1, 3, 5, 7]
>>> example[10:0:-2]
[9, 7, 5, 3, 1]
>>> exapmle[::-2]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    exapmle[::-2]
NameError: name 'exapmle' is not defined
>>> example[::-2]
[9, 7, 5, 3, 1]
>>> [7,4,5]+[4,6,5]
[7, 4, 5, 4, 6, 5]
>>> 'bucky'+'roberts'
'buckyroberts'
>>> 'bucky'*10
'buckybuckybuckybuckybuckybuckybuckybuckybuckybucky'
>>> 21*10
210
>>> [21]*10
[21, 21, 21, 21, 21, 21, 21, 21, 21, 21]
>>> na,e='roastbeef'
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    na,e='roastbeef'
ValueError: too many values to unpack (expected 2)
>>> name='roastbeef'
>>> 'z'
'z'
>>> 'z' in name
False
>>> 'r' in name
True
>>> family=['mom', 'dad', 'bro']
>>> 'sis'in family
False
>>> 'mom' in family
True
>>> numbers=[8,1,4,17,28,165,7]
>>> len(numbers)
7
>>> max(numbers)
165
>>> min(numbers)
1
>>> list('bucky')
['b', 'u', 'c', 'k', 'y']
>>> numbers
[8, 1, 4, 17, 28, 165, 7]
>>> numbers[3]=77
>>> numbers
[8, 1, 4, 77, 28, 165, 7]
>>> del numbers[3]
>>> numbers
[8, 1, 4, 28, 165, 7]
>>> example=list('esayhoss')
>>> example
['e', 's', 'a', 'y', 'h', 'o', 's', 's']
>>> example[4:]=list('baby')
>>> example
['e', 's', 'a', 'y', 'b', 'a', 'b', 'y']
>>> example[4:]=lust('racecars')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    example[4:]=lust('racecars')
NameError: name 'lust' is not defined
>>> example[4:]=list('racecars')
>>> example
['e', 's', 'a', 'y', 'r', 'a', 'c', 'e', 'c', 'a', 'r', 's']
>>> example=[7,8,9]
>>> example
[7, 8, 9]
>>> example[1:1]=[3,3,3]
>>> example
[7, 3, 3, 3, 8, 9]
>>> example[1:5]=[]
>>> example
[7, 9]
>>> face=[21,18,30]
>>> face
[21, 18, 30]
>>> face.append(45)
>>> face
[21, 18, 30, 45]
>>> apples['i', 'love', 'apples', 'apples', 'now']
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    apples['i', 'love', 'apples', 'apples', 'now']
NameError: name 'apples' is not defined
>>> apples=['i', 'love', 'apples', 'apples', 'now']
>>> apples
['i', 'love', 'apples', 'apples', 'now']
>>> apples.count('apples')
2
>>> one=[1,2,3]
>>> one
[1, 2, 3]
>>> two=[4,5,6]
>>> two
[4, 5, 6]
>>> one.extend(two)
>>> one
[1, 2, 3, 4, 5, 6]
>>> 