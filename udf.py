def primenum(num):

    if num==1:
        print(num,"Is not prime or composite number")
    elif num>1:
        for i in range (2,num+1):
            if num%i==0:
                print("Not A prime Number")
                break
            else:
                print(num,"IS A Prime Number")
                break

    else:

        print("Not A prime Number")
        primenum(10)
    

    
            
