a= 10
b= 20
c=a+b               # COMPARATIVE OPERATORS
p=b**a
print(a==b)#False
print(a!=b) #true
print(a>=b)#False
print(a<=b)  #true
print(c)   #30
print(p)    #.......

c-=b    #c=c-b
print(c)                    #Assignment operators
c+=b   #c=c+b                 
print(c)
#True/False ==> Boolean

## MEMBERSHIP OPERATORS ##
# To check whether a letter is there in a word.
#Python is case sensitive
print("y" in "Python")  #true
print("l" in "python") #false
print("p" in "Python") #false 
print("i" not in "Python")  #false


#Identity operators
print( 2 is 2) #true
print(7 is 78) #false
print(78 is not 87) #true

x= a+ 0
a=10
print(x is a)

## Precedence of Operators
"""If an expression contains more than one operator, then order of evaluation
depends on the order of operations
alke

PEMDAS (Parentheses, Exponentiation, Multiplication, Division, Addition, Subtraction)
Parentheses have the highest precedence and can be used to force an
caras
expression to evaluate in the order that we want
Exponentiation has the next highest precedence
Multiplication and Division have higher precedence than Addition and Subtraction
Operators with the same precedence are evaluated from left to right
 (except exponentiation)"""


#When we do division of 2 integers we get answer in float.
import math
print(f"{math.pi:.2f}")                                           #PEDMAS
print(type(f"{math.pi:.2f}"))

print(type(False))   #Bool

#Newline character --- "/n"

x=" Mahendra Bahubali is he son of Amrendra Bahubali.\n"
print(x)
print(type(x),"\n")
print("The length of this string is", len(x),".")

