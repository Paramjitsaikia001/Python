number =[4,2,3,1]

def square(list):
    result=[]
    for i in number:
        result.append(i**2)
    return result

finalList=square(number)

print(finalList)

#time complexity is O(n)