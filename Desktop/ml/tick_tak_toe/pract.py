from math import sqrt


def fun(name, age):
    print("Name:",name)
    print("Age:",age)

fun("neha",20)

print("Welcome to class CSE- 11")

#x=input("Name:")
#y=input("roll no.:")
#z=input("branch:")
#print(f'My name is {x}, roll no. {y} and branch is {z}')

"""
a=int(input("Ener the first no.:" ))
b=int(input("Ener the second no.:" ))
print("select the operation "
    "1.Add \n"
    "2.Sub \n"
    "3.Mult \n"
    "4.Div \n")
     
choice = input("enter choice:")
if choice == '1':
        print(a+b)

elif choice == '2':
        print(a-b)
    
elif choice == '3':
    print(a*b)
elif choice == '4':
    print(a/b)

else:
    print("invalid")
"""
"""
c=int(input("enter tempetature in  C"))
f=(9/5)*c+32
print("temp in F is:",f)
"""


"""
a=int(input("enter a no."))
if (a%2==0):
    print("even")
else:
    print("odd")

"""
"""
x,y,z=input("enter 3 no.:").split()# takes space
print(x,y,z)
if(x>=y and x>=z):
   print(f'{x} is largest')
elif(y>=x and y>=z):
  print(f'{y}is largest')
else  :
    print(f'{z} is largest' )
    """
"""
n=int(input("enter a no."))
for i in range(1,n+1):
    print(i)

    """

"""
n=int(input("enter a no."))
fact =1
for i in range(1,n+1):
    fact = fact*i
print(fact)


"""
"""
list = input("enter 5 no.:").split()
print(max(list))
print(min(list))
"""
#OR
"""
n = input("Enter 5 no.: ").split()

print("list:", n)

min= int(n[0])
max= int(n[0])

for num in n:
       num= int(n)
    if num< min:
        min=num
    if num> max:
        max= num

print(f"Min no.: {min}")
print(f"Max no.: {max}")

"""

"""

n=int(input("enter a no."))
if n>1:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print(n, "is not prime")
            break
    else:
        print(n,"is prime")
else:
    print(n,"not prime.")

"""
"""
#or
n=int(input("enter a no."))
if n<0:
    print("invalid")    
if n==0 or n==1:
    print(n,"not prime")
else:
    for i in range(2,n):
        if n%i==0:
            print(n,"not prime")
            break
    else:
        print(n,"is prime")
          """
