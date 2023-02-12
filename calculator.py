from tkinter import *
import parser

root = Tk()
root.title("Calculator")
display = Entry(root)
display.grid(row=0, columnspan=5, sticky=W+E, pady=2)
i = 0

#function to read inputs
def get_unput(num):
    global i
    display.insert(i, num)
    i+=1

#function for switch AC
def clear_all():
    display.delete(0,END)

def clear_last():
    cs = display.get()
    if len(cs):
        ns = cs[:-1]
        clear_all()
        display.insert(0,ns)
    else:
        clear_all()
        display.insert(0,"ERROR")

#function to read the operators
def get_operation(opr):
    global i
    length = len(opr)
    display.insert(i,opr)
    i+= length

#function for the final evaluation
def calculator():
    cs = display.get()
    try:
        a = parser.expr(cs).compile()
        res = eval(a)
        clear_all()
        display.insert(0,res)
    except:
        clear_all()
        display.insert(0,"ERROR")

#buttons
Button(root,text="1",command=lambda :get_unput(1)).grid(row=1,column=0)
Button(root,text="2",command=lambda :get_unput(2)).grid(row=1,column=1)
Button(root,text="3",command=lambda :get_unput(3)).grid(row=1,column=2)
Button(root,text="+",command=lambda :get_operation("+")).grid(row=1,column=3)
Button(root,text="<-",command=lambda :clear_last()).grid(row=1,column=4)

Button(root,text="4",command=lambda :get_unput(4)).grid(row=2,column=0)
Button(root,text="5",command=lambda :get_unput(5)).grid(row=2,column=1)
Button(root,text="6",command=lambda :get_unput(6)).grid(row=2,column=2)
Button(root,text="-",command=lambda :get_operation("-")).grid(row=2,column=3)
Button(root,text="AC",command=lambda :clear_all()).grid(row=2,column=4)

Button(root,text="7",command=lambda :get_unput(7)).grid(row=3,column=0)
Button(root,text="8",command=lambda :get_unput(8)).grid(row=3,column=1)
Button(root,text="9",command=lambda :get_unput(9)).grid(row=3,column=2)
Button(root,text="x",command=lambda :get_operation("x")).grid(row=3,column=3)
Button(root,text="exp",command=lambda :get_operation("**")).grid(row=3,column=4)

Button(root,text="/",command=lambda :get_operation("/")).grid(row=4,column=0)
Button(root,text="0",command=lambda :get_unput(0)).grid(row=4,column=1)
Button(root,text=".",command=lambda :get_unput(".")).grid(row=4,column=2)
Button(root,text="^2",command=lambda :get_operation("**2")).grid(row=4,column=3)
Button(root,text="=", bg="red",command=lambda :calculator()).grid(row=4,column=4)

root.mainloop()