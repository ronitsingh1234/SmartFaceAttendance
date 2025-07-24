from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime

class FaceRecognition:
    def __init__(self, win):
        self.win = win
        self.win.geometry("1900x850+0+0")
        self.win.title("FACE ATTENDANCE SYSTEM")

        # Background Image
        img = Image.open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\photos\face1.webp")
        img = img.resize((1530, 850))
        self.photoimg1 = ImageTk.PhotoImage(img)

        bg_img = Label(self.win, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1530, height=850)

        # Button
        facerecognition_btn = Button(
            bg_img,
            command=self.face_recog,
            text="FACE RECOGNIZE",
            font=("times new roman", 15, "bold"),
            bg="red",
            fg="black",
            cursor="hand2"
        )
        facerecognition_btn.place(x=510, y=750, width=500, height=40)

    # =================== Attendance ======================
    def mark_attendance(self, i, r, n, d):
        with open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\ronit.csv", "r+", newline="\n") as f:
            mydatalist = f.readlines()
            name_list = []
            for line in mydatalist:
                entry = line.split(",")
                name_list.append(entry[0])
            if i not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtstring = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")

    # =================== Face Recognition ======================
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100)
            )
            coord = []
            for (x, y, w, h) in features:
                id, confidence = clf.predict(gray_image[y:y+h, x:x+w])
                print(f"Detected ID: {id}, Confidence: {confidence}")

                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Mmmmmmmm12@",
                    database="face_recognizer"
                )
                cur = conn.cursor()

                cur.execute("SELECT name FROM student WHERE Student_id=%s", (id,))
                n = cur.fetchone()
                n = "+".join(n) if n else "Unknown"

                cur.execute("SELECT roll FROM student WHERE Student_id=%s", (id,))
                r = cur.fetchone()
                r = "+".join(r) if r else "Unknown"

                cur.execute("SELECT dep FROM student WHERE Student_id=%s", (id,))
                d = cur.fetchone()
                d = "+".join(d) if d else "Unknown"

                cur.execute("SELECT Student_id FROM student WHERE Student_id=%s", (id,))
                i = cur.fetchone()
                i = "+".join(i) if i else "Unknown"

                if confidence > 50:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Roll: {r}", (x, y - 50), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Dept: {d}", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, clf)
            return img

        faceCascade = cv2.CascadeClassifier(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\haarcascade_frontalface_default.xml")

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            if not ret:
                break
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Enter key
                break

        video_cap.release()
        cv2.destroyAllWindows()

# ================= Run App =====================
if __name__ == "__main__":
    win = Tk()
    obj = FaceRecognition(win)
    win.mainloop()
