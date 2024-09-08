#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2

def add(a,b):
    if choice == "+" :
        return a + b
    
def subtract(a,b):
    if choice == "-":
        return a - b
    
def mltiply(a,b):
    if choice == "*":
        return a * b
    
def devide(a,b):
    if choice == "/":
        return a/b
    
def power(a,b):
    if choice == "^":
        return a ** b
    
def reminder(a,b):
    if  choice == "%":
        return a % b
    




#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3


       



#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
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
