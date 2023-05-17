import numpy as np
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import validate
import LU as LU
import Gauss as ga
import gaussandjacobi as gaj
from Bracketing import Bracket
from FixedPoint import Fixed
from SecantMethod import Secant
from NewtonRapshon import Newton


class GUI:
    
    def roots(self):

        def prev():
            self.frame2.pack_forget()
            frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT)
        frame.pack_forget()
        self.array=[]
        self.inputs=[]
        option=["Choose","Bisection", "False position", "Newton Raphson", "Fixed Point", "Secant"]
        self.click = StringVar()
        self.equation = StringVar()
        self.prec_var=IntVar()
        self.prec_var.set(5)
        self.click.set("Choose")
        self.frame2=Frame(master=root,bg="#FCFCFC")
        label=Label(self.frame2,text="Choose the method to get the root",font=("Arial bold",10),bg='#E9E6E6',fg="black")
        label2=Label(self.frame2,text="Enter the equation",font=("Arial bold",25),bg="#4276EF",fg="#000000")
        equation=Entry(self.frame2,textvariable=self.equation,width=50,justify="center", font=('Times', 25))
        precion_lab=Label(self.frame2,text="Precion",font=('Times',20),bg='white')
        precion=Spinbox(self.frame2, textvariable=self.prec_var,width=8, font=('Times', 20), from_=1, to=10,state="readonly")
        solve_button=Button(self.frame2, image=solve_img, border=0,command=self.findroot)
        txt=Text(self.frame2,font=('Times', 15))
        pp=OptionMenu(self.frame2 ,self.click ,*option ,command=self.selected )
        Button(self.frame2,text="Back",width=10,command=prev).place(x=0,y=0)
        pp.config(width=20,height=5)
        equation.config(highlightthickness=10,border=10)
        txt.insert(END,"Please enter the equation in this format:\n  -Use only one unknown variables x \n  -Use exponent function in this format exp(x)\n  -Use sin or cos in this form sin(x)\n -If you didn't enter Tolerance or Number of \n   iteration it would be set\n  >number of iteration =50 >Tolerance=0.00001\n >>Example:-  x^2-2x+sin(x)-x*exp(x)")
        txt.config(state=DISABLED,height=8,width=40)

        self.frame2.pack(fill=BOTH,expand=True)
        label2.pack(padx=5,pady=5)
        equation.pack(padx=5,pady=5)
        label.pack(padx=5,pady=5)
        pp.pack(padx=5,pady=5)
        txt.place(x=50,y=450)
        solve_button.place(x=440,y=280)
        precion_lab.place(x=700,y=210)
        precion.place(x=700,y=240)

    def findroot(self):
        val=validate.Valid()
        equation=val.validate(self.equation.get())
        print(equation)
        method=self.click.get()
        try:
            if method == "Choose":
                messagebox.showerror("Error","Please choose a method")
            elif self.equation.get() == "":
                messagebox.showerror("Error","Please enter the equation")
            elif equation == 'error':
                messagebox.showerror("Error","Please enter the equation in the correct format")
            elif method == "Bisection":
                if self.inputs[0].get() == "" or self.inputs[1].get() == "" or self.inputs[2].get() == "" or self.inputs[3].get() == "":
                    messagebox.showerror("Error","Please enter all the inputs")
                else:
                    try:
                        xl=float(self.inputs[0].get())
                        xu=float(self.inputs[1].get())
                        er=float(self.inputs[2].get())
                        no=int(self.inputs[3].get())
                        self.bracket=Bracket()
                        try:
                            data3,plt3,state3,root3=self.bracket.bisection(xl,xu,equation,no,er,self.prec_var.get())
                            self.show_ans(data=data3,root=root3,state=state3,plt=plt3)
                        except:
                            messagebox.showerror("Error","Incorrect Initial Guesses.")

                    except ValueError:
                        messagebox.showerror("Error","Please enter the inputs in the correct format")
            elif method == "False position":
                if self.inputs[0].get() == "" or self.inputs[1].get() == "" or self.inputs[2].get() == "" or self.inputs[3].get() == "":
                    messagebox.showerror("Error","Please enter all the inputs")
                else:
                    try:
                        xl=float(self.inputs[0].get())
                        xu=float(self.inputs[1].get())
                        er=float(self.inputs[2].get())
                        no=int(self.inputs[3].get())
                        try:
                            data3,plt3,state3,root3=self.bracket.false_postion(xl,xu,equation,no,er,self.prec_var.get())
                            self.show_ans(data=data3,root=root3,state=state3,plt=plt3)
                        except:
                            messagebox.showerror("Error","Incorrect Initial Guesses.")

                    except ValueError:
                        messagebox.showerror("Error","Please enter the inputs in the correct format")
            elif method == "Newton Raphson":
                if self.inputs[0].get() == "" or self.inputs[1].get() == "" or self.inputs[2].get() == "":
                    messagebox.showerror("Error","Please enter all the inputs")
                else:
                    try:
                        x0=float(self.inputs[0].get())
                        er=float(self.inputs[1].get())
                        no=int(self.inputs[2].get())
                        obj=Newton()
                        data,plot,state,root=obj.solve(currentX=x0,fi=equation,MaxNoOfIterations=no,error=er,sf=self.prec_var.get())
                        self.show_ans(data=data,root=root,state=state,plt=plot)
                    except ValueError:
                        messagebox.showerror("Error","Please enter the inputs in the correct format")
            elif method == "Fixed Point":
                if self.inputs[0].get() == "" or self.inputs[1].get() == "" or self.inputs[2].get() == "":
                    messagebox.showerror("Error","Please enter all the inputs")
                else:
                    try:
                        x0=float(self.inputs[0].get())
                        er=float(self.inputs[1].get())
                        no=int(self.inputs[2].get())
                        obj2=Fixed()
                        data2,plt2,state2,root2=obj2.solve(x0,equation,no,er,self.prec_var.get())
                        self.show_ans(data=data2,root=root2,state=state2,plt=plt2)

                    except ValueError:
                        messagebox.showerror("Error","Please enter the inputs in the correct format")
            elif method == "Secant":
                if self.inputs[0].get() == "" or self.inputs[1].get() == "" or self.inputs[2].get() == "" or self.inputs[3].get() == "":
                    messagebox.showerror("Error","Please enter all the inputs")
                else:
                    try:
                        x0=float(self.inputs[0].get())
                        x1=float(self.inputs[1].get())
                        er=float(self.inputs[2].get())
                        no=int(self.inputs[3].get())
                        sec=Secant()
                        data1,plt1,state1,root1=sec.solve(prevX=x0,currentX=x1,fi=equation,error=er,MaxNoOfIterations=no,sf=self.prec_var.get())
                        self.show_ans(data=data1,root=root1,state=state1,plt=plt1)
                    except ValueError:
                        messagebox.showerror("Error","Please enter the inputs in the correct format")
        except ZeroDivisionError:
            messagebox.showerror("Error","Error Division By Zero")


    def show_ans(self,data,root,state,plt):
        step=str()
        for i in data['steps']:
            step+=i
            step+='\n'
        def showplt():
            plt.show()
        res_v=Toplevel()
        res_v.title("Solution")
        res_v.iconphoto(False, icon_img)
        res_v.config(background="silver")
        res_v.geometry(f'{850}x{600}+{100}+{70}')
        fr2=Frame(master=res_v,bg="#FCFCFC",height=500,width=900)
        my_canvas=Canvas(fr2,scrollregion=(0,0,1000,1000),height=400,width=800)
        fr3=Frame(my_canvas)
        scl_y=tk.Scrollbar(fr2,orient=tk.VERTICAL,command=my_canvas.yview)
        fr2.pack(fill=BOTH,expand=True)
        my_canvas.pack(fill=BOTH,expand=True,side=LEFT)
        scl_y.pack(side=tk.RIGHT,fill=tk.Y,expand=True)
        my_canvas.configure(yscrollcommand=scl_y.set)
        my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        my_canvas.create_window(50,50,window=fr3,anchor=tk.CENTER)

        plot_btn=Button(fr3,text="Show plot",font=('Times', 20),command=showplt,fg='#000000',bg='#DBDDCB',width=10)
        res_lab=Label(fr3,text="Steps",padx=20, font=('Times', 20))
        res_lab0=Label(fr3,text=step,padx=20, font=('Times', 20))
        res_lab1=Label(fr3,text="Solution:  "+str(root),padx=20, font=('Times', 20))
        res_lab2=Label(fr3,text="State:  "+str(state),padx=20, font=('Times', 20))
        res_lab3=Label(fr3,text="Number of iteration performed:  "+str(data['number']),padx=20, font=('Times', 20))
        res_lab4=Label(fr3,text="Time:  "+str(data['time']),padx=20, font=('Times', 20))
        
        plot_btn.pack(anchor=S,side='bottom')
        res_lab.pack()
        res_lab0.pack()
        res_lab1.pack(anchor=S)
        res_lab2.pack(anchor=S)
        res_lab3.pack(anchor=S)
        res_lab4.pack(anchor=S)

    def selected(self,event):
        
        method=self.click.get()
        if (method == "Bisection" or method == "False position"):
            for i in self.array:
                i.place_forget()
            self.array.clear()
            self.inputs.clear()
            x1_var=StringVar()
            x2_var=StringVar()
            er_var=StringVar()
            no_var=StringVar()
            er_var.set('0.0001')
            no_var.set('50')
            l1=Label(self.frame2,text="Enter xl", font=('Times', 15))
            xl=Entry(self.frame2,textvariable=x1_var,width=10, justify=CENTER,font=('Times', 15))
            l2=Label(self.frame2,text="Enter xu", font=('Times', 15))
            xu=Entry(self.frame2,textvariable=x2_var,width=10,justify=CENTER,font=('Times', 15))
            l3=Label(self.frame2,font=('Times', 15),text="Enter tolerance")
            er=Entry(self.frame2,textvariable=er_var,width=10, justify=CENTER,font=('Times', 15))
            l4=Label(self.frame2,text="Enter Number of iterations", font=('Times', 15))
            no=Entry(self.frame2,textvariable=no_var,width=10,justify=CENTER,font=('Times', 15))
            l1.place(x=700,y=280)
            xl.place(x=700,y=310)
            l2.place(x=700,y=350)
            xu.place(x=700,y=380)
            l3.place(x=700,y=420)
            er.place(x=700,y=450)
            l4.place(x=700,y=480)
            no.place(x=700,y=520)
            self.array.extend([l1,l2,l3,l4,xl,xu,er,no])
            self.inputs.extend([x1_var,x2_var,er_var,no_var])

        elif method == "Fixed Point" or method == "Newton Raphson":

            for i in self.array:
                i.place_forget()
            self.array.clear()
            self.inputs.clear()
            x0_var=StringVar()
            er_var=StringVar()
            no_var=StringVar()
            er_var.set('0.00001')
            no_var.set('50')
            l1=Label(self.frame2,text="Enter x0", font=('Times', 15))
            x0=Entry(self.frame2,textvariable=x0_var,width=10, justify=CENTER,font=('Times', 15))
            l3=Label(self.frame2,font=('Times', 15),text="Enter tolerance")
            er=Entry(self.frame2,textvariable=er_var,width=10, justify=CENTER,font=('Times', 15))
            l4=Label(self.frame2,text="Enter Number of iterations", font=('Times', 15))
            no=Entry(self.frame2,textvariable=no_var,width=10,justify=CENTER,font=('Times', 15))
            l1.place(x=700,y=280)
            x0.place(x=700,y=310)
            l3.place(x=700,y=350)
            er.place(x=700,y=380)
            l4.place(x=700,y=420)
            no.place(x=700,y=450)
            self.array.extend([l1,l3,l4,x0,er,no])
            self.inputs.extend([x0_var,er_var,no_var])

        elif method == "Secant":
            for i in self.array:
                i.place_forget()
            self.array.clear()
            self.inputs.clear()
            x0_var=StringVar()
            x1_var=StringVar()
            er_var=StringVar()
            no_var=StringVar()
            er_var.set('0.0001')
            no_var.set('50')

            l1=Label(self.frame2,text="Enter x0", font=('Times', 15))
            x0=Entry(self.frame2,textvariable=x0_var,width=10,justify=CENTER,font=('Times', 15))
            l2=Label(self.frame2,text="Enter x1", font=('Times', 15))
            x1=Entry(self.frame2,textvariable=x1_var,width=10,justify=CENTER,font=('Times', 15))
            l3=Label(self.frame2,font=('Times', 15),text="Enter tolerance")
            er=Entry(self.frame2,textvariable=er_var,width=10, justify=CENTER,font=('Times', 15))
            l4=Label(self.frame2,text="Enter Number of iterations", font=('Times', 15))
            no=Entry(self.frame2,textvariable=no_var,width=10,justify=CENTER,font=('Times', 15))
            l1.place(x=700,y=280)
            x0.place(x=700,y=310)
            l2.place(x=700,y=350)
            x1.place(x=700,y=380)
            l3.place(x=700,y=420)
            er.place(x=700,y=450)
            l4.place(x=700,y=480)
            no.place(x=700,y=520)
            self.array.extend([l1,l2,l3,l4,x0,x1,er,no])
            self.inputs.extend([x0_var,x1_var,er_var,no_var])

    def run(self):
        def fork():
            if combotext.get()=="System of linear equations":
                frame.pack_forget()
                fr1.pack(fill=BOTH,expand=True)
            elif combotext.get()=="Roots of a equation":
                frame.pack_forget()
                self.roots()
            else:
                messagebox.showwarning("ERROR","Please choose any type.")
        def backs():
            frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT)
            fr1.pack_forget()
        global solve_img
        global prec
        global no_var
        global icon_img
        global root
        global clicked
        global fr1
        global frame
        root = Tk()
        icon_img = PhotoImage(file="images/icon.png")
        next_img = PhotoImage(file="images/next.png")
        solve_img = PhotoImage(file="images/solve.png")
        no_var = IntVar()
        prec = IntVar()
        clicked=StringVar()
        combotext = tk.StringVar()
        frame=Frame(master=root,width="1000",height="700", bg="#FFFFFF",relief=tk.GROOVE)
        fr1=Frame(master=root,width="1000",height="700", bg="#FCFCFC",relief=tk.GROOVE)
        label=Label(frame,text="Choose which kind of problems you want to solve.",font=("Arial",20),background="#BBB9B9",fg="#000000")
        numofeqn=Spinbox(fr1, textvariable=no_var,width=15, font=('Times', 20), from_=2, to=20)
        next_button = Button(fr1, image=next_img, border=0, command=self.show_table)
        lbl1 = Label(fr1,text="Enter the number of variables :", background="#A3B7FF", font=('Times', 20))
        box = ttk.Combobox(frame,width=20 ,textvariable=combotext, state='readonly')
        box.config(width=100,height=20)
        btn=Button(frame,text="Confirm",font="Arial 20 bold",command=fork)
        back=Button(fr1,text="back",width=10,command=backs)
        box['values'] = ("System of linear equations",
                "Roots of a equation")

        combotext.set('Select')
        clicked.set("Gauss Elimination")
        clicked.trace_add('write',lambda *args:self.set_type(clicked.get()))
        no_var.set(3)
        root.iconphoto(False, icon_img)
        root.title("Equation Solver")
        width = 1000
        height = 700
        root.geometry(f'{width}x{height}+{250}+{70}')
        root.config(background="silver")

        # fr1.place(x=300,y=250)
        frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT)
        label.pack(padx=10, pady=10, fill=X,anchor=CENTER)
        box.pack(padx=10,pady=10, ipady=5,anchor=CENTER)
        btn.pack(pady=10,padx=10,anchor=S)
        lbl1.pack(padx=10, pady=10, fill=X,anchor=CENTER)
        numofeqn.pack(padx=10, ipady=5,anchor=CENTER)
        next_button.pack(pady=10,anchor=S)
        back.place(x=0,y=0)


        root.mainloop()

    def show_table(self):
        global rows
        global cols
        global matrix
        global box
        global arr
        global fr2
        global arr_we
        
        arr_we=[]
        arr=[]
        matrix=[]
        rows=no_var.get()
        cols=rows+1
        fr1.pack_forget()
        fr2=Frame(master=root,bg="#FCFCFC")
        my_canvas=Canvas(fr2,scrollregion=(0,0,1000,1000),height=400,width=800)
        scl_y=tk.Scrollbar(fr2,orient=tk.VERTICAL,command=my_canvas.yview)
        scl_x=tk.Scrollbar(fr2,orient=tk.HORIZONTAL,command=my_canvas.xview)
        fr3=Frame(my_canvas)
        precion=Spinbox(fr2, textvariable=prec,width=8, font=('Times', 20), from_=1, to=10,state="readonly")
        precion_lab=Label(fr2,text="Precion",font=('Times',20),bg='white')
        drop=OptionMenu(fr2,clicked,"Gauss Elimination","Gauss-Jordan","LU Decomposition","Gauss-Seidel","Jacobi-Iteration")
        solve_button=Button(fr2, image=solve_img, border=0,command=self.solve)
        back=Button(fr2,text="back",width=10,command=self.backf)


        fr2.pack(fill=BOTH,expand=True)
        my_canvas.place(x=100,y=0)
        scl_y.pack(side=tk.RIGHT,fill=tk.Y)
        my_canvas.configure(yscrollcommand=scl_y.set,xscrollcommand=scl_x.set)
        my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        my_canvas.create_window(50,50,window=fr3,anchor=tk.CENTER)
        scl_x.pack(side=tk.BOTTOM,fill=tk.X)
        precion_lab.place(x=700,y=410)
        drop.place(x=280,y=410)
        back.place(x=0,y=0)
        precion.place(x=700,y=440)
        solve_button.place(x=280,y=450)
        
        
        for k in range(1,rows+1):
            x1=Label(fr3,text="X"+str(k),padx=20, font=('Times', 20))
            x1.grid(row=0, column=k+1)
        B = Label(fr3,text="B",padx=20, font=('Times', 20))
        B.grid(row=0, column=rows+2)
        for i in range (1,rows+1) :
            count=Label(fr3,text=str(i),padx=20, font=('Times', 20))
            count.grid(row=i,column=0)
            for j in range(1,cols+1):
                inputs=StringVar()
                inputs.set('0')
                box=Entry(fr3, width=5,textvariable=inputs,justify="center", font=('Times', 20))
                box.grid(row=i,column=j+1 , ipady=5)
                arr.append(inputs)
   
    def solve(self):
        matrix.clear()
        flag=TRUE
        for i in arr:
            try:
                f=float(i.get())
                matrix.append(f)
            except ValueError:
                messagebox.showerror("Error", "Invalid input")
                flag=False
                break;
        x=np.array(matrix)
        x.resize(rows,cols)
        if flag:
            if clicked.get()=="Gauss Elimination":
                cof=x[:rows,:cols-1].tolist()
                bs=x[:rows,cols-1:cols].reshape(rows,).tolist()
                step,data,t=ga.Gauss(rows,prec.get(),cof,bs,x.tolist())
                res_v=Toplevel()
                res_v.title("Solution")
                res_v.iconphoto(False, icon_img)
                res_v.config(background="silver")
                res_v.geometry(f'{500}x{500}+{100}+{70}')
                res_v.config()
                fr2=Frame(master=res_v,bg="#FCFCFC")
                my_canvas=Canvas(fr2,scrollregion=(0,0,1000,1000),height=400,width=800)
                fr3=Frame(my_canvas)
                scl_y=tk.Scrollbar(fr2,orient=tk.VERTICAL,command=my_canvas.yview)
                fr2.pack(fill=BOTH,expand=True)
                my_canvas.pack(fill=BOTH,expand=True,side=LEFT)
                scl_y.pack(side=tk.RIGHT,fill=tk.Y)
                my_canvas.configure(yscrollcommand=scl_y.set)
                my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                my_canvas.create_window(50,50,window=fr3,anchor=tk.CENTER)
                if step["Forward Elimination"]!=[]:
                    res_lab=Label(fr3,text="Steps",padx=20, font=('Times', 20))
                    res_lab.pack()
                    res_lab0=Label(fr3,text=str(np.array(step['Forward Elimination'])),padx=20, font=('Times', 20))
                    res_lab0.pack()
                res_lab1=Label(fr3,text="Solution:  "+str(data),padx=20, font=('Times', 20))
                res_lab1.pack(anchor=S)
                res_lab2=Label(fr3,text="Time:  "+str(abs(t)),padx=20, font=('Times', 20))
                res_lab2.pack(anchor=S)
            elif clicked.get()=="Gauss-Jordan":
                cof=x[:rows,:cols-1].tolist()
                bs=x[:rows,cols-1:cols].reshape(rows,).tolist()
                step,data,t=ga.Gauss_Jordan(rows,prec.get(),cof,bs,x.tolist())
                res_v=Toplevel()
                res_v.title("Solution")
                res_v.iconphoto(False, icon_img)
                res_v.config(background="silver")
                res_v.geometry(f'{700}x{700}+{100}+{70}')
                res_v.config()
                fr2=Frame(master=res_v,bg="#FCFCFC")
                my_canvas=Canvas(fr2,scrollregion=(0,0,1000,1000),height=400,width=800)
                scl_y=tk.Scrollbar(fr2,orient=tk.VERTICAL,command=my_canvas.yview)
                fr3=Frame(my_canvas)
                fr2.pack(fill=BOTH,expand=True)
                my_canvas.place(x=100,y=0)
                scl_y.pack(side=tk.RIGHT,fill=tk.Y,expand=True)
                my_canvas.configure(yscrollcommand=scl_y.set)
                my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                my_canvas.create_window(50,50,window=fr3,anchor=tk.CENTER)
                res_lab=Label(fr3,text="Forward Elimination ",padx=20, font=('Times', 15))
                res_lab.pack()
                res_lab1=Label(fr3,text="Steps:  "+str(np.array(step['Forward Elimination'])),padx=20, font=('Times', 20))
                res_lab1.pack()
                res_lab2=Label(fr3,text="Backward Elimination ",padx=20, font=('Times', 15))
                res_lab2.pack()
                res_lab3=Label(fr3,text="Steps:  "+str(np.array(step['Backward Elimination'])),padx=20, font=('Times', 20))
                res_lab3.pack()
                res_lab5=Label(fr3,text="Solution:  "+str(data),padx=20, font=('Times', 20))
                res_lab5.pack(anchor=S)
                res_lab6=Label(fr3,text="Time:  "+str(t),padx=20, font=('Times', 20))
                res_lab6.pack(anchor=S)
            elif clicked.get()=="LU Decomposition":
                data=[]
                if type_var.get()==1:
                    cof=x[:rows,:cols-1]
                    bs=x[:rows,cols-1:cols].reshape(rows,)
                    res,data,time=LU.doolittle(cof,bs,5)
                    res_v=Toplevel()
                    res_v.title("Solution")
                    res_v.iconphoto(False, icon_img)
                    res_v.config(background="silver")
                    res_v.geometry(f'{700}x{700}+{100}+{70}')
                    if res!='':
                        labm3=Label(res_v,text="L matrix",padx=20, font=('Times', 20))
                        labm3.pack()
                        labm1=Label(res_v,text=str(np.array(res["L"])),padx=20, font=('Times', 20))
                        labm1.pack()
                        labm4=Label(res_v,text="U matrix",padx=20, font=('Times', 20))
                        labm4.pack()
                        labm2=Label(res_v,text=str(np.array(res["U"])),padx=20, font=('Times', 20))
                        labm2.pack()
                    labm=Label(res_v,text="Solution"+str(data),padx=20, font=('Times', 20))
                    labm.pack()
                    labm1=Label(res_v,text="time"+str(time),padx=20, font=('Times', 20))
                    labm1.pack()
                elif type_var.get()==2:
                    cof=x[:rows,:cols-1]
                    bs=x[:rows,cols-1:cols].reshape(rows,)
                    res,data,time=LU.crout(cof,bs,prec.get())
                    res_v=Toplevel()
                    res_v.title("Solution")
                    res_v.iconphoto(False, icon_img)
                    res_v.config(background="silver")
                    res_v.geometry(f'{700}x{700}+{100}+{70}')
                    if res!='':
                        labm3=Label(res_v,text="L matrix",padx=20, font=('Times', 20))
                        labm3.pack()
                        labm1=Label(res_v,text=str(np.array(res["L"])),padx=20, font=('Times', 20))
                        labm1.pack()
                        labm4=Label(res_v,text="U matrix",padx=20, font=('Times', 20))
                        labm4.pack()
                        labm2=Label(res_v,text=str(np.array(res["U"])),padx=20, font=('Times', 20))
                        labm2.pack()
                    res_lab=Label(res_v,text="Solution"+str(np.array(data)),padx=20, font=('Times', 20))
                    res_lab.pack()
                    res_lab2=Label(res_v,text="time"+str(time),padx=20, font=('Times', 20))
                    res_lab2.pack()
                elif type_var.get()==3:
                    cof=x[:rows,:cols-1]
                    bs=x[:rows,cols-1:cols].reshape(rows,)
                    res,data,time=LU.cholesky(cof,bs,prec.get())
                    res_v=Toplevel()
                    res_v.title("Solution")
                    res_v.iconphoto(False, icon_img)
                    res_v.config(background="silver")
                    res_v.geometry(f'{700}x{700}+{100}+{70}')
                    if res!='':
                        labm3=Label(res_v,text="L matrix",padx=20, font=('Times', 20))
                        labm3.pack()
                        labm1=Label(res_v,text=str(np.array(res["L"])),padx=20, font=('Times', 20))
                        labm1.pack()
                        labm4=Label(res_v,text="U matrix",padx=20, font=('Times', 20))
                        labm4.pack()
                        labm2=Label(res_v,text=str(np.array(res["U"])),padx=20, font=('Times', 20))
                        labm2.pack()
                    res_lab=Label(res_v,text="Solution"+str(np.array(data)),padx=20, font=('Times', 20))
                    res_lab.pack()
                    res_lab2=Label(res_v,text="time"+str(time),padx=20, font=('Times', 20))
                    res_lab2.pack()
            elif clicked.get()=="Gauss-Seidel":
                cof=x[:rows,:cols-1].tolist()
                bs=x[:rows,cols-1:cols].reshape(rows,).tolist()
                first_guess=[]
                for i in fir_guess:
                    first_guess.append(int(i.get()))
                data,Ans,end,noOfIterations=gaj.gauss_siedel(rows,rows,numberofiter.get(),relerror.get(),prec.get(),first_guess,cof,bs)

                res_v=Toplevel()
                res_v.title("Solution")
                res_v.iconphoto(False, icon_img)
                res_v.config(background="silver")
                res_v.geometry(f'{700}x{700}+{100}+{70}')
                fr2=Frame(master=res_v,bg="#FCFCFC")
                my_canvas=Canvas(fr2,scrollregion=(0,0,1000,1000),height=400,width=800)
                scl_y=tk.Scrollbar(fr2,orient=tk.VERTICAL,command=my_canvas.yview)
                fr3=Frame(my_canvas)
                fr2.pack(fill=BOTH,expand=True)
                my_canvas.place(x=100,y=0)
                scl_y.pack(side=tk.RIGHT,fill=tk.Y)
                my_canvas.configure(yscrollcommand=scl_y.set)
                my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                my_canvas.create_window(50,50,window=fr3,anchor=tk.CENTER)

                if data!='':
                    res_lab=Label(res_v,text="Steps",padx=20, font=('Times', 20))
                    res_lab.pack()
                    res_lab1=Label(res_v,text=str(np.array(data['Steps'])),padx=20, font=('Times', 20))
                    res_lab1.pack()
                res_lab2=Label(res_v,text="answer:  "+str(Ans),padx=20, font=('Times', 20))
                res_lab2.pack()
                res_lab3=Label(res_v,text="time:   "+str(end),padx=20, font=('Times', 20))
                res_lab3.pack()
                res_lab5=Label(res_v,text="Number of iteration:  "+str(noOfIterations),padx=20, font=('Times', 20))
                res_lab5.pack(anchor=S)
            elif clicked.get()=="Jacobi-Iteration":
                cof=x[:rows,:cols-1].tolist()
                bs=x[:rows,cols-1:cols].reshape(rows,).tolist()
                first_guess=[]
                for i in fir_guess:
                    first_guess.append(int(i.get()))
                data,Ans,end,noOfIterations=gaj.jacobi(rows,rows,numberofiter.get(),relerror.get(),prec.get(),first_guess,cof,bs)
                
                res_v=Toplevel()
                res_v.title("Solution")
                res_v.iconphoto(False, icon_img)
                res_v.config(background="silver")
                res_v.geometry(f'{700}x{700}+{100}+{70}')
                fr2=Frame(master=res_v,bg="#FCFCFC")
                my_canvas=Canvas(fr2,scrollregion=(0,0,1000,1000),height=500,width=600)
                scl_y=tk.Scrollbar(fr2,orient=tk.VERTICAL,command=my_canvas.yview)
                fr3=Frame(my_canvas)
                fr2.pack(fill=BOTH,expand=True)
                my_canvas.pack(side=LEFT,fill=BOTH,anchor='nw')
                scl_y.pack(side=tk.RIGHT,fill=tk.Y)
                my_canvas.configure(yscrollcommand=scl_y.set)
                my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
                my_canvas.create_window(50,50,window=fr3,anchor=tk.CENTER)

                if data!='':
                    res_lab=Label(fr3,text="Steps",padx=20, font=('Times', 20))
                    res_lab.pack()
                    res_lab1=Label(fr3,text=str(np.array(data['Steps'])),padx=20, font=('Times', 10))
                    res_lab1.pack()
                    res_lab3=Label(fr3,text="time:   "+str(end),padx=20, font=('Times', 20))
                    res_lab3.pack()
                    res_lab5=Label(fr3,text="Number of iteration:  "+str(noOfIterations),padx=20, font=('Times', 20))
                    res_lab5.pack(anchor=S)
                res_lab2=Label(fr3,text="answer:  "+str(Ans),padx=20, font=('Times', 20))
                res_lab2.pack()

    def backf(self):
        fr2.pack_forget()
        fr1.pack(fill=BOTH,expand=True)
    
    def set_type(self,name):
        global type_var
        global fir_guess
        global numberofiter
        global relerror
        fir_guess=[]
        i=410
        if name=="LU Decomposition":
            for i in arr_we:
                i.place_forget()
            arr_we.clear()
            types=[('Doolittle',1),('Crout',2),('Cholesky',3)]
            type_var=IntVar()
            type_var.set('Doolittle')
            for txt,value in types:
                wedgit=Radiobutton(fr2,text=txt,variable=type_var,value=value)
                arr_we.append(wedgit)
                wedgit.place(x=550,y=i)
                i+=20
        elif name=="Gauss-Seidel" or name=="Jacobi-Iteration":
            for i in arr_we:
                i.place_forget()
            arr_we.clear()
            fir_guess.clear()
            numberofiter=IntVar()
            relerror=DoubleVar()
            numberofiter.set(20)
            relerror.set(1e-3)
            lab1=Label(fr2,text="number of iterations")
            ent1=Entry(fr2,width=5,textvariable=numberofiter,justify="center", font=('Times', 20))
            lab2=Label(fr2,text="relative error(%)")
            ent2=Entry(fr2,width=8,textvariable=relerror,justify="center", font=('Times', 20))
            lab1.place(x=410,y=410)
            ent1.place(x=420,y=430)
            lab2.place(x=550,y=410)
            ent2.place(x=550,y=430)
            counter=50
            arr_we.append(lab1)
            arr_we.append(lab2)
            arr_we.append(ent1)
            arr_we.append(ent2)
            for i in range (1,cols):
                inputs=StringVar()
                inputs.set(0)
                count=Label(fr2,text="X"+str(i),padx=20, font=('Times', 15))
                enter=Entry(fr2, width=4,textvariable=inputs,justify="center", font=('Times', 15))
                count.place(x=counter,y=550)
                enter.place(x=counter,y=600)
                fir_guess.append(inputs)
                arr_we.append(count)
                arr_we.append(enter)
                counter+=70
        else:
            for i in arr_we:
                i.place_forget()


