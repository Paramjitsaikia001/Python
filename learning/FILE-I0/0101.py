# f = open("demo.txt","r")

with open("demo.txt","r") as f:

# data=f.read()
    data = f.readlines()
    print(data)

# f.close()