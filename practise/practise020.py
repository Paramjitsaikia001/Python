# from a file containing numbers separated by comma . print the count of even numbers

count=0
with open("practise2.txt","r") as f:
    data=f.read()

    # ONE WAY

    # num =""
    # for i in range(len(data)):
    #     if(data[i]==','):
    #         print(int(num))
    #         if int(num)%2==0:
    #             count+=1
    #         num=""
    #     else:
    #         num+=data[i]
    # data=f.read()



    # ANOTHER WAY
    num=data.split(",")
    print(num)
    for val in num:
        if(int(val)%2==0):
            count+=1
            print(int(val))

print("Total numbers: ",count)