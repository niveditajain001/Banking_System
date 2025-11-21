import create
def deleteacc(n,p):
 if(p==create.d2[n]):
  del create.d1[n]
  print("account deleted")
 else:
  print("wrong pin")