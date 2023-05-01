from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
def insert():
    id=e_id.get();
    name=e_name.get();
    phone=e_phone.get();
    if(id == " " or name==" " or phone==" "):
        MessageBox.showinfo("insert status","All fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="poornima",database="register")
        cursor=con.cursor()
        cursor.execute("insert into data values('"+id+"','"+name+"','"+phone+"') ")
        cursor.execute("commit");
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')
        MessageBox.showinfo("insert status","inserted successfully");
        con.close();
def delete():
    if (e_id.get()==" "):
        MessageBox.showinfo("delete status","ID is compulsory for delete")
    else:
        con=mysql.connect(host="localhost",user="root",password="poornima",database="register")
        cursor=con.cursor()
        cursor.execute("delete from data where id='"+e_id.get() +"'")
        cursor.execute("commit");
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')
        MessageBox.showinfo("delete status","deleted successfully");
        con.close();
def update():
    id=e_id.get();
    name=e_name.get();
    phone=e_phone.get();
    if(id==" " or name==" " or phone==" "):
        MessageBox.showinfo("update status","All the fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="poornima",database="register")
        cursor=con.cursor()
        cursor.execute("update data set name='"+name+"',phone='"+phone+"' where id='"+id+"'")
        cursor.execute("commit");
        e_id.delete(0,'end')
        e_name.delete(0,'end')
        e_phone.delete(0,'end')
        MessageBox.showinfo("update status","update successfully");
        con.close();
def get():
    if(e_id.get()==" "):
        MessageBox.showinfo("fetch status","ID is compulsory for fetch")
    else:
        con=mysql.connect(host="localhost",user="root",password="poornima",database="register")
        cursor=con.cursor()
        cursor.execute("select * from data where id='"+e_id.get()+"'")
        rows=cursor.fetchall()
        for row in rows:
            e_name.insert(0,row[1])
            e_phone.insert(0,row[2])
        con.close();
def show():
        con=mysql.connect(host="localhost",user="root",password="poornima",database="register")
        cursor=con.cursor()
        cursor.execute("select * from data")
        rows=cursor.fetchall()
        list.delete(0, list.size())
        for row in rows:
            insertData=str(row[0])+' '(+row[1])
            list.insert(list.size()+1,insertData)
        con.close();
 
root=Tk()
root.geometry("600x300")
root.title("mini project")
id =Label(root,text="enter the Aadhaar id",font=('bold',10))
id.place(x=20,y=30)
name=Label(root,text="enter the name",font=('bold',10))
name.place(x=20,y=60)
phone=Label(root,text="enter the phone",font=('bold',10))
phone.place(x=20,y=90)
e_id=Entry()
e_id.place(x=150,y=30)
e_name=Entry()
e_name.place(x=150,y=60)
e_phone=Entry()
e_phone.place(x=150,y=90)

insert=Button(root,text="Insert",font=("bold",10),bg="white",command=insert)
insert.place(x=20,y=140)
delete=Button(root,text="Delete",font=("bold",10),bg="white",command=delete)
delete.place(x=70,y=140)
update=Button(root,text="update",font=("bold",10),bg="white",command=update)
update.place(x=130,y=140)
get=Button(root,text="get",font=("bold",10),bg="white",command=get)
get.place(x=190,y=140)
root.mainloop()
