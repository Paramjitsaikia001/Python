#try catch
''' 
while True :
        try :
            x = int(input("enter value: "))
           # print(f"value = {x}")
            break
        except ValueError:
            print("x is not an integer")
        # else:
        #      break
        
print(f"value = {x}")

'''


# def main():
#     x=data_value()
#     print(f"value = {x}")


# def data_value():
#         while True:
#             try :
#                 x = int(input("enter value: "))
           
#             except ValueError:
#                 print("x is not an integer")
#             else:
#                 return x
        

# main()



#PASS-use to pass the excepting

# def main():
#     x=data_value()
#     print(f"value = {x}")


# def data_value():
#         while True:
#             try :
#                 return int(input("enter value: "))
           
#             except ValueError:
#                 pass #pass
        

# main()



#new method to show the input

def main():
    x=data_value("what is the value ? :")
    print(f"value = {x}")


def data_value(prompt):
        while True:
            try :
                x = int(input(prompt))
           
            except ValueError:
                print("x is not an integer")
            else:
                return x
        

main()