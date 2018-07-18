x = int(input ("x= "))
op = input ("operation(+,-,*,/) : ")
y = int(input("y= "))
print("*" * 5 )
if op == "+" :
    ans = x+y
 
elif op == "-" :
    ans = x-y
  
elif op == "*" :
    ans = x*y
 
elif  op == "/" :
    ans = x/y

print("*"*5)
print("{0} {1} {2} ={3}".format(x,op,y,ans))
print("*"*5)
    