a=110502
b=190784
c=100321
d=abs(a-c)
print(d)
e=abs(a-b)
print(e)
if d>e:
  print("d is greater")
else:
  print("e is greater")
X=bool(1)
Y=bool(0)
Z=(X and not Y)
print(bool(Z))
W=(X!=Y)
if W==Z:
  print(bool(1))
else:
  print(bool(0))
