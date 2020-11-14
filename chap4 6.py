"""Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters
(hours and rate)"""
def computepay(h,r):
    if h<=0:
        pay=h*r
    else:
        pay=((h-40)*(1.5*r)+(40*r))
    return pay
h=float(input("enter hour: "))
r=float(input("enter rate: "))
print(computepay(h,r))
