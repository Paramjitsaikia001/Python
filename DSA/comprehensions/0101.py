#list comprehensions

square = [x*2 for x in range(1,6)]
print(square)

even_nums = [x for x in range(11) if x%2==0]
print('even numbers:',even_nums)

names = [ "paramjit saikia","niyar kalita","moucham talukdar"]

print ([name.upper() for name in names])


# dictionary comprehensions

dict_nums = {x*2:x*10 for x in range(5)}
print("dict numbers:",dict_nums)

dict_even_nums = {i:(x,x%2==0) for i,x in enumerate(range(11))}

print("dict even numbers:",dict_even_nums)