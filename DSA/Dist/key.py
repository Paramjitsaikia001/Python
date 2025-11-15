d={
    "name":"paramjit saikia",
    "age":21,
    "college name":"lcb college"
}

for k in d.keys():
     values=d[k]
     print(k,values)

print(type("h"))

l=[x**2 for x in range(5) if (x%2)==0 ]
print(l)

print([(a,b) for a ,b in zip(range(3),range(4,6))])

print({a:b for a ,b in zip(range(3),range(4,7))})

print(chr(97))
print(ord("a"))
print({a:chr(a+64) for a in range(1,27)})