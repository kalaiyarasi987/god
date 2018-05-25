n=int(input(""))
s=[]
for i in range(0,n):
  b=int(input(""))
  s.append(b)
print(s)
a1=s[::2]
b1=s[1::2]
if(sum(a1)>sum(b1)):
  print(sum(a1))
else:
  print(sum(b1))
