d1={}
d2={}
class Create:
    def __init__(self,n,ib,p):
        self.name=n
        self.balance=ib
        self.pin=p
    def createacc(self):
        d1[self.name]=self.balance
        d2[self.name]=self.pin
        print("congratulations account created")