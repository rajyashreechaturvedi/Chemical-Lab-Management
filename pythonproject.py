from tkinter import*
root=Tk()
root.configure(background='black')
root.geometry("1600x550")
root.title("Chemistry Lab Management System")


def Add_Record():
    f=open('rajyashree.txt','a')
    CHEMICAL_NO=s1.get()
    CHEMICAL_NAME=s2.get()
    QUANTITY=s3.get()
    PRICE=s4.get()
    MAN_DATE=s5.get()
    EXPIRY=s6.get()
    BUYER=s7.get()
    DEMAND=s8.get()
    if(CHEMICAL_NO=='' or CHEMICAL_NAME=='' or QUANTITY=='' or PRICE=='' or MAN_DATE=='' or EXPIRY==''or BUYER==''or DEMAND==''):
        print("Details can't be empty!")
        exit()
    f.writelines(CHEMICAL_NO.ljust(20)+CHEMICAL_NAME.ljust(20)+QUANTITY.ljust(20)+PRICE.ljust(20)+MAN_DATE.ljust(20)+EXPIRY.ljust(20)+BUYER.ljust(20)+DEMAND.ljust(20)+"\n")
    print("The chemical has been registered !!")
    print("Chemical number = ",CHEMICAL_NO)
    print("Chemical name = ",CHEMICAL_NO)
    print("Quantity = ",CHEMICAL_NO)
    print("Price = ",CHEMICAL_NAME)
    print("Manufacturing Date = ",MAN_DATE)
    print("Expiry = ",EXPIRY)
    print("Buyer = ",BUYER)
    print("Demand = ",DEMAND,"\n")
    f.close()
    

def update():
    x1=s1.get()
    x2=s2.get()
    x3=s3.get()
    x4=s4.get()
    x5=s5.get()
    x6=s6.get()
    x7=s7.get()
    x8=s8.get()
    f=open("rajyashree.txt",'r')
    k=f.readlines()
    f.close()
    f=open("rajyashree.txt",'w')
    z=0
    for i in k:
        j=i.split()
        if(j[0]!=x1):
            f.writelines(j[0].ljust(20)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(20)+j[5].ljust(20)+j[6].ljust(20)+j[7].ljust(20)+"\n")     
        else:
            f.writelines(x1.ljust(20)+x2.ljust(20)+x3.ljust(20)+x4.ljust(20)+x5.ljust(20)+x6.ljust(20)+x7.ljust(20)+x8.ljust(20)+"\n")
            z=1
            print("\nThe chemical has successfully been updated!\n")
            print("Updated Chemical number = ",x1)
            print("Updated Chemical name = ",x2)
            print("Updated Quantity = ",x3)
            print("Updated Price = ",x4)
            print("Updated Manufacturing Date = ",x5)
            print("Updated Expiry = ",x6)
            print("Updated Buyer = ",x7)
            print("Updated Demand = ",x8,"\n")
            print
    if(z==0):
        print("\nThere was an unidentified error, the chemical could not be updated!\n")
 

def SEARCH():
    k=s1.get()
    f=open('rajyashree.txt','r')
    h=f.readlines() 
    flag=0
    for i in h: 
        j=i.split() 
        if(j[0]==k): 
            print("Chemical found !!")  
            print("Chemical number = ",j[0])
            print("Chemical name = ",j[1])
            print("Quantity = ",j[2])
            print("Price = ",j[3])
            print("Manufacturing Date = ",j[4])
            print("Expiry = ",j[5])
            print("Buyer = ",j[6])
            print("Demand = ",j[7],"\n")
            flag=1
    if(flag==0):
        print("Chemical not in the inventory !!\n")              
    f.close()       


def delrec(): 
    x1=s1.get() 
    f=open("rajyashree.txt","r") 
    lines=f.readlines()  
    f.close() 
    f=open("rajyashree.txt","w")
    flag=0 
    for i in lines: 
        m=i.split()  
        if(m[0]!=x1): 
             f.writelines(m[0].ljust(20)+m[1].ljust(20)+m[2].ljust(20)+m[3].ljust(20)+m[4].ljust(20)+m[5].ljust(20)+m[6].ljust(20)+m[7].ljust(20)+"\n")              
        else:
             flag=1
             print("The following chemical has been deleted !!\n")
             print("Chemical number = ",m[0])
             print("Chemical name = ",m[1])
             print("Quantity = ",m[2])
             print("Price = ",m[3])
             print("Manufacturing Date = ",m[4])
             print("Expiry = ",m[5])
             print("Buyer = ",m[6])
             print("Demand = ",m[7],"\n")
    if(flag==0):
        print("The Chemical could not be found in the inventory !!\n")
    f.close() 


def get_previous():
    f=open("rajyashree.txt",'r')
    ctr=len(f.readlines())
    if(ctr==0):
        print("There are no chemicals in the inventory !!")
    else:
        f=open("rajyashree.txt",'r')    
        k=f.readlines()[0]
        j=k.split()
        print("\nThis is the oldest chemical !!\n")
        print("Chemical number = ",j[0])
        print("Chemical name = ",j[1])
        print("Quantity = ",j[2])
        print("Price = ",j[3])
        print("Manufacturing Date = ",j[4])
        print("Expiry = ",j[5])
        print("Buyer = ",j[6])
        print("Demand = ",j[7],"\n")
    f.close()


def sort_quant():
    file1 = open("rajyashree.txt", "r")
    count = 0
    dic = {}
    print("\nChemicals are now in sorted order least to maximum quantity  !!\n")
    for line in file1:
        temp = line.split("                  ")
        dic[count] = temp
        count += 1
    for key, value in sorted(dic.items(), key=lambda e: e[1][2]):
        print("Chemical ",key+1," = ", value)


def sort_price():
    file1 = open("rajyashree.txt", "r")
    count = 0
    dic = {}
    print("\nChemicals are now in sorted order cheapest to most expensive !!\n")
    for line in file1:
        temp = line.split("                  ")
        dic[count] = temp
        count += 1
    for key, value in sorted(dic.items(), key=lambda e: e[1][3]):
        print("Chemical ",key+1," = ", value)


def get_all():
    f=open("rajyashree.txt","r") 
    lines=f.readlines()
    k=1
    flag=0 
    for i in lines:
        print("Chemical ",k," = ",i)
        k=k+1
        flag=1
    if(flag==0):
        print("There are no chemicals in the inventory !!") 

                
def clear():
     f=open("rajyashree.txt","r+")
     f.truncate()
     print("The inventory has been cleared !!\n")       

def reset_text():
    s1.set("")
    s2.set("") 
    s3.set("") 
    s4.set("") 
    s5.set("") 
    s6.set("")
    s7.set("")
    s8.set("") 

 
l1=Label(root,text="CHEMISTRY LAB MANAGEMET SYSTEM",font=('Ariel',20,'bold'),bg="black",fg="white").place(x=450,y=10)
l2=Label(root,text="CHEMICAL NUMBER",font=('Ariel',15,'bold'),bg="black",fg="white").place(x=100,y=120)
l3=Label(root,text="CHEMICAL NAME",font=('Ariel',15,'bold'),bg="black",fg="white").place(x=700,y=120)
l4=Label(root,text="QUANTITY",font=('Ariel',15,'bold'),bg="black",fg="white").place(x=100,y=180)
l5=Label(root,text="PRICE",font=('Ariel',15,'bold'),bg="black",fg="white").place(x=700,y=180)
l6=Label(root,text="MANUFACTURE DATE",font=('Ariel',15,'bold'),bg="black",fg="white").place(x=100,y=240)
l7=Label(root,text="EXPIRY DATE",font=('Ariel',15,'bold'),bg="black",fg="white").place(x=700,y=240)
l8=Label(root,text="PURCHASED BY",font=('Ariel',15,'bold'),bg="black",fg="white").place(x=100,y=300)
l9=Label(root,text="DEMAND",font=('Ariel',15,'bold'),bg="black",fg="white").place(x=700,y=300)

s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
s6=StringVar()
s7=StringVar()
s8=StringVar()

e2=Entry(root,textvariable=s1,bg="white").place(x=350,y=125)
e3=Entry(root,textvariable=s2,bg="white").place(x=950,y=125)
e4=Entry(root,textvariable=s3,bg="white").place(x=350,y=185)
e5=Entry(root,textvariable=s4,bg="white").place(x=950,y=185)
e6=Entry(root,textvariable=s5,bg="white").place(x=350,y=245)
e7=Entry(root,textvariable=s6,bg="white").place(x=950,y=245)
e8=Entry(root,textvariable=s7,bg="white").place(x=350,y=305)
e9=Entry(root,textvariable=s8,bg="white").place(x=950,y=305)

b1=Button(root,text="ADD CHEMICAL",bg="RED",font=('Ariel',10,'bold'),command=Add_Record,width=20).place(x=0,y=60)
b2=Button(root,text="UPDATE CHEMICAL",bg="RED",font=('Ariel',10,'bold'),command=update,width=20).place(x=150,y=60)
b3=Button(root,text="SEARCH CHEMICAL",bg="RED",font=('Ariel',10,'bold'),command=SEARCH,width=20).place(x=300,y=60)
b4=Button(root,text="DELETE CHEMICAL",bg="RED",font=('Ariel',10,'bold'),command=delrec,width=20).place(x=450,y=60)
b5=Button(root,text="OLDEST CHEMICAL",bg="RED",font=('Ariel',10,'bold'),command=get_previous,width=20).place(x=600,y=60)
b6=Button(root,text="SORT BY QUANTITY",bg="RED",font=('Ariel',10,'bold'),command=sort_quant,width=20).place(x=750,y=60)
b7=Button(root,text="SORT BY PRICE",bg="RED",font=('Ariel',10,'bold'),command=sort_price,width=20).place(x=900,y=60)
b8=Button(root,text="SHOW ALL",bg="RED",font=('Ariel',10,'bold'),command=get_all,width=20).place(x=1050,y=60)
b9=Button(root,text="REMOVE ALL",bg="RED",font=('Ariel',10,'bold'),command=clear,width=20).place(x=1200,y=60)
b10=Button(root,text="RESET",bg="YELLOW",font=('Ariel',10,'bold'),command=reset_text,width=20).place(x=550,y=400)

root.mainloop()


