#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2

def add(a,b):
    return a + b
    
def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b
    
def devide(a,b):
    try:
        return a/b
    except:
        print("float division by zero.")
    
def power(a,b):
    return a ** b
    
def reminder(a,b):
    return a % b
    

def select_op(choice):
    if choice == "#":
        return -1
    elif choice == "$":
        return 0
    elif choice in ("+","-","/","*","^","%"):
        while (True):
            num1 = str(input("Input first number: "))
            if num1 == "#":
                return -1
            elif num1 == "$":
                return 0 
            try:
                num1 = float(num1)
                break
            except:
                print("Not a vallid number, Please enter a valid number!")
                continue

        while (True):
            num2 = str(input("Enter second number: "))
            if num2 == "#":
                return -1
            elif num2 == "$":
                return 0 
            try:
                num2 = float(num2)
                break
            except:
                print("Not a vallid number, Please enter a valid number!")
                continue

        if choice == "+":
            print( num1,"+",num2,"=", add(num1, num2))
        elif choice == "-":
            print(num1,"-",num2,"=", subtract(num1,num2))
        elif choice == "*":
            print(num1,"*",num2,"=", multiply(num1,num2))
        elif choice == "/":
            print(num1,"/",num2, "=", devide(num1,num2))
        elif choice == "^":
            print(num1,"^",num2, "=", power(num1,num2))
        elif choice == "%":
            print(num1,"%",num2, "=" , reminder(num1,num2))
        else:
            print("Something Went Wrong")

while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()
