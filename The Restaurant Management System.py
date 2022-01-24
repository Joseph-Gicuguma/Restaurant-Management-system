from tkinter import*
import sys;
import time;
import random;
import tkinter.messagebox as tkMessageBox;
#---------------------------------Developed By Joseph Gicuguma Kamau------------------------------------------------
#-----------------Log In ----------
#-----------------Log in window Password-----
def command1(event):
    if entry1.get() == 'ADMIN' and entry2.get() == 'password' or entry1.get() == 'JOMAH' and entry2.get()== 'password':
        home.deiconify()
        top.destroy()
    else:
        result = tkMessageBox.showwarning('ERROR', 'Incorrect Credentials', icon="warning")

def command2():
    home.destroy()
    top.destroy()
    sys.exit()

home = Tk()
top = Toplevel()

top.geometry('500x400')
top.title("Joseph Gicuguma.LTD")
top.configure(background='powder blue')
photo1 = PhotoImage(file="logo.png")
photo = Label(top, image=photo1, bg='white')
lbl7 = Label(top, text='LOGIN', font=('times', 15, 'bold'), fg='black', bg='powder blue', bd=15, anchor=W)
lbl0 = Label(top, text='Welcome to the Restaurant Management System', font=('times', 15), bg='powder blue')
lbl1 = Label(top, text='Username:', font=('times', 10), bg='powder blue')
entry1 = Entry(top)
lbl2 = Label(top, text='Password:', font=('times', 10), bg='powder blue')
entry2 = Entry(top, show="*")
btn2 = Button(top, text='Cancel', fg='red', bg='powder blue', command=lambda:command2())

entry2.bind('<Return>', command1)

lbl = Label(top, text='© Copyright Login screen 2021', font=('Arial', 9), bg='powder blue')
lbl8 = Label(top, text='Developed By: Joseph Gicuguma Kamau', font=('Helvetica', 8), bg='powder blue')

photo.grid(row=1, column=2)
lbl0.grid(row=0, column=2)
lbl7.grid(row=2, column=2)
lbl1.grid(row=3, column=1)
entry1.grid(row=3, column=2)
lbl2.grid(row=4, column=1)
entry2.grid(row=4, column=2)
btn2.grid(row=5, column=2)
lbl.grid(row=6, column=2)
lbl8.grid(row=7, column=2)
#-------------restaurant management system-----------------------------
#-----------------Restaurant Management system Window----------
home.title("Restaurant Management System")
home.geometry("1600x800")

text_Input = StringVar()
operator = ""

tops = Frame(home, width=1600, height=50, bg='light blue', relief=SUNKEN)
tops.pack(side=TOP)

f1 = Frame(home, width=800, height=500, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(home, width=300, height=500, relief=SUNKEN)
f2.pack(side=RIGHT)

localtime = time.asctime(time.localtime(time.time()))

lblinfo = Label(tops, font=('arial', 50, 'bold'), text="Restaurant Management System", fg='steel blue', bd=10,
                anchor='w')
lblinfo.grid(row=0, column=1)
lblinfo = Label(tops, font=('arial', 30, 'bold'), text=localtime, fg='steel blue', bd=10, anchor='w')
lblinfo.grid(row=1, column=1)

#---------------Calculator---------------------
def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btncleardisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    operator = ""
    text_Input.set(sumup)



txtDisplay = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg='powder blue',
                   justify='right')
txtDisplay.grid(columnspan=4)

btn7 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='7', bg='powder blue',
              command=lambda: btnclick(7)).grid(row=2, column=0)

btn8 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='8', bg='powder blue',
              command=lambda: btnclick(8)).grid(row=2, column=1)

btn9 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='9', bg='powder blue',
              command=lambda: btnclick(9)).grid(row=2, column=2)

btn6 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='6', bg='powder blue',
              command=lambda: btnclick(6)).grid(row=3, column=0)

btn5 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='5', bg='powder blue',
              command=lambda: btnclick(5)).grid(row=3, column=1)

btn4 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='4', bg='powder blue',
              command=lambda: btnclick(4)).grid(row=3, column=2)

btn3 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='3', bg='powder blue',
              command=lambda: btnclick(3)).grid(row=4, column=0)

btn2 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='2', bg='powder blue',
              command=lambda: btnclick(2)).grid(row=4, column=1)

btn1 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='1', bg='powder blue',
              command=lambda: btnclick(1)).grid(row=4, column=2)

btn0 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='0', bg='powder blue',
              command=lambda: btnclick(0)).grid(row=5, column=0)

btnequals = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='=',
                   bg='powder blue', command=btnEquals).grid(row=5, column=2)

btnclear = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='C',
                   bg='powder blue', command=btncleardisplay).grid(row=5, column=1)

division = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='/',
                   bg='powder blue', command=lambda: btnclick("/")).grid(row=5, column=3)

multiplication = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='x',
                   bg='powder blue', command=lambda: btnclick("*")).grid(row=4, column=3)

addition = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='+',
                   bg='powder blue', command=lambda: btnclick("+")).grid(row=2, column=3)

subtraction = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='-',
                   bg='powder blue', command=lambda: btnclick("-")).grid(row=3, column=3)
#-------------------------------------------menu----------------------------------------------------------------------
rand = StringVar()
fries = StringVar()
burger = StringVar()
filet = StringVar()
subtotal = StringVar()
total = StringVar()
service_charge = StringVar()
drinks = StringVar()
tax = StringVar()
cost =StringVar()
chicken_burger = StringVar()
chees_burger = StringVar()

lblreference = Label(f1, font=('arial', 16, 'bold'), text='Reference', bd=16, anchor='w')
lblreference.grid(row=0, column=0)
txtreference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4, bg='powder blue',
                     justify='right')
txtreference.grid(row=0, column=1)

lblfries = Label(f1, font=('arial', 16, 'bold'), text='Large Fries', bd=16, anchor='w')
lblfries.grid(row=1, column=0)
txtfries = Entry(f1, font=('arial', 16, 'bold'), textvariable=fries, bd=10, insertwidth=4, bg='powder blue',
                     justify='right')
txtfries.grid(row=1, column=1)

lblburger = Label(f1, font=('arial', 16, 'bold'), text='Burger Meal', bd=16, anchor='w')
lblburger.grid(row=2, column=0)
txtburger = Entry(f1, font=('arial', 16, 'bold'), textvariable=burger, bd=10, insertwidth=4, bg='powder blue',
                     justify='right')
txtburger.grid(row=2, column=1)

lblfilet = Label(f1, font=('arial', 16, 'bold'), text='Filet_o_Meal', bd=16, anchor='w')
lblfilet.grid(row=3, column=0)
txtfilet = Entry(f1, font=('arial', 16, 'bold'), textvariable=filet, bd=10, insertwidth=4, bg='powder blue',
                     justify='right')
txtfilet.grid(row=3, column=1)

lblchicken = Label(f1, font=('arial', 16, 'bold'), text='Chicken Meal', bd=16, anchor='w')
lblchicken.grid(row=4, column=0)
txtchicken = Entry(f1, font=('arial', 16, 'bold'), textvariable=chicken_burger, bd=10, insertwidth=4, bg='powder blue',
                     justify='right')
txtchicken.grid(row=4, column=1)

lblcheese = Label(f1, font=('arial', 16, 'bold'), text='Cheese Meal', bd=16, anchor='w')
lblcheese.grid(row=5, column=0)
txtcheese = Entry(f1, font=('arial', 16, 'bold'), textvariable=chees_burger, bd=10, insertwidth=4, bg='powder blue',
                     justify='right')
txtcheese.grid(row=5, column=1)

lbldrinks = Label(f1, font=('arial', 16, 'bold'), text='Drinks', bd=16, anchor='w')
lbldrinks.grid(row=0, column=2)
txtdrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=drinks, bd=10, insertwidth=4, bg='powder blue',
                     justify='right')
txtdrinks.grid(row=0, column=3)

lblcost = Label(f1, font=('arial', 16, 'bold'), text='Cost of Meal', bd=16, anchor='w')
lblcost.grid(row=1, column=2)
txtcost = Entry(f1, font=('arial', 16, 'bold'), textvariable=cost, bd=10, insertwidth=4, bg='powder blue',
                     justify='right')
txtcost.grid(row=1, column=3)

lblservice = Label(f1, font=('arial', 16, 'bold'), text='Service Cost', bd=16, anchor='w')
lblservice.grid(row=2, column=2)
txtservice = Entry(f1, font=('arial', 16, 'bold'), textvariable=service_charge, bd=10, insertwidth=4, bg='powder blue',
                     justify='right')
txtservice.grid(row=2, column=3)



lbltax = Label(f1, font=('arial', 16, 'bold'), text='State Tax', bd=16, anchor='w')
lbltax.grid(row=3, column=2)
txttax = Entry(f1, font=('arial', 16, 'bold'), textvariable=tax, bd=10, insertwidth=4, bg='powder blue',
                     justify='right')
txttax.grid(row=3, column=3)

lblsutotal = Label(f1, font=('arial', 16, 'bold'), text='Sub Total', bd=16, anchor='w')
lblsutotal.grid(row=4, column=2)
txtsutotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=subtotal, bd=10, insertwidth=4, bg='powder blue',
                     justify='right')
txtsutotal.grid(row=4, column=3)

lbltotal = Label(f1, font=('arial', 16, 'bold'), text='Total Cost', bd=16, anchor='w')
lbltotal.grid(row=5, column=2)
txttotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=total, bd=10, insertwidth=4, bg='powder blue',
                     justify='right')
txttotal.grid(row=5, column=3)

#--------------BUTTONS----------
def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    cof = float(fries.get())
    cod = float(drinks.get())
    cob = float(burger.get())
    cofil = float(filet.get())
    coc = float(chicken_burger.get())
    cocheese = float(chees_burger.get())

    codrink = cod * 50
    cofries = cof * 100
    coburger = cob * 250
    cofilet = cofil * 200
    cocheeseburger = cocheese * 300
    cochicken = coc * 150

    costofmeal = "Ksh", str('%.2f' % (codrink + cofries + coburger + cofilet + cocheeseburger + cochicken))

    paytax = ((codrink + cofries + coburger + cofilet + cocheeseburger + cochicken) * 0.2)

    totalcost = (codrink + cofries + coburger + cofilet + cocheeseburger + cochicken)

    servicecharge = ((codrink + cofries + coburger + cofilet + cocheeseburger + cochicken)/99)

    service = "Ksh", str('%.2f' % servicecharge)

    overalcost = "Ksh", str('%.2f' % (paytax + totalcost + servicecharge))
    paidtax = "Ksh", str('%.2f' % paytax)

    service_charge.set(service)
    total.set(overalcost)
    tax.set(paidtax)
    cost.set(costofmeal)
    subtotal.set(costofmeal)


def Quit():
    home.destroy()

def Reset():
    rand.set("")
    fries .set("")
    burger.set("")
    filet .set("")
    subtotal.set("")
    total.set("")
    service_charge.set("")
    drinks.set("")
    tax.set("")
    cost.set("")
    chicken_burger.set("")
    chees_burger.set("")


btntotal = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'), width=10,
                  text='Total', bg="powder blue", command=Ref).grid(row=7, column=1)

btnreset = Button(f1, padx=16, pady=8, bd=16, fg='black', font=('arial', 16, 'bold'), width=10,
                  text='Reset', bg="powder blue", command=Reset).grid(row=7, column=2)

btnexit = Button(f1, padx=16, pady=8, bd=16, fg='red', font=('arial', 16, 'bold'), width=10,
                  text='Exit', bg="powder blue", command=Quit).grid(row=7, column=3)


home.withdraw()
home.mainloop()