#r is the number of infected individuals
#r_rate of 1.2 means each infected individual will on average infect 1.2 individuals.
r_rate=1.2

#define a function
def w(n):
  if n==0:
    return 84
  else:
   r=w(n-1)*r_rate
  return r

r=w(int(5))
print("when r rate equals to 1.2, after 5 generations, there are "+str(r)+" infected individuals")


