try:
    f = open("Data.txt", "x") 
except FileExistsError:
    pass
f=open("Data.txt","a+")
m1=0
m2=0
m3=0
m4=0
m5=0
total=0
def menu():
    print("```````MAIN MENU``````")
    print("Enter 1 to Add Items")
    print("Enter 2 to Delete Items")
    print("Enter 3 to View Cart")
    print("Enter 4 to Pay Bill")
    print("Enter 5 to Exit")
    c=int(input("Enter a number - "))
    if c==1:
        add()
    elif c==2:
        delete()
    elif c==3:
        view()
    elif c==5:
        print("Thanks For visiting our shop")
        input("Click enter to exit")
        exit()
    elif c==4:
        bill()
    else :
        print("Enter a correct number ")
        print("\n")

        menu()

def bill():
    print()
    name=input("Enter your name: ")
    phone_number=input("Enter your phone number: ")
    total = m1 * 100 + m2 * 200 + m3 * 300 + m4 * 400 + m5 * 500
    f.write(f"{name}, {phone_number}, {total}\n")
    print("Bill saved Successfully")
    input("Click enter to exit")
    exit()


def list():
    print("")

    print("Enter 1 to select Mango1 : 100")
    print("Enter 2 to select Mango2 : 200")
    print("Enter 3 to select Mango3 : 300")
    print("Enter 4 to select Mango4 : 400")
    print("Enter 5 to select Mango5 : 500")
    print("Enter 6 to return main menu")
    print("\n")

    c1=int(input("Enter your Choice : "))
    return c1

def add():
    global m1, m2, m3, m4, m5
    c2=list()
    print("\n")

    if c2==1:
        print("Mango1 selected ")
        a=int(input("Enter the Quantity : "))
        m1=a

    elif c2==2:
        print("Mango2 selected ")
        a=int(input("Enter the Quantity : "))
        m2+=a

    elif c2==3:
        print("Mango3 selected ")
        a=int(input("Enter the Quantity : "))
        m3+=a
    elif c2==4:
        print("Mango4 selected ")
        a=int(input("Enter the Quantity : "))
        m4+=a
    elif c2==5:
        print("Mango5 selected ")
        a=int(input("Enter the Quantity : "))
        m5+=a
    elif c2==6:
        menu()
    else:
        print("Enter Proper number ")
        add()
    print("Item(s) added successfully")
    input("Click enter to continue")
    print()

    menu()

def delete():
    global m1, m2, m3, m4, m5
    c3=list()
    print()
    
    if c3==1:
        if m1>0:
            print("Mango1 selected ")
            a=int(input("Enter the Quantity : "))
            if a<=m1:
                m1-=a
            else:
                print("Entered Quantity is more than the cart")
                print("\n")

                delete()
        else:
            print("This item is not in your cart")
            print("\n")

            delete()
    elif c3==2:
        if m2>0:
            print("Mango2 selected ")
            a=int(input("Enter the Quantity : "))
            if a<=m2:
                m2-=a
            else:
                print("Entered Quantity is more than the cart")
                print("\n")

                delete()
        else:
            print("This item is not in your cart")
            print("\n")

            delete()
    elif c3==3:
        if m3>0:
            print("Mango3 selected ")
            a=int(input("Enter the Quantity : "))
            if a<=m3:
                m3-=a
            else:
                print("Entered Quantity is more than the cart")
                print("\n")

                delete()
        else:
            print("This item is not in your cart")
            print("\n")

            delete()

    elif c3==4:
        if m4>0:
            print("Mango4 selected ")
            a=int(input("Enter the Quantity : "))
            if a<=m4:
                m4-=a
            else:
                print("Entered Quantity is more than the cart")
                print("\n")

                delete()
        else:
            print("This item is not in your cart")
            print("\n")

            delete()
            
    elif c3==5:
        if m5>0:
            print("Mango1 selected ")
            a=int(input("Enter the Quantity : "))
            if a<=m5:
                m5-=a
            else:
                print("Entered Quantity is more than the cart")
                print("\n")

                delete()
        else:
            print("This item is not in your cart")
            print("\n")

            delete()
    elif c3==6:
        print("\n")

        menu()
    else:
        print("Enter Proper number ")
        print("\n")

        delete()
    print("Items Deleted successfully")
    input("Click enter to continue")
    print("\n")
    menu()
from tabulate import tabulate
def view():
    global m1,m2,m3,m4,m5,total
    print("\n")
    print("````Total Bill````")
    total=m1*100+m2*200+m3*300+m4*400+m5*500
    table=[
        ["ITEM", "Quantity", "Price(total)"],
        ["Mango1",m1,m1*100],
        ["Mango2",m2,m2*200],
        ["Mango3",m3,m3*300],
        ["Mango4",m4,m4*400],
        ["Mango5",m5,m5*500],
        ["Total","",total]
    ]
    print(tabulate(table, headers="firstrow", tablefmt="grid"))
    input("Click enter to continue")
    print("\n")
    menu()




menu()