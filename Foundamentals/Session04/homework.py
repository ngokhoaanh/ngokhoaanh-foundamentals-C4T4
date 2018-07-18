# Bai 2
# catalogue = ["C,R,U,D"]
# i = input("Welcome to our shop, what do you want ?")
# R =["T-shirt,Sweater"]
# v = input("Enter new item :")
# R.append("Jeans")

# print("Our items :" ,*R, sep=" ")

# Bai 3
# i = input("Welcome to our shop, what do you want ?")
# Catalogue =["T-shirt","Sweater"]
# v = input ("Update position :")
# b = input ("New item :")
# Catalogue[1] = "Skirt"
# Catalogue.append("Jeans")
# print("Our items :",*Catalogue,sep=" ")

i = input("Welcome to our shop, what do you want ?")
Catalogue =["T-shirt","Skirt","Jeans"]
v = input("Delete position :")
del Catalogue[2]
print("Our items :",*Catalogue)

