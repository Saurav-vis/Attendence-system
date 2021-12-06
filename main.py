from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1330x700+0+0")
        self.root.title("Face Recognition System")

        img = Image.open((r"clg_img\university1.jpg"))
        img = img.resize((100,100),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)


        #bg_image
        img1 = Image.open((r"clg_img\university.jpg"))
        img1 = img1.resize((1330,700),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=0,width=1330,height=700)

        #first label
        f_lbl = Label(bg_img,image=self.photoimg)
        f_lbl.place(x=1400,y=0,width=100,height=100)

        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("time new roman",20,"bold"),fg="black")
        title_lbl.place(x=150,y=0,width=1200,height =45)

        #student button
        img2 = Image.open(r"clg_img\student.jpg")
        img2 = img2.resize((200,200),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage((img2))

        b1 = Button(bg_img,image=self.photoimg2,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=150,width=200,height=200)

        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2")
        b1_1.place(x=200,y=300,width=200,height=50)

        #Face Dector button
        img3 = Image.open(r"clg_img\face_detector1.jpg")
        img3 = img3.resize((200,200),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage((img3))

        b2 = Button(bg_img,image=self.photoimg3,command=self.face_data,cursor="hand2")
        b2.place(x=500,y=150,width=200,height=200)

        b1_2 = Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2")
        b1_2.place(x=500,y=300,width=200,height=50)

        #Attendace face button
        img4 = Image.open(r"clg_img\images.jpg")
        img4 = img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage((img4))

        b3 = Button(bg_img,image=self.photoimg4,command=self.attendance_data,cursor="hand2")
        b3.place(x=800,y=150,width=200,height=200)

        b1_3 = Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2")
        b1_3.place(x=800,y=300,width=200,height=50)

        #Help button
        img5 = Image.open(r"clg_img\help.jpg")
        img5 = img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage((img5))

        b4 = Button(bg_img,image=self.photoimg5,cursor="hand2")
        b4.place(x=1100,y=150,width=200,height=200)

        b1_4 = Button(bg_img,text="Help",cursor="hand2")
        b1_4.place(x=1100,y=300,width=200,height=50)

        #Train Data button
        img6 = Image.open(r"clg_img\facialrecognition.png")
        img6 = img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage((img6))

        b5 = Button(bg_img,image=self.photoimg6,command=self.train_data,cursor="hand2")
        b5.place(x=200,y=500,width=200,height=200)

        b1_5 = Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2")
        b1_5.place(x=200,y=650,width=200,height=50)

        #Photos button
        img7 = Image.open(r"clg_img\clg.jpg")
        img7 = img7.resize((200,200),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage((img7))

        b6 = Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=500,width=200,height=200)

        b1_6 = Button(bg_img,text="Photos",cursor="hand2",command=self.open_img)
        b1_6.place(x=500,y=650,width=200,height=50)

        # Developer button
        img8 = Image.open(r"clg_img\di.jpg")
        img8 = img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage((img8))

        b7 = Button(bg_img,image=self.photoimg8,cursor="hand2")
        b7.place(x=800,y=500,width=200,height=200)

        b1_7 = Button(bg_img,text="Developer",cursor="hand2")
        b1_7.place(x=800,y=650,width=200,height=50)

        #Exit button
        img9 = Image.open(r"clg_img\exit.jpg")
        img9 = img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage((img9))

        b8 = Button(bg_img,image=self.photoimg9,cursor="hand2")
        b8.place(x=1100,y=500,width=200,height=200)

        b1_8 = Button(bg_img,text="Exit",cursor="hand2")
        b1_8.place(x=1100,y=650,width=200,height=50)
        
    def open_img(self):
        os.startfile("data")


    #===================Functions Button======
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        







if __name__== "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()