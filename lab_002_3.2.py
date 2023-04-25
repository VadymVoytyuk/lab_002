number = int(input("Enter 5 digit number:"))
a = number//10000
b=(number-a*10000)//1000
c=(number-a*10000-b*1000)//100
d=(number-a*10000-b*1000-c*100)//10
e=number%10
print(e*10000+d*1000+c*100+b*10+a)


