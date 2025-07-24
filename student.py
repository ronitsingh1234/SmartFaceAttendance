from tkinter import*
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import cv2
import mysql.connector



class Student:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1900x850+0+0")
        self.win.title("FACE ATTENDANCE SYSTEM")
        
        
        self.var_dep=StringVar() 
        self.var_course=StringVar() 
        self.var_year=StringVar() 
        self.var_semester=StringVar() 
        self.var_std_id=StringVar() 
        self.var_std_name=StringVar() 
        self.var_div=StringVar() 
        self.var_roll=StringVar() 
        self.var_gender=StringVar() 
        self.var_dob=StringVar() 
        self.var_email=StringVar() 
        self.var_phone=StringVar() 
        self.var_address=StringVar() 
        self.var_father=StringVar()
        

        
        title_label = Label(self.win, text = "STUDENT  DETAILS", font=("times new roman",35,"bold"),bg = "white" , fg = "black")
        title_label.place(x = 0, y = 0,width=1550,height=100)
        
        main_frame = Frame(self.win,bd=2,bg="white")
        main_frame.place(x=0,y=100,width=1550,height=700)
        
        # left label frame 
        Left_frame = LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Student details",font=("times new roman",14,"bold"))
        Left_frame.place(x=30,y=10,width=700,height=680)
        
        img1 = Image.open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\photos/ani2.jpg")
        img1 = img1.resize((680,250))
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        student_img = Label(Left_frame,image = self.photoimg1)
        student_img.place(x=0 , y=3,width=680,height=250)
        
        #course frame
        frame_1 = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Course details",font=("times new roman",12,"bold"))
        frame_1.place(x=5,y=200,width=680,height=110)
        
        dep_label = Label(frame_1,text = "Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        dep_combobox = ttk.Combobox(frame_1,textvariable=self.var_dep,font=("times new roman",12),width=20,state="readonly")
        dep_combobox['values'] = ("Select Department" , "USCS" , "UIT" , "UIM","SALS","UCHS")
        dep_combobox.current(0)
        dep_combobox.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        
        
        course_label = Label(frame_1,text = "Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=20,pady=10,sticky=W)
        
        course_combobox = ttk.Combobox(frame_1, textvariable=self.var_course, font=("times new roman",12),width=20,state="readonly")
        course_combobox['values'] = ("Select Course" , "BCA" , "BTECH" , "BBA","MCA","MBA")
        course_combobox.current(0)
        course_combobox.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        
         
        year_label = Label(frame_1,text = "Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        
        year_combobox = ttk.Combobox(frame_1, textvariable=self.var_year,font=("times new roman",12),width=20,state="readonly")
        year_combobox['values'] = ("Select Year" , "1" , "2" , "3","4")
        year_combobox.current(0)
        year_combobox.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        
        
        semester_label = Label(frame_1,text = "Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)
        
        semester_combobox = ttk.Combobox(frame_1, textvariable=self.var_semester, font=("times new roman",12),width=20,state="readonly")
        semester_combobox['values'] = ("Select Semester" , "Even","Odd")
        semester_combobox.current(0)
        semester_combobox.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
        
        #student information frame
        frame_2 = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        frame_2.place(x=5,y=310,width=680,height=340)
        
        #student id
        studentID_label = Label(frame_2,text = "StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        studentID_entry = ttk.Entry(frame_2,textvariable=self.var_std_id,font=("times new roman",12),width=20)
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #student name
        studentname_label = Label(frame_2,text = "Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        studentname_entry = ttk.Entry(frame_2,textvariable=self.var_std_name,font=("times new roman",12),width=20)
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #student divison 
        studentdivison_label = Label(frame_2,text = "Class Divison:",font=("times new roman",12,"bold"),bg="white")
        studentdivison_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        studentdivison_entry = ttk.Entry(frame_2,textvariable=self.var_div,font=("times new roman",12),width=20)
        studentdivison_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
         #Roll no 
        studentrollno_label = Label(frame_2,text = "Roll No:",font=("times new roman",12,"bold"),bg="white")
        studentrollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        studentrollno_entry = ttk.Entry(frame_2, textvariable=self.var_roll,font=("times new roman",12),width=20)
        studentrollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        
         # Gender 
        gender_label = Label(frame_2,text = "Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        gender_combobox = ttk.Combobox(frame_2, textvariable=self.var_gender,font=("times new roman",12),width=20,state="readonly")
        gender_combobox['values'] = ("Select Gender" , "Male" , "Female")
        gender_combobox.current(0)
        gender_combobox.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        
         #DOB  
        dob_label = Label(frame_2,text = "DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dob_entry = ttk.Entry(frame_2, textvariable=self.var_dob,font=("times new roman",12),width=20)
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        
        #Email  
        Email_label = Label(frame_2,text = "Email:",font=("times new roman",12,"bold"),bg="white")
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        
        Email_entry = ttk.Entry(frame_2, textvariable=self.var_email,font=("times new roman",12),width=20)
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        
        
        #phone no  
        phoneno = Label(frame_2,text = "Phone No:",font=("times new roman",12,"bold"),bg="white")
        phoneno.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        phoneno_entry = ttk.Entry(frame_2, textvariable=self.var_phone,font=("times new roman",12),width=20)
        phoneno_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        
        
        #Address  
        Address = Label(frame_2,text = "Address:",font=("times new roman",12,"bold"),bg="white")
        Address.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        
        Address_entry = ttk.Entry(frame_2,textvariable=self.var_address,font=("times new roman",12),width=20)
        Address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        #Father name  
        Father = Label(frame_2,text = "Father Name:",font=("times new roman",12,"bold"),bg="white")
        Father.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        
        Father_entry = ttk.Entry(frame_2, textvariable=self.var_father,font=("times new roman",12),width=20)
        Father_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
    
        # radio buttons 
        self.var_radio1=StringVar()
        radiobtn2 = ttk.Radiobutton(frame_2, variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn2.grid(row=5, column=0,padx=10,pady=5)

        radiobtn2 = ttk.Radiobutton(frame_2, variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5, column=1,padx=10,pady=5)
        
        
        #Button frame
        btnframe = LabelFrame(frame_2,bd=2,bg="white",relief=RIDGE)
        btnframe.place(x=5,y=210,width=660,height=35)
        
        save_btn = Button(btnframe,text="Save" ,command=self.add_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=15,cursor="hand2")
        save_btn.grid(row=0,column=0)
        
        
        update_btn = Button(btnframe,text="Update" ,command=self.update_data, font=("times new roman",13,"bold"),bg="blue",fg="white",width=16,cursor="hand2")
        update_btn.grid(row=0,column=1)
        
        
        delete_btn = Button(btnframe,text="Delete" , command = self.delete_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=15,cursor="hand2")
        delete_btn.grid(row=0,column=2)
        
        reset_btn = Button(btnframe,command=self.reset_data,text="Reset" , font=("times new roman",13,"bold"),bg="blue",fg="white",width=16,cursor="hand2")
        reset_btn.grid(row=0,column=3)
        
       
        btnframe1 = LabelFrame(frame_2,bd=2,bg="white",relief=RIDGE)
        btnframe1.place(x=5,y=246,width=660,height=35)
        
        takephotobtn = Button(btnframe1,text="Take Photo Sample" , command=self.generate_dataset,font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2",width=33)
        takephotobtn.grid(row=1,column=0)
        
        updatephotobtn = Button(btnframe1,text="Update Photo Sample" , font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2",width=33)
        updatephotobtn.grid(row=1,column=1)
        
        
        
        
        # Right label frame 
        Right_frame = LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Student details",font=("times new roman",14,"bold"))
        Right_frame.place(x=780,y=10,width=700,height=680)
        
        img2 = Image.open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\photos/class.png")
        img2 = img2.resize((700,200))
        self.photoimg3 = ImageTk.PhotoImage(img2)
        
        student_img = Label(Right_frame,image = self.photoimg3)
        student_img.place(x=0 , y=3,width=700,height=200)
        
        
        #search frame
        search_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=210,width=680,height=70)
        
        search_label= Label(search_frame,text = "Search By:",font=("times new roman",12,"bold"),bg="red", fg = "white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combobox = ttk.Combobox(search_frame,font=("times new roman",12),width=16,state="readonly")
        search_combobox['values'] = ("Select" ,"Name", "Roll No","Phone_No")
        search_combobox.current(0)
        search_combobox.grid(row= 0, column=1,padx=2,pady=10,sticky=W)
        
        search_entry = ttk.Entry(search_frame,font=("times new roman",12),width=20)
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn = Button(search_frame,text="Search" , font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2",width=10)
        search_btn.grid(row=0,column=3,padx=4)
        
        ShowAll = Button(search_frame,text="Show All" , font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2",width=10)
        ShowAll.grid(row=0,column=4)
        
        
        #table frame
        table_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        table_frame.place(x=5,y=290,width=680,height=350)
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,column=('dep','course','year','sem','id','name','div','roll','gender','dob','email','phone','address','father','photo'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        self.student_table.heading("roll", text="Roll No") 
        self.student_table.heading("name", text="Name") 
        self.student_table.heading("dep", text="Department") 
        self.student_table.heading("course", text="Course") 
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester") 
        self.student_table.heading("id", text="StudentId") 
        self.student_table.heading("div", text="Division") 
        self.student_table.heading("dob", text="DOB") 
        self.student_table.heading("email", text="Email") 
        self.student_table.heading("gender", text="Gender") 
        self.student_table.heading("phone", text="Phone") 
        self.student_table.heading("address", text="Address") 
        self.student_table.heading("father", text="Father Name") 
        self.student_table.heading("photo", text="PhotoSampleStatus") 
        self.student_table["show"]="headings" 
       
        self.student_table.column("dep", width=100) 
        self.student_table.column("course", width=100) 
        self.student_table.column("year", width=100) 
        self.student_table.column("sem", width=100) 
        self.student_table.column("id", width=100) 
        self.student_table.column("name", width=100) 
        self.student_table.column("roll", width=100) 
        self.student_table.column("gender", width=100) 
        self.student_table.column("div", width=100) 
        self.student_table.column("dob", width=100) 
        self.student_table.column("email", width=100) 
        self.student_table.column("phone", width=100) 
        self.student_table.column("address", width=100) 
        self.student_table.column("father", width=100) 
        self.student_table.column("photo", width=150)
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    # functions declaration
    
    def add_data(self):
        if self.var_dep.get() =="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required",parent = self.win)
        else:
            try:
                conn=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Mmmmmmmm12@",
                    database = 'face_recognizer'
                )
                cur = conn.cursor()
                cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                    self.var_dep.get(), 
                    self.var_course.get(), 
                    self.var_year.get(), 
                    self.var_semester.get(), 
                    self.var_std_id.get(), 
                    self.var_std_name.get(), 
                    self.var_div.get(), 
                    self.var_roll.get(), 
                    self.var_gender.get(), 
                    self.var_dob.get(), 
                    self.var_email.get(), 
                    self.var_phone.get(), 
                    self.var_address.get(), 
                    self.var_father.get(),
                    self.var_radio1.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student details has been added Successfully",parent=self.win)
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.win)
                
    #fetching data
    def fetch_data(self):
        conn=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Mmmmmmmm12@",
                    database = 'face_recognizer'
                )
        cur = conn.cursor()
        cur.execute("select * from student")
        data=cur.fetchall()
        
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
                
                
    # cursor function
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        
        self.var_dep.set(data[0])
        self.var_course.set(data[1]) 
        self.var_year.set(data[2]) 
        self.var_semester.set(data[3]) 
        self.var_std_id.set(data[4]) 
        self.var_std_name.set(data[5]) 
        self.var_div.set(data[6]) 
        self.var_roll.set(data[7]) 
        self.var_gender.set(data[8]) 
        self.var_dob.set(data[9]) 
        self.var_email.set(data[10]) 
        self.var_phone.set(data[11]) 
        self.var_address.set(data[12]) 
        self.var_father.set(data[13])
        self.var_radio1.set(data[14])
        
    # update function
    def update_data(self):
        if self.var_dep.get() =="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required",parent = self.win)
        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update",parent = self.win)
                if Update>0:
                    conn=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Mmmmmmmm12@",
                    database = 'face_recognizer'
                    )
                    cur = conn.cursor()
                    cur.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Student_id=%s,Name=%s,Divison=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Father=%s,PhotoSample=%s where Student_id=%s",(
                        self.var_dep.get(), 
                        self.var_course.get(), 
                        self.var_year.get(), 
                        self.var_semester.get(), 
                        self.var_std_id.get(),
                        self.var_std_name.get(), 
                        self.var_div.get(), 
                        self.var_roll.get(), 
                        self.var_gender.get(), 
                        self.var_dob.get(), 
                        self.var_email.get(), 
                        self.var_phone.get(), 
                        self.var_address.get(), 
                        self.var_father.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                    
                else:
                   if  not Update:
                       return
                messagebox.showinfo("Success", "Student Details Successfully Updated",parent=self.win)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.win)
                    
            
    # delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.win)
        else:
            try:
                delete = messagebox.askyesno("Confirmation","Do you want to delete this data",parent=self.win)
                if delete>0:
                    conn=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="Mmmmmmmm12@",
                                database = 'face_recognizer'
                            )
                    cur = conn.cursor()
                    cur.execute("delete from student where Student_id=%s", (self.var_std_id.get(),))
                else:
                    if not delete:
                     return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Data deleted Successfully")
            except Exception as es:
                messagebox.showerror("Error","Due to:"f"{str(es)}",parent = self.win)
        
            
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester") 
        self.var_std_id.set("")
        self.var_std_name.set("") 
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("Select Gender") 
        self.var_dob.set("")
        self.var_email.set("") 
        self.var_phone.set("")
        self.var_address.set("")
        self.var_father.set("")
        self.var_radio1.set("")
    
    # Generate data set or take photo samples
    def generate_dataset(self):
        if self.var_dep.get() =="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required",parent = self.win)
        else:
            try:
                conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Mmmmmmmm12@",
                database = 'face_recognizer'
                )
                cur = conn.cursor()
                 
                id=self.var_std_id.get()
                cur.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Student_id=%s,Name=%s,Divison=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Father=%s,PhotoSample=%s where Student_id=%s",(
                        self.var_dep.get(), 
                        self.var_course.get(), 
                        self.var_year.get(), 
                        self.var_semester.get(), 
                        self.var_std_id.get(),
                        self.var_std_name.get(), 
                        self.var_div.get(), 
                        self.var_roll.get(), 
                        self.var_gender.get(), 
                        self.var_dob.get(), 
                        self.var_email.get(), 
                        self.var_phone.get(), 
                        self.var_address.get(), 
                        self.var_father.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()==id
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #load predefinded data on face frontals from opencv=======
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
               
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor = 1.3
                    # minimum neighbour = 5
                    
                    for(x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="face_data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,55),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id) == 50:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed successfully")
          
            except Exception as es:
                messagebox.showerror("Error","Due to:"f"{str(es)}",parent = self.win)
        
        
if __name__ == "__main__":
    win = Tk()
    obj = Student(win)
    win.mainloop()
