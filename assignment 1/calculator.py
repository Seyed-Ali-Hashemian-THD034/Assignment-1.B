#calculator
import math
op = input(''' Which of the operations from the list do you want to perform?
           
1.+
2.-
3.*
4./ 
5.sin
6.cos
7.tan
8.cot
9.radical
10.factorial

Enter the symbol of the operation in question:''')

if op== "+" or op== "-" or op== "*" or op== "/":
    print("Operation you selected is" "A" ,op ,"B")
    a=float(input("\nenter A:"))
    b=float(input("\nenter B:"))
    
    if op=="+":
        result=a+b
        
    if op=="-":
        result=a-b
        
    if op=="*":
        result=a*b
        
    if op=="/":
        result=a/b
        
    print("The operation you wrote is:" ,a,op,b, "The operation you wrote is:", result)
    
elif op=="sin" or op== "cos" or op=="tan" or op=="cot" or op=="radical" or op=="factorial" :
    print("Operation you selected is" ,op,"x")
    x=float(input("\nenter x:"))


    if op == "sin":
        result = math.sin(math.radians(x))
        
    if op == "cos":
        result = math.cos(math.radians(x))
        
    if op == "tan":
        result = math.tan(math.radians(x))
        
    if op == "cot":
        result = 1/math.tan(math.radians(x))

    if op=="radical":
        result=math.sqrt(x)

    if op=="factorial":
        result=math.factorial(int(x))
        

    print("The operation you wrote is:",op,x,"/The operation you wrote is:",result)
    