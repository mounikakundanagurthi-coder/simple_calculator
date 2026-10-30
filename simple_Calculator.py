print("** Sample Calculator **")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def exit_():
    print("exit")
n1=int(input("enter first no:"))
n2=int(input("enter second no:"))
option=int(input("selct option form 1 to 5:"))
if option==1:
    add(n1,n2)
elif option==2:
    sub(n1,n2)
elif option==3:
    mul(n1,n2)
elif option==4:
    div(n1,n2)
elif option==5:
    exit_()
else:
    print("invalid option")
