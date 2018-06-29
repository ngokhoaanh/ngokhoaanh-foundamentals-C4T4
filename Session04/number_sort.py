numbers = [-10,0,5,-20,2,-100,2018]

# sorted_list =[]
# sorting = True

# while sorting :
#     min_numb = min(numbers)
#     sorted_list.append(min_numb)
#     numbers.remove(min_numb)

#     if len(numbers)==0 :
#         sorting = False

# print (*sorted
print("Guess your number game")
print("now think of a number(0-100),then press Enter")
input()
print("""All you have to do is to answer to my guess
'c' if my guess is 'C'orrect
's' if my guess is 'S'maller than your number
'l' if my guess is 'L'arger than your number
""")

low = 0
high = 100
playing= True
while playing :
    mid = (low+high)//2
    ans = input("Is {0} your number :".format(mid)).upper()

    if ans =="C" :
        print("I knew it!!!")
        playing = False
    elif ans =="S" :
        low = mid
    elif ans == "L" :
        high = mid
    else :
        playing = False

