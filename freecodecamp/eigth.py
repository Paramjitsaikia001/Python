def main():
    show(get_number())

def get_number():
    while True:
        n=int(input("n = "))
        if n > 0:
            return n


def show(n):
    for _ in range(n):
        print("happy teachers day")


main()