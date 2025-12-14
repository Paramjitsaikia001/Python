# Python
Learning python

## NOTE
1. input() function always take string by default
2. we need to convert it as our requirement
3. to the values from the key in dictionary , we should use .get() function because it doesnot return error , it return "none"
4. we cannot use dict and list in the set because they are mutable and set is immuatable
5. super METHOD
6. DUNDER FUNCTION

## DECORETOR
1. staticmethod
2. classmethod


## usage of __str__ method in class
```
WITHOUT this method the object class will print like 

print(s) #s is the object of class

OUTPUT:
<__main__.Student object at 0x7f8c...>


WITH this method the output will be like

def __str__(self):
        return f"Student Name: {self.name}, Age: {self.age}"

s = Student("Paramjit", 21)
print(s)


OUTPUT :Student Name: Paramjit, Age: 21
```
