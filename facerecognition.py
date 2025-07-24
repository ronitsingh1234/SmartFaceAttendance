from tkinter import*
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime




class facerecognition:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1900x850+0+0")
        self.win.title("FACE ATTENDANCE SYSTEM")
    
    
    
        img = Image.open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\photos/face1.webp")
        img = img.resize((1530,850))
        self.photoimg1= ImageTk.PhotoImage(img)
        
        bg_img = Label(self.win,image = self.photoimg1)
        bg_img.place(x=0 , y=0,width=1530,height=850)
        
        
        facerecognition = Button(bg_img,command=self.face_recog,text="FACE RECOGNIZE",font=("times new roman",15,"bold"),bg="red",fg="black",cursor="hand2",width=33)
        facerecognition.place(x = 510,y=750,width=500,height=40)
    
    
    # Attendance 
    def mark_attendance(self,i,r,n,d):
        with open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\ronit.csv","r+",newline="\n") as f:
            mydatalist = f.readlines()
            name_list=[]
            for line in mydatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")
            
            
            
    #  face recongnition
    def face_recog(self): 
        def draw_boundray(img,classifier, scaleFactor, minNeighbors, color, text, clf): 
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
            features=classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord=[] 
            for (x,y,w,h) in features: 
                cv2.rectangle(img,(x,y), (x+w,y+h), (0,255,0),3) 
                id, predict=clf.predict(gray_image[y:y+h,x:x+w]) 
                confidence=int((100*(1-predict/300)))
            
                conn=mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Mmmmmmmm12@",
                        database = 'face_recognizer'
                    )
                cur = conn.cursor()
                
                cur.execute("select name from student where Student_id=" + str(id))
                n=cur.fetchone()
                n="+".join(n) if n else "unknown"
                
                cur.execute("select roll from student where Student_id=" + str(id))
                r=cur.fetchone()
                r="+".join(r) if r else "unknown"
                
                
                cur.execute("select dep from student where Student_id=" + str(id))
                d=cur.fetchone()
                d="+".join(d)  if d else "unknown"
                
                cur.execute("select Student_id from student where Student_id=" + str(id))
                i=cur.fetchone()
                i="+".join(i)  if i else "unknown"
                
                if confidence>77:
                    cv2.putText(img, f"ID:{i}", (x,y-79), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3) 
                    cv2.putText(img, f"Roll:{r}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255),3) 
                    cv2.putText(img, f"Name: {n}", (x,y-30), cv2. FONT_HERSHEY_COMPLEX, 0.8, (255,255, 255), 3) 
                    cv2.putText(img, f"Department: {d}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255, 255), 3) 
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y), (x+w,y+h), (0,0,255),3) 
                    cv2.putText(img, "Unknown Face", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255, 255), 3) 
                    
                coord=[x,y,w,h]
            return coord
    
        def recognize (img,clf, faceCascade): 
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25,255), "Face", clf) 
            return img 
        faceCascade=cv2.CascadeClassifier(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\haarcascade_frontalface_default.xml") 
        clf=cv2.face.LBPHFaceRecognizer_create() 
        clf.read(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\classifier.xml") 
        
        video_cap=cv2.VideoCapture(0) 
        while True: 
            ret,img=video_cap.read() 
            img=recognize(img,clf, faceCascade) 
            cv2.imshow("Welcome To face Recognition", img) 
            
            if cv2.waitKey(1)==13: 
                break 
        video_cap.release()
        cv2.destroyAllWindows()
            
if __name__ == "__main__":
    win = Tk()
    obj = facerecognition(win)
    win.mainloop()