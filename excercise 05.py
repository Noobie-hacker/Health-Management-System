#Health Management System
#3 clients- Tommy, Aurther, Jhon
#import datetime


#def getdate():
   # import datetime
   # return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client
import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter 1 for Food and 2 for Excercise: "))
        if c==1:
            value=input("Type here: ")
            with open("Tommy-food.txt","a") as op:
                op.write(str([str(gettime())]) + ": "+  value+ "\n")
            print("Succesfully Written")
        elif c==2:
            value = input("Type here: ")
            with open("Tommy-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Succesfully Written")
    elif k==2:
        c = int(input("Enter 1 for Food and 2 for Excercise: "))
        if c == 1:
            value = input("Type here: ")
            with open("Aurther-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Succesfully Written")
        elif c == 2:
            value = input("Type here: ")
            with open("Aurther-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Succesfully Written")
    elif k==3:
        c = int(input("Enter 1 for Food and 2 for Excercise: "))
        if c == 1:
            value = input("Type here: ")
            with open("Jhon-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Succesfully Written")
        elif c == 2:
            value = input("Type here: ")
            with open("Jhon-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Succesfully Written")
    else:
        print("Enter Valid input.")
def retrive(k):
    if k==1:
        c=int(input("Enter 1 for food and  2 for excercise: "))
        if c==1:
            with open("Tommy-food.txt") as op:
                for i in op:
                    print(i, end="")
        elif c==2:
            with open("Tommy-ex.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 2:
        c = int(input("Enter 1 for food and  2 for excercise: "))
        if c == 1:
            with open("Aurther-food.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Aurther-ex.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 1:
        c = int(input("Enter 1 for food and  2 for excercise: "))
        if c == 1:
            with open("Jhon-food.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Jhon-ex.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Please enter valid input")
print("Wlecome to Bappy's Health Management System")
a=int(input("Press 1 to log the value and press 2 to retrive the value: "))
if a==1:
    b=int(input("Press 1 for Tommy, 2 for Aurther, 3 for Jhon: "))
    take(b)
else:
    b=int(input("Press 1 for Tommy, 2 for Aurther, 3 for Jhon: "))
    retrive(b)