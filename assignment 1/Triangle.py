#Triangle
print('''You have a shape that has 3 sides, and I want to see if it is a triangle or not.
    Enter them one by one.''')
s1 =(input("enter the side1 .a. :"))
s2 =(input("enter the side2 .b. :"))
s3 =(input("enter the side3 .c. :"))
if s1+s2 > s3 and s2+s3 > s1 and s1+s3 > s2 :
    print("Be happy because your triangle is perfectly healthy.")
else : 
    print("The shape you draw is not a triangle . damn it .")