from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from tkinter import messagebox
import os
import numpy as np
import cv2
import mysql.connector
from time import strftime
import datetime

class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("FACE RECOGNITION SYSTEM") 
        
        
        img_top=Image.open(r"C:\facerecognition\face9.jpg")
        img_top=img_top.resize((800,200),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=800,height=200)
        #===========================SECOND IMAGE=================================
        img_bottom=Image.open(r"C:\facerecognition\face15.jpg")
        img_bottom=img_bottom.resize((800,200),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=805,y=55,width=800,height=200)
        
        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=10,y=260,width=1480,height=600)
        
        left_frame=LabelFrame(self.root,bd=2,bg="white",relief=RIDGE,text="STUDENT ATTENDANCE DETAILS",font=("times new roman",15,"bold"),fg="green")
        left_frame.place(x=10,y=270,width=730,height=580,)
        
        img_left=Image.open(r"C:\facerecognition\face20.jpg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=710,height=130)
        
        left_inside_frame=Frame(self.root,bd=2,bg="white",relief=RIDGE)
        left_inside_frame.place(x=15,y=440,width=710,height=400)
        
        #====================LABEL AND ENTRY===============================
        #ATTENDANCE ID=============================
        attedanceId_label=Label(left_inside_frame,text="Attendance_Id:",font=("times new roman",15,"bold"),bg="white")
        attedanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attedanceId_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
        attedanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        #=============================NAME=========================
        rollLabel=Label(left_inside_frame,text="Roll:",bg="white",fg="black",font="comicsansns 11 bold")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)
        
        atten_roll=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_roll.grid(row=0,column=3,pady=8)
        
        #===========================================DATE====================================
        
        nameLabel=Label(left_inside_frame,text="NAME:",font="comicsansns 11 bold",bg="white")
        nameLabel.grid(row=1,column=0)
        
        
        
        atten_name=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_name.grid(row=1,column=1,pady=8)
        
        #==========================department==========================
        
        DepLabel=Label(left_inside_frame,text="Department:",font="comicsansns 11 bold",bg="white")
        DepLabel.grid(row=1,column=2)
        
        
        
        atten_dep=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_dep.grid(row=1,column=3,pady=8)
        
        #===========================TIME=====================================================
        
        timeLabel=Label(left_inside_frame,text="Time:",font="comicsansns 11 bold",bg="white")
        timeLabel.grid(row=2,column=0)
        
        
        
        atten_time=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,pady=8)
        
        #=======================================DATE================================
        dateLabel=Label(left_inside_frame,text="Date:",font="comicsansns 11 bold",bg="white")
        dateLabel.grid(row=2,column=2)
        
        
        
        atten_date=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3,pady=8)
        
        #=================================ATTENDANCE====================================
        attendanceLabel=Label(left_inside_frame,text="ATTENDANCE STATUS",bg="white",font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)
        
        self.atten_status=ttk.Combobox(left_inside_frame,width=20,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","present","absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        #--------------------------------BUTTONS FRAME-------------------------------------------------
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=360,width=710,height=30,)
        
        save_btn=Button(btn_frame,text="Import csv",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Export csv",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="DELETE",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,)
        
        reset_btn=Button(btn_frame,text="RESET",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        
        
        #===============================RIGHT FRAME============================
        
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="ATTENDANCE DETAILS",font=("times new roman",15,"bold"),fg="green")
        right_frame.place(x=750,y=10,width=725,height=580)
        
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=710,height=445)
        
        #============================SCRILL BAR TABLE===========================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","atten"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X) 
        scroll_y.pack(side=RIGHT,fill=Y) 
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Student_id")
        self.AttendanceReportTable.heading("roll",text="Roll_no")
        self.AttendanceReportTable.heading("name",text="Name:")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("atten",text="Attendance")
       
        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("atten",width=100)
        
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
         
                                                        
if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop() 
        
        