#lambda function 
# NOTE : lambda function is anonymous function that have only one expression but can take any number of agrument


# simple 
x = lambda a :a + 10
y = lambda a,b : a+b
print(x(10)) # OUTPUT : 20
print(y(10,20)) # OUTPUT : 30

# lambda function within function

def myfunc(n):
    return lambda a :a**n

power = myfunc(2)

print("power of ",power(3)) #OUTPUT 9

#map 
#NOTE : apply function to all element in an iterable


def double(n):
    return n**2
nums=[x for x in range(1,20)]

# doubled = list(map(double(x),nums))
# ❌ it will show error because map want function object not the function call



# doubled = list(map(double,nums))
# **** here we need lambda function 


doubled = list(map(lambda x :x**2,nums)) 

print("squre using map func:",doubled)


even_nums = list(filter(lambda x :x%2==0 , nums))
print("printing the even number using filter function:",even_nums)


# ZIP : its combine the two tuple/list in tuple pair values and return a object

one =["hello","morning","blue","apple","zerox"]
two =["bye","night"]

com = zip(one,two)
print(list(com))
print(tuple(com)) #it will show error bcz zip() returns an iterator, and an iterator can only be used one time.

for_sort =[3,5,1,23,11,55,12,1,0]
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

#sorting : it function is not support in tuple and set
# for_sort.sort(key=lambda x : x%3)
# print("sorting one using sort function",for_sort)

cars.sort(key=lambda x :x["car"])
print("sorting cars using sort function",cars)


# sorted 

