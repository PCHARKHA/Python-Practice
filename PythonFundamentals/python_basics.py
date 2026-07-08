# =========================
# VARIABLES AND DATA TYPES
# =========================
a = 34 #integer
b = -34 # integer
c = 12/3
print(type(c))  #Output is float : since it is a fraction
d = 56.8   #Output is float : since it is a decimal
e = 34j # complex
print(type(e))
str1 = "Hello" #string , you can use single or double quotes
t = True # boolean : True/False

""" String stores every character with their own Unicode
To check unicode:we use ord() function which takes argument as the character
To convert back in character we use chr() function which takes argument as the unicode
"""
ch = 'A'
print(ord(ch))

ch1 = 97
print("Printing character from unicode: " +chr(ch1))
"""String indexing & slicing :[start : end : step]
end works  with n-1 concept"""
strstr = "student"
print(strstr[0])  #output:s
print(strstr[-1])  # output:t(last letter)
print(strstr[1:4:1]) # output : tud (this is slicing)
# =========================
# TYPE CONVERSION
# =========================
""" TYPE CONVERSION
Use int(),float(),bool(),str()
Type conversions : Implicit - In this python automatically converts data from one data 
type to another.
 and Explicit-  In this we as a user use in build functions to convert one data 
type to another"""
nu = 111
print(str(nu))
""" There are truthy values and Falsy values, and there are only 
7 falsy values that means only 7 things will be converted to 
false rest True.
Falsy values are : 0,0.0,"",[],(),{},False"""
print(bool(0)) #output:false
print(bool([]))

# =========================
# INPUT,OUTPUT,FSTRING
# =========================
name = input("Enter your name:")
print(f"Hello {name}!!!")  #fstring -->new convention
print("Hello",name,"!!!") #rawstring -->This is the old convention which create too many strings in the memory
age = int(input("Enter age:")) # to take number as input
print(f"Age is {age}")

# =========================
# OPERATORS
# =========================
""" ARITHMETIC operators ----> addition ,subtraction,multiplication,division                                
Floor division :// ,modulus:% ,Exponentiation :** 
Python follows bodmas with associativity                  
"""
n1 = 10
n2 = 3
print(n1 + n2)   # 13
print(n1 - n2)   # 7
print(n1 * n2)   # 30
print(n1 / n2)   # 3.333...
print(n1 // n2)  # 3
print(n1 % n2)   # 1
print(n1 ** n2)  # 1000
"""ASSIGNMENT operators---->used to assign values to variables
+= Add and assign                                                                                   
*=  Multiply and assign /= ,//= ,%= ,**=                                             
"""
num = 10

num += 5   # num = num + 5
print(num)  # 15

num -= 3   # num = num - 3
print(num)  # 12

num *= 2   # num = num * 2
print(num)  # 24

num /= 4   # num = num / 4
print(num)  # 6.0

num //= 2  # num = num // 2
print(num)  # 3.0

num %= 2   # num = num % 2
print(num)  # 1.0

num **= 3  # num = num ** 3
print(num)  # 1.0
"""COMPARISION OPERATORS ----> ==,!=,>=,<=,>,<
They return output in boolean type """
num1 = 10
num2 = 5
print(num1 == num2)  # False
print(num1 != num2)  # True
print(num1 > num2)   # True
print(num1 < num2)   # False
print(num1 >= num2)  # True
print(num1 <= num2)  # False
print(ord("A") > ord("B"))
"""LOGICAL OPERATORS ----> and,or,not- they are used to combine multiple conditions 
& return a Boolean result
and   - Return True if both condition are True
or      - Return True if at least one condition is True
not    - Reverse the boolean value"""
no1 = 10
no2 = 5
print(no1 > 5 and no2 < 10)  # True
print(no1 > 15 or no2 < 10)  # True
print(not(num1 > no2))        # False



