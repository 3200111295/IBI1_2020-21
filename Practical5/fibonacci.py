def feb(n):
  if n==1:
    return 1
  if n==2:
    return 1
  else:
    tz=feb(n-2)+feb(n-1)
    return tz
temp=int(13)
tzs=feb(temp)
print(tzs)


