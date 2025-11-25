from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="black",fg="white")
        title.pack(side=TOP,fill=X)

        #All variables
        self.Roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

        #Manage Frame

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Manage_Frame.place(x=20,y=100,width=450,height=600)

        m_title=Label(Manage_Frame,text="Manage Students",bg="black",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0, columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="black",fg="white",font=("times new roman",20,"bold") )
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll=Entry(Manage_Frame,textvariable=self.Roll_no_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name",bg="black",fg="white",font=("times new roman",20,"bold") )
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_Email=Label(Manage_Frame,text="Email",bg="black",fg="white",font=("times new roman",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_Email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
        lbl_Gender=Label(Manage_Frame,text="Gender",bg="black",fg="white",font=("times new roman",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state="readonly")
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        lbl_Contact=Label(Manage_Frame,text="Contact",bg="black",fg="white",font=("times new roman",20,"bold"))
        lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_Contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_DOB=Label(Manage_Frame,text="D.O.B",bg="black",fg="white",font=("times new roman",20,"bold"))
        lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        
        txt_DOB=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_address=Label(Manage_Frame,text="Address",bg="black",fg="white",font=("times new roman",20,"bold"))
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_address=Text(Manage_Frame,width=26,height=4,font=("",10))
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        #button frame
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="black")
        btn_Frame.place(x=15,y=530,width=420,)

        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        cleanbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)


        #Detail Frame

        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="black")
        Detail_Frame.place(x=500,y=100,width=800,height=600)

        lbl_search=Label(Detail_Frame,text="Search By",bg="black",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,width=10,textvariable=self.search_by,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values']=("Roll_no","Name","Contact")
        combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="w")

        txt_search=Entry(Detail_Frame,width=20,textvariable=self.search_txt,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

#Table Frame
        table_frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="black")
        table_frame.place(x=10,y=70,width=760,height=500)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll",text="Roll no.")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("address",text="Address")
        self.student_table['show']='headings'
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("contact",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("address",width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_students(self):
        if self.Roll_no_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","all field are required !!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_no_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.txt_address.get('1.0',END)
                                                                            ))
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo("success","Record has been inserted")
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()
    def clear(self):
        self.Roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)
    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        row=content['values']
        self.Roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])
    
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                                                 self.name_var.get(),
                                                                                                 self.email_var.get(),
                                                                                                 self.gender_var.get(),
                                                                                                 self.contact_var.get(),
                                                                                                 self.dob_var.get(),
                                                                                                 self.txt_address.get('1.0',END),
                                                                                                 self.Roll_no_var.get()
                                                                                                 ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("success","Record has been updated")
    
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_no_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get()+"%'"))
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()



root=Tk()
ob=student(root)
root.mainloop()