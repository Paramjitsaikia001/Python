str='paramjit saikia'
#check=str.endswith('ia') #it is true if'ia' is the end characters of string
check=str.endswith('jit')
print("using string function check it is exist or not :",check)
print("using string function to capitilize the first character :",str.capitalize()) #it is use to capitalize the 1st character of string
# replace = str.replace("a","o") #it is use to replce a old string to new string its format is str.replace("old"."new")
replace = str.replace("paramjit","debojit")#it can also replace a sub string
print("using string function to replace old to new : ",replace) 
# find=str.find("r")#it is use to find the index of a character that exist in the string in first from left side
# find=str.find("saikia") #it can also find theindex of sub string
find=str.find("n") #if the string is not  exist then it's ouput is -1
print("using string function to find the index of a string : ",find)
count=str.count("a")#it is use to frequence of a string
print("using string function to count the frequence of a string : ",count)