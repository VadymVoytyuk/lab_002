
number = int(input("Enter number 4 digit number:"))
a = number//1000
print (a)
b=(number-a*1000)//100
print(b)
c=(number-a*1000-b*100)//10
print(c)
d = number%10
print(d)
