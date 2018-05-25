a,b=map(int,input().split(" "))
fact=1
fact1=1
for i in range(1,a+1):
  fact=fact*i
for i in range(1,b+1):
  fact1=fact1*i
print(round(fact/fact1))

