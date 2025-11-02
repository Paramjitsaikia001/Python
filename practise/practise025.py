# display the all element of a nested list

a=[2,3,["a","b","c"],4,5,]


for x in a:
    if isinstance(x,list):
        for y in x:
            print(y)
    else:
        print(x)
