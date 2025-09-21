dict={
    "name":"Paramjit Saikia",
    "result":{
        "Mathematics":90,
        "Physics":40,
        "English":97,
        "Science":79,
    }
}
# NOTE: to the values from the key in dictionary , we should use .get() function because it doesnot return error , it return "none"

# print(dict["name"]) #return error 

# print(dict.get("result"))

# print(dict["result"].get("Mathematics"))

# adding new key values using update function
new_dict={
    "name":"rahul kumar",
    "age":20
}
# dict.update(new_dict)

# adding new key values using assigning
dict["DOB"]="28-02-2005"
dict["name"]="Paramjit Saikia"

# removing element
# pop function can remove any key values
# dict.pop("DOB")

# popitem() function can remove last inserted key values
# dict.popitem()


# del keyword can delete one and totally the dict
# del dict["DOB"]
del dict
print(dict)