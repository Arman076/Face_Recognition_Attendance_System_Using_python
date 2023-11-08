from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from tkinter import messagebox
import os
import numpy as np
import cv2
import mysql.connector

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("TRAIN DATA SET") 
        
        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        #----------------FIRST  IMAGE------------------
        img_top=Image.open(r"C:\facerecognition\banner.jpg")
        img_top=img_top.resize((1530,325),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=10,y=55,width=1530,height=325)
        
        #=======================================BACKGROUND IMAGE=====================================
        img3=Image.open(r"C:\facerecognition\t_bg1.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=10,y=380,width=1530,height=710)
        
        #===============================TRAIN DATA BUTTON==========================================
        #b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",45,"bold"),bg="yellow",fg="white")
        #b1_1.place(x=10,y=380,width=1530,height=60)
        std_img_btn=Image.open(r"t_btn1.png")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.train_classifier,image=self.std_img1,cursor="hand2")
        std_b1.place(x=650,y=30,width=180,height=210)

        std_b1_1 = Button(bg_img,command=self.train_classifier,text="Train Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=650,y=230,width=180,height=45)
       
        
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') #GRAY SCALE IMAGE
            imageNp=np.array(img,'uint8') #unit8 is 0a data type in numpy array
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training image data",imageNp) 
            cv2.waitKey(1)==13
        ids=np.array(ids)
    
    #=======================TRAIN THE CLASSIFIER AND SAVE==================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","trainig data set completed",parent=self.root)
        
        
    
    
                                          
  
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()