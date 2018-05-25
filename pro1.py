n=list(input(""))
p=list(input(""))
s=[]
for i in range(0,len(n)):
  if(n[i]==p[i]):
    s.append(n[i])
  else:
    break
print("".join(str(x) for x in s))
