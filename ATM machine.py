'''def main()
def atm_1()
print(\n "please insit your card")
print(\n"enter your pin number")'''
pin=1234
ammount=10000
print(" welcome ")
print("please insit your card")
vpin=int(input("enter your pin number"))
if vpin==pin:
    option=int(input("\n 1.withdrawal,\n 2.Deposite,\n 3.balance enquire,\n 4.mini statement,\n 5.others"))
    if option==1:
        at=int(input("\n 1.saving account,\n 2.current account"))
        if at==1 or at==2:
            
            ea=int(input("enter your ammount"))
            print("sucessfull transcation")
            blc=ammount-ea
            print("balance",blc)
    elif option==2:
        da=int(input("enter your deposite ammount"))
        print("sucessfull your deposite")
        blc_1=ammount+da
        print("balance : ",blc_1)
    elif option==3:
        print("your account balance : ",ammount)
    elif option==4:
        print("account holder name : parthasarathi")
        print("account number:45612378946")
        print("your balance ammount:",ammount)
              
        
    
else:
    print("invalid pin")
print("*** Thanking you ****")    





    
    

