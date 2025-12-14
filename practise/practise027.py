class AgeError(Exception):
    def __init__(self, message):
        self.message = message



try:
    age = int(input("Enter age: "))
    if age < 18:
        raise AgeError("Age must be 18 or above")
    print("Eligible")
except AgeError as e:
    print("Custom Exception:", e.message)