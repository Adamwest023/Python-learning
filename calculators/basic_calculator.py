# define functions needed: add,sub,div,mult
# print options to the user
# ask for values
# call the functions
# while loop to continue the program until the user exits

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
    answer = a - b 
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")
    
def div(a, b):
    answer = a / b 
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")
    
def mult(a, b):
    answer = a * b 
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")
    
while True: 
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("input your choice: ")
        
    if choice == "a" or choice =="A":
        print('Addition')
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        add(a,b)
        print("Would you like to make another calculation?")
    elif choice == "b" or choice == "B": 
        print('Subtraction')
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        sub(a,b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        mult(a,b)
    elif choice == "d" or choice == "D":
        print("Division") 
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        div(a,b)
    elif choice == "e" or choice == "E":
        print("Program ended")
        quit() 
