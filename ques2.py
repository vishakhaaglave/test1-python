#program to calculate the simple interest
p=float(input("enter the principle amount:"))
t=float(input("enter the time:"))
r=float(input("enter the rate of interest:"))
si=(p*t*r)/100
print("simple interest is:",si)

#program to accept distance in km and convert into ms and cms 
d=float(input("enter the distance in kms:"))
m=d*1000
cm=d*100000
print("distance in meters is:",m)
print("distance in centimeters is:",cm)