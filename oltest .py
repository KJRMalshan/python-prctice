def push(stak, value):
    stak.append(value)

def pull(stak):
    stak.pop()

list = []
push(list, 'a')
push(list, 'hai')
push(list, 'hu')
pull(list)
pull(list)


print(list)
def fiender():
    while True:
        try:
            print("press q to quit!")
            n = int(input("number: "))
            if n % 2 == 1:
                print("Weird")
            elif 2 < n <= 5:
                print("Not Weird")
            elif 5 < n < 20 :
                print("Weird")
            elif n >= 20 :
                print("Not Weird")
        except:
            return False
fiender()



n = int(input("enter a number:"))
for i in range(n+1) :
    if i == n +1:
        break
    else:
        print(i*i)
