from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1330x700+0+0")
        self.root.title("Attendance Management System")
        
        #Variables
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()
        
        img_top = Image.open(r"clg_img\smart-attendance.jpg")
        img_top = img_top.resize((650,200),Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage((img_top))
        
        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=650,height=200)
        
        img_top1 = Image.open(r"clg_img\clg.jpg")
        img_top1 = img_top1.resize((650,200),Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage((img_top1))
        
        f_lbl = Label(self.root,image=self.photoimg_top1)
        f_lbl.place(x=675,y=50,width=650,height=200)
        
        title_lbl = Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font=("time new roman",40,"bold"),bg="blue",fg="white")
        title_lbl.place(x=0,y=200,width=1330,height =50)
        
        main_frame = Frame(self.root,bd=2,bg="white")
        main_frame.place(x=10,y=270,width=1300,height=400)
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=620,height=380)
        
        left_inside_frame = Frame(main_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=20,y=40,width=600,height=240)
        
        #attendance ID
        attendanceID_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",12,"bold"),bg="white")
        attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendanceID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_id,width=17,font=("times new roman",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #Roll
        R_label=Label(left_inside_frame,text="Roll no:",font=("times new roman",12,"bold"),bg="white")
        R_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        R_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_roll,width=17,font=("times new roman",12,"bold"))
        R_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #Name
        Name_label=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        Name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        Name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_name,width=17,font=("times new roman",12,"bold"))
        Name_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #Department
        Dep_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",12,"bold"),bg="white")
        Dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        Dep_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_dep,width=17,font=("times new roman",12,"bold"))
        Dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #Time
        Time_label=Label(left_inside_frame,text="DateD:",font=("times new roman",12,"bold"),bg="white")
        Time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        Time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_time,width=17,font=("times new roman",12,"bold"))
        Time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #Date
        Date_label=Label(left_inside_frame,text="DateD:",font=("times new roman",12,"bold"),bg="white")
        Date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        Date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_date,width=17,font=("times new roman",12,"bold"))
        Date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        #Attendance
        y_label=Label(left_inside_frame,text="Attendance",font=("times new roman",12,"bold"),bg="white")
        y_label.grid(row=3,column=0,padx=10,sticky=W)
        
        y_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_attend_attendance,font=("times new roman",12,"bold"),width=15,state="readonly")
        y_combo["values"]=("Status","Present","Absent")
        y_combo.current(0)
        y_combo.grid(row=3,column=1,padx=10,pady=10,sticky=W)
        
        #Button Frame
        
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=180,width=582,height=50)
        
        #Save Buttons
        
        save_btn=Button(btn_frame,text="Import.csv",command=self.importCsv,font=("times new roman",12,"bold"),bg="blue",fg="white",width=15)
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Export.csv",command=self.exportCsv,font=("times new roman",12,"bold"),bg="blue",fg="white",width=15)
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Update",font=("times new roman",12,"bold"),bg="blue",fg="white",width=15)
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white",width=15)
        reset_btn.grid(row=0,column=3)
        
        
        #Right Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text=" Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=660,y=0,width=610,height=380)
        
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=10,width=582,height=340)
        
        #==================scroll bar table===================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    #Fetch Data
    
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
            
    
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])
        
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")
        
                
            
        
        
        
        
        
        
if __name__=="__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
