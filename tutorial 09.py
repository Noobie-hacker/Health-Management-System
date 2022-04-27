#Exercise 2: faulty Calculator

n1=int(input("Enter the first number: "))
n2=int(input("Enter the Second number: "))
n3=input("Enter an operator (+,-,*,/): ")

if n1==45 and n2==3 and n3=="*":
    print("multiplication is: 555")
elif n1==56 and n2==9 and "+":
    print("The addition is: 77")
elif n1==56 and n2==4 and n3=="/":
    print("The division is: 4")
elif n3=="+":
    print("The addition is: ",n1+n2)
elif n3=="*":
    print("The multiplication is: ", n1*n2)
elif n3=="/":
    print("The division is: ",n1/n2)
elif n3=="-":
    print("The substraction is: ",n1-n2)
else:
    print("Error ")
