import mysql
import MySQLdb
import smtplib
db=MySQLdb.connect("localhost","root","123","library")
cur=db.cursor()
from tkinter import*
import tkinter as tk
from PIL import ImageTk, Image
win=Tk()
path=('library.jpg')
img=ImageTk.PhotoImage(Image.open(path))
w=img.width()
h=img.height()
win.geometry('%dx%d+150+20'%(w,h))
win.title('Login page')
    
panel=tk.Label(win, image=img)
panel.place(x=0,y=0)
lbl=Label(win, text="Login",font=("algerian",50),bg='yellow',fg="blue",width=7)
win.wm_attributes('-transparentcolor','yellow')
lb2=Label(win, text="User Id",bg='black',fg='white',font=('bold'),width=15) 
lb3=Label(win, text="Password",bg='black',fg='white',font=('bold'),width=15)
lbl.place(x=340,y=30)
lb2.place(x=230,y=170)
lb3.place(x=230,y=240)

x1 = StringVar()
y1 = StringVar()

txt1=Entry(win,width=20,bg="grey",fg='white',font=("bold"),textvariable = x1)
txt2=Entry(win,show='*',width=20,bg="grey",fg='white',font=("bold"),textvariable = y1)

txt1.place(x=600,y=170)
txt2.place(x=600,y=240)


def login():
    user_val = x1.get()
    pass_val = y1.get();
    cur.execute('select *from lib')
    rows=cur.fetchall()
    c=0
    #print(user_val)
    #print(pass_val)
    for i in range(0,len(rows)):
        for j in range(1,3):
            if user_val==rows[i][j] and j==1:
                if pass_val==rows[i][2]:
                    c+=1
    if c==0:     
        lbl=Label(win,text="Sorry you have entered wrong UserId or Password",bg='black',font=('bold'),fg='red',width=40)
        lbl.place(x=400,y=350)
    else:
        win3=Toplevel()
        win.withdraw()
        #win3.geometry("200x300")
        #win=Tk()
        path=('libview.jpg')
        img1=ImageTk.PhotoImage(Image.open(path))
        w=img1.width()
        h=img1.height()
        win3.geometry('%dx%d+250+150'%(w,h))
        panel=Label(win3, image=img1)
        panel.place(x=0,y=0)

        def home():
            win4=Toplevel()
            win3.withdraw()
            #win4.geometry('200x200+200+250')
            path=('libbooks.jpg')
            img1=ImageTk.PhotoImage(Image.open(path))
            w=img1.width()
            h=img1.height()
            win4.geometry('%dx%d+250+450'%(w,h))
            panel=Label(win4, image=img1)
            panel.place(x=0,y=0)
            
            win4.title('Home')
            def profile():
                win5=Toplevel()
                win4.withdraw()
                win5.geometry('400x500')
                win5.title("Profiles")
                lb2=Label(win5, text="UserId",bg='black',fg='white',font=('bold'),width=15)
                lb3=Label(win5, text="Password",bg='black',fg='white',font=('bold'),width=15)
                lb4=Label(win5, text="Roll No",bg='black',fg='white',font=('bold'),width=15)
                lb5=Label(win5, text="Name",bg='black',fg='white',font=('bold'),width=15)
                lb6=Label(win5, text="Course",bg='black',fg='white',font=('bold'),width=15)
                lb7=Label(win5, text="Branch",bg='black',fg='white',font=('bold'),width=15)
                lb8=Label(win5, text="Semester",bg='black',fg='white',font=('bold'),width=15)
                lb9=Label(win5, text="Phone No",bg='black',fg='white',font=('bold'),width=15)

                            
  
                            #lb1.place(x=30,y=30)
                            
                lb2.place(x=30,y=30)
                lb3.place(x=30,y=80)
                lb4.place(x=30,y=130)
                lb5.place(x=30,y=180)
                lb6.place(x=30,y=230)
                lb7.place(x=30,y=280)
                lb8.place(x=30,y=330)
                lb9.place(x=30,y=380)

                data='select *from lib where user_id ="'+user_val+'"'
                            #print(data)
                cur.execute(data)
                row=cur.fetchall()
                t=30
                for rows in row:
                    for i in range(1,9):
                        lbl1=Label(win5,text=rows[i],font=('bold'),width=15)
                        lbl1.place(x=250,y=t)
                        t+=50
                def exit1():
                    win5.destroy()
                    win4.deiconify()
                btn2=Button(win5,text='Exit',bg='green',fg='white',width=15,command=exit1)
                btn2.place(x=250,y=430)
                win5.mainloop()
            def edit():
                win6=Toplevel()
                win4.withdraw()
                win6.geometry('500x550')
                win6.title("Profiles")
                lb2=Label(win6, text="UserId",bg='black',fg='white',font=('bold'),width=15)
                lb3=Label(win6, text="Password",bg='black',fg='white',font=('bold'),width=15)
                lb4=Label(win6, text="Roll No",bg='black',fg='white',font=('bold'),width=15)
                lb5=Label(win6, text="Name",bg='black',fg='white',font=('bold'),width=15)
                lb6=Label(win6, text="Course",bg='black',fg='white',font=('bold'),width=15)
                lb7=Label(win6, text="Branch",bg='black',fg='white',font=('bold'),width=15)
                lb8=Label(win6, text="Semester",bg='black',fg='white',font=('bold'),width=15)
                lb9=Label(win6, text="Phone No",bg='black',fg='white',font=('bold'),width=15)

                            
  
                            #lb1.place(x=30,y=30)
                            
                lb2.place(x=30,y=30)
                lb3.place(x=30,y=80)
                lb4.place(x=30,y=130)
                lb5.place(x=30,y=180)
                lb6.place(x=30,y=230)
                lb7.place(x=30,y=280)
                lb8.place(x=30,y=330)
                lb9.place(x=30,y=380)

                data='select *from lib where user_id ="'+user_val+'"'
                            #print(data)
                cur.execute(data)
                row=cur.fetchall()
                            
                txt2=Entry(win6,width=15,bg='grey',fg='white',font=('bold'))
                txt2.insert(0,row[0][1])
                txt3=Entry(win6,width=15,bg='grey',fg='white',font=('bold'))
                txt3.insert(0,row[0][2])
                txt4=Entry(win6,width=15,bg='grey',fg='white',font=('bold'))
                txt4.insert(0,row[0][3])
                txt5=Entry(win6,width=15,bg='grey',fg='white',font=('bold'))
                txt5.insert(0,row[0][4])
                txt6=Entry(win6,width=15,bg='grey',fg='white',font=('bold'))
                txt6.insert(0,row[0][5])
                txt7=Entry(win6,width=15,bg='grey',fg='white',font=('bold'))
                txt7.insert(0,row[0][6])
                txt8=Entry(win6,width=15,bg='grey',fg='white',font=('bold'))
                txt8.insert(0,row[0][7])
                txt9=Entry(win6,width=15,bg='grey',fg='white',font=('bold'))
                txt9.insert(0,row[0][8])
                        #txt1.place(x=280,y=30)
                txt2.place(x=280,y=30)
                txt3.place(x=280,y=80)
                txt4.place(x=280,y=130)
                txt5.place(x=280,y=180)
                txt6.place(x=280,y=230)
                txt7.place(x=280,y=280)
                txt8.place(x=280,y=330)
                txt9.place(x=280,y=380)

                def submit():
                    data='update lib set user_id="'+str(txt2.get())+'",'+' password ="'+str(txt3.get())+'",'+'roll_no='+txt4.get()+','+'name="'+str(txt5.get())+'",'
                    data+='course="'+str(txt6.get())+'",'+'branch="'+str(txt7.get())+'",'+'semester="'+str(txt8.get())+'",'+'phone_no='+txt9.get()
                    data+=' where user_id="'+user_val+'"'
                    cur.execute(data)
                    db.commit()
                    lb1=Label(win6,text='you have sucessfully updated data',bg='green',fg='white')
                    lb1.place(x=260,y=400)
                def exit1():
                    win6.destroy()
                    win4.deiconify()
                button1=Button(win6,text="Submit",width=15,bg='green',fg='white',command=submit)
                button1.place(x=280,y=430)
                button2=Button(win6,text="Exit",width=15,bg='green',fg='white',command=exit1)
                button2.place(x=280,y=480)
                win6.mainloop()
            def exit2():
                win4.destroy()
                win3.deiconify()
            btn1=Button(win4,text='profile',bg='black',fg='white',width=15,command=profile)
            btn1.place(x=30,y=10)
            btn2=Button(win4,text='Edit profile',bg='black',fg='white',width=15,command=edit)
            btn2.place(x=30,y=60)
            btn3=Button(win4,text='Exit',width=15,bg='black',fg='white',command=exit2)
            btn3.place(x=30,y=110)
            win4.mainloop()
                    
        def help():
            win31=Toplevel()
            win3.withdraw()
            win31.geometry('550x400')
            lbl=Label(win31, text="For any query you can send us mail",font=("algerian",20),fg="green")
            lbl.place(x=20,y=20)
            lb2=Label(win31, text="SENDER MAIL",font=("algerian",18),fg="green")
            lb2.place(x=70,y=70)
            tx1=Entry(win31,width=20,bg="black",fg='white',font=("bold"))
            tx1.place(x=250,y=80)
            tx2=Entry(win31,show='*',width=20,bg="black",fg='white',font=("bold"))
            tx2.place(x=250,y=130)
            lb4=Label(win31,text="Password",font=("algerian",18),fg="green")
            lb4.place(x=70,y=120)
            lb5=Label(win31,text="Enter mail",font=("algerian",18),fg="green")
            lb5.place(x=70,y=170)
            tx4=Entry(win31,width=20,bg="black",fg='white',font=("bold"))
            tx4.place(x=250,y=180)


                

            def sendfun():
                sender=str(tx1.get())
                pasword=str(tx2.get())
                msg=str(tx4.get())
                print(sender,pasword,msg)
                mail=smtplib.SMTP('smtp.gmail.com',587)
                mail.starttls()
                mail.login(sender,pasword)
                            #sender=sender
                recipient='to:tushargargcse@gmail.com'
                content=msg
                mail.sendmail(sender,recipient,content)
                print("send")
            def exit5():
                win31.destroy()
                win3.deiconify()
            bit=Button(win31,text="Send",fg='white',bg='green',font=('bold'),width=15,command=sendfun)
            bit.place(x=280,y=250)
            bit1=Button(win31,text="Exit",fg='white',bg='green',font=('bold'),width=15,command=exit5)
            bit1.place(x=280,y=300)

        def edit():
            wind1=Toplevel()
            win3.withdraw()
            wind1.geometry('500x400')
            wind1.title('Add/Remove Data')
            data='select *from lib where user_id ="'+user_val+'"'
            lb2=Label(wind1, text="BookID",bg='black',fg='white',font=('bold'),width=15)
            lb3=Label(wind1, text="Issue Date",bg='black',fg='white',font=('bold'),width=15)
            lb4=Label(wind1, text="Expire Date",bg='black',fg='white',font=('bold'),width=15)
            lb5=Label(wind1, text="Return Date",bg='black',fg='white',font=('bold'),width=15)
            lb6=Label(wind1, text="Fine",bg='black',fg='white',font=('bold'),width=15)

            lb2.place(x=30,y=30)
            lb3.place(x=30,y=80)
            lb4.place(x=30,y=130)
            lb5.place(x=30,y=180)
            lb6.place(x=30,y=230)
            cur.execute(data)
            row=cur.fetchall()
            txt2=Entry(wind1,width=15,bg='grey',fg='white',font=('bold'))
            txt2.insert(0,row[0][9])
            txt3=Entry(wind1,width=15,bg='grey',fg='white',font=('bold'))
            txt3.insert(0,row[0][10])
            txt4=Entry(wind1,width=15,bg='grey',fg='white',font=('bold'))
            txt4.insert(0,row[0][11])
            txt5=Entry(wind1,width=15,bg='grey',fg='white',font=('bold'))
            txt5.insert(0,row[0][12])
            txt6=Entry(wind1,width=15,bg='grey',fg='white',font=('bold'))
            txt6.insert(0,row[0][13])

            txt2.place(x=280,y=30)
            txt3.place(x=280,y=80)
            txt4.place(x=280,y=130)
            txt5.place(x=280,y=180)
            txt6.place(x=280,y=230)
            def submit():
                data='update lib set  bookID="'+str(txt2.get())+'",'+' book_IsuedId ="'+str(txt3.get())+'",'+' date="'+str(txt4.get())+'",'+' expire_date="'+str(txt5.get())+'",'
                data+='fine='+txt6.get()
                data+=' where user_id="'+user_val+'"'
                cur.execute(data)
                db.commit()
                lb7=Label(wind1,text='you have succesfully update data',bg='green',fg='white',width=40)
                lb7.place(x=240,y=260)
            def exit1():
                wind1.destroy()
                win3.deiconify()
            button1=Button(wind1,text="Submit",width=15,bg='green',fg='white',command=submit)
            button1.place(x=280,y=300)
            button2=Button(wind1,text="Exit",width=15,bg='green',fg='white',command=exit1)
            button2.place(x=280,y=360)
                
            wind1.mainloop()    
            
                   
        def show():
            wind2=Toplevel()
            win3.withdraw()
            wind2.geometry('400x400')
            wind2.title('Add data')
            
            lb2=Label(wind2, text="BookID",bg='black',fg='white',font=('bold'),width=15)
            lb3=Label(wind2, text="Issue date",bg='black',fg='white',font=('bold'),width=15)
            lb4=Label(wind2, text="Expire date",bg='black',fg='white',font=('bold'),width=15)
            lb5=Label(wind2, text="Return date",bg='black',fg='white',font=('bold'),width=15)
            lb6=Label(wind2, text="Fine",bg='black',fg='white',font=('bold'),width=15)

            lb2.place(x=30,y=30)
            lb3.place(x=30,y=80)
            lb4.place(x=30,y=130)
            lb5.place(x=30,y=180)
            lb6.place(x=30,y=230)
            data='select *from lib where user_id ="'+user_val+'"'
            cur.execute(data)
            row=cur.fetchall()
            t=30
            for rows in row:
                for i in range(9,14):
                    lbl1=Label(wind2,text=rows[i],font=('bold'),width=15)
                    lbl1.place(x=250,y=t)
                    t+=50
            def exit1():
                wind2.destroy()
                win3.deiconify()
            btn1=Button(wind2,text='Exit',width=15,bg='black',fg='white',command=exit1)
            btn1.place(x=250,y=300)
            wind2.mainloop() 



        
        def exit1():
            win3.destroy()
            win.deiconify()
                    

        btn=Button(win3,text="Help",fg='white',bg='black',width=15,command=help)   
        btn.place(x=20,y=200)
        btn1=Button(win3,text='Home',bg="black",fg="white",width=15,command=home)
        btn1.place(x=20,y=20)
        btn2=Button(win3,text='Edit data',bg="black",fg="white",width=15,command=edit)
        btn2.place(x=20,y=80)
        btn3=Button(win3,text='Show data',bg="black",fg="white",width=15,command=show)
        btn3.place(x=20,y=140)
        btn5=Button(win3,text='Exit',bg="black",fg="white",width=15,command=exit1)
        btn5.place(x=20,y=260)
        win3.mainloop()
    


                    
def create():
    
    win1=Toplevel()
    win.withdraw()
    win1.geometry('600x600')
    win1.title("Create accoumt")
   # lb1=Label(win1, text="S.no",bg='white',font=('bold'),width=15)
    lb2=Label(win1, text="UserId",bg='black',fg='white',font=('bold'),width=15)
    lb3=Label(win1, text="password",bg='black',fg='white',font=('bold'),width=15)
    
    lb4=Label(win1, text="Roll No",bg='black',fg='white',font=('bold'),width=15)
    lb5=Label(win1, text="Name",bg='black',fg='white',font=('bold'),width=15)
    lb6=Label(win1, text="Course",bg='black',fg='white',font=('bold'),width=15)
    lb7=Label(win1, text="Branch",bg='black',fg='white',font=('bold'),width=15)
    lb8=Label(win1, text="Semester",bg='black',fg='white',font=('bold'),width=15)
    lb9=Label(win1, text="Phone No",bg='black',fg='white',font=('bold'),width=15)
    
  
    #lb1.place(x=30,y=30)
    lb2.place(x=30,y=30)
    lb3.place(x=30,y=80)
    lb4.place(x=30,y=130)
    lb5.place(x=30,y=180)
    lb6.place(x=30,y=230)
    lb7.place(x=30,y=280)
    lb8.place(x=30,y=330)
    lb9.place(x=30,y=380)
    
   # txt1=Entry(win1,width=15,font=('bold'))
    txt2=Entry(win1,width=15,bg='grey',fg='white',font=('bold'))
    txt3=Entry(win1,width=15,bg='grey',fg='white',font=('bold'))
    txt4=Entry(win1,width=15,bg='grey',fg='white',font=('bold'))
    txt5=Entry(win1,width=15,bg='grey',fg='white',font=('bold'))
    txt6=Entry(win1,width=15,bg='grey',fg='white',font=('bold'))
    txt7=Entry(win1,width=15,bg='grey',fg='white',font=('bold'))
    txt8=Entry(win1,width=15,bg='grey',fg='white',font=('bold'))
    txt9=Entry(win1,width=15,bg='grey',fg='white',font=('bold'))

    #txt1.place(x=280,y=30)
    txt2.place(x=280,y=30)
    txt3.place(x=280,y=80)
    txt4.place(x=280,y=130)
    txt5.place(x=280,y=180)
    txt6.place(x=280,y=230)
    txt7.place(x=280,y=280)
    txt8.place(x=280,y=330)
    txt9.place(x=280,y=380)
    
    
    def submit():
        cur=db.cursor()
        cur.execute('select *from lib')
        sql="insert into lib values(null,'"
        sql+=str(txt2.get())+"','"+str(txt3.get())+"',"+str(txt4.get())+",'"
        sql+=str(txt5.get())+"','"+str(txt6.get())+"','"+str(txt7.get())+"','"+str(txt8.get())+"',"+str(txt9.get())
        sql+=',"a","b","c","d",1'
        sql+=")"        
        cur.execute(sql)
        db.commit()
        lb7=Label(win1,text='you have succesfully sign up',bg='green',fg='white',width=40)
        lb7.place(x=350,y=430)
        
    def exit1():
        win1.destroy()
        win.deiconify()
        
    btn1=Button(win1,text="submit",bg="green",fg="white",font=("bold"),width=15,command=submit)
    btn1.place(x=400,y=480)
    btn2=Button(win1,text="Exit",bg="green",fg="white",font=("bold"),width=15,command=exit1)
    btn2.place(x=400,y=530)
    win1.mainloop()
    

def exit():
    win.destroy()

#exit2=PhotoImage(file="C:\\Users\\Dewan\\Desktop\\is.png")
btn1=Button(win,text="Login",fg='white',bg='green',font=('bold'),width=15,command=login)
btn2=Button(win,text="Create Account",fg='white',bg='green',font=('bold'),width=15,command=create)
btn3=Button(win,text="Exit",fg='white',bg='green',font=('bold'),width=15,command=exit)

btn1.place(x=650,y=400)
btn2.place(x=650,y=450)
btn3.place(x=650,y=500)

win.mainloop()
