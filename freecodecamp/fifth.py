day = input("enter a day :").lower() #the lower function convert the string into lowercase

'''
match day :
    case "monday":
        print("it's a weekday")
    case "tuesday":
        print("it's a weekday")
    case "webnesday":
        print("it's a weekday")
    case "thursday":
        print("it's a weekday")
    case "friday":
        print("it's a weekday")
    case "saturday":
        print("it's a weekday")
    case "sunday":
        print("wow! weeken")
    case _:
        print("invalid day")

'''

#we can write as

match day :
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday" | "saturday":
        print ("it's a weekday")
    case "sunday":
        print("WOW!! it's weekend")
    case _:
        print("invalid day")