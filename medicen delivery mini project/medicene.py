def me():
    m1='bandages'
    m2='eye__drops'
    m3='cotton__balls'
    m4='antiseptic'
    m5='ice__pack'
    m6='tweezers'
    m7='heat__package'
    m8='alcohol'
    m9='pain killer'
    bandages=200
    eye__drops=150
    cotton__balls=199
    antiseptic=349
    ice__pack=299
    tweezers=199
    heat__package=449
    alcohol=179
    pain__killer=399
    #global Y
    def list():
        select=int(input("1.bandages\n 2.eye__drops\n 3.cotton__balls\n 4.antiseptic\n 5.ice__pack\n 6.tweezers\n 7.heat__package\n 8.alcohol\n 9.pain killer"))
        print("Enter your medicen :",select)
        i = select
        for i in range(1,9):
            if select==1:
                qutity=int(input("enter the value"))
                a = qutity*bandages
                print(a)
                break
            elif select==2:

                qutity=int(input("enter the value"))
                b=qutity*eye__drops
                print(b)
                break
            elif select==3:
                qutity=int(input("enter the value"))
                c=qutity*cotton__balls
                print(c)
                break
            elif select==4:
                qutity=int(input("enter the value"))
                d=qutity*antiseptic
                print(d)
                break
            elif select==5:
                qutity=int(input("enter the value"))
                e=qutity*ice__pack
                print(e)
                break

            elif select==6:
                qutity=int(input("enter the value"))
                f=qutity*tweezers
                print(f)
                break
            elif select==7:
                qutity=int(input("enter the value"))
                g=qutity*heat__package
                print(g)
                break
            elif select==8:
                qutity=int(input("enter the value"))
                h=qutity*alcohol
                print(h)
                break
            elif select==9:
                 qutity=int(input("enter the value"))
                 i=qutity*pain__killer
                 print(i)   
                 break
            else:
                print("invalid option")
    list()
    a,b,c,d,e,f,g,h,i, =0
    
    c=int(input("1.add more\n 2.conform order"))
    for i in range(1,9):
        if c==1:
            list()
            t_amount = a+b+c+d+e+f+g+h+i
            c=int(input("1.add more\n 2.conform order"))


            

        
               
