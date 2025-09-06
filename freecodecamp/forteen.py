import sys
# print("my name is ", sys.argv)

# output :
#         python3 forteen.py
#             my name is  ['forteen.py']
#         paramjitsaikia@Paramjits-MacBook-Air freecodecamp % python3 forteen.py paramjit saikia
#             my name is  ['forteen.py', 'paramjit', 'saikia']

# print("my name is ", sys.argv[1])

# output :python3 forteen.py "Paramjit Saikia"
#         my name is  Paramjit Saikia


# if len(sys.argv) < 2 :
#     print("too few argument")
# elif len(sys.argv) >2:
#     print("too many agrument")
# else :
#     print("my name is ", sys.argv[1])

# NOTE: work in every situation


# WHAT IF ?

# if len(sys.argv) < 2 :
#     print("too few argument")
# elif len(sys.argv) >2:
#     print("too many agrument")

# print("my name is ", sys.argv[1])

# NOTE : though i apply if condition still it'll show syntaxError : list index out of range


# the solution is 

if len(sys.argv) < 2 :
    sys.exit("too few argument")
elif len(sys.argv) >2:
    sys.exit("too many agrument")

print("my name is", sys.argv[1])