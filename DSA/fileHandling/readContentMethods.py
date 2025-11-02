with open("sample.txt","r") as f:
    # print("readlines",f.readlines()) #read line by one
    print("readline",f.readline()) #read one line at atime
    # print("read",f.read()) #read all content character by character