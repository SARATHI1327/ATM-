def py():
    print("payment method :")
    op='UPI method'
    cd='cash on delivery method'
    option=int(input("1.UPI method\n2.cash on delivery method"))
    print('enther the method:',option)
    if option==1:
          am=str(input("enter your upi id :"))
          print("payment sucessfully")
    elif option==2:
           print("sucessful order")
               


