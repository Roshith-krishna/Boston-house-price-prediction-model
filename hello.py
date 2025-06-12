from datetime import date
t=date.today()
day=t.day
month=t.month
year=t.year
a=int(input("enter your year of birth"))
b=int(input("enter your month of birth"))
#c=int(input("enter your day of birth"))
age=year-a
print("you lived ",age,"years")

if b==month:
    mo=age*12
elif month>b:
     f=b-month
     m=age*12+f
print("you lived ",mo,"months")      
