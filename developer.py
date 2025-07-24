from tkinter import*
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import cv2
import mysql.connector



class Developer:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1900x850+0+0")
        self.win.title("FACE ATTENDANCE SYSTEM")
        
        title_label = Label(self.win, text = "DEVELOPER", font=("times new roman",35,"bold"), fg = "darkblue")
        title_label.place(x = 0, y = 0,width=1450,height=50)
        
        img111 = Image.open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\photos/developer2.png")
        img111 = img111.resize((1540,800))
        self.photoimg1= ImageTk.PhotoImage(img111)
        
        bg_img1 = Label(self.win,image = self.photoimg1)
        bg_img1.place(x=0 , y=50,width=1530,height=800)
        
        
        main_frame = Frame(bg_img1,bd=2,bg="white")
        main_frame.place(x=10,y=20,width=1500,height=700)
        
        
        img11 = Image.open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\photos/ronit.jpg")
        img11 = img11.resize((400,600))
        self.photoimg2= ImageTk.PhotoImage(img11)
        
        bg_img = Label(main_frame,image = self.photoimg2)
        bg_img.place(x=1100 , y=-1,width=400,height=600)
        
        
        dep_label = Label(main_frame,text = "RONIT SINGH",font=("times new roman",43,"bold"),bg="white")
        dep_label.place(x=1100,y=610,height=50)
        
        textlabel = Label(main_frame,text="I am a passionate and detail-oriented developer who independently built this",font=("times new roman",25,"bold"),bg="white")
        textlabel.place(x=10,y=10)
        
    
        textlabe2 = Label(main_frame,text="Facial Recognition Attendance System as apractical implementation of",font=("times new roman",25,"bold"),bg="white")
        textlabe2.place(x=10,y=50)
        
        textlabe3 = Label(main_frame,text="computer vision and database management. From Designing the user",font=("times new roman",25,"bold"),bg="white")
        textlabe3.place(x=10,y=90)
        
        textlabe4 = Label(main_frame,text="interface using Tkinter to integrating OpenCV for real-time face recognition",font=("times new roman",25,"bold"),bg="white")
        textlabe4.place(x=10,y=130)
        
        textlabe5 = Label(main_frame,text="and setting up MySQL for secure data storage, I handeled every aspect of the",font=("times new roman",25,"bold"),bg="white")
        textlabe5.place(x=10,y=170)
        
        textlabe6 = Label(main_frame,text="project. The experience not only strengthen my programming and problem",font=("times new roman",25,"bold"),bg="white")
        textlabe6.place(x=10,y=210)
        
        textlabe7 = Label(main_frame,text="solving skills but also deepened my understanding of how AI can be applied",font=("times new roman",25,"bold"),bg="white")
        textlabe7.place(x=10,y=250)
        
        textlabe8 = Label(main_frame,text="applied to real-world solutions.",font=("times new roman",25,"bold"),bg="white")
        textlabe8.place(x=10,y=290)
    
        
if __name__ == "__main__":
    win = Tk()
    obj = Developer(win)
    win.mainloop()