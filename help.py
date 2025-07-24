from tkinter import*
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import cv2
import mysql.connector



class Help:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1900x850+0+0")
        self.win.title("FACE ATTENDANCE SYSTEM")
        
        title_label = Label(self.win, text = "HELP DESK", font=("times new roman",35,"bold"), bg = "skyblue",fg = "black")
        title_label.place(x = 0, y = 0,width=1550,height=50)
        
        img111 = Image.open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\photos/helpdesk.png")
        img111 = img111.resize((1540,800))
        self.photoimg1= ImageTk.PhotoImage(img111)
        
        bg_img1 = Label(self.win,image = self.photoimg1)
        bg_img1.place(x=0 , y=50,width=1530,height=800)
        
        helplabel = Label(self.win, text = "ContactUs at ronitsingh@gmail.com", font=("times new roman",25,"bold"),bg = "skyblue",fg = "black")
        helplabel.place(x = 415, y = 500,width=695,height=50)
        


if __name__ == "__main__":
    win = Tk()
    obj = Help(win)
    win.mainloop()