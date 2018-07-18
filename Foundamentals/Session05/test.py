# minh_duc = ["Minh Duc","Son La",19,2,1,10]
# dictionary/object/map

# key : value
# create new dictionary
person = {
    "name": "Minh Duc",
    "age" : 19,
    "ex" : 2,
    "IQ" : 1

}
# print (person)
# # add/update new key - value
# person["hometown"] = "Son La"
# print (person)
# person['ex'] = 3 
# print(person)

# read
# print(person["age"])
# for key in person.keys() :
#     print(key,end = "\t")

# for value in person.values() :
#     print(value)

key = "school"
if key in person :

    print(person[key])
else : 
    print("Not found")

