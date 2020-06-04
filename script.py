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
