# try to store 9 and 9.0 in set

# values ={9,9.0} ❌
# values ={int(9),float(9.0)} ❌

# values = {9,"9.0"} WORKED
values ={
    ("float",9.0),
    ("int",9)
}
print(values)