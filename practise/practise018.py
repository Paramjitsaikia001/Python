# WAP to replace all occurances of "java" with python

with open("practise.txt","w") as f:
    f.write("hello from java.\njava can develop app.\njava is popular programming language")

with open("practise.txt","r") as f:
    data=f.read()
    word="popular"
    if data.find(word)==-1:
        print("WORD not found")
    else:
        print("FOUND")

data =data.replace("java","python")

with open("practise.txt","w") as f:
    f.write(data)