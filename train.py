from tkinter import*
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np



class Train:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1900x850+0+0")
        self.win.title("FACE ATTENDANCE SYSTEM")
    
    
        title_label = Label(self.win, text = "TRAIN DATA SET", font=("times new roman",35,"bold"),bg="midnight blue", fg = "skyblue")
        title_label.place(x = 0, y = 0,width=1550,height=50)
        
        img111 = Image.open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\photos/traindata1.png")
        img111 = img111.resize((1600,800))
        self.photoimg1= ImageTk.PhotoImage(img111)
        
        bg_img1 = Label(self.win,image = self.photoimg1)
        bg_img1.place(x=0 , y=50,width=1600,height=785)
       
        textlabel = Label(bg_img1,text="TAKE PHOTO SAMPLE",font=("times new roman",15,"bold"),bg="midnight blue",fg="white",width=33)
        textlabel.place(x = 260,y=493,width=230,height=40)
        
        
        textlabel = Label(bg_img1,text="DATA SET",font=("times new roman",15,"bold"),bg="midnight blue",fg="white",width=33)
        textlabel.place(x = 265,y=110,width=240,height=40)
    
    
        trainbtn1 = Button(bg_img1, command=self.train_classifier,text = "TRAIN THE FACES", font=("times new roman",35,"bold"),bg="skyblue", cursor="hand2",fg = "black")
        trainbtn1.place(x = 900, y = 290,width=550,height=100)
        
        
    def train_classifier(self):
        data_dir = (r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\face_data")
        path=[os.path.join(data_dir, file) for file in os.listdir(data_dir)]
             
        faces=[]   
        ids=[]     
        
        for image in path:
            img=Image.open(image).convert('L')    #gray scale image convert
            imagenp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imagenp)
            ids.append(id)
            cv2.imshow("Training",imagenp)
            cv2.waitKey(1) == 13
        
        ids=np.array(ids)
        
        # train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!")
        
        
if __name__ == "__main__":
    win = Tk()
    obj = Train(win)
    win.mainloop()
