from tkinter import *
from tkinter import messagebox
import math
from PIL import ImageTk, Image
import vlc
import os

from gtts import gTTS 

class Fitness:
    def generate(self):
                if(self.Name.get()=='' and self.Age.get()=='' and self.Male.get()==0 and self.Female.get()==0 and self.Weight.get()=='' and self.Height.get()==''):
                    messagebox.showerror('error','enter your details')
                if(self.Name.get()==''):
                    messagebox.showerror('error','enter your name')
                elif(self.Age.get()==''):
                    messagebox.showerror('error','enter your Age')
                elif(self.Male.get()==0 and self.Female.get()==0):
                    messagebox.showerror('error','Mark your gender')    
                elif(self.Male.get()+self.Female.get()>1):
                    messagebox.showerror('error','Mark not more than one CHOICE OF GENDER')
                elif(self.Height.get()==''):
                    messagebox.showerror('error','Enter your Height')
                elif(self.Weight.get()==''):
                    messagebox.showerror('error','Enter your Weight')    
                else:
                    self.kl.pack_forget()
                    self.k2=Frame(self.root,height=15)
                    self.k2.pack()
                    self.j()
                    label1 = Label(self.k2, text="FITNESS REPORT",font=("Arial Bold", 15),bg="skyblue",bd=10,relief="raise")
                    label1.grid(row=0,column=1)
                    label2 = Label(self.k2, text="Name",font=("Arial Bold", 15),width=15,bg="skyblue",bd=10,relief="raise")
                    label2.grid(row=1)
                    label3 = Label(self.k2, text=" :-  "+self.Name.get(),font=("Arial Bold", 15))
                    label3.grid(row=1,column=1)
                    label4 = Label(self.k2, text="Age",font=("Arial Bold", 15),width=15,bg="skyblue",bd=10,relief="raise")
                    label4.grid(row=2)
                    label5 = Label(self.k2, text=":-  "+self.Age.get(),font=("Arial Bold", 15))
                    label5.grid(row=2,column=1)
                    label6 = Label(self.k2, text="Gender",font=("Arial Bold", 15),width=15,bg="skyblue",bd=10,relief="raise")
                    label6.grid(row=3)
                    if(self.Male.get()==1):
                        label7 = Label(self.k2, text=":-  Male",font=("Arial Bold", 15))
                        label7.grid(row=3,column=1)
                    else:
                        label7 = Label(self.k2, text=":-  Female",font=("Arial Bold", 15))
                        label7.grid(row=3,column=1)
                    label8 = Label(self.k2 , text="WEIGHT",font=("Arial Bold",15),width=15,bg="skyblue",bd=10,relief="raise")
                    label8.grid(row=4)
                    label9 = Label(self.k2, text=":-  "+self.Weight.get(),font=("Arial Bold", 15))
                    label9.grid(row=4,column=1)
                    label10 = Label(self.k2, text="HEIGHT",font=("Arial Bold", 15),width=15,bg="skyblue",bd=10,relief="raise")
                    label10.grid(row=5)
                    label11 = Label(self.k2, text=":-  "+self.Height.get(),font=("Arial Bold", 15))
                    label11.grid(row=5,column=1)
                    label12 = Label(self.k2, text="BODY MASS INDEX",font=("Arial Bold", 15),width=15,bg="skyblue",bd=10,relief="raise")
                    label12.grid(row=6)
                    label13 = Label(self.k2, text="        :-  "+self.S_()+" "+self.S(),font=("Arial Bold", 15))
                    label13.grid(row=6,column=1)
                    label14 = Label(self.k2 , text="BLOODPRESSURE",font=("Arial Bold",15),width=15,bg="skyblue",bd=10,relief="raise")
                    label14.grid(row=7)
                    label15 = Label(self.k2, text="    :-  "+self.BP.get()+" "+self.B(),font=("Arial Bold", 15))
                    label15.grid(row=7,column=1)
                    label16 = Label(self.k2 , text="PULSE RATE",font=("Arial Bold",15),width=15,bg="skyblue",bd=10,relief="raise")
                    label16.grid(row=8)
                    label17 = Label(self.k2, text="    :-  "+self.PR.get()+" "+self.P(),font=("Arial Bold", 15))
                    label17.grid(row=8,column=1)
                    label18 = Label(self.k2 , text="RBC COUNT",font=("Arial Bold",15),width=15,bg="skyblue",bd=10,relief="raise")
                    label18.grid(row=9)
                    label19 = Label(self.k2, text="    :-  "+self.RBC.get()+" "+self.R(),font=("Arial Bold", 15))
                    label19.grid(row=9,column=1)
                    label20 = Label(self.k2 , text="WBC COUNT",font=("Arial Bold",15),width=15,bg="skyblue",bd=10,relief="raise")
                    label20.grid(row=10)
                    label21 = Label(self.k2, text="    :-  "+self.WBC.get()+" "+self.W(),font=("Arial Bold", 15))
                    label21.grid(row=10,column=1)
                    label22 = Label(self.k2 , text="PLATELETS",font=("Arial Bold",15),width=15,bg="skyblue",bd=10,relief="raise")
                    label22.grid(row=11)
                    label23 = Label(self.k2, text="    :-  "+self.PL.get()+" "+self.PA(),font=("Arial Bold", 15))
                    label23.grid(row=11,column=1)
                    label24 = Label(self.k2 , text="HEMOGLOBIN",font=("Arial Bold",15),width=15,bg="skyblue",bd=10,relief="raise")
                    label24.grid(row=12)
                    label25 = Label(self.k2, text="    :-  "+self.HB.get()+" "+self.H(),font=("Arial Bold", 15))
                    label25.grid(row=12,column=1)
                    label26 = Label(self.k2 , text="URIC ACID",font=("Arial Bold",15),width=15,bg="skyblue",bd=10,relief="raise")
                    label26.grid(row=13)
                    label27 = Label(self.k2, text="    :-  "+self.UA.get()+" "+self.U(),font=("Arial Bold", 15))
                    label27.grid(row=13,column=1)
                    label28 = Label(self.k2 , text="CHOLESTOROL",font=("Arial Bold",15),width=15,bg="skyblue",bd=10,relief="raise")
                    label28.grid(row=14)
                    label29 = Label(self.k2, text="    :-  "+self.C.get()+" "+self.CH(),font=("Arial Bold", 15))
                    label29.grid(row=14,column=1)
                    button3 = Button(self.k2 , text="QUIT",command=self.root.destroy,font=("Arial Bold",15),bg="skyblue",bd=10,relief="raise")
                    button3.grid(row=14,column=2)
    #BMI calculation
    def S_(self):
         w=float(self.Weight.get())
         h=float(self.Height.get())
         a=(w/(h*h))
         bi=math.floor(a)
         bmi=str(bi)
         return bmi               
    def S(self):
         w=float(self.Weight.get())
         h=float(self.Height.get())
         a=(w/(h*h))
         bi=math.floor(a)
         if bi < 18.5:
             
             return "UNDERWEIGHT"
             
         else:
             if bi>=18.5 and bi<=24.5:
                return "HEALTHY"
             else:
                 if bi>=24.5 and bi <=30:
                    return "OVERWEIGHT"
                 else:
                    return "OBESE"
    #blood pressure
    def B(self):
        if(self.BP.get()==''):
           return ''
        else:
            b=int(self.BP.get())
            if b<=90:
                return "Low"
            else:
                if b>90 and b<=120:
                    return "Normal"
                else:
                    if b>120 and b<=130:
                        return "Elevated"
                    else:
                        if b>130 and b<=140:
                            return "High"
                        else:
                            return "VeryHigh"
                        
    #pulse rate
    def P(self):
        if(self.PR.get()==''):
            return ''
        else:
            p=int(self.PR.get())
            if p>=54 and p <=60:
                self.j()
                return "athlete"
            else:
                if p>60 and p<=65:
                    return "Excellent"
                else:
                    if p>65 and p<=70:
                        return "good"
                    else:
                        if p>70 and p<=75:
                            return "AboveAverage"
                        else:
                            if p>75 and p<=85:
                                return "Average"
                            else:
                                return "Poor"
                        
    #RBC count
    def R(self):
        if(self.RBC.get()==''):
            return ''
        else:
            r=float(self.RBC.get())
            a=int(self.Age.get())
            if r>=4.7 and r<=6.1 or a>18 and a<=24:
                return "NORMAL"
            else:
                if r<4.7 or a>18 and a<=24:
                    return "LOW"
                else:
                    if r>6.1 or a>18 and a<=24:
                        return "HIGH"
                    else:
                        if r>3.8 and r<=5.5 or a>13 and a<=18:
                            return "NORMAL"
                        else:
                            if r<3.8 or a>13 and a<=18:
                                return "LOW"
                            else:
                                if r>5.5 or a>13 and a<=18:
                                    return "HIGH"
                                else:
                                    if r>4.4 and r<5.8 or a<13:
                                        return "NORMAL"
                                    else:
                                        if r<4.4 or a<13:
                                            return "LOW"
                                        else:
                                            if r>5.6 or a<13:
                                                return "HIGH"
    #WBC count
    def W(self):
        if(self.WBC.get()==''):
            return ''
        else:
            w=float(self.WBC.get())
            a=int(self.Age.get())
            if w>=4.5 and w<=10 or a>18 and a<=24:
                return "NORMAL"
            else:
                if w<4.5 or a>18 and a<=24:
                    return "LOW"
                else:
                    if w>10 or a>18 and a<=24:
                        return "HIGH"
                    else:
                        if w>4.5 and w<=10 or a>13 and a<=18:
                            return "NORMAL"
                        else:
                            if w<4.5 or a>13 and a<=18:
                                return "LOW"
                            else:
                                if w>10 or w>13 and a<=18:
                                    return "HIGH"
                                else:
                                    if w>4 and w<10 or a<13:
                                        return "NORMAL"
                                    else:
                                        if w<4 or a<13:
                                            return "LOW"
                                        else:
                                            if w>10 or a<13:
                                                return "HIGH"

    #platelets                                
    def PA(self):
        if(self.PL.get()==''):
            return ''
        else:
            pl=float(self.PL.get())
            if pl>150 and pl<400:
                return "normal"
            else:
                if pl<150:
                    return "low"
                else:
                    if pl>400:
                        return "high"
                
    #Hemoglobin
    def H(self):
        if(self.HB.get()==''):
            return ''
        else:
            h=float(self.HB.get())
            a=int(self.Age.get())
            if h>=12 and h<=16 or a>18 and a<=24:
                return "NORMAL"
            else:
                if h<12 or a>18 and a<=24:
                    return "LOW"
                else:
                    if h>16 or a>18 and a<=24:
                        return "HIGH"
                    else:
                        if h>11 and h<=13 or a>13 and a<=18:
                            return "NORMAL"
                        else:
                            if h<11 or a>13 and a<=18:
                                return "LOW"
                            else:
                                if h>13 or a>13 and a<=18:
                                    return "HIGH"
                                else:
                                    if h>11 and h<15 or a<13:
                                        return "NORMAL"
                                    else:
                                        if h<11 or a<13:
                                            return "LOW"
                                        else:
                                            if h>15 or a<13:
                                             return "HIGH"
    #Uric acid
    def U(self):
        if(self.UA.get()==''):
            return ''
        else:
            u=float(self.UA.get())
            if u>3.4 and u<7.0:
                return "NORMAL"
            else:
                if u>7.0:
                    return "HIGH"
                else:
                    return "LOW"

    #cholesterol
    def CH(self):
        if(self.C.get()==''):
            return ''
        else:
            c=int(self.C.get())
            if c>130 and c<=160:
                return "HIgH"
            else:
                if c>160:
                    return "VeryHigh"
                else:
                    if c>=100 and c<130:
                        return "Average"
                    else:
                        return "NORMAL"
    def page(self):
        self.Height=StringVar()
        self.Weight=StringVar()
        self.Name=StringVar()
        self.Age=StringVar()
        self.Male=IntVar()
        self.Female=IntVar()
        self.BP=StringVar()
        self.PR=StringVar()
        self.RBC=StringVar()
        self.WBC=StringVar()
        self.PL=StringVar()
        self.HB=StringVar()
        self.C=StringVar()
        self.UA=StringVar()
        
        if(self.username.get()=='user' and self.password.get()=='123'):
            messagebox.showinfo('info','successfully logged in')
            self.lf.pack_forget()
            self.kl=Frame(self.root,height=15)
            self.kl.pack()
            self.ac()
            

            label1 = Label(self.kl, text="FITNESS CALCULATOR",font=("Arial Bold", 15),bg="skyblue",bd=10,relief="raise")
            label1.grid(row=0,column=1)
            label13 = Label(self.kl , text="Name",font=("Arial Bold",15),bg="skyblue",width=12,bd=10,relief="raise")
            entry13=Entry(self.kl,textvariable=self.Name)
            label13.grid(row=1)
            entry13.grid(row=1,column=1)
            label14 = Label(self.kl , text="Age",font=("Arial Bold",15),bg="skyblue",width=12,bd=10,relief="raise")
            entry14=Entry(self.kl,textvariable=self.Age)
            label14.grid(row=2)
            entry14.grid(row=2,column=1)
            label5 = Label(self.kl , text="Gender",font=("Arial Bold",15),bg="skyblue",width=12,bd=10,relief="raise")
            label5.grid(row=3)
            radio1 = Checkbutton(self.kl , text="Male",variable=self.Male,font=("Arial Bold",15),bg="skyblue")
            radio2 = Checkbutton(self.kl , text="Female",variable=self.Female,font=("Arial Bold",15),bg="skyblue")
            radio1.grid(row=3,column=1)
            radio2.grid(row=3,column=2)
            label2 = Label(self.kl , text="Height(M)",font=("Arial Bold",15),bg="skyblue",width=12,bd=10,relief="raise")
            entry2=Entry(self.kl,textvariable=self.Height)
            label2.grid(row=4)
            entry2.grid(row=4,column=1)
            label3 = Label(self.kl , text="Weight(KG)",font=("Arial Bold",15),bg="skyblue",width=12,bd=10,relief="raise")
            entry3=Entry(self.kl,textvariable=self.Weight)
            label3.grid(row=5)
            entry3.grid(row=5,column=1)
            label4 = Label(self.kl , text="BloodPressure",font=("Arial Bold",15),bg="skyblue",width=12,bd=10,relief="raise")
            entry4=Entry(self.kl,textvariable=self.BP)
            label4.grid(row=6)
            entry4.grid(row=6,column=1)
            label6 = Label(self.kl , text="PULSE RATE",font=("Arial Bold",15),bg="skyblue",width=12,bd=10,relief="raise")
            entry6=Entry(self.kl,textvariable=self.PR)
            label6.grid(row=7)
            entry6.grid(row=7,column=1)
            label7 = Label(self.kl , text="RBC COUNT",font=("Arial Bold",15),bg="skyblue",width=12,bd=10,relief="raise")
            entry7=Entry(self.kl,textvariable=self.RBC)
            label7.grid(row=8)
            entry7.grid(row=8,column=1)
            label8 = Label(self.kl , text="WBC COUNT",font=("Arial Bold",15),bg="skyblue",width=12,bd=10,relief="raise")
            entry8=Entry(self.kl,textvariable=self.WBC)
            label8.grid(row=9)
            entry8.grid(row=9,column=1)
            label9 = Label(self.kl , text="PLATELETS",font=("Arial Bold",15),bg="skyblue",width=12,bd=10,relief="raise")
            entry9=Entry(self.kl,textvariable=self.PL)
            label9.grid(row=10)
            entry9.grid(row=10,column=1)
            label10 = Label(self.kl , text="HEMOGLOBIN",font=("Arial Bold",15),bg="skyblue",width=12,bd=10,relief="raise")
            entry10=Entry(self.kl,textvariable=self.HB)
            label10.grid(row=11)
            entry10.grid(row=11,column=1)
            label11 = Label(self.kl , text="URIC ACID",font=("Arial Bold",15),bg="skyblue",width=12,bd=10,relief="raise")
            entry11=Entry(self.kl,textvariable=self.UA)
            label11.grid(row=12)
            entry11.grid(row=12,column=1)
            label12 = Label(self.kl , text="CHOLESTOROL",font=("Arial Bold",15),bg="skyblue",width=12,bd=10,relief="raise")
            entry12=Entry(self.kl,textvariable=self.C)
            label12.grid(row=13)
            entry12.grid(row=13,column=1)
            btn = Button(self.kl, text="Generate Report",command=self.generate,font=("Arial Bold",12),bg="skyblue",width=13,activebackground="purple",bd=10,relief="raise")
            btn.grid(column=2, row=14)
        else:
            if(self.username.get()=='' or self.password.get()==''):
                messagebox.showerror('error','enter complete details')
            else:
                messagebox.showerror('error','wrong username or password')
    def login(self):
            self.lf=Frame(self.root,padx=10,pady=10)
            self.lf.pack()
            self.username=StringVar()
            self.password=StringVar()
            Label(self.lf,text='Enter Username: ',font=('',18),bg="skyblue",bd=10,relief="raise").grid(sticky=W)
            Entry(self.lf,bd = 5,textvariable=self.username,font = ('',15)).grid(row=0,column=2)
            Label(self.lf,text='Enter password: ',bg="skyblue",bd=10,relief="raise",font=('',18)).grid(sticky=W)
            Entry(self.lf,bd = 5,textvariable=self.password,font = ('',15),show = '*').grid(row=1,column=2)
            Button(self.lf,text = 'Login',bg="skyblue",bd=10,relief="raise",width=11,activebackground="purple",font=("Arial Bold",18),command=self.page).grid(row=2,column=2)
    def main_page(self):
            self.root = Tk()
            self.root.title("Welcome to Fitness Calculator of a person")
            self.root.geometry("725x725")
            img = ImageTk.PhotoImage(Image.open(r"C:\Users\RJKIRAN\desktop\gym.jpg"))
 
            self.l = Label(self.root,image=img)
            self.l.place(x=0,y=0)

            self.login()
            
            self.root.mainloop()
           

    def ac(self):
        '''mytext ='Welcome to Fitness Calculator.Please enter your details'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("welcome.mp3") 
        os.system("mpg321 welcome.mp3")'''
        import python-vlc as vlc 
        
        p = vlc.MediaPlayer("welcome.mp3")
        
        p.play()
        
    def j(self):
       '''text ='Thank you for your details.This is your fitness report'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("report.mp3") 
        os.system("mpg321 report.mp3")'''
       import vlc 
        
       p = vlc.MediaPlayer("report.mp3")
        
       p.play()
            

obj=Fitness()
obj.main_page()
