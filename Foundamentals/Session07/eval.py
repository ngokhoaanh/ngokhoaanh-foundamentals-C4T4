# define
# arguments 


def calculate (x,y,op) :

    if op == "+" :
        res = x + y 
    elif op == "-" :
        res = x-y
    elif op == "*" :
        res = x*y 
    elif op == "/" :
        res = x/y
    
    return res 



# call function
result = calculate (1,2,"+")
print(result)

