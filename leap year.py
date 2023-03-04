year=int(input("enter year"))
if(year%4==0)and (year%400==0):
    print("leap year")
elif year%400==0:
    print(year,"is a leap year")
else:
    print("not leap year")
             
    
