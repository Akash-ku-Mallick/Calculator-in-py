from tkinter import *
import math

window = Tk()
window.title = "Calculator"

num1 = 0.00
num2 = 0.00
result = 0.00
operation = " "

e = Entry(window, width=16, font=('Time', 28, 'italic'))
e.grid(row=1, column=0, columnspan=4)

top = Entry(window, width=59, font=('Time', 10, 'normal'))
top.grid(row=0, column=0, columnspan=5)


def start(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def top_insert(number, symbol):
    if symbol == "√" or "=":
        top.insert(0, symbol + str(number))
    else:
        top.insert(0, str(number) + symbol)


def plus():
    global num1, operation
    first_num = e.get()
    num1 = float(first_num)
    operation = "add"
    top_insert(num1, "+")
    e.delete(0, END)


def minus():
    global num1, operation
    first_num = e.get()
    num1 = float(first_num)
    operation = "sub"
    top_insert(num1, "-")
    e.delete(0, END)


def multi():
    global num1, operation
    first_num = e.get()
    num1 = float(first_num)
    operation = "mul"
    top_insert(num1, "x")
    e.delete(0, END)


def dev():
    global num1, operation
    first_num = e.get()
    num1 = float(first_num)
    operation = "dived"
    top_insert(num1, "/")
    e.delete(0, END)


def mod():
    global num1, operation
    first_num = e.get()
    num1 = float(first_num)
    operation = "mod"
    top_insert(num1, "%")
    e.delete(0, END)


def power():
    global num1, operation
    first_num = e.get()
    num1 = float(first_num)
    operation = "pow"
    top_insert(num1, "^2")
    e.delete(0, END)


def sqrt():
    top_insert(num1, "√")
    e.insert(0, str(math.sqrt(num1)))


def fact():
    global num1
    first_num = e.get()
    num1 = float(first_num)
    e.delete(0, END)
    top_insert(num1, "!")
    e.insert(0, str(math.factorial(int(num1))))


def clear():
    e.delete(0, END)


def clean():
    top.delete(0, END)


def equal():
    global num1, num2, operation, result
    sec_num = e.get()
    num2 = int(sec_num)
    e.delete(0, END)
    top_insert(num2, "=")
    if operation == "add":
        result = num1 + num2
        e.insert(0, str(result))
    if operation == "sub":
        result = num1 - num2
        e.insert(0, str(result))
    if operation == "mul":
        result = num1 * num2
        e.insert(0, str(result))
    if operation == "dived":
        result = num1 / num2
        e.insert(0, str(result))
    if operation == "mod":
        result = num1 % num2
        e.insert(0, str(result))
    if operation == "pow":
        result = math.pow(num1, num2)
        e.insert(0, str(result))
    result = 0
    window.bind("<Key>", key_pressed)


b_clear = Button(window, text=" AC ", command=clear, activeforeground="black", activebackground="red")

b_1 = Button(window, text=" 1 ", command=lambda: start(1), activeforeground="black", activebackground="red",
             padx=30, pady=15)
b_2 = Button(window, text=" 2 ", command=lambda: start(2), activeforeground="black", activebackground="red",
             padx=30, pady=15)
b_3 = Button(window, text=" 3 ", command=lambda: start(3), activeforeground="black", activebackground="red",
             padx=30, pady=15)
b_4 = Button(window, text=" 4 ", command=lambda: start(4), activeforeground="black", activebackground="red",
             padx=30, pady=15)
b_5 = Button(window, text=" 5 ", command=lambda: start(5), activeforeground="black", activebackground="red",
             padx=30, pady=15)
b_6 = Button(window, text=" 6 ", command=lambda: start(6), activeforeground="black", activebackground="red",
             padx=30, pady=15)
b_7 = Button(window, text=" 7 ", command=lambda: start(7), activeforeground="black", activebackground="red",
             padx=30, pady=15)
b_8 = Button(window, text=" 8 ", command=lambda: start(8), activeforeground="black", activebackground="red",
             padx=30, pady=15)
b_9 = Button(window, text=" 9 ", command=lambda: start(9), activeforeground="black", activebackground="red",
             padx=30, pady=15)
b_0 = Button(window, text=" 0 ", command=lambda: start(0), activeforeground="black", activebackground="red", padx=30,
             pady=15)
b_plus = Button(window, text=" + ", command=plus, activeforeground="black", activebackground="red", padx=29, pady=15)
b_minus = Button(window, text=" - ", command=minus, activeforeground="black", activebackground="red", padx=30, pady=15)
b_multi = Button(window, text=" x ", command=multi, activeforeground="black", activebackground="red", padx=30, pady=15)
b_div = Button(window, text=" / ", command=dev, activeforeground="black", activebackground="red", padx=30, pady=15)
b_equal = Button(window, text=" = ", command=equal, activeforeground="black", activebackground="red", padx=70, pady=15)
b_mod = Button(window, text="%", command=mod, activeforeground="black", activebackground="red", padx=30, pady=15)
b_pow = Button(window, text="^", command=power, activeforeground="black", activebackground="red", padx=30, pady=15)
b_sqrt = Button(window, text="√", command=sqrt, activeforeground="black", activebackground="red", padx=30, pady=15)
b_fact = Button(window, text="n!", command=fact, activeforeground="black", activebackground="red", padx=30, pady=15)
b_clean = Button(window, text="AC", command=clean, activeforeground="black", activebackground="red", width=5)

b_plus.grid(row=2, column=3)
b_minus.grid(row=3, column=3)
b_multi.grid(row=4, column=3)
b_div.grid(row=5, column=3)

b_7.grid(row=2, column=0)
b_8.grid(row=2, column=1)
b_9.grid(row=2, column=2)
b_4.grid(row=3, column=0)
b_5.grid(row=3, column=1)
b_6.grid(row=3, column=2)
b_1.grid(row=4, column=0)
b_2.grid(row=4, column=1)
b_3.grid(row=4, column=2)
b_0.grid(row=5, column=2)
b_equal.grid(row=5, column=0, columnspan=2)
b_clear.grid(row=1, column=4)
b_mod.grid(row=2, column=4)
b_pow.grid(row=3, column=4)
b_sqrt.grid(row=4, column=4)
b_fact.grid(row=5, column=4)
b_clean.grid(row=0, column=4)


def key_pressed(event):
    key = event.char
    if key == "1" or key == "2" or key == "3" or key == "4":
        start(int(key))
    if key == "5" or key == "6" or key == "7" or key == "8":
        start(int(key))
    if key == "9" or key == "0":
        start(int(key))
    if key == "p":
        power()
    if key == "r":
        sqrt()
    if key == "f":
        fact()
    if key == "c":
        clear()
    if key == "C":
        clean()
    if key == "=":
        plus()
    if key == "-":
        minus()
    if key == " ":
        equal()
    if key == "/":
        dev()
    if key == "x":
        multi()
    window.bind("<Key>", key_pressed)


window.bind("<Key>", key_pressed)

window.mainloop()
