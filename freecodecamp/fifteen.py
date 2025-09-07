# import sys

# if len(sys.argv) < 2 :
#     sys.exit("too few argument")

# for arg in sys.argv:
#     print("hello , ",arg)

# OUTPUT :
# python3 fifteen.py paramjit niyar moucham git jyotishman
# hello ,  fifteen.py
# hello ,  paramjit
# hello ,  niyar
# hello ,  moucham
# hello ,  git
# hello ,  jyotishman



#SLICE function- it is a subset of a list
# name = ["paramjit","niyar","moucham","giti","joy"]
# print(name[1:4])
# print(name[:2])
# print(name[3:])

# OUTPUT:
# python3 fifteen.py                                      
# ['niyar', 'moucham', 'giti']
# ['paramjit', 'niyar']
# ['giti', 'joy']




import sys

if len(sys.argv) < 2 :
    sys.exit("too few argument")

for arg in sys.argv[1:]:
    print("hello , ",arg)