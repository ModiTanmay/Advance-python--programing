Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=== RESTART: C:/Users/modit/OneDrive/Desktop/python programs/demo_program.py ===
hello
 a=10
...  
SyntaxError: unexpected indent
>>> a=10
>>>  a=10
...  
SyntaxError: unexpected indent
>>> a=20
>>> print("A:",a)
A: 20
>>> A: 20
>>> print(type(a))
<class 'int'>
>>>  <class 'int'>
...  
SyntaxError: unexpected indent
>>> a=int(input("Enter A:"))
Enter A:
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a=int(input("Enter A:"))
ValueError: invalid literal for int() with base 10: ''
>>> a=int(input("Enter A:"))
Enter A:
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a=int(input("Enter A:"))
ValueError: invalid literal for int() with base 10: ''
>>> a=int(input("Enter A:"))
Enter A:
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a=int(input("Enter A:"))
ValueError: invalid literal for int() with base 10: ''
>>> a=int(input("Enter A:"))
Enter A:10
>>> a=10
>>> b=20
>>> c=a+b
>>> print("Addition:",c)
Addition: 30
>>> Addition: 30
>>> a=int(input("Enter A:"))
Enter A:10
>>> 
===================================================================== RESTART: Shell ====================================================================
>>> a=int(input("Enter A:"))
