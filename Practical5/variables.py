#input the three variables
a=110502
b=190784
c=100321

#calculate the difference value 
d=abs(a-c)
print(d)
e=abs(a-b)
print(e)

#compare the varibales
if d>e:
  print("d is greater")
else:
  print("e is greater")


#use the Boolean
X=bool(1)
Y=bool(0)
Z=(X and not Y) or (Y and not X)
print(bool(Z))
W=(X!=Y)
if W==Z:
  print(bool(1))
else:
  print(bool(0))
