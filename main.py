from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image , ImageTk
from student import Student
from train import Train
from facerecognition import facerecognition
from attendance import Attendance
from developer import Developer
from help import Help
import os
from time import strftime
from datetime import datetime

class Face_Attendance_System:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1900x850+0+0")
        self.win.title("FACE ATTENDANCE SYSTEM") 

        #background image
        img = Image.open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\photos\bge.png")
        img = img.resize((1900,850))
        self.photoimg = ImageTk.PhotoImage(img)
        
        bg_img = Label(self.win,image = self.photoimg)
        bg_img.place(x=0 , y=0,width=1900,height=850)
        
        title_label = Label(bg_img, text = "FACIAL  RECOGNITION  ATTENDANCE  SYSTEM  SOFTWARE",font=("times new roman",35,"bold"),bg = "white" , fg = "black")
        title_label.place(x = 40, y = 50,width=1450,height=100)
    
        def time():
            string = strftime('%H:%M:%S %p')
            lb1.config(text=string)
            lb1.after(1000,time)
        
        lb1 = Label(self.win, font=('times new roman',14,"bold"),bg="white",fg="black")
        lb1.place(x=5,y=5,width=110,height=30)
        time()
         # student button 
        student_button_img = Image.open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\photos/student.png")
        student_button_img.resize((220,220))
        self.photoimg1 = ImageTk.PhotoImage(student_button_img)
        
        b1 = Button(bg_img,image = self.photoimg1,cursor="hand2",command = self.student_details)
        b1.place(x = 100 , y = 200 , width = 220, height=220)
        
        b1_1 = Button(bg_img,text = "STUDENT DETAILS",cursor="hand2",command = self.student_details,font=("times new roman",15,"bold"),bg = "white" , fg = "black")
        b1_1.place(x = 100 , y = 420 , width = 220, height=30)
        
        
        # Detect face button
        DetectFace_button_img = Image.open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\photos/DetectFace.png")
        DetectFace_button_img.resize((220,220))
        self.photoimg2 = ImageTk.PhotoImage(DetectFace_button_img)
        
        b2 = Button(bg_img,command=self.facerecognition,image = self.photoimg2,cursor="hand2")
        b2.place(x = 450 , y = 200 , width = 220, height=220)
        
        b2_1 = Button(bg_img,command=self.facerecognition,text = "FACE DETECTOR",cursor="hand2",font=("times new roman",15,"bold"),bg = "white" , fg = "black")
        b2_1.place(x = 450 , y = 420 , width = 220, height=30)
        
        
        #Attendance button
        Attendance_button_img = Image.open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\photos/Attendance.png")
        Attendance_button_img.resize((220,220))
        self.photoimg3 = ImageTk.PhotoImage(Attendance_button_img)
        
        b3 = Button(bg_img,command=self.attendance,image = self.photoimg3,cursor="hand2")
        b3.place(x = 820 , y = 200 , width = 220, height=220)
        
        b3_1 = Button(bg_img,command=self.attendance,text = "ATTENDANCE",cursor="hand2",font=("times new roman",15,"bold"),bg = "white" , fg = "black")
        b3_1.place(x = 820 , y = 420 , width = 220, height=30)
        
        
        #Help
        Help_button_img = Image.open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\photos/help.png")
        Help_button_img.resize((220,220))
        self.photoimg4 = ImageTk.PhotoImage(Help_button_img)
        
        b4 = Button(bg_img,command=self.help,image = self.photoimg4,cursor="hand2")
        b4.place(x = 1170 , y = 200 , width = 220, height=220)
        
        b4_1 = Button(bg_img,command=self.help,text = "HELP",cursor="hand2",font=("times new roman",15,"bold"),bg = "white" , fg = "black")
        b4_1.place(x = 1170 , y = 420 , width = 220, height=30)
         
         
         #Train data
        Train_button_img = Image.open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\photos/Trained.png")
        Train_button_img.resize((220,220))
        self.photoimg5 = ImageTk.PhotoImage(Train_button_img)
        
        b5 = Button(bg_img,command=self.train_data,image = self.photoimg5,cursor="hand2")
        b5.place(x = 100 , y = 520 , width = 220, height=220)
        
        b5_1 = Button(bg_img,command=self.train_data,text = "TRAIN DATA",cursor="hand2",font=("times new roman",15,"bold"),bg = "white" , fg = "black")
        b5_1.place(x = 100 , y = 740 , width = 220, height=30)
        
        
        #Photos
        Photos_button_img = Image.open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\photos/photos.png")
        Photos_button_img.resize((220,220))
        self.photoimg6 = ImageTk.PhotoImage(Photos_button_img)
        
        b6 = Button(bg_img,command = self.open_img,image = self.photoimg6,cursor="hand2")
        b6.place(x = 450 , y = 520 , width = 220, height=220)
        
        b6_1 = Button(bg_img,command = self.open_img,text = "PHOTOS",cursor="hand2",font=("times new roman",15,"bold"),bg = "white" , fg = "black")
        b6_1.place(x = 450 , y = 740 , width = 220, height=30)
        
        #Developer
        Developer_button_img = Image.open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\photos/developer.png")
        Developer_button_img.resize((220,220))
        self.photoimg7 = ImageTk.PhotoImage(Developer_button_img)
        
        b7 = Button(bg_img,command=self.developer,image = self.photoimg7,cursor="hand2")
        b7.place(x = 820 , y = 520 , width = 220, height=220)
        
        b7_1 = Button(bg_img,command=self.developer,text = "DEVELOPER",cursor="hand2",font=("times new roman",15,"bold"),bg = "white" , fg = "black")
        b7_1.place(x = 820 , y = 740 , width = 220, height=30)
        
        
        #Exit
        Exit_button_img = Image.open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\photos/exit.png")
        Exit_button_img.resize((220,220))
        self.photoimg8 = ImageTk.PhotoImage(Exit_button_img)
        
        b8 = Button(bg_img,command=self.exit,image = self.photoimg8,cursor="hand2")
        b8.place(x = 1170 , y = 520 , width = 220, height=220)
        
        b8_1 = Button(bg_img,command=self.exit,text = "EXIT",cursor="hand2",font=("times new roman",15,"bold"),bg = "white" , fg = "black")
        b8_1.place(x = 1170 , y = 740 , width = 220, height=30)
        
        
    
    def open_img(self):
        os.startfile(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\face_data")
      
        # ***********functions button********
    def student_details(self):
        self.new_window = Toplevel(self.win)
        self.app = Student(self.new_window)
    
    def train_data(self):
        self.new_window = Toplevel(self.win)
        self.app = Train(self.new_window)
    
    def facerecognition(self):
        self.new_window = Toplevel(self.win)
        self.app = facerecognition(self.new_window)
    
    def attendance(self):
        self.new_window = Toplevel(self.win)
        self.app = Attendance(self.new_window)
        
    def developer(self):
        self.new_window = Toplevel(self.win)
        self.app = Developer(self.new_window)
    
    def help(self):
        self.new_window = Toplevel(self.win)
        self.app = Help(self.new_window) 
        
    def exit(self):
        self.iExit = messagebox.askyesno("Face Recongnition","Are you sure to exit",parent=self.win)
        if self.iExit >0:
            self.win.destroy()
        else:
            return
        
if __name__ == "__main__":
    win = Tk()
    obj = Face_Attendance_System(win)
    win.mainloop()
