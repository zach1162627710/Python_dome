import tkinter
import turtle


def wjx(event):
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
root = tkinter.Tk()
###
menu = tkinter.Menu(root)  #建一个menu菜单
submenu = tkinter.Menu(menu, tearoff=0) #建一个下拉菜单
menu.add_cascade(label="File", menu=submenu) #submen加载到menu上
submenu.add_command(label="Open") #子菜单增加label "Open"
submenu.add_command(label="Save") #子菜单增加label "Save"
root.config(menu=menu)            #将menu config到root上

###

label = tkinter.Label(root, text="你好")
label.pack()

button1 = tkinter.Button(root, text="五角星")
button1.pack()

button1.bind('<Button-1>', wjx)
root.mainloop()


