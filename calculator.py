def add(a,b):
    answer = a+b
    print(f"{a} + {b} = {answer}")
    
    
    
    
def sub(a,b):
    answer = a-b
    print(f"{a} - {b} = {answer}")
    
    
    
    
def mul(a,b):
    answer = a*b
    print(f"{a} * {b} = {answer}")
    
    
    
    
def div(a,b):
    answer = a/b
    print(f"{a} / {b} = {answer}")
    
while True:
    print("A.Addition")  
    print("B.SUbtraction")  
    print("C.Multiplication")  
    print("D.Division")  
    print("E.Exit")  
    
    choice  = input("input your choice: \n")
    
    if choice == "a" or choice=="A":
        print("Addition")
        a= int(input("enter first number\n"))
        b= int(input("enter Second number\n"))
        add(a,b)
    if choice == "b" or choice=="B":
        print("Subtraction")
        a= int(input("enter first number\n"))
        b= int(input("enter Second number\n"))
        sub(a,b)
    if choice == "c" or choice=="C":
        print("Multiply")
        a= int(input("enter first number\n"))
        b= int(input("enter Second number\n"))
        mul(a,b)
    if choice == "d" or choice=="D":
        print("Division")
        a= int(input("enter first number\n"))
        b= int(input("enter Second number\n"))
        div(a,b)
    if choice == "e" or choice=="E":
        print("Exit")
        print("end of program")
        quit()
        
    
    