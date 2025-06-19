class add:
    def __init__(self,x,y):
        self.result=x+y

class sub:
    def __init__(self,x,y):
        self.result=x-y

n1=int(input("enter the first number: "))
n2=int(input("enter the second number: "))
ob1=add(n1,n2)  
ob2=sub(n1,n2)
print(ob1.result) 
print(ob2.result)    

