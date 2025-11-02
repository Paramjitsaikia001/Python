def Pairs(list):
    result=[]
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            pairTuple=(list[i],list[j])
            result.append(pairTuple)
    return result

number=[2,3,4,5]
finalResult = Pairs(number)
print(finalResult)

print(not True)
