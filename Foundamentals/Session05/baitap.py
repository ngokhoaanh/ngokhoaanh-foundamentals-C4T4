dictionary = {
    "hc" : "hoc",
    "ng" : "nguoi",
    "pt" : "piet",
    "eny": "em nguoi yeu",
    "any":"anh nguoi yeu",
    "ns":"noi",
    "ngta":"nguoi ta",
    "lm":"lam",
    "r":"roi",
    "stt":"status"

}

loop = True 
while loop : 

    for key in dictionary.keys() :
        print(key,end="\t")

    print()
    code = input("Your code ?")
    key = code
    print("*"*20)
    if key in dictionary :
        print("Translation :" ,dictionary[key])
    else :
        no = input("Not found , do you want to contribute this word ? (Y/N) ?")
        if no == "Y" :
            r = input("Enter your translation :")
            print("*"*20)
            dictionary[code] = r
            for key in dictionary.keys() :
                print(key,end="\t")
        else : 
            print("Bye")
            loop = False 
        
        

        


