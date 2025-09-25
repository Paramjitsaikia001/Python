def searchLine(word):
    data=True
    line=1
    with open("practise.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line)
                return
            line+=1
    return -1

searchLine("developer")