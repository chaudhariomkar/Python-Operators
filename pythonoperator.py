#OPERATORS IN PYTHON
#Operators are used to perform some operations with respect to operatos

#1.Arithmatic Operators
#Addition - Adds both operands together
print(10+20)
#Subtraction - Subtracts right side operand from the left side operand
print(10-20)
#Multiplication - Multiplies both operands together
print(10*20)
#Division - Divides the left side operand with the right side operand
print(10/20)
#Modulus - Takes a modulus using two operands and assigns the result to the left
print(10%20)
#Exponent - Does exponential operations
print(10**2)
#Floor Division - Takes the result of the quotient and rejects the mantissa
print(10//2)

#2.Assignment Operators -
# =  - It assigns a value from the right-side operand to the left side.
a = 100
b = 200
c = 300
c = a + b
print(c)
# += - Adds and it adds the right operand to the left operand and assigns the result to the left operand.
c += a
print(c) #means c = c+a
# -= - Subtracts and it subtracts the right operand from the left operand and assigns the result to left operand.
c -= a
print(c) #means c = c-a
# *= - Multiplies and it multiplies the right operand with the left operand and assigns the result to the left operand.
c *= a
print(c) #means c = c*a
# /= - Divides and it divides the left operand by the right operand and assigns the result to the left operand.
c /= a
print(c) #means c = c/a
# %= - Takes the modulus using the two operands and assigns the result to the left operand.
c %= a
print(c) #means c = c%a

#3.Comparison or Conditional Operator - Gives Boolean Output
# == - Compares both the left and right operands and depending on the result, displays either True or False
print(20==30)
# >  - Compares the left operand with the right operand and depending on the result, (greater) displays either True or False
print(30>20)
# <  - Compares the left operand with the right operand and depending on the result, (left) displays either True or False
print(30<20)
# != - If the values of the two operands aren't equal, then displays the condition accordingly
print(30!=20)
# >= - If the value of the left operand is greater than the right-side operand, then the condition becomes true
print(30>=20)
# <= - If the value of the left operand is greater than the right-side operand, then the condition becomes true
print(30<=20)

#4.Identity Operator - Checks the address of the an object and compares accordingly, displays either True or False
#There are two types of Identity operator - is, is not
x = 10
y = 10
print(id(x))
print(id(y))
print(x is y) #if ids are same returns True
print(x is not y) #otherwise False
# Content Equality and Address Equality
# == performs Content Equality
# is performs Address equality

#5.Membership Operator - Checks an object is a member of a sequence or not
#There are two types of membership operator - in, not in
p = 'Virat Kohli'
print('Virat' in p) #If subsequence is present in main sequence, returns True
print('Virat' not in p) #Otherwise False

#6.Logical Operator - Used to test the condition and its output between two objects
#There are three types of logical operator - and, or, not
# and - Returns True if both statements are True
# or - Returns True if one of the statements is True
# not - Reverse the result, returns False if the result is True