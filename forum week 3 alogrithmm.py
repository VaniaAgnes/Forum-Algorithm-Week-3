#1
radius= float(input("radius:"))

area_of_the_circle= (3.14 * (radius*radius))

print(area_of_the_circle)

#2
first_name= input("first name:")
last_name= input("last name:")

print(last_name, first_name)

#3
list = ('Red','Green','White','Black')

print (list[0])
print (list[3])

#4
int = float(input("interger:"))
n= int
result= ((n)+(n*n)+(n*n*n))
print(result)

#5
r= 6
pi= 3.14
volume_sphere= ((4/3))*(pi)*(r**3)
print(volume_sphere)

#6
given_number= float(input("enter the given number:"))
difference= float(given_number-17)
if (given_number > 17):
    print(difference*2)
elif (given_number < 17):
    print(difference)
#7
x= float(input("enter the value of x:"))
y= float(input("enter the value of y:"))
z= float(input("enter the value of z:"))

sum= (x+y+z)

if (x==y==z):
    print(x*3)
else:print(sum)

#8
v=int(input("enter the given number:"))
oe= v%2
if (oe > 0): print("this given number is odd")

else:print("this given number is even")

#9
letter= str(input("enter the letter:"))
vowel= ('a','i','u','e','o')

if (letter=='a'or letter=='i'or letter=='u' or letter=='e' or letter=='o'):
    print("this letter is a vowel")
else:print("this letter is not part of the vowel")

#10
num= int(input("the given number:"))
list= {13,17,24,56,78,10}

if (num==13 or num==17 or num==24 or num==56 or num==78 or num==10):
    print("this given number is in the list")
else:print("this given number is not in the list")

#11
import matplotlib.pyplot as plt
interger_list = [5,6,7]
plt.hist(interger_list)
plt.show()

#12
numbers= [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
 958,743, 527]
y= numbers % 2
if y == 0:
    print(y)

#13
base= float(input("enter the value of base:"))
height= float(input("enter the value of height"))

area_of_triangle= ((1/2)*(base)*(height))
print(area_of_triangle)

#14
interger_one= int(input("enter the first interger:"))
interger_two= int(input("enter the second interger:"))
import math
print(math.lcm(interger_one,interger_two))

#15
int_one= int(input("enter the first interger:"))
int_two= int(input("enter the second interger:"))
int_three= int(input("enter the third interger:"))

sum_intergers= (int_one+int_two+int_three)

if (int_one==int_two) or (int_two==int_three) or (int_one==int_three):
 print("your sum is 0")
else: print(sum_intergers)

#16
x= int(input("enter the amount of x:"))
y= int(input("enter the amount of y:"))
calculation= (x+y)*(x+y)
print(calculation)

#17
A= float(input("enter the value of A:"))
R= float(input("enter the value of R:"))
t= float(input("enter the value of t:"))

P= (((1+ (R/100)**t))/A)
compound_interest= A-P
print(compound_interest)

#18
x1= int(input("enter the value of x1:"))
y1= int(input("enter the value of y1:"))

x2= int(input("enter the value of x2:"))
y2= int(input("enter the value of y2:"))
import math
distance_formula= math.sqrt(((x2-x1)**2) +((y2-y1)**2))
print(distance_formula)

#19
v= int(input("enter the intergers number:"))
sum_calculation= (v*(v+1)/2)
print(sum_calculation)

#20
foot_length= float(input("enter the amount of feet:"))
inches_length= float(input("enter the amount of inches:"))

conversion_to_centimeters1= (foot_length*30.48) +(inches_length*2.54)
print((conversion_to_centimeters1), end=" cm")

#21
import math
a= float(input("enter the value of a:"))
b= float(input("enter the value of b:"))

hypotenese_formula= math.sqrt(((a)**2)+((b)**2))
print("The hypotenese is",hypotenese_formula)

#22
weight= float(input("enter the weight in kg:"))
height= float(input("enter the height in m:"))

BMI_calculator= (weight/((height)**2))
print("BMI =", BMI_calculator)

#23
x1= int(input("enter the value of x1:"))
y1= int(input("enter the value of y1:"))

x2= int(input("enter the value of x2:"))
y2= int(input("enter the value of y2:"))

midpoint_formula= (x1+x2)/2 ,(y1+y2)/2
print(midpoint_formula)

#24
w1=[]
for y in range(2000,3201):
    if (y%7==0) and (y%5==0):
        w1.append(str(y))
        print(','.join(w1))