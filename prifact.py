n=int(input(""))
for num in range(2,n+1):
  if(num>1):
    for i in range(2,num):
      if((num%i)==0):
        break
    else:
      if(n%num==0):
        print(num)
