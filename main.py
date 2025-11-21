import add
import create
import withdraw
import delete

def main():
    
    while(True):
        ch=int(input("enter 1 for account creation 2 for deletion 3 for money withdrawal 4 for money addition or if you dont wish to continue with any further processes type 5 : "))
        if(ch==1):
           n1=input("enter account holder name to create account for: ")
           p=int(input("enter pin : "))
           b1=int(input("enter initial balance : "))
           ob=create.Create(n1,b1,p)
           ob.createacc()
        elif(ch==2):
           n1=input("enter account holder name to be deleted : ")
           p=int(input("enter pin : "))
           delete.deleteacc(n1,p)
        elif(ch==3):
           n1=input("enter account holder name to withdraw money from : ")
           p=int(input("enter pin : "))
           b1=int(input("enter amount to be withdrawn : "))
           withdraw.Withdraw(n1,b1,p)
        elif(ch==4):
           n1=input("enter account holder name to add balance to  : ")
           b1=int(input("enter amount to be added : "))
           p=int(input("enter pin : "))
           add.addm(n1,b1,p)
        elif(ch==5):
           break
        print("current status")
        print(create.d1)
main()