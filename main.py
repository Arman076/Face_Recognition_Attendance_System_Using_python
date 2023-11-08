
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
import os
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpsupport import Help

class Face_recogonition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("Face recogonition system")
        #----------------FIRST  IMAGE------------------
        img=Image.open(r"C:\facerecognition\face1.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=130)
        #---------------SECOND  IMAGE------------------

        img1=Image.open(r"C:\facerecognition\face2.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=510,height=130)
        #----------------THIRD  IMAGE------------------
        
        img2=Image.open(r"C:\facerecognition\face3.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=510,height=130)
        
        #----------------BACKGROUND IMAGE-----------------------------------
        img3=Image.open(r"C:\facerecognition\bg2.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE BASE SS\YSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #-----------------------BUTTON IMAGE-------------------------------
        img4=Image.open(r"face5.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,command=self.student_details,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)
        
        #-----------------------FACE DETECTOR-------------------------------

        img5=Image.open(r"face9.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,curso="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="FACE DETECTOR",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),fg="white",bg="darkblue")
        b1_1.place(x=500,y=300,width=220,height=40)
        
        #-----------------------ATTENDANCE IMAGE-------------------------------

        img6=Image.open(r"face16.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,curso="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="ATTENDANCE",command=self.attendance_pannel,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="darkblue")
        b1_1.place(x=800,y=300,width=220,height=40)

        #-----------------------HELPDESK IMAGE-------------------------------


        img7=Image.open(r"face15.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,curso="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="HELP DESK",command=self.help,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="darkblue")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        #-----------------------TRAIN DATA IMAGE-------------------------------


        img8=Image.open(r"face13.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="TRAIN DATA",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),fg="white",bg="darkblue")
        b1_1.place(x=200,y=600,width=220,height=40)

        #-----------------------PHOTOS IMAGE-------------------------------


        img9=Image.open(r"face12.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=500,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="PHOTOS",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="darkblue")
        b1_1.place(x=500,y=600,width=220,height=40)

        #-----------------------DEVELOPER IMAGE-------------------------------

        img10=Image.open(r"FARMAN PHOTOS.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,curso="hand2")
        b1.place(x=800,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="DEVELOPER",command=self.developer,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="darkblue")
        b1_1.place(x=800,y=600,width=220,height=40)

        #-----------------------EXIT IMAGE-------------------------------

        img11=Image.open(r"face14.jpg")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,curso="hand2")
        b1.place(x=1100,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="EXIT",command=self.Close,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="darkblue")
        b1_1.place(x=1100,y=600,width=220,height=40)
        
    def open_img(self):
            os.startfile("data")
        
        #------------------------------------FUNCTION--------------------------------------------------------
        
    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)
    
    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)
            
    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition(self.new_window)
            
            
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
    
    def Close(self):
        root.destroy()
        

        #------------------------------------------------------ERROR PROBLEM----------------------------------------
        #LINE NUMBER 51 and 54 THERE put the command   command=self.student_details use for the click the first page student then open student file but this function not work

        

    
if __name__=="__main__":
    root=Tk()
    obj=Face_recogonition(root)
    root.mainloop()

