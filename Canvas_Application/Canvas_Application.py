"""
File Name: Canvas_Application.py
Author: Bhavana Vankhede
Date: 12/14/2018
Notes: This implementation file serves as the GUI layer. 
"""

import tkinter as tk
from tkinter import ttk
import Repository as rep
import urllib.request as url
from tkinter import filedialog



FRAME_TITLE_FONT=("Verdana",20,"bold italic")
TITLE_FONT=("Verdana",16,"bold")
LARGE_FONT=("Verdana",12)
STUDENT_ID=0

def getFile(filename,destination):          #method for downloading the assignment or course material files.
        url.urlretrieve("file:///C:/Users/wbhaw/source/repos/Project_1029055/Canvas_Application/Canvas_Application/Download/"+str(filename),str(destination)+str(filename))

def switch_page(F,base_frame,controller,parent):            #generic method for switching the frames within the application.
    base_frame.grid_forget()
    frame=F(parent,controller)
    frame.tkraise()
    print(frame,base_frame,controller,parent)

def setup_Frame1(base_frame,controller,parent):            #generic meethod for populating the default fixed frame.
    btn1_photo=tk.PhotoImage(file="People.gif")    
    btn2_photo=tk.PhotoImage(file="assignment.gif")
    btn3_photo=tk.PhotoImage(file="grade.gif")
    btn4_photo=tk.PhotoImage(file="File.gif")
    btn5_photo=tk.PhotoImage(file="grade1.gif")
    lbl_photo=tk.PhotoImage(file="logo.gif")

    btn1=ttk.Button(base_frame,text="People",image=btn1_photo,command=lambda:switch_page(list_of_people,controller,controller,parent))
    btn1.image=btn1_photo
    btn1.pack(padx=2,pady=2)
    btn2=ttk.Button(base_frame,text="Assignments",image=btn2_photo,command=lambda:switch_page(Assignments,controller,controller,parent))
    btn2.image=btn2_photo
    btn2.pack(padx=2,pady=2)
    btn3=ttk.Button(base_frame,text="Grade",image=btn3_photo,command=lambda:switch_page(Grades,controller,controller,parent))
    btn3.image=btn3_photo
    btn3.pack(padx=2,pady=2)
    btn4=ttk.Button(base_frame,text="Files",image=btn4_photo,command=lambda:switch_page(Files,controller,controller,parent))
    btn4.image=btn4_photo
    btn4.pack(padx=2,pady=2)
    btn5=ttk.Button(base_frame,text="Announcements",image=btn5_photo,command=lambda:switch_page(Announcements,controller,controller,parent))
    btn5.image=btn5_photo
    btn5.pack(padx=2,pady=2)
    lbl=ttk.Label(base_frame,text="",image=lbl_photo)
    lbl.image=lbl_photo
    lbl.pack(padx=2,pady=5)


##################################################################################################################################################3


def setup_Frame2(base_frame,controller,parent):            #generic meethod for populating the default fixed frame.
    btn1_photo=tk.PhotoImage(file="People.gif")    
    btn2_photo=tk.PhotoImage(file="assignment.gif")
    btn3_photo=tk.PhotoImage(file="grade.gif")
    btn4_photo=tk.PhotoImage(file="File.gif")
    btn5_photo=tk.PhotoImage(file="grade1.gif")
    lbl_photo=tk.PhotoImage(file="logo.gif")

    btn1=ttk.Button(base_frame,text="People",image=btn1_photo,command=lambda:switch_page(list_of_people,controller,controller,parent))
    btn1.image=btn1_photo
    btn1.pack(padx=2,pady=2)
    btn2=ttk.Button(base_frame,text="Assignments",image=btn2_photo,command=lambda:switch_page(uploadAssignments,controller,controller,parent))
    btn2.image=btn2_photo
    btn2.pack(padx=2,pady=2)
    btn3=ttk.Button(base_frame,text="Grade",image=btn3_photo,command=lambda:switch_page(Grades,controller,controller,parent))
    btn3.image=btn3_photo
    btn3.pack(padx=2,pady=2)
    btn4=ttk.Button(base_frame,text="Files",image=btn4_photo,command=lambda:switch_page(Files,controller,controller,parent))
    btn4.image=btn4_photo
    btn4.pack(padx=2,pady=2)
    btn5=ttk.Button(base_frame,text="Announcements",image=btn5_photo,command=lambda:switch_page(Announcements,controller,controller,parent))
    btn5.image=btn5_photo
    btn5.pack(padx=2,pady=2)
    lbl=ttk.Label(base_frame,text="",image=lbl_photo)
    lbl.image=lbl_photo
    lbl.pack(padx=2,pady=5)


#####################################################################################################################################################

class Canvas_Application(tk.Tk):
    def __init__(self, *args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.iconbitmap(self,default="icon.ico")
        tk.Tk.title(self,"Canvas")
        self.resizable(False,False)
        base_frame=ttk.Frame(self)
        base_frame.pack(fill=tk.BOTH,expand=True)
        menubar=tk.Menu(base_frame)
        file_menu=tk.Menu(menubar,tearoff=0)
        file_menu.add_command(label="Exit",command=exit)
        menubar.add_cascade(label="Option",menu=file_menu)
        tk.Tk.config(self,menu=menubar)
        login_view=Login(base_frame)
        self.geometry("900x400")

class Login(tk.Tk):             #class for the Login module
    def __init__(self,base_frame):
        self.root=tk.Tk()
        self.root.geometry("300x200")
        parent=tk.Frame(self.root,bg='purple')
        parent.pack(fill=tk.BOTH,expand=True)
        self.root.wm_title("Login")
        self.root.resizable(False,False)

        label=ttk.Label(parent,text="Please Login!!")
        label.grid(row=1,column=0,columnspan=10)
        User_lbl=ttk.Label(parent,text="UserName")
        User_lbl.grid(row=3,column=0)
        User_pwd=ttk.Label(parent,text="Password")
        User_pwd.grid(row=5,column=0)
        self.Text_UID=tk.IntVar()
        self.Text_pwd=tk.StringVar()
        User_txt=ttk.Entry(parent,textvariable=self.Text_UID)
        User_txt.grid(row=3,column=1)
        User_pwd=ttk.Entry(parent,textvariable=self.Text_pwd,show="*")
        User_pwd.grid(row=5,column=1)
        login_std_btn=ttk.Button(parent,text="StudentLogin",command=lambda:self.verifyUser(int (User_txt.get()),User_pwd.get(),'S',base_frame))
        login_std_btn.grid(row=9,column=0)
        login_adm_btn=ttk.Button(parent,text="AdminLogin",command=lambda:self.verifyUser(int (User_txt.get()),User_pwd.get(),'A',base_frame))
        login_adm_btn.grid(row=9,column=1)
        self.Status_lbl=ttk.Label(parent,text="")
        self.Status_lbl.grid(row=11,column=0,columnspan=10)
        for child in parent.winfo_children():
            child.grid_configure(padx=5,pady=5)

        self.root.lift()

    def verifyUser(self,Text_UID,Text_pwd,role,base_frame):              #method to verify the user
        print(Text_UID,Text_pwd,role)
        print(self.Text_UID.get(),self.Text_pwd.get())
        self.status=rep.ComposeSQL.verifyUser(self,Text_UID,Text_pwd)
        if (self.status==True and role=='S'):
            self.Status_lbl.configure(text="Login successful!!!!")
            global STUDENT_ID
            STUDENT_ID=int(Text_UID)
            print('test:',STUDENT_ID)
            self.root.destroy()
            frame=Home(base_frame)
        elif(self.status==True and role=='A'):
            self.Status_lbl.configure(text="Login successful!!!!")
            STUDENT_ID=int(Text_UID)
            print('test:',STUDENT_ID)
            self.root.destroy()
            frame=Admin(base_frame)

        else:
            self.Status_lbl.configure(text="Login un-successful!!!!")

class Home(ttk.Frame):              #class to initiate the Home page.
    def __init__(self,parent):
        super(Home,self).__init__()
        self.fr1=tk.Frame(parent,bg='blue',width=20)
        self.fr2=tk.Frame(parent,bg="black",width=80)
        
        self.fr1.grid(row=2,column=0,sticky='nsew')
        self.fr2.grid(row=2,column=1,sticky='nsew')
        self.label1=ttk.Label(parent,text="UB Canvas Dashboard",font=LARGE_FONT)
        self.label1.grid(row=1,column=0,columnspan=2)

        photo1=tk.PhotoImage(file="pqr.gif")
        button=ttk.Button(self.fr2,text="Python Programming",image=photo1,width=50,command=lambda:switch_page(list_of_people,parent,self,parent))
        button.config(width=10)
        button.grid(row=5,column=10)
        button.image=photo1
        self.fr2.grid_columnconfigure(10,weight=1)
        self.fr2.grid_rowconfigure(5,weight=1)

        parent.grid_rowconfigure(2,weight=1)
        parent.grid_columnconfigure(0,weight=1,uniform='group1')
        parent.grid_columnconfigure(1,weight=3,uniform='group1')

class Admin(ttk.Frame):              #class to initiate the Home page.
    def __init__(self,parent):
        super(Admin,self).__init__()
        self.fr1=tk.Frame(parent,bg='blue',width=20)
        self.fr2=tk.Frame(parent,bg="black",width=80)
        
        self.fr1.grid(row=2,column=0,sticky='nsew')
        self.fr2.grid(row=2,column=1,sticky='nsew')
        self.label1=ttk.Label(parent,text="UB Canvas Dashboard",font=LARGE_FONT)
        self.label1.grid(row=1,column=0,columnspan=2)

        photo1=tk.PhotoImage(file="pqr.gif")
        button=ttk.Button(self.fr2,text="Python Programming",image=photo1,width=50,command=lambda:switch_page(Admin_list_of_people,parent,self,parent))
        button.config(width=10)
        button.grid(row=5,column=10)
        button.image=photo1
        self.fr2.grid_columnconfigure(10,weight=1)
        self.fr2.grid_rowconfigure(5,weight=1)

        parent.grid_rowconfigure(2,weight=1)
        parent.grid_columnconfigure(0,weight=1,uniform='group1')
        parent.grid_columnconfigure(1,weight=3,uniform='group1')


        
class list_of_people(ttk.Frame):                    #class to display the Peoples module
    def __init__(self,parent,controller):
        super(list_of_people,self).__init__()
        self.fr1=tk.Frame(parent,bg='blue',width=20)
        self.fr2=tk.Frame(parent,bg='orange',width=80)
        
        self.fr1.grid(row=2,column=0,sticky='nsew')
        self.fr2.grid(row=2,column=1,sticky='nsew')
        self.title=ttk.Label(self.fr2,text="People",font=FRAME_TITLE_FONT)
        self.title.grid(row=0,column=0,columnspan=2)
        
        self.record=()

        self.record=rep.ComposeSQL.peopleList(self)
        lbl1=ttk.Label(self.fr2,text="Name",font=TITLE_FONT,borderwidth=2,relief="solid")
        lbl1.grid(row=2,column=0)
        lbl2=ttk.Label(self.fr2,text="Role",font=TITLE_FONT,borderwidth=2,relief="solid")
        lbl2.grid(row=2,column=1)
        for i in range(0,len(self.record)):
            for j in range(0,2):
                var1=tk.StringVar()                
                var1.set(self.record[i][j])
                lbl=ttk.Label(self.fr2,text=var1.get(),font=LARGE_FONT,borderwidth=2,relief="solid")
                lbl.grid(row=i+5,column=j)

        setup_Frame1(self.fr1,self,parent)
        
        parent.grid_rowconfigure(2,weight=1)
        parent.grid_columnconfigure(0,weight=1,uniform='group1')
        parent.grid_columnconfigure(1,weight=3,uniform='group1')

        for child in self.fr2.winfo_children():
            child.grid_configure(padx=2,pady=2)
        

class Admin_list_of_people(ttk.Frame):                    #class to display the Peoples module
    def __init__(self,parent,controller):
        super(Admin_list_of_people,self).__init__()
        self.fr1=tk.Frame(parent,bg='blue',width=20)
        self.fr2=tk.Frame(parent,bg='orange',width=80)      
        self.fr1.grid(row=2,column=0,sticky='nsew')
        self.fr2.grid(row=2,column=1,sticky='nsew')
        lbl1=ttk.Label(self.fr2,text="Course Code")
        lbl1.grid(row=5,column=0)
        self.CourseCode=tk.StringVar()
        User_code=ttk.Entry(self.fr2,textvariable=self.CourseCode)
        User_code.grid(row=5, column=1)
        lbl2=ttk.Label(self.fr2,text="Course Name")
        lbl2.grid(row=7,column=0)
        self.CourseName=tk.StringVar()
        User_crs_name=ttk.Entry(self.fr2,textvariable=self.CourseName)
        User_crs_name.grid(row=7, column=1)
        lbl3=ttk.Label(self.fr2,text="Credits")
        lbl3.grid(row=9,column=0)
        self.Credits=tk.StringVar()
        User_credits=ttk.Entry(self.fr2,textvariable=self.Credits)
        User_credits.grid(row=9, column=1)
        lbl4=ttk.Label(self.fr2,text="StudentID")
        lbl4.grid(row=11,column=0)
        self.StudentID=tk.StringVar()
        User_stdID=ttk.Entry(self.fr2,textvariable=self.StudentID)
        User_stdID.grid(row=11, column=1)
        btn=ttk.Button(self.fr2,text="Add Student", command=lambda:rep.ComposeSQL.updatePeopleList(self,'11','22',3,1019022))
        btn.grid(row=13, column=1)
        
        self.record=()

        self.record=rep.ComposeSQL.peopleList(self)
        
        lbl1=ttk.Label(self.fr2,text="Name",font=TITLE_FONT,borderwidth=2,relief="solid")
        lbl1.grid(row=15,column=0)
        lbl2=ttk.Label(self.fr2,text="Role",font=TITLE_FONT,borderwidth=2,relief="solid")
        lbl2.grid(row=15,column=1)
        print('hi')
        for i in range(0,len(self.record)):
            for j in range(0,2):
                var1=tk.StringVar()                
                var1.set(self.record[i][j])
                lbl=ttk.Label(self.fr2,text=var1.get(),font=LARGE_FONT,borderwidth=2,relief="solid")
                lbl.grid(row=i+15+5,column=j)

        setup_Frame2(self.fr1,self,parent)
        
        parent.grid_rowconfigure(2,weight=1)
        parent.grid_columnconfigure(0,weight=1,uniform='group1')
        parent.grid_columnconfigure(1,weight=3,uniform='group1')

        for child in self.fr2.winfo_children():
            child.grid_configure(padx=2,pady=2)

        


class Assignments(ttk.Frame):                   #class to display the Assignments module
    def __init__(self,parent,controller):
        super(Assignments,self).__init__()
        self.fr1=tk.Frame(parent,bg='blue',width=20)
        self.fr2=tk.Frame(parent,bg="red",width=80)
        
        self.fr1.grid(row=2,column=0,sticky='nsew')
        self.fr2.grid(row=2,column=1,sticky='nsew')
        self.title=ttk.Label(self.fr2,text="Assignment",font=FRAME_TITLE_FONT)
        self.title.grid(row=0,column=0,columnspan=2)
        self.note=ttk.Label(self.fr2,text='''Please note to submit the below assignments before the due date. 
        Please email the assignments to GA.
        mail id: bvankhed@my.bridgeport.edu''')
        self.note.grid(row=1,column=0,columnspan=2)
        self.record=()

        self.record=rep.ComposeSQL.listAssignments(self,STUDENT_ID)
        lbl1=ttk.Label(self.fr2,text="Name",font=TITLE_FONT,borderwidth=2,relief="solid")
        lbl1.grid(row=3,column=0)        
        lbl3=ttk.Label(self.fr2,text="Due Date",font=TITLE_FONT,borderwidth=2,relief="solid")
        lbl3.grid(row=3,column=1)
        self.destination="C:\\Users\\wbhaw\\source\\repos\\Project_1029055\\Canvas_Application\\Canvas_Application\\Assignment\\"
        for i in range(0,len(self.record)):
            for j in range(0,2):
                var1=tk.StringVar()                
                var1.set(self.record[i][j])
                lbl=ttk.Label(self.fr2,text=var1.get(),font=LARGE_FONT,borderwidth=2,relief="solid")
                lbl.grid(row=i+5,column=j)
            btn=ttk.Button(self.fr2,text="Download",command=lambda cnt=i:getFile(str(self.record[cnt][2]),self.destination))
            print('dwnload:',str(self.record[i][2]))
            btn.grid(row=i+5,column=2)

        setup_Frame1(self.fr1,self,parent)        

        parent.grid_rowconfigure(2,weight=1)
        parent.grid_columnconfigure(0,weight=1,uniform='group1')
        parent.grid_columnconfigure(1,weight=3,uniform='group1')

        for child in self.fr2.winfo_children():
            child.grid_configure(padx=2,pady=2)


class uploadAssignments(ttk.Frame):                   #class to display the Assignments module
    def __init__(self,parent,controller):
        super(uploadAssignments,self).__init__()
        self.fr1=tk.Frame(parent,bg='blue',width=20)
        self.fr2=tk.Frame(parent,bg="red",width=80)
        
        self.fr1.grid(row=2,column=0,sticky='nsew')
        self.fr2.grid(row=2,column=1,sticky='nsew')
        self.title=ttk.Label(self.fr2,text="Assignment",font=FRAME_TITLE_FONT)
        self.title.grid(row=0,column=0,columnspan=2)
        self.note=ttk.Label(self.fr2,text='''Please note to submit the below assignments before the due date. 
        Please email the assignments to GA.
        mail id: bvankhed@my.bridgeport.edu''')
        self.note.grid(row=1,column=0,columnspan=2)
        self.record=()

        self.record=rep.ComposeSQL.listAssignments(self,STUDENT_ID)
        lbl1=ttk.Label(self.fr2,text="Name",font=TITLE_FONT,borderwidth=2,relief="solid")
        lbl1.grid(row=3,column=0)        
        lbl3=ttk.Label(self.fr2,text="Due Date",font=TITLE_FONT,borderwidth=2,relief="solid")
        lbl3.grid(row=3,column=1)
        self.source="C:\\Users\\wbhaw\\source\\repos\\Project_1029055\\Canvas_Application\\Canvas_Application\\Assignment\\"
        self.destination="C:\\Users\\wbhaw\\source\\repos\\Project_1029055\\Canvas_Application\\Canvas_Application\\Download\\"
        #fileSource= tk.asksaveasfile(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

        for i in range(0,len(self.record)):
            for j in range(0,2):
                var1=tk.StringVar()                
                var1.set(self.record[i][j])
                lbl=ttk.Label(self.fr2,text=var1.get(),font=LARGE_FONT,borderwidth=2,relief="solid")
                lbl.grid(row=i+5,column=j)
            btn=ttk.Button(self.fr2,text="Upload",command=lambda cnt=i:getFile(str(self.record[cnt][2]),self.destination))
            print('dwnload:',str(self.record[i][2]))
            btn.grid(row=i+5,column=2)

        setup_Frame2(self.fr1,self,parent)        

        parent.grid_rowconfigure(2,weight=1)
        parent.grid_columnconfigure(0,weight=1,uniform='group1')
        parent.grid_columnconfigure(1,weight=3,uniform='group1')

        for child in self.fr2.winfo_children():
            child.grid_configure(padx=2,pady=2)

class Files(ttk.Frame):                     #class to display the Files module.
    def __init__(self,parent,controller):
        super(Files,self).__init__()
        self.fr1=tk.Frame(parent,bg='blue',width=20)
        self.fr2=tk.Frame(parent,bg="purple",width=80)
        
        self.fr1.grid(row=2,column=0,sticky='nsew')
        self.fr2.grid(row=2,column=1,sticky='nsew')
        self.title=ttk.Label(self.fr2,text="Files",font=FRAME_TITLE_FONT)
        self.title.grid(row=0,column=0,columnspan=2)
        self.note=ttk.Label(self.fr2,text='''Please use the following material for exam preparation.
        For any questions, please consult me or GA.
        mail id: bvankhed@my.bridgeport.edu''')
        self.note.grid(row=1,column=0,columnspan=2)
        self.record=()

        self.record=rep.ComposeSQL.listFiles(self,STUDENT_ID)
        lbl1=ttk.Label(self.fr2,text="Name",font=TITLE_FONT,borderwidth=2,relief="solid")
        lbl1.grid(row=3,column=0)
        self.destination="C:/Users/wbhaw/source/repos/Project_1029055/Canvas_Application/Canvas_Application/Files/"
        for i in range(0,len(self.record)):
            for j in range(0,1):
                var1=tk.StringVar()                
                var1.set(self.record[i][j])
                lbl=ttk.Label(self.fr2,text=var1.get(),font=LARGE_FONT,borderwidth=2,relief="solid")
                lbl.grid(row=i+5,column=j)
            btn=ttk.Button(self.fr2,text="Download",command=lambda cnt=i:getFile(str(self.record[cnt][1]),self.destination))
            btn.grid(row=i+5,column=2)

        setup_Frame1(self.fr1,self,parent)
        
        parent.grid_rowconfigure(2,weight=1)
        parent.grid_columnconfigure(0,weight=1,uniform='group1')
        parent.grid_columnconfigure(1,weight=3,uniform='group1')

        for child in self.fr2.winfo_children():
            child.grid_configure(padx=2,pady=2)
        
class Grades(ttk.Frame):                    #class to display the Grades module
    def __init__(self,parent,controller):
        super(Grades,self).__init__()
        self.fr1=tk.Frame(parent,bg='blue',width=20)
        self.fr2=tk.Frame(parent,bg="orange",width=80)
        
        self.fr1.grid(row=2,column=0,sticky='nsew')
        self.fr2.grid(row=2,column=1,sticky='nsew')
        self.title=ttk.Label(self.fr2,text="Grades",font=FRAME_TITLE_FONT)
        self.title.grid(row=0,column=0,columnspan=2)
        self.note=ttk.Label(self.fr2,text='''Following are the grades for submitted Assignments/Projects/Midterm/Finals.
        For any questions, please consult me or GA.
        mail id: bvankhed@my.bridgeport.edu''')
        self.note.grid(row=1,column=0,columnspan=2)
        self.record=()

        self.record=rep.ComposeSQL.getGrades(self,STUDENT_ID)
        
        lbl1=ttk.Label(self.fr2,text="Name",font=TITLE_FONT,borderwidth=2,relief="solid")
        lbl1.grid(row=3,column=0)
        lbl1=ttk.Label(self.fr2,text="Due Date",font=TITLE_FONT,borderwidth=2,relief="solid")
        lbl1.grid(row=3,column=1)
        lbl1=ttk.Label(self.fr2,text="Score",font=TITLE_FONT,borderwidth=2,relief="solid")
        lbl1.grid(row=3,column=2)
        lbl1=ttk.Label(self.fr2,text="Out Of",font=TITLE_FONT,borderwidth=2,relief="solid")
        lbl1.grid(row=3,column=3)
        
        for i in range(0,len(self.record)):
            for j in range(0,4):
                var1=tk.StringVar()                
                var1.set(self.record[i][j])
                lbl=ttk.Label(self.fr2,text=var1.get(),font=LARGE_FONT,borderwidth=2,relief="solid")
                lbl.grid(row=i+5,column=j)
            
            
        setup_Frame1(self.fr1,self,parent)        

        parent.grid_rowconfigure(2,weight=1)
        parent.grid_columnconfigure(0,weight=1,uniform='group1')
        parent.grid_columnconfigure(1,weight=3,uniform='group1')

        for child in self.fr2.winfo_children():
            child.grid_configure(padx=2,pady=2)


class Announcements(ttk.Frame):                    #class to display the Peoples module
    def __init__(self,parent,controller):
        super(Announcements,self).__init__()
        self.fr1=tk.Frame(parent,bg='blue',width=20)
        self.fr2=tk.Frame(parent,bg='green',width=80)
        
        self.fr1.grid(row=2,column=0,sticky='nsew')
        self.fr2.grid(row=2,column=1,sticky='nsew')
        self.title=ttk.Label(self.fr2,text="Important Announcements",font=FRAME_TITLE_FONT)
        self.title.grid(row=0,column=0,columnspan=2)
        
        self.record=()

        self.record=rep.ComposeSQL.getAnnouncement(self)
        lbl1=ttk.Label(self.fr2,text="Date",font=TITLE_FONT,borderwidth=2,relief="solid")
        lbl1.grid(row=2,column=0)
        lbl2=ttk.Label(self.fr2,text="Announcements",font=TITLE_FONT,borderwidth=2,relief="solid")
        lbl2.grid(row=2,column=1)
        for i in range(0,len(self.record)):
            for j in range(0,2):
                var1=tk.StringVar()                
                var1.set(self.record[i][j])
                lbl=ttk.Label(self.fr2,text=var1.get(),font=LARGE_FONT,borderwidth=2,relief="solid")
                lbl.grid(row=i+5,column=j)

        setup_Frame1(self.fr1,self,parent)
        
        parent.grid_rowconfigure(2,weight=1)
        parent.grid_columnconfigure(0,weight=1,uniform='group1')
        parent.grid_columnconfigure(1,weight=3,uniform='group1')

        for child in self.fr2.winfo_children():
            child.grid_configure(padx=2,pady=2)
    
def main():             #main method.
    obj=Canvas_Application()
    obj.geometry("900x500")
    obj.mainloop()

if __name__=="__main__":
    main()
