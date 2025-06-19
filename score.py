def avg(mmm,aa):
    average=sum(mmm)/aa
    print(f"Average mark: {average}")   
    print("Overall Grade: ",end='') 
    if(average>=90):
        print("O")
    elif(average>=80):
        print("A")
    elif(average>=70):
        print("B")
    else:
        print("U")