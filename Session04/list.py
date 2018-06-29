print("Hi there , here you favote things so far")
menu = ["death note","netflix","teaching"]
print(*menu,sep = ", ")
y =str(input("name on thing you want to add ?"))
menu .append(y)
print(*menu,sep = ", ")
print(len(menu))