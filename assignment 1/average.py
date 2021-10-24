#average
name=input("enter your name:")
a=float(input("enter score1:"))
b=float(input("enter score2:"))
c=float(input("enter score3:"))

x = (a+b+c)/3

if x >= 17:
    print(name ,"dear, you are great")
if 17> x >= 12:
    print(name ,"dear, you are normal")
if x < 12:
    print(name ,"dear, you are fail")