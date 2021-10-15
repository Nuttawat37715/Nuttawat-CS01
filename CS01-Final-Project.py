from tkinter import*
def clear():
    global expression
    global lable_show_cal
    result="0"
    expression =""
    lable_show_cal.set(result)

def press(number):
    global expression
    global lable_show_cal
    expression=expression+number
    lable_show_cal.set(expression)
def equal():
    try:
        global expression
        global lable_show_cal
        result=str(eval(expression))
        lable_show_cal.set(result)
    except:
        result="error"
        expression=""
        lable_show_cal
    lable_show_cal.set(result)
TJ = Tk()
TJ.title("My Calculator")
TJ.option_add("font","consolas 30")
TJ.geometry("165x270")
TJ.configure(background="light blue")
lable_show_cal=StringVar()
lable_show_cal.set(0)
expression_field = Entry(TJ, textvariable=lable_show_cal)
expression_field.grid(columnspan=4, ipadx=20)
expression=""
Button(TJ,text="clear",fg="red",font=10,command=clear).grid(row=1,column=0,columnspan=4,sticky="news")
Button(TJ,text="7",font=10,command=lambda:press("7"),height=1, width=2).grid(row=2,column=0)
Button(TJ,text="8",font=10,command=lambda:press("8"),height=1, width=2).grid(row=2,column=1)
Button(TJ,text="9 ",font=10,command=lambda:press("9"),height=1, width=2).grid(row=2,column=2)
Button(TJ,text="/",font=10,command=lambda:press("/"),height=1, width=2).grid(row=2,column=3)

Button(TJ,text="4",font=10,command=lambda:press("4"),height=1, width=2).grid(row=3,column=0)
Button(TJ,text="5",font=10,command=lambda:press("5"),height=1, width=2).grid(row=3,column=1)
Button(TJ,text="6",font=10,command=lambda:press("6"),height=1, width=2).grid(row=3,column=2)
Button(TJ,text="*",font=10,command=lambda:press("*"),height=1, width=2).grid(row=3,column=3)

Button(TJ,text="1",font=10,command=lambda:press("1"),height=1, width=2).grid(row=4,column=0)
Button(TJ,text="2",font=10,command=lambda:press("2"),height=1, width=2).grid(row=4,column=1)
Button(TJ,text="3",font=10,command=lambda:press("3"),height=1, width=2).grid(row=4,column=2)
Button(TJ,text="-",font=10,command=lambda:press("-"),height=1, width=2).grid(row=4,column=3)

Button(TJ,text="0",font=10,command=lambda:press("0"),height=1, width=2).grid(row=5,column=0)
Button(TJ,text=".",font=10,command=lambda:press("."),height=1, width=2).grid(row=5,column=1,columnspan=2,sticky="news")
Button(TJ,text="+",font=10,command=lambda:press("+"),height=1, width=2).grid(row=5,column=3)

Button(TJ,text="=",font=10,bg="yellow",command=equal).grid(row=6,column=0,columnspan=4,sticky="news")

TJ.mainloop()
