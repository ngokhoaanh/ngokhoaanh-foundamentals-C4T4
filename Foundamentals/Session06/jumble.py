# 
# for i in range (len[chars]) :

#     from random import choice

#     chars = ['a','b','c']

#     rand_char = choice(chars)
#     print(rand_char)

# Cach 1
# chars = ['v','o','d','k','a']

# for i in range (len(chars)) :
#     from random import choice 
#     rand_char = choice(chars)
#     print(rand_char,end =" ")
#     chars.remove(rand_char)
# print()
# j = input("your answer :")
# if j == "vodka" :
#     print ("Hura")
# else :
#     print (":(")

# Cach 2
from random import choice 
words = ["champion","dungeon","vodka"]
word = choice(words)
chars = list(word)

while len(chars) > 0 :
    rand_chars = choice(chars)
    print(rand_chars,end=" ")
    chars.remove(rand_chars)


print()

while True :
    ans = input("Your guest :")

    if ans == word :
        print ("Hura")
        break
    else :
        print(":(")

