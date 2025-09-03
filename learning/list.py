# mark=[78,89,90,67]
# print(mark)#output=[78,89,90,67]
# print(mark[3])#output=67
# print(type(mark))# output:<class 'list'>
# print(len(mark))#output=4
# print(mark[1:4])#[89, 90, 67]
# print(mark[:4])#[78, 89, 90, 67]
# print(mark[1:])#[89, 90, 67]
# print(mark[1:len(mark)])#[89, 90, 67]
# print(mark[-3:-1])#[89, 90]

# #different datatypes
# student=["paranm",67,"jorhat"]
# print(student)
# len(student)
# print(student[1])
# student[0]="debojit" #list is mutable
# print(student[0])
# print(student)

# # #list method
# list=[2,5,3]
# append=list.append(4)#help to add new value in the end
# print(list.append(1)) #return none because append cannot return anything
# print("after apppend:",list) #[1, 2, 3, 4]

# sort=list.sort()#use to sorting in ascending order
# print(list.sort())#return none because sort cannot return anything 
# print("after sort:",list)

# sortR=list.sort(reverse=True)#use sorting in desandinf order
# print("descending order:",list)

# #sorting method is also allow in string according to alphabet
# str=["apple","mango","banana","orange"]
# sort=str.sort()
# print("using sorting in string",str)#['apple', 'banana', 'mango', 'orange']
# str.reverse()#to reverse the string
# print("using reverse:",str)

list=[2,4,5,6]
list2=["param","giti","hirak"]
list.insert(0,1)#use any value in any index of the list .its format is list.insert(index,value)
list2.insert(1,"debojit")
print(list ,list2) #[1, 2, 4, 5, 6] ['param', 'debojit', 'giti', 'hirak']

list.remove(4)#use to remove the first value from left side
list2.pop(2)#use to remve the value as their index 
print(list,list2)#[1, 2, 5, 6] ['param', 'debojit', 'hirak']
