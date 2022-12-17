while True:
    print("------------------------------------------------------")
    print("------------------------------------------------------")
    print("||===WELCOME TO SBI ATM===||\n")
    p = int(input("Enter Your pin: "))
    if (p==1234):
        print("====Welcom====")
        print(" :) \n")
    else:
            print("====Wrong Pin====\n")
            break
            
    m=1000
    print("================================") 
    print("|| Balance Check || Press(1) ")
    print("|| Deposit       || Press(2) ")
    print("|| withdrwal     || Press(3) ")
    print("|| Exit          || press(4) ")
    print("================================")
    c=int(input("Enter Your option: "))
    if(c==1):
            print("your current Balance Is: ",m)
            
            print("Thank you  :)")
    elif(c==2):
            d = int(input("Enter Your amount: "))
            sum = m + d
            print("Your Amount Successfuly Deposit :)")
           
            print("Now your Current Balanace Is: ", sum)
    elif(c==3):
            w = int(input("Enter your Withdral Amount: "))
    elif(w<m):
            sub = m - w
            print("Your Amount Successfuly withsral :)")
           
            print("Now your current Balance Is: ",sub)
    if(w>=m):
            print("Insufficient Balance:")    
    elif(c==4):
            
      print(":Have A Good Day Sir:")


        


        
