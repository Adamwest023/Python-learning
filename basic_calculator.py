# define functions needed: add,sub,div,mult
# print options to the user
# ask for values
# call the functions
# while loop to continue the program until the user exits

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))

def sub(a, b):
    answer = a - b 
    print(str(a) + " - " + str(b) + " = " + str(answer))
    
def div(a, b):
    answer = a / b 
    print(str(a) + " / " + str(b) + " = " + str(answer))
    
def mult(a, b):
    answer = a * b 
    print(str(a) + " * " + str(b) + " = " + str(answer))
    

print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("E. Exit")

choice = input("input your choice")

if choice == "a" or choice =="A":
    print('Addition')
    a = int(input("input first number: "))
    b = int(input("input second number: "))
    add(a,b)
elif choice == "b" or choice == "B": 
    print('Subtraction')
      
