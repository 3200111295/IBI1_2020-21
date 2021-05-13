#the first two numbers are 1,1
a=1
b=1
print(a)
print(b)

for i in range (3,14):
    i=i=1
    #the sum of the previous two numbers is the next number
    c=a+b
    #repeat adding the previous two numbers
    a=b
    b=c
    print(c)
  
