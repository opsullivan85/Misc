n=1
d=1
f=''
for _ in range(12):
  n,d=n**2+2*d**2,2*d*n
for _ in range(1001):
  q=n//d
  f+=str(q)
  n-=q*d
  d//=10
print('1.'+f[1:])
