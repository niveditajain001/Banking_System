import create
def addm(n,b,p):
  if(p==create.d2[n]):
    m=create.d1[n]
    m=m+b
    create.d1[n]=m
  else:
    print("wrong pin")

