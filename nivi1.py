n=str(input())
a=[]
for i in n:
  if i not in a:
    a.append(i)
print(len(a))
