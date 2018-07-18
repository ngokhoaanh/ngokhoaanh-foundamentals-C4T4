from random import choice , randint 
import eval
x = randint(1,10)
y = randint(1,10)
op = choice (["+","-","*","/"])
error = choice ([-1,0,1])

res = eval.calculate (x,y,op)
print("{0} {1} {2} = {3}".format(x,op,y,res))
ans = input ("(Y/N) ?").lower()
if error == 0 :
    if ans =="Y" :
        a = True
        print("Yay")
    elif ans =="N":
        A = False
        print("Wrong")
if error != 0 :
    if ans =="Y" :
        a = False
        print("Wrong")
    if ans =="N" :
        a = True 
        print("True")





