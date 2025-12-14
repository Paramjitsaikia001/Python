# f = open("demo2.txt","w")

# f.write("hello from paramjit saikia a web developer")
# f.close()

names =["paramjit saikia \n","bill gates"]
with open("demo2.txt","w") as f:
    f.writelines(names)