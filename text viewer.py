from ttkbootstrap import *
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

def openfile():
     
    filepath = filedialog.askopenfilename(filetypes= (("text files","*.txt"),("all files","*.*"),("PDF files ","*.pdf*")))

    file = open(filepath,'r')
    a = (file.read())
    print(a)
    file.close()

    view_box = Text(screen , height=100, width=50, font=("arial black", 17,"bold" ), fg="blue", bg="purple") 
    view_box.place(x=250,y=250) 
    view_box.insert(1.0, a)


def showimage():
    screen.destroy()
    import passwordgenerator



def showchart():
    screen.destroy()
    import chart

screen = Tk()
style = Style(theme="solar")

label = Label(text="Text Viewer",font=("times",100),fg="brown") .pack()

button = Button(text="choose a file",command=openfile)
screen.geometry('1000x1000')
button.place(x=450,y=200)

#img = ImageTk.PhotoImage(Image.open("youtube-logo-new.jpg"))

#label = Label(screen, image = img)
#label.place(x=500,y= 250)

#button1 = Button(text="click here to go to password generator",command=showimage,height= "10",width="30")
#button1.place(x=1000,y=250)

#button2 = Button(text ="show chart",command=showchart).place(x= 500,y=500)

screen.mainloop()