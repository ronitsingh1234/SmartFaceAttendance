from tkinter import*
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import cv2
import mysql.connector
import os 
import csv
from tkinter import filedialog


mydata = []
class Attendance:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1900x850+0+0")
        self.win.title("FACE ATTENDANCE SYSTEM")
        
        
        # variables
        self.var_atten_id = StringVar()
        self.var_roll= StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_name = StringVar()
        self.var_status = StringVar()
        self.var_department = StringVar()
        
        
        
        img = Image.open(r"C:\Users\Ronit Singh\Desktop\Python\FACE RECOGNITION\photos/at.jpg")
        img = img.resize((1900,520))
        self.photoimg = ImageTk.PhotoImage(img)
        
        bg_img = Label(self.win,image = self.photoimg)
        bg_img.place(x=0 , y=10,width=1900,height=320)
        
        
        title_label = Label(self.win, text = "STUDENT  ATTENDANCE", font=("times new roman",35,"bold"),bg = "white" , fg = "black")
        title_label.place(x = 0, y = 0,width=1600,height=60)
        
           
        main_frame = Frame(self.win,bd=2,bg="white")
        main_frame.place(x=0,y=330,width=1600,height=700)
        
        Left_frame = LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Student Attendace details",font=("times new roman",14,"bold"))
        Left_frame.place(x=10,y=10,width=750,height=480)
        
        frame_2 = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        frame_2.place(x=10,y=10,width=720,height=430)
        
        attendanceId_label = Label(frame_2,text = "AttendanceId:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        
        attendanceid_entry = ttk.Entry(frame_2,textvariable=self.var_atten_id,font=("times new roman",12),width=20)
        attendanceid_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        studentrollno_label = Label(frame_2,text = "Roll No:",font=("times new roman",12,"bold"),bg="white")
        studentrollno_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)
        
        studentrollno_entry = ttk.Entry(frame_2,textvariable=self.var_roll,font=("times new roman",12),width=20)
        studentrollno_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)
        
        
        name = Label(frame_2,text = "Name:",font=("times new roman",12,"bold"),bg="white")
        name.grid(row=1,column=0,padx=10,pady=15,sticky=W)
        
        name_entry = ttk.Entry(frame_2,textvariable=self.var_name,font=("times new roman",12),width=20)
        name_entry.grid(row=1,column=1,padx=10,pady=15,sticky=W)
        
        
        department = Label(frame_2,text = "Department:",font=("times new roman",12,"bold"),bg="white")
        department.grid(row=1,column=2,padx=10,pady=15,sticky=W)
        
        department_entry = ttk.Entry(frame_2,textvariable=self.var_department,font=("times new roman",12),width=20)
        department_entry.grid(row=1,column=3,padx=10,pady=15,sticky=W)
        
        
        time = Label(frame_2,text = "Time:",font=("times new roman",12,"bold"),bg="white")
        time.grid(row=2,column=0,padx=10,pady=15,sticky=W)
        
        time_entry = ttk.Entry(frame_2,textvariable=self.var_time,font=("times new roman",12),width=20)
        time_entry.grid(row=2,column=1,padx=10,pady=15,sticky=W)
        
        date = Label(frame_2,text = "Date:",font=("times new roman",12,"bold"),bg="white")
        date.grid(row=2,column=2,padx=10,pady=15,sticky=W)
        
        date_entry = ttk.Entry(frame_2,textvariable=self.var_date,font=("times new roman",12),width=20)
        date_entry.grid(row=2,column=3,padx=10,pady=15,sticky=W)
        
        mark = Label(frame_2,text = "Attendance Status:",font=("times new roman",12,"bold"),bg="white")
        mark.grid(row=3,column=0,padx=10,pady=15,sticky=W)
        
        mark_entry = ttk.Combobox(frame_2,textvariable=self.var_status,font=("times new roman",12),width=20,state="readonly")
        mark_entry['values'] = ("Status" , "Present" , "Absent")
        mark_entry.current(0)
        mark_entry.grid(row=3,column=1,padx=10,pady=15,sticky=W)
        
        btnframe = LabelFrame(frame_2,bd=2,bg="white",relief=RIDGE)
        btnframe.place(x=20,y=300,width=660,height=35)
        
        importcsv_btn = Button(btnframe,command=self.importCsv,text="Import CSV" ,font=("times new roman",13,"bold"),bg="blue",fg="white",width=15,cursor="hand2")
        importcsv_btn.grid(row=0,column=0)
        
    
        exportcsv_btn = Button(btnframe,command=self.exportCsv,text="Export CSV" , font=("times new roman",13,"bold"),bg="blue",fg="white",width=16,cursor="hand2")
        exportcsv_btn.grid(row=0,column=2)
        
        
        Update_btn = Button(btnframe,text="Update" ,font=("times new roman",13,"bold"),bg="blue",fg="white",width=15,cursor="hand2")
        Update_btn.grid(row=0,column=4)
        
        reset_btn = Button(btnframe,text="Reset" ,command=self.reset, font=("times new roman",13,"bold"),bg="blue",fg="white",width=16,cursor="hand2")
        reset_btn.grid(row=0,column=6)
        
        
        Right_frame = LabelFrame(main_frame,bd=3,bg="white",relief=SUNKEN,text="Student details",font=("times new roman",14,"bold"))
        Right_frame.place(x=770,y=10,width=740,height=480)
        
        table_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=10,width=720,height=430)
        
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable = ttk.Treeview(table_frame,column=('id','roll','name','department','time','date','attendance'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
         
        self.AttendanceReportTable.heading("id", text="Attendance ID") 
        self.AttendanceReportTable.heading("roll", text="Roll No") 
        self.AttendanceReportTable.heading("name", text="Name") 
        self.AttendanceReportTable.heading("department", text="Department") 
        self.AttendanceReportTable.heading("time", text="Time") 
        self.AttendanceReportTable.heading("date", text="Date") 
        self.AttendanceReportTable.heading("attendance", text="Attendance") 
      
      
        self.AttendanceReportTable.column("id", width=100) 
        self.AttendanceReportTable.column("roll", width=100) 
        self.AttendanceReportTable.column("name", width=100) 
        self.AttendanceReportTable.column("department", width=100) 
        self.AttendanceReportTable.column("time", width=100) 
        self.AttendanceReportTable.column("date", width=100) 
        self.AttendanceReportTable.column("attendance", width=100) 
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    def importCsv(self):
        global mydata
        mydata.clear()
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.win)
        with open(filename) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data found to export",parent = self.win)
                return False
            filename = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.win)
            with open(filename,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Sucess","Your Data exported to "+os.path.basename(filename)+" successfully")
        except Exception as e:
            messagebox.showerror("Error",f"Due To:{str(e)}",parent=self.win)
    
    def get_cursor(self,event=""):
        cursor_focus = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_focus)
        data = content["values"]
        
        self.var_atten_id.set(data[0])
        self.var_roll.set(data[1])
        self.var_name.set(data[2])
        self.var_department.set(data[3])
        self.var_time.set(data[4])
        self.var_date.set(data[5])
        self.var_status.set(data[6])
        
    def reset(self):
        self.var_atten_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_department.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_status.set("Status")
        
        
if __name__ == "__main__":
    win = Tk()
    obj=Attendance(win)
    win.mainloop()
