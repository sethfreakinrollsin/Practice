#Q1
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.
l=[]
for i in range(2000,3201):
    if(i%7==0 and i%5!=0):
        l.append(str(i))
print(','.join(l))


# Q2
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
num=int(input("Enter A Number : "))
fact=[]
factorial=1
for i in range(1,num+1):
    factorial=i*factorial
    fact.append(str(factorial))
print(','.join(fact))

# Q3
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
number=int(input("Enter the Number : "))
dictionary=dict()
for i in range(1,number+1):
    dictionary[i]=i*i
print(dictionary)

#Q4
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

sequence=input("Enter a Comma-Seperated Sequence : ")
sequence=sequence.split(',')
lists=list()
tuples=tuple()
for i in range(0,len(sequence)):
    lists.append(sequence[i])
    tuples+=(sequence[i],)

print(lists,'\n',tuples)

#Q5
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class test:
    def __init__(self):
        self.value=''
    def getString(self):
        self.value=input("Enter a Value : ")
        
    def printString(self):
        print('\n',self.value.upper())
t=test()
t.getString()
t.printString()

#Q6
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
import math
c=50
h=30
d=input("Enter Comma Seperated Sequence : ")
d=d.split(',')
l=list()
for number in d:
    q=math.sqrt((2*c*int(number))/h)
    l.append(str(int(q)))
print(','.join(l))
