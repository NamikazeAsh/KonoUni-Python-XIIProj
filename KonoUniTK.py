
from matplotlib import pyplot as plt 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
    
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="namisenpaiisagod")
mycur=mydb.cursor()

#mycur.execute("create table namiboi(appid int not null auto_increment primary key,fname char(50),name char(50),lname char(50),courses char(200),board char(50),marks int(5),sports char(4))")
#mycur.execute("truncate namiboi")
#mycur.execute("drop table namiboi")

mycur.execute("truncate table namiboi")

nami=Tk()
nami.config(bg="light gray")
nami.geometry("700x700")
nami.title("Konoha University's Main Page")
   
logo=PhotoImage(file="namilogo.png")
intrologo=Label(nami,image=logo,bd=0)
intrologo.pack()

introlabel=Label(nami,text="✧ Welcome to Konoha University ✧",font=("Impact",25),bg="darkslategray",fg="azure3")
introlabel.pack(fill=X)

    ######################################################################################################################################
def namigui():
    
    #By Ashwin Satish
    
    nami.iconify()
    
    cocur=Toplevel()
    cocur.title("Konoha University's Co-Curricular Form")
    cocur.geometry("700x900")
    cocur.configure(background="cornsilk4")
    
    ######################################################################################################################################
    
    ######################################################################################################################################
    
    '''
    background_image=PhotoImage(file="BG Pour Le Namiboi.png")
    backgroun=Label(cocur, image=background_image)
    backgroun.place(x=0, y=0, relwidth=1, relheight=1)
    '''
    
    ######################################################################################################################################
    
    
    logo=PhotoImage(file="namitkinter.png")
    headd=Label(cocur,image=logo,bd=0,bg="cornsilk4")
    headd.grid(row=0,column=0,padx=10,pady=10,columnspan=4)  
    
    
    ######################################################################################################################################
    
    '''
    cocur.title("Konoha University's Admission Form")
    head = Label(cocur,text="Konoha University",font=("Lucida Calligraphy",40,'bold'),relief=FLAT,justify=CENTER,bg="cornsilk4")
    head.configure(fg="Green",)
    head.grid(column=0,row=0,padx=10, pady=10,columnspan=2)
    '''
    
    ######################################################################################################################################
    
    fname=Label(cocur,text="First Name: ",font=("Adobe Fan Heiti Std B",10),bg="cornsilk4")
    
    fname.grid(row=1,column=0,sticky="E")
    fnametxtf= Entry(cocur,width=30,font=("MS Gothic",10),relief=GROOVE)
    fnametxtf.grid(row=1,column=1,padx=10, pady=10,sticky="W")
    
    ######################################################################################################################################
    
    mname=Label(cocur,text="Middle Name: ",font=("Adobe Fan Heiti Std B",10))
    mname.configure(background="cornsilk4")
    mname.grid(row=2,column=0,sticky="E")
    mnametxtf=Entry(cocur,width=30,font=("MS Gothic",10),relief=GROOVE)
    mnametxtf.grid(row=2,column=1,padx=10, pady=10,sticky="W")
    
    ######################################################################################################################################
    
    lname=Label(cocur,text="Last Name: ",font=("Adobe Fan Heiti Std B",10))
    lname.configure(background="cornsilk4")
    lname.grid(row=3,column=0,sticky="E")
    lnametxtf= Entry(cocur,width=30,font=("MS Gothic",10),relief=GROOVE)
    lnametxtf.grid(row=3,column=1,padx=10, pady=10,sticky="W")
    
    ######################################################################################################################################
    
    courses=["Bachelor of Sacred Theology","Bachelor of Science in Agriculture","Bachelor of Science in Aquatic Resources and Technology","Bachelor of Science in Biomedical Engineering",
    "Bachelor of Science in Cardiopulmonary Therapy",
    "Bachelor of Science in Human Biology",
    "Bachelor of Science in Information Technology",
    "Bachelor of Science in Law",
    "Bachelor of Science in Nursing","Bachelor of Science in Public Health","Bachelor of Science in Respiratory Care","Bachelors Degree Examination for Self-Education","Self-Taught Higher Education Examinations","Bachelor of Social Science","Bachelor of Social Services","Bachelor of Software Engineering",]
    
    ccombolabel=Label(cocur,text="Select A Course: ",font=("Adobe Fan Heiti Std B",10))
    ccombolabel.configure(background="cornsilk4")
    ccombolabel.grid(row=4,column=0,sticky="E")
    ccombo =ttk.Combobox(cocur,width=40,font=("MS Gothic",10),justify="center")
    ccombo['values']=courses
    ccombo.grid(row=4,column=1,padx=10, pady=10,sticky="W")
    
    ######################################################################################################################################
    
    boards=["CBSE","ICSE","IB","HSC/State Board","CISCE","TBSE"]
    boardlabel=Label(cocur,text="Select The Board From Which You Passed: ",font=("Adobe Fan Heiti Std B",10))
    boardlabel.configure(background="cornsilk4")
    boardlabel.grid(row=5,column=0,sticky="E")
    boardcombo=ttk.Combobox(cocur,width=40,font=("MS Gothic",10),justify="center")
    boardcombo['values']=boards
    boardcombo.grid(row=5,column=1,padx=10, pady=10,sticky="W")
    
    ######################################################################################################################################
    
    mobt=Label(cocur,text="Marks Obtained (In %): ",font=("Adobe Fan Heiti Std B",10))
    mobt.configure(background="cornsilk4")
    mobt.grid(row=6,column=0,sticky="E")
    mobte=Entry(cocur,width=30,font=("MS Gothic",10),relief=GROOVE)
    mobte.grid(row=6,column=1,padx=10, pady=10,sticky="W")
  
    
    ######################################################################################################################################
    
    athletica=Label(cocur,text="Attended A Zonal Level or Higher [Any Sport]:",font=("Adobe Fan Heiti Std B",10))
    athletica.configure(background="cornsilk4")
    athletica.grid(row=7,column=0,padx=10, pady=10)
    
    a=StringVar()
    
    frame=Frame(cocur,bg="cornsilk4")
    frame.grid(row=7,column=1,sticky="W")
    
    a1=Radiobutton(frame,text="Yes",value="Yes",variable=a,bg="cornsilk4")
    a1.grid(row=7,column=1,padx=10, pady=10)
    a1.deselect()
    
    a2=Radiobutton(frame,text="No",value="No",variable=a,bg="cornsilk4")
    a2.grid(row=7,column=2,padx=10, pady=10)
    a2.deselect()
    
    ######################################################################################################################################
    
    cets=Label(cocur,text="Common Entrance Test [CET] Score:",font=("Adobe Fan Heiti Std B",10))
    applicationide=Entry(cocur,width=30,font=("MS Gothic",10),relief=GROOVE)
    cets.grid(row=8,column=0,padx=10,pady=10,sticky="E")
    cets.configure(background="cornsilk4")
    applicationide.grid(row=8,column=1,padx=10,pady=10,sticky="W")
    
    ######################################################################################################################################
    
    def clear():
        fnametxtf.delete(first=0,last=100)
        mnametxtf.delete(first=0,last=100)
        lnametxtf.delete(first=0,last=100)
        ccombo.delete(first=0,last=100)
        boardcombo.delete(first=0,last=100)
        mobte.delete(first=0,last=100)
        applicationide.delete(first=0,last=100)
        
    clearbutton = Button(cocur,text="【Clear Entries】",command=clear,width=40,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),cursor="circle")
    clearbutton.grid(row=10,column=0,padx=10, pady=10,sticky="E")
    
    ######################################################################################################################################
    
    def inserto():
        st="insert into namiboi(fname,name,lname,courses,board,marks,Sports,cet)values(%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(fnametxtf.get(),mnametxtf.get(),lnametxtf.get(),ccombo.get(),boardcombo.get(),mobte.get(),a.get(),applicationide.get())
        mycur.execute(st,val)
        mydb.commit()
    
    insertob=Button(cocur,text="【Submit】",command=inserto,width=40,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),cursor="circle")
    insertob.grid(row=12,column=0,padx=10, pady=10,sticky="E")
    
    ######################################################################################################################################
    
    def selecto():
        dispappy=Toplevel(bg="darkslategray")
        dispappy.geometry("600x500")
        dispappy.title("Table's Data")
        mycur.execute("select * from namiboi")
        results=mycur.fetchall()
        
        dispoopy=Label(dispappy,text="Data From The Table",fg="gray25",bg="azure3",font=("AR CENA",45))
        dispoopy.pack(fill=X)
        
        for x in results:
            print("****************************************************************************************")
            print(x)
            print("****************************************************************************************")
        
            dispoppy=Label(dispappy,text=x,font=("Impact",13),fg="azure3",bg="darkslategray")
            dispoppy.pack(fill=Y)
        
        def disexit():
            dispappy.destroy()
        
        disexit=Button(dispappy,text="Ok",command=disexit,width=20,height=2,relief=RIDGE,bg="honeydew3",fg="gray25",cursor="circle",font=("Impact",13))
        disexit.pack(side=BOTTOM,pady=30)
            
       
        
    
    selectb=Button(cocur,text="【Show Data】",command=selecto,width=40,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),cursor="circle")
    selectb.grid(row=12,column=1)
    
    ######################################################################################################################################
    
    def update():
        
        updateframe=Frame(cocur,bg="cornsilk4")
        updateframe.grid(row=18,column=1)
        admnul=Label(updateframe,text="Application No:",font=("Adobe Fan Heiti Std B",10),width=15,bg="cornsilk4")
        admnul.grid(row=18,column=0,padx=5,pady=10,sticky="E")
        admnu=Entry(updateframe,font=("MS Gothic",10),relief=GROOVE)
        admnu.grid(row=18,column=1,padx=5, pady=10,sticky="W")
       
           
        
        def nameupdate():
            boardoption.destroy()
            courseoption.destroy()
            nameoption.destroy()
            optionl.destroy()
            marksoption.destroy()
            
            fnameupdatel=Label(updateframe,text="New First Name:",font=("Adobe Fan Heiti Std B",10),bg="cornsilk4")
            fnameupdatel.grid(row=19,column=0)
            
            mnameupdatel=Label(updateframe,text="New Middle Name:",font=("Adobe Fan Heiti Std B",10),bg="cornsilk4")
            mnameupdatel.grid(row=20,column=0)
            
            lnameupdatel=Label(updateframe,text="New Last Name:",font=("Adobe Fan Heiti Std B",10),bg="cornsilk4")
            lnameupdatel.grid(row=21,column=0)
            
            firstup=Entry(updateframe,font=("MS Gothic",10),relief=GROOVE)
            firstup.grid(row=19,column=1)
            
            midup=Entry(updateframe,font=("MS Gothic",10),relief=GROOVE)
            midup.grid(row=20,column=1)
            
            lastup=Entry(updateframe,font=("MS Gothic",10),relief=GROOVE)
            lastup.grid(row=21,column=1)
            
            def fnameupdate():
                
                st="update namiboi set fname=(%s),name=(%s),lname=(%s) where appid=%s"
                val=(firstup.get(),midup.get(),lastup.get(),admnu.get())
                mycur.execute(st,val)
                mydb.commit()
                
                
                updateframe.destroy()
                
            
            updaten=Button(updateframe,text="【Update】",command=fnameupdate,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),cursor="circle")
            updaten.grid(row=22,column=1)
            
         
        def courseupdate():
            marksoption.destroy() 
            boardoption.destroy()
            courseoption.destroy()
            nameoption.destroy()
            optionl.destroy()
              
            courseupdatel=Label(updateframe,text="New Course:",font=("Adobe Fan Heiti Std B",10),bg="cornsilk4")
            courseupdatel.grid(row=19,column=0)
              
            courseupdatee=Entry(updateframe,font=("MS Gothic",10),relief=GROOVE)
            courseupdatee.grid(row=19,column=1)
            
            def fcourseupdate():
                
                st="update namiboi set courses=(%s) where appid=(%s)"
                val=(courseupdatee.get(),admnu.get())
                mycur.execute(st,val)
                mydb.commit()
                
                updateframe.destroy()
                
            updateco=Button(updateframe,text="【Update】",command=fcourseupdate,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),cursor="circle")
            updateco.grid(row=22,column=1)
            
            
        def boardupdate():
            marksoption.destroy()
            boardoption.destroy()
            courseoption.destroy()
            nameoption.destroy()
            optionl.destroy()
        
            boardupdatel=Label(updateframe,text="New Board:",font=("Adobe Fan Heiti Std B",10),bg="cornsilk4")
            boardupdatel.grid(row=19,column=0)
            
            boardupdatee=Entry(updateframe,font=("MS Gothic",10),relief=GROOVE)
            boardupdatee.grid(row=19,column=1)
                
            
            def fcourseupdate():
                    
                    st="update namiboi set board=(%s) where appid=(%s)"
                    val=(boardupdatee.get(),admnu.get())
                    mycur.execute(st,val)
                    mydb.commit()
                    
                    updateframe.destroy()
                    
            updatebo=Button(updateframe,text="【Update】",command=fcourseupdate,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),cursor="circle")
            updatebo.grid(row=22,column=1)
            
            
        def marksupdate():
            boardoption.destroy()
            courseoption.destroy()
            nameoption.destroy()
            optionl.destroy()
            marksoption.destroy()
            
            marksupdatel=Label(updateframe,text="New Marks:",font=("Adobe Fan Heiti Std B",10),bg="cornsilk4")
            marksupdatel.grid(row=19,column=0)
            
            marksupdatee=Entry(updateframe,font=("MS Gothic",10),relief=GROOVE)
            marksupdatee.grid(row=19,column=1)
            
            def fmarksupdate():
                
                st="update namiboi set marks=(%s) where appid=(%s)"
                val=(marksupdatee.get(),admnu.get())
                mycur.execute(st,val)
                mydb.commit()
                
                updateframe.destroy()
                
            updatema=Button(updateframe,text="【Update】",command=fmarksupdate,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),cursor="circle")
            updatema.grid(row=22,column=1)
                
            
                    
        optionl=Label(updateframe,text="Change field==>",font=("Adobe Fan Heiti Std B",10),bg="cornsilk4")
        optionl.grid(row=19,column=0)        
        
        nameoption=Button(updateframe,text="【Name】",command=nameupdate,width=10,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),cursor="circle")
        nameoption.grid(row=19,column=1,sticky="W") 
        
        courseoption=Button(updateframe,text="【Course】",command=courseupdate,width=10,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),cursor="circle")
        courseoption.grid(row=19,column=2)
        
        boardoption=Button(updateframe,text="【Board】",command=boardupdate,width=10,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),cursor="circle")
        boardoption.grid(row=20,column=1,sticky="W")
        
        marksoption=Button(updateframe,text="【Marks】",command=marksupdate,width=10,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),cursor="circle")
        marksoption.grid(row=20,column=2)
        
        
    updateb=Button(cocur,text="【Modify Records】" ,command=update,width=40,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),cursor="circle")
    updateb.grid(row=14,column=1,padx=10, pady=10)
    
    ######################################################################################################################################
    
    def searchosancho():
        searchframe=Frame(cocur,bg="cornsilk4")
        searchframe.grid(row=15,column=0)
        searche=Entry(searchframe,width=20,font=("MS Gothic",10),relief=GROOVE)
        searche.grid(row=15,column=1,padx=10, pady=10)
        searchl=Label(searchframe,text="App ID:",font=("Adobe Fan Heiti Std B",10),bg="cornsilk4")
        searchl.grid(row=15,column=0)
        
        def fsearchosancho():        
            st="select * from namiboi where appid=%s" 
            val=(searche.get(),)
            mycur.execute(st,val)
            searchr=mycur.fetchall()
            print("****************************************************************************************")
            for x in searchr:
                print(x)
            print("****************************************************************************************")
            fsearchosanchob.destroy()
            searche.destroy()
            searchl.destroy()
            searchframe.destroy()
            
            
        fsearchosanchob=Button(searchframe,text="✓",command=fsearchosancho,width=5,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),cursor="circle")
        fsearchosanchob.grid(row=15,column=3)
        
    
    searchosanchob=Button(cocur,text="【Search】",command=searchosancho,width=40,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),cursor="circle")
    searchosanchob.grid(row=14,column=0,padx=10, pady=10,sticky="E")
    
    ######################################################################################################################################
    
    def deleto():
        deleteframe=Frame(cocur,bg="cornsilk4")
        deleteframe.grid(row=11,column=1)
        deletel=Label(deleteframe,text="Enter the AppID:",font=("Adobe Fan Heiti Std B",10))
        deletel.grid(row=11,column=1,sticky="W")
        deletel.configure(bg="cornsilk4")
        deletee=Entry(deleteframe,font=("MS Gothic",10),relief=GROOVE)
        deletee.grid(row=11,column=1,sticky="E")
       
        def fdeleto():
            st="delete from namiboi where appid= %s"
            messagebox.showinfo("Successful","Data has been deleted")
            val=(deletee.get(),)
            mycur.execute(st,val)
            mydb.commit()
            deletee.destroy()
            fdelete.destroy()
            deleteframe.destroy()
        
        fdelete=Button(deleteframe,text="【Delete the entry】",command=fdeleto,width=40,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),cursor="circle")
        fdelete.grid(row=12,column=1,padx=10, pady=10)
        
    deleteb=Button(cocur,text="【Delete】",command=deleto,width=40,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),cursor="circle")
    deleteb.grid(row=10,column=1,padx=10,pady=10)
    
    ######################################################################################################################################
    
    def graph():
        
        l=[]    
        
        st="select marks from namiboi"
        mycur.execute(st)
        results=mycur.fetchall()
        for row in results:
            marks=row[0]
            l.append(marks)    
    
        x=[0,0,0,0,0,0,0]
        y=["100%","90-99%","80-89%","70-79%","60-69%","50-59%","40-49%"]
        for a in range(len(l)):
            if l[a]==100:
                x[0]+=1
            if l[a]>90 and l[a]<100:
                x[1]+=1
            elif l[a]>80 and l[a]<90:
                x[2]+=1
            elif l[a]>70 and l[a]<80:
                x[3]+=1
            elif l[a]>60 and l[a]<70:
                x[4]+=1
            elif l[a]>50 and l[a]<60:
                x[5]+=1
            elif l[a]>40 and l[a]<50:
                x[6]+=1
        
        print (x)
        
        plt.bar(y,x,color=["purple","red","blue","cyan","white","yellow","orange"])
        plt.savefig("#nami_g2.png",bbox_inches="tight")
        
        plt.show()
        
           
        labels =y
        sizes =x   
        patches, texts = plt.pie(sizes, shadow=True, startangle=90)
        plt.legend(patches, labels, loc="best")
        plt.axis('equal')
        plt.tight_layout()
        plt.savefig("#nami_g.png",bbox_inches="tight")
       
        plt.show()
        
        
        
    
    
        def disp_graph():
            
           displayggl.destroy()
           grxph=Toplevel()
           grxph.title("Graph Data Representation")
           
           g1=PhotoImage(file="#nami_g.png")
           g2=PhotoImage(file="#nami_g2.png")
           
                         
           gl1 = Label(grxph,image=g1,bd=0)
           gl1.grid(row=0,column=0,padx=10,pady=10)
           gl1.configure(background="cornsilk4")
           
           gl2=Label(grxph,image=g2,bd=0)
           gl2.grid(row=0,column=1,padx=10,pady=10)
           gl2.configure(background="cornsilk4")
           
          
           grxph.mainloop()
        
        
        displayggl=Button(cocur,text="【Display Graph】",command=disp_graph,width=40,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),cursor="circle")
        displayggl.grid(row=31,column=0,padx=10,pady=10,sticky="E")
        
    ''' 
        labels = y
        sizes = x
        
        
        plt.pie(sizes,labels=labels,
        autopct='%1.1f%%', shadow=True, startangle=140)
        
        plt.axis('equal')
        plt.show()  
        
    '''
    
    graphandchart=Button(cocur,text="【Data Analysis】",command=graph,width=40,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),cursor="circle")
    graphandchart.grid(row=30,column=0,padx=10,pady=10,sticky="E")
    
    ######################################################################################################################################
    
    def exitc():
        nami.deiconify()
        cocur.destroy()
    
    exitb=Button(cocur,text="【Main Page】",width=40,command=exitc,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),cursor="circle")
    exitb.grid(row=30,column=1,padx=10,pady=10)
    
    ######################################################################################################################################
    '''
    def contactus():
        
        contact=Toplevel()
        contact.configure(bg="cornsilk4")
        contact.geometry("1000x1000")
        
        contacti1=Label(contact,text="Co-Curricular Form Made by Nami Senpai",font=("Tw Cen MT Condensed Extra Bold",15),bg="cornsilk4",fg="Dark Green")
        contacti1.pack()
        
        contacti2=Label(contact,text="Contact Information:",font=("Tw Cen MT Condensed Extra Bold",15),bg="cornsilk4",fg="Dark Green")
        contacti2.pack()
        
        contacti3=Label(contact,text="Email ==> asdfg123@gmail.com",font=("Tw Cen MT Condensed Extra Bold",15),bg="cornsilk4",fg="Dark Green")
        contacti3.pack()
        
        contacti4=Label(contact,text="Mobile Number ==> +91xxxxxxxx",font=("Tw Cen MT Condensed Extra Bold",15),bg="cornsilk4",fg="Dark Green")
        contacti4.pack()
        
        sponsorlabel=Label(contact,text="Sponsors",font=("Tw Cen MT Condensed Extra Bold",25),bg="cornsilk4",fg="Dark Green")
        sponsorlabel.pack()
        
        def showspons():
            sponslvl=Toplevel()
            sponslvl.title("Sponsors")
            
            sponsor1=PhotoImage(file=r"sponsor1.png")
            sponsor2=PhotoImage(file=r"sponsor2.png")
            sponsor3=PhotoImage(file=r"sponsor3.png")
            
            spons1=Label(sponslvl,image=sponsor1)
            spons1.grid(row=1,column=0)
            
            spons2=Label(sponslvl,image=sponsor2)
            spons2.grid(row=2,column=0)
            
            spons3=Label(sponslvl,image=sponsor3)
            spons3.grid(row=3,column=0)
            
        
        sponsorbutton=Button(contact,text="【Show Sponsors】",font=("Tw Cen MT Condensed Extra Bold",15),bg="cornsilk4",fg="Dark Green",command=showspons,cursor="circle")
        sponsorbutton.pack()
        
        
        
       
        
    contactb=Button(cocur,text="【Contact Us】",command=contactus,bg="cornsilk3",relief=GROOVE,font=("Tekton Pro",10),width=40,cursor="circle")
    contactb.grid(row=31,column=0,padx=10,pady=10,sticky="E")
    '''
    cocur.mainloop()
    ######################################################################################################################################


#For Zohaib's GUI  
    

def zgui():
    
    #By Syed Zuhaib Ali
    
    nami.iconify()
    info = Toplevel()
    info.geometry("")
    info.title("Konoha University's Admission form")
    info.configure(backg="dark olive green")
    head=Label(info,text="KONOHA UNIVERSITY",font=("papyrus",30))
    head.place(x=350,y=0)
    head.configure(fg="lemon chiffon",bg='dark olive green')
    label =Label(info, text ="❀ PERSONAL DETAILS:",font=("papyrus",15))
    label.grid(row=1,column=0,sticky="W")
    label.configure(backg="dark olive green",fg='white')
    xyz=Label(info,text="⦿ Student details:",font=("papyrus",12))
    xyz.grid(row=2,column=0)
    xyz.configure(backg="dark olive green",fg='white')
    fname=Label(info,text="First Name: ",font=("Adobe Fan Heiti Std B",10))
    fname.configure(background="dark olive green",fg='white')
    fname.grid(row=3,column=0,sticky="E")
    fnametxtf= Entry(info,width=30,font=("PAPYRUS",10),relief=FLAT,bg="lemon chiffon")
    fnametxtf.grid(row=3,column=1,padx=10, pady=10,sticky="W")                
    mname=Label(info,text="Middle Name: ",font=("Adobe Fan Heiti Std B",10))
    mname.configure(background="dark olive green",fg='white')
    mname.grid(row=4,column=0,sticky="E")
    mnametxtf=Entry(info,width=30,font=("PAPYRUS",10),relief=FLAT,bg="lemon chiffon")
    mnametxtf.grid(row=4,column=1,padx=10, pady=10,sticky="W")
    lname=Label(info,text="Last Name: ",font=("Adobe Fan Heiti Std B",10))
    lname.configure(background="dark olive green",fg='white')
    lname.grid(row=5,column=0,sticky="E")
    lnametxtf= Entry(info,width=30,font=("PAPYRUS",10),relief=FLAT,bg="lemon chiffon")
    lnametxtf.grid(row=5,column=1,padx=10, pady=10,sticky="W")
    xy=Label(info,text="⦿ parent/guardian details:",font=("papyrus",12))
    xy.grid(row=7,column=0,)
    xy.configure(backg="dark olive green",fg='white')
    ffname=Label(info,text="Father's First Name",font=("Adobe Fan Heiti Std B",10))
    ffname.grid(row=8,column=0,sticky="E")
    ffname.configure(backg="dark olive green",fg='white')
    ffnametxt=Entry(info,width=30,font=("PAPYRUS",10),relief=FLAT,bg="lemon chiffon")
    ffnametxt.grid(row=8,column=1,padx=10, pady=10,sticky="W")
    flname=Label(info,text="Father's Last Name",font=("Adobe Fan Heiti Std B",10))
    flname.grid(row=9,column=0,sticky="E")
    flname.configure(backg="dark olive green",fg='white')
    flnametxt=Entry(info,width=30,font=("PAPYRUS",10),relief=FLAT,bg="lemon chiffon")
    flnametxt.grid(row=9,column=1,padx=10, pady=10,sticky="W")
    sphn=Label(info,text="Student's Contact",font=("Adobe Fan Heiti Std B",10))
    sphn.grid(row=4,column=3,sticky="E")
    sphn.configure(backg="dark olive green",fg='white')
    sphntxt=Entry(info,width=30,font=("PAPYRUS",10),relief=FLAT,bg="lemon chiffon")
    sphntxt.grid(row=4,column=4,padx=10, pady=10,sticky="W")
    fphn=Label(info,text="Father's Contact",font=("Adobe Fan Heiti Std B",10))
    fphn.grid(row=8,column=3,sticky='E')
    fphn.configure(backg="dark olive green",fg='white')
    fphntxt=Entry(info,width=30,font=("PAPYRUS",10),relief=FLAT,bg="lemon chiffon")
    fphntxt.grid(row=8,column=4,padx=10, pady=10,sticky="W")
    fmail=Label(info,text="Email",font=("Adobe Fan Heiti Std B",10))
    fmail.grid(row=9,column=3,sticky="E")
    fmail.configure(backg="dark olive green",fg='white')
    fmailtxt=Entry(info,width=30,font=("PAPYRUS",10),relief=FLAT,bg="lemon chiffon")
    fmailtxt.grid(row=9,column=4,padx=10, pady=10,sticky="W")
    dob=Label(info,text="D.O.B",font=("Adobe Fan Heiti Std B",10))
    dob.grid(row=5,column=3,sticky="E")
    dob.configure(backg="dark olive green",fg='white')
    dobtxt=Entry(info,width=30,font=("PAPYRUS",10),relief=FLAT,bg="lemon chiffon")
    dobtxt.grid(row=5,column=4,padx=10, pady=10,sticky="W")
    #---------------------------------------------------------------------------------------------------------------
    label2 =Label(info, text ="❀ COMMUNICATION ADDRESS:",font=("papyrus",15))
    label2.grid(row=13,column=0,sticky="W")
    label2.configure(backg="dark olive green",fg='white')
    houseno=Label(info,text="House No.",font=("Adobe Fan Heiti Std B",10))
    houseno.grid(row=17,column=0,sticky='E')
    houseno.configure(backg="dark olive green",fg='white')
    housenotxt=Entry(info, width=30,font=("PAPYRUS",10),relief=FLAT,bg="lemon chiffon")
    housenotxt.grid(row=17,column=1,padx=10, pady=10,sticky="W")
    street=Label(info,text="Street",font=("Adobe Fan Heiti Std B",10))
    street.grid(row=16,column=3,sticky="E")
    street.configure(backg="dark olive green",fg='white')
    streettxt=Entry(info,width=30,font=("PAPYRUS",10),relief=FLAT,bg="lemon chiffon")
    streettxt.grid(row=16,column=4,padx=10, pady=10,sticky="W")
    city=Label(info,text="City",font=("Adobe Fan Heiti Std B",10))
    city.grid(row=19,column=0,sticky='E')
    city.configure(backg="dark olive green",fg='white')
    citytxt=Entry(info,width=30,font=("PAPYRUS",10),relief=FLAT,bg="lemon chiffon")
    citytxt.grid(row=19,column=1,padx=10, pady=10,sticky="W")
    pincode=Label(info,text="Pincode",font=("Adobe Fan Heiti Std B",10))
    pincode.grid(row=19,column=3,sticky="E")
    pincode.configure(backg="dark olive green",fg='white')
    pincodetxt=Entry(info,width=30,font=("PAPYRUS",10),relief=FLAT,bg="lemon chiffon")
    pincodetxt.grid(row=19,column=4,padx=10, pady=10,sticky="W")
    region=["Delhi","Outside Delhi"]
    regionl=Label(info,text="Region",font=("Adobe Fan Heiti Std B",10),bg="dark olive green",fg="white")
    regionl.configure(background="dark olive green")
    regionl.grid(row=16,column=0,sticky="E")
    regioncombo=ttk.Combobox(info,width=30,font=("MS Gothic",10),justify="center")
    regioncombo['values']=region
    regioncombo.grid(row=16,column=1,padx=10, pady=10,sticky="W")
    category=["Gen","OBC","SC","ST"]
    categoryl=Label(info,text="Category",font=("Adobe Fan Heiti Std B",10),bg="dark olive green",fg="white")
    categoryl.configure(background="dark olive green")
    categoryl.grid(row=3,column=3,sticky="E")
    categorycombo=ttk.Combobox(info,width=30,font=("MS Gothic",10),justify="center")
    categorycombo['values']=category
    categorycombo.grid(row=3,column=4,padx=10, pady=10,sticky="W")
    gender=["Male","Female"]
    genderl=Label(info,text="Gender",font=("Adobe Fan Heiti Std B",10),bg="dark olive green",fg="white")
    genderl.configure(background="dark olive green")
    genderl.grid(row=6,column=0,sticky="E")
    gendercombo=ttk.Combobox(info,width=30,font=("MS Gothic",12),justify="center")
    gendercombo['values']=gender
    gendercombo.grid(row=6,column=1,padx=10, pady=10)
    state=["New Delhi","Lucknow","Punjab","Chennai","Noida","Bihar"]
    statel=Label(info,text="State",font=("Adobe Fan Heiti Std B",10),bg="dark olive green",fg="white")
    statel.configure(background="dark olive green")
    statel.grid(row=17,column=3,sticky="E")
    statecombo=ttk.Combobox(info,width=30,font=("MS Gothic",12),justify="center")
    statecombo['values']=state
    statecombo.grid(row=17,column=4,padx=10, pady=10,sticky="W")
    #---------------------------------------------------------------------------------------------------------------
    def clear():
           fnametxtf.delete(first=0,last=100)
           mnametxtf.delete(first=0,last=100)
           lnametxtf.delete(first=0,last=100)
           sphntxt.delete(first=0,last=100)
           ffnametxt.delete(first=0,last=100)
           flnametxt.delete(first=0,last=100)
           fphntxt.delete(first=0,last=100)
           fmailtxt.delete(first=0,last=100)
           housenotxt.delete(first=0,last=100)
           streettxt.delete(first=0,last=100)
           citytxt.delete(first=0,last=100)
           pincodetxt.delete(first=0,last=100)
           categorycombo.delete(first=0,last=100)
           statecombo.delete(first=0,last=100)
           regioncombo.delete(first=0,last=100)
           gendercombo.delete(first=0,last=100)
           dobtxt.delete(first=0,last=100)       
    clearbutton = Button(info,text=("Clear Entries"),command=clear,width=20,relief=GROOVE,font=("papyrus",10),cursor="circle")
    clearbutton.grid(row=21,column=4,padx=10, pady=10)
    #---------------------------------------------------------------------------------------------------------------
    def inserto():
            st="insert into studinfo(fname,mname,lname,sphn,DOB,ffname,flname,fphn,fmail,houseno,street,pincode,category,state,region,gender)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(fnametxtf.get(),mnametxtf.get(),lnametxtf.get(),sphntxt.get(),dobtxt.get(),ffnametxt.get(),flnametxt.get(),fphntxt.get(),fmailtxt.get(),housenotxt.get(),streettxt.get(),pincodetxt.get(),categorycombo.get(),statecombo.get(),regioncombo.get(),gendercombo.get())
            mycur.execute(st,val)
    insertob=Button(info,text="Submit",command=inserto,width=20,relief=GROOVE,font=("papyrus",10),cursor="circle")
    insertob.grid(row=22,column=4,padx=10, pady=10)
    #---------------------------------------------------------------------------------------------------------------
    def selecto():
        display=Toplevel(bg="lemon chiffon")
        display.geometry("700x700")
        display.title("Table's Data")
        mycur.execute("select * from studinfo")
        searched=mycur.fetchall()   
        displ=Label(display,text="Data From The Table",fg="lemon chiffon",bg="dark olive green",font=("zapfino",45))
        displ.pack(fill=X)        
        for x in searched:
            print("-------------------------------------------------------------------------------")
            print(x)
            print("-------------------------------------------------------------------------------")        
            dispop=Label(display,text=x,font=("Impact",13),fg="dark olive green",bg="lemon chiffon")
            dispop.pack(fill=Y)   
        def disexit():
            display.destroy()        
        disexit=Button(display,text="DONE",command=disexit,width=20,height=2,relief=RIDGE,bg="lemon chiffon",fg="dark olive green",cursor="circle",font=("Impact",13))
        disexit.pack(side=BOTTOM,pady=30)                             
    selectb=Button(info,text="Show Data",command=selecto,width=20,relief=GROOVE,font=("papyrus",10),cursor="circle")
    selectb.grid(row=21,column=3)   
    #--------------------------------------------------------------------------------------------------------------
    def search():
            searchframe=Frame(info,bg="dark olive green")
            searchframe.grid(row=21,column=1)
            searche=Entry(searchframe,width=20,font=("PAPYRUS",10),relief=FLAT)
            searche.grid(row=21,column=1,padx=10, pady=10,sticky='W')
            searchl=Label(searchframe,text="App ID:",font=("Adobe Fan Heiti Std B",10),bg="dark olive green",fg="white")
            searchl.grid(row=21,column=0)        
            def fsearch():        
                st="select * from studinfo where appid=%s" 
                val=(searche.get(),)
                mycur.execute(st,val)
                searchr=mycur.fetchall()
                print("----------------------------------------------------------------------------------------")
                for x in searchr:
                    print(x)
                print("----------------------------------------------------------------------------------------")
                fsearchb.destroy()
                searche.destroy()
                searchl.destroy()
                searchframe.destroy()
            fsearchb=Button(searchframe,text="✓",command=fsearch,width=5,bg="dark olive green",relief=FLAT,font=("papyrus",10),cursor="circle")
            fsearchb.grid(row=21,column=2)
    searchb=Button(info,text="Search",command=search,width=20,relief=GROOVE,font=("papyrus",10),cursor="circle")
    searchb.grid(row=21,column=1,padx=10, pady=10)
    #---------------------------------------------------------------------------------------------------------------
    def delete():
            deleteframe=Frame(info,bg="dark olive green")
            deleteframe.grid(row=22,column=1)
            deletex=Label(deleteframe,text="AppID:",font=("Adobe Fan Heiti Std B",10),fg="white")
            deletex.grid(row=22,column=0)
            deletex.configure(bg="dark olive green")
            deletey=Entry(deleteframe,font=("PAPYRUS",10),relief=FLAT)
            deletey.grid(row=22,column=1,)      
            def fdelete():
                st="delete from studinfo where appid= %s"
                val=(deletey.get(),)
                mycur.execute(st,val)
                mydb.commit()
                deletey.destroy()
                fdelete.destroy()
                deleteframe.destroy()        
            fdelete=Button(deleteframe,text="【Delete the entry】",command=fdelete,width=15,bg="dark olive green",relief=FLAT,font=("papyrus",10),cursor="circle")
            fdelete.grid(row=22,column=2,padx=10, pady=10)        
    deleteb=Button(info,text="Delete",command=delete,width=20,relief=GROOVE,font=("papyrus",10),cursor="circle")
    deleteb.grid(row=22,column=1,padx=10,pady=10)
    #-------------------------------------------------------------------------------------------------------------------
    def exitz():
            nami.deiconify()
            info.destroy()
            
    exitb=Button(info,text="Main Page",width=20,command=exitz,relief=GROOVE,font=("papyrus",10),cursor="circle")
    exitb.grid(row=22,column=3,padx=10,pady=10)    
    info.mainloop()
##################################################################################################################################################################
    
ch1=Label(nami,text="Choose A Form to Enter Details in",font=("AR CENA",15),fg="gray25",bg="azure3")
ch1.pack(fill=X)
 
       
zuhji=Button(nami,text="Student Information",width=30,height=2,font=("Impact",13),relief=RIDGE,bg="honeydew3",fg="gray25",cursor="circle",command=zgui)
zuhji.pack(padx=30,pady=30)


namiboo=Button(nami,text="Co-Curricular Gui",command=namigui,width=30,height=2,font=("Impact",13),relief=RIDGE,bg="honeydew3",fg="gray25",cursor="circle")
namiboo.pack(padx=30,pady=30)

#def join():
    

      
      
    ######################################################################################################################################

showjointdata=Label(nami,text="Show Data From Both Forms",font=("AR CENA",15),fg="gray25",bg="azure3")
showjointdata.pack(fill=X,pady=30)

joindata=Button(nami,text="Join",command=join,font=("Impact",13),width=30,height=2,relief=RIDGE,bg="honeydew3",fg="gray25",cursor="circle")
joindata.pack(padx=30,pady=30)
    
    ######################################################################################################################################
     

nami.mainloop()
