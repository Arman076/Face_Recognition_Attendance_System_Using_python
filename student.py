from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")  
        
        #----------------------------------VARIABLE---------------------------------
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
        self.var_teacher=StringVar()
        self.var_PhotoSample=IntVar()
         #----------------FIRST  IMAGE------------------
        img=Image.open(r"C:\facerecognition\face17.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=10,y=0,width=510,height=130)
        #---------------SECOND  IMAGE------------------

        img1=Image.open(r"C:\facerecognition\face3.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=510,height=130)
        #----------------THIRD  IMAGE------------------
        
        img2=Image.open(r"C:\facerecognition\face9.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=510,height=130)
        #-----------------------BACKGROUND IMAGE-------------------------------------
        img3=Image.open(r"C:\facerecognition\bg2.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=10,y=0,width=1530,height=45)
        
        #---------------------------------------------------------------------------
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=50,width=1480,height=600)
        
        
        
        
        #----------------------------------LEFT FRAME------------------------------------------
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",15,"bold"),fg="green")
        left_frame.place(x=10,y=10,width=720,height=580,)
        
        
        img_left=Image.open(r"C:\facerecognition\face9.jpg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=710,height=130)
        
        current_coure_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="CURRENT COURSE INFORMATION",font=("times new roman",15,"bold"),fg="green")
        current_coure_frame.place(x=5,y=140,width=700,height=120)
        ####################################DEPARTMENT-------------------------------------------
        dep_label=Label(current_coure_frame,text="department",font=("times new roman",13,"bold"))
        dep_label.grid(row=0,column=0,padx=2,sticky=W) 
        
        dep_combo=ttk.Combobox(current_coure_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),width=21,state="readonly")
        dep_combo['values']=("SELECT DEPARTMENT","computer","it","bms","bmm","bammc","bcom","ba","bsc","bbi","baf")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        #-------------------------------------------COURSE-------------------------------------
        course_label=Label(current_coure_frame,text="COURSESS",font=("times new roman",13,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W) 
        
        course_combo=ttk.Combobox(current_coure_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),width=20,state="readonly")
        course_combo['values']=("SELECT COURSE","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=15,pady=10,sticky=W)
        
        #-----------------------------------------YEAR-----------------------------------------------------
        year_label=Label(current_coure_frame,text="YEARS",font=("times new roman",15,"bold"))
        year_label.grid(row=1,column=0,padx=2,sticky=W) 
        
        year_combo=ttk.Combobox(current_coure_frame,textvariable=self.var_year,font=("times new roman",15,"bold"),width=19,state="readonly")
        year_combo['values']=("SELECT YEAR","2015-2016","2017-2018","2019-2020","2021-2022","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        #------------------------------SEMESTER----------------------------------------
        semester_label=Label(current_coure_frame,text="SEMESTER",font=("times new roman",13,"bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W) 
        
        semester_combo=ttk.Combobox(current_coure_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),width=21,state="readonly")
        semester_combo['values']=("SELECT SEMESTER","FIRST I","SECOND II","THIRD III","FOURTH IV","FIFTH V","SIXTH VI","SEVENTH VII","EIGHT VIII")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)
        
        #-------------------------------------CLASS STUDENT INFORMATION---------------------------------------------
        class_Student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="CLASS STUDENT INFORMATION INFORMATION",font=("times new roman",15,"bold"),fg="green")
        class_Student_frame.place(x=5,y=260,width=710,height=290)
        
        studentId_label=Label(class_Student_frame,text="STUDENTID",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W) 
        
        studentId_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)
              
        #------------------------------------STUDENT NAME-----------------------------------------------
        studentName_label=Label(class_Student_frame,text="STUDENT NAME:",font=("times new roman",13,"bold"))
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W) 
        
        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        
        
        
        #----------------------------------------CLASS DIVISIONN---------------------------------------------
        class_div_label=Label(class_Student_frame,text="CLASS DIVISION:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W) 
        
       
        
        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",15,"bold"),width=18,state="readonly")
        div_combo['values']=("SELECT DIVISION","A","B","C","D","E","F","G","ANOTHER")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
        #------------------------------------ROLL NO-------------------------------------------
        Roll_no_label=Label(class_Student_frame,text="ROLL NO:",font=("times new roman",13,"bold"),bg="white")
        Roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W) 
        
        Roll_no__entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        Roll_no__entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #--------------------------------------GENDER--------------------------------------------
        gender_label=Label(class_Student_frame,text="GENDER:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W) 
        
        
        
        
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",15,"bold"),width=18,state="readonly")
        gender_combo['values']=("SELECT GENDER","MALE","FEMALE","TRANSGENDER","OTHER")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #-----------------------------------------DOB---------------------------------------------
        
        dob_label=Label(class_Student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W) 
        
        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        
        
        
        
        #----------------------------------------EMAIL--------------------------------------------------
        email_label=Label(class_Student_frame,text="EMAIL:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W) 
        
        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        
        
        
        #--------------------------------------PHONE NO----------------------------------------------------
        phone_label=Label(class_Student_frame,text="PHONE NO:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W) 
        
        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        
        
        
        #-------------------------------------------ADDRESS----------------------------------------------------
        address_label=Label(class_Student_frame,text="ADDRESS:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W) 
        
        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        
        
        #-------------------------------------------TEACHER NAME----------------------------------------------------
        teacher_label=Label(class_Student_frame,text="TEACHER NAME:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W) 
        
        teacher_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #--------------------------------------------RADIO BUTTONS-----------------------------------
        self.var_radio1=StringVar()
        radio_btn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take photo sample",value="YES")
        radio_btn1.grid(row=6,column=0)
        
        
        radio_btn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No photo sample",value="NO")
        radio_btn2.grid(row=6,column=1)
        
        #--------------------------------BUTTONS FRAME-------------------------------------------------
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=200,width=700,height=30,)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=5)
        
        update_btn=Button(btn_frame,text="UPDATE",command=self.update_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=5)
        
        delete_btn=Button(btn_frame,text="DELETE",command=self.delete_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx=5)
        
        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=5)
        
        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=235,width=700,height=30,)
        
        Take_photo_btn=Button(btn_frame1,text="take photo",command=self.genrate_dataset,width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Take_photo_btn.grid(row=0,column=0,padx=5)
        
        update_photo_btn=Button(btn_frame1,text="UPDATE PHOTO",command=self.genrate_dataset,width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1,padx=5)
        
        
        
        #--------------------------------------RIGHT FRAME-----------------------------------
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",15,"bold"),fg="green")
        right_frame.place(x=750,y=10,width=720,height=580)
        
       
        
        
        img_right=Image.open(r"C:\facerecognition\face20.jpg")
        img_right=img_right.resize((720,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=710,height=130)
        
        #---------------------------SEARCH SYSTEM---------------------------------------------------------
        Search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="SEARCH SYSTEM",font=("times new roman",15,"bold"),fg="green")
        Search_frame.place(x=5,y=135,width=710,height=70)
        
        Search_label=Label(Search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="red")
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        self.var_searchTX=StringVar()
        #Student_ID, Dep,Course,Year,Semester,Name,Division,Gender,Dob,Email,Phone,Address
        Search_combo=ttk.Combobox(Search_frame,textvariable=self.var_searchTX,font=("times new roman",13,"bold"),width=21,state="readonly")
        Search_combo['values']=("SELECT SEARCH","ROLL-NO")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        self.var_search=StringVar()
        
        Search_entry=ttk.Entry(Search_frame,text="Search",textvariable=self.var_search,width=15,font=("Bebas Neue",13,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        Search_btn=Button(Search_frame,text="Search",command=self.search_data,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3)
        
        ShowAll_btn=Button(Search_frame,text="SHOW ALL",width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=4)
        
        #---------------------------------------------TABLE FRAME-------------------------------------------------------
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=340)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone_no","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X) 
        scroll_y.pack(side=RIGHT,fill=Y) 
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)        
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll_No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone_no",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photos")  
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone_no",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=125)
        
        
        self.student_table.pack(fill=BOTH,expand=1) 
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
        #---------------------------------------------------FUNCTION DECLARATION-------------------------------------
    def add_data(self):
            if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","ALL FIELDS ARE REQUIRED",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database='face_recognizer')
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                
                                                                                                            ))
                    conn.commit()
                    self.fetch_data()
                    #self.get_cursor()#here is blank it is use me
                    conn.close()
                    messagebox.showinfo("success","student detals has been added successfully",parent=self.root)
                    
                except Exception as es:
                    messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
        
        #-------------------------FETCH DATA---------------------------------------------------------------------------------------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database='face_recognizer')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                conn.commit()
        conn.close()  
        
    #------------------------GET CURSOR----------------------------------------------------UPDATE BUTTON WORK----------------------------------                 
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)   
        data=content['values']
        self.var_dep.set(data[0]),#HERE 0 BEFORE EDIT
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
    #-----------------------------UPDATE FUNCTION-----------------------------------------------------------------
    def update_data(self):
        if self.var_dep.get()=="SELECT DEPARTMENT" or self.var_std_name.get()=="" or self.var_std_id.get()=="":#var deo get after SELECT DEPARTMENT
                messagebox.showerror("Error","ALL FIELDS ARE REQUIRED",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("UPDATE","DO YOU WANT TO UPDATE THIS STUDENT DATA",parent=self.root)
                if Upadate>0:
                   conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database='face_recognizer')
                   my_cursor=conn.cursor()
                   my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get(),
                                                                                                                                                                                        
                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                    ))
                   
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("success","student Details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()            
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
                
    #-------------------------------------DElETE FUNCTION BUTTON-------------------------------------------------
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database='face_recognizer')
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s" 
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)     
    
#-----------------------------------------RESET BUTTON FUNCTION----------------------------------------------------------------
    def reset_data(self):
        self.var_dep.set("SELECT DEPARTMENT")
        self.var_course.set("SELECT COURSE")
        self.var_year.set("SELECT YEAR")
        self.var_semester.set("SELECT SEMESTER")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("SELECT DIVISION")
        self.var_roll.set("")
        self.var_gender.set("SELECT GENDER")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("") 
        self.var_teacher.set("") 
        self.var_radio1.set("") 
        
    #======================================SEARCH DATASET====================================================================
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='Arman@123',host='localhost',database='face_recognizer')
                my_cursor = conn.cursor()
                sql = "SELECT Dep,Course,Year,Semester,Name,Division,Gender,Dob,Email,Phone,Address,TeacherPhotoSample, Roll='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                #my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    #--------------------------------GENRATE DATA SET OR TAKE PHOTO SAMPLE-----------------------------------------------------
    def genrate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","all fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Arman@123",database='face_recognizer')  
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(), 
                                                                                                                self.var_std_id.get()==id+1   
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #=============================LOAD PRE DEFINED DATA ON FACE FRONTALS FROM OPENCV
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):   
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
                    faces=face_classifier.detectMultiScale(gray,1.3,5)#SCALING FACTOR 1.3 MINIMUM NEIGHBOUR=5
                    
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                #===============================CAMERACAPTURE ===========================================
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped face",face)
                        
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                
                messagebox.showinfo("RESULT","GENRATING DATA SET COMPLETED!!!!",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                
                
                
                    
                        
                    
                    
                    
                        
                               
                          
                    
        
        
        
        
        
        

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
       
#-------------------------------------ERROR--------------------------------------------
#THE UPDATE BUTTON IS WORK BUT UPDATE DATA IS NOT WORK THE PROBLEM THERE IS LINNE 409 TO 447 UNDER ERROR IS RESOLVED SUCCESSFULLY THE DATABASE CCHECK HEDER NAME THATS REQUIRE IN THE PROG
