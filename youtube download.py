from tkinter import filedialog,messagebox
from pytube import YouTube
from tkinter import *
from ttkbootstrap import *
from PIL import ImageTk, Image



def Browse():
	
 download_Directory = filedialog.askdirectory(
 initialdir="YOUR DIRECTORY PATH", title="Save Video")
 download_Path.set(download_Directory)

def audio():
 Y = YouTube(link.get())
 download_Directory = download_Path.get()
 Y = Y.streams.get_audio_only()
 Y = Y.download((download_Directory))
 messagebox.showinfo("SUCCUSEFULLY DOWNLOADED","IN LOW RESOLUTION😒")

def DownloadL():

 Y = YouTube(link.get())
 download_Directory = download_Path.get()
 Y = Y.streams.get_lowest_resolution()
 Y = Y.download((download_Directory))
 messagebox.showinfo("SUCCUSEFULLY DOWNLOADED","IN LOW RESOLUTION😒")
 
 


def DownloadH():

  Y = YouTube(link.get())
  download_Directory = download_Path.get()
  Y = Y.streams.get_highest_resolution()
  Y.download((download_Directory)) 
  messagebox.showinfo("SUCCUSEFULLY DOWNLOADED","IN HIGH RESOLUTION😘")



u = Tk()
u.title("youtube downloader")
style = Style(theme="solar")
u.geometry("1000x1000")



label = Label(text = "Enter link: ",font='arial 16' ).place(x=300,y=300)



img = ImageTk.PhotoImage(Image.open("youtube-logo-new.jpg"))
label1 = Label(u,image = img,height=100,width=400).place(x = 300,y = 100)

link = StringVar()

entry = Entry(u, textvariable = link, width=24, font='arial 16',bg="white").place(x=400,y=300)


b3 = Button(text="select the save location",command=Browse,font="10").place(x=420,y=350)
b1 = Button(text="DOWNLOAD IN LOW RESOLUTION",command=DownloadL,font="10").place(x=400,y=450)
b2 = Button(text="DOWNLOAD IN HIGH RESOLUTION",command=DownloadH,font="10").place(x=400,y=500)
b4 = Button(text="DOWNLOAD THE MUSIC",command=audio,font="10").place(x=400,y=550)

download_Path = StringVar()

u.mainloop()