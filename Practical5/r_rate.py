#r is the number of infected individuals
#r_rate of 1.2 means each infected individual will on average infect 1.2 individuals.
r_rate=1.2
def feb(n):
  if n==0:
    return 84
  else:
   r=feb(n-1)*r_rate
  return r
temp=int(5)
r=feb(temp)
print('when r rate equals to 1.2, after 5 generations, there are',str(r),'infected individuals')


