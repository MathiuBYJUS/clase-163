from tkinter import*

root=Tk()
root.geometry("500x500")
root.title("Fiebre")

label_1=Label(root,text="Tienes dolor de cabeza")
label_1.place(relx=0.5 , rely=0.1 , anchor=CENTER)

question_1=StringVar(value="0")
question_1_rb=Radiobutton(root,text="Si",variable=question_1,value="1")
question_1_rb.place(relx=0.5, rely=0.2,anchor=CENTER)
question_2=StringVar(value="0")
question_2_rb=Radiobutton(root,text="No",variable=question_2,value="2")
question_2_rb.place(relx=0.5 , rely=0.3 , anchor=CENTER)

label_2=Label(root,text="Tienes temperatura corporal alta")
label_2.place(relx=0.5 , rely=0.4 , anchor=CENTER)
question_3=StringVar(value="0")
question_3_rb=Radiobutton(root,text="Si",variable=question_3,value="3")
question_3_rb.place(relx=0.5 , rely=0.5 , anchor=CENTER)
question_4=StringVar(value="0")
question_4_rb=Radiobutton(root,text="No",variable=question_4,value="4")
question_4_rb.place(relx=0.5 , rely=0.6 , anchor=CENTER)

label_3=Label(root,text="Tienes algun sntoma de enrojecimiento en los ojos")
label_3.place(relx=0.5,rely=0.7,anchor=CENTER)
question_5=StringVar(value="0")
question_5_rb=Radiobutton(root,text="Si",variable=question_5,value="5")
question_5_rb.place(relx=0.5,rely=0.8,anchor=CENTER)
question_6=StringVar(value="0")
question_6_rb=Radiobutton(root,text="No",variable=question_6,value="6")
question_6_rb.place(relx=0.5 , rely=0.9 , anchor=CENTER)

def respuesta():
    
    a=0 
    if question_1.get()=="1":
        a=a+1
        print (a)
    if question_3.get()=="3":
        a=a+1
    if question_5.get()=="5":
        a=a+1
    
    
    

        
    
        


button_1=Button(root,text="Dame click par saber si requieres ir al doctor o no")
button_1.place(relx=0.5 , rely=1 , anchor=CENTER)
root.mainloop()
