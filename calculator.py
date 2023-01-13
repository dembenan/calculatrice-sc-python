from tkinter import *
import math
import tkinter.messagebox

root = Tk()

root.title("scientific calculator")
root.configure(background="blue")
root.resizable(width=False,height=False)
root.geometry("430x568+0+0")

calculator = Frame(root)
calculator.grid()
# -------------------------DEBUT ZONE DE SAISIR INFOS----------------------------------
txtDisplay = Entry(calculator,font=('arial',20,'bold'),bg="gray",bd=30,width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")
# -------------------------DEBUT LOGIQUE----------------------------------
class Calculator:
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.opper = ''
        self.result = False
        
    def numberEnter(self,num):
        self.result = False
        first_number = txtDisplay.get()
        second_number = str(num)
        
        if self.input_value:
            self.current = second_number
            self.input_value = False
        else:
            if second_number == '.':
                if second_number in first_number:
                    return
            self.current = first_number + second_number
        self.display(self.current)
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())
    def valid_function(self):
        if self.opper == 'add':
            self.total += self.current
        if self.opper == 'sub':
            self.total -= self.current
        if self.opper == 'mul':
            self.total *= self.current
        if self.operator == 'div':
            self.total /= self.current
        if self.operator == 'mod':
            self.total %= self.current
            
        self.input_value = True
        self.check_sum = False
        self.display(self.total)
        
    def operator(self,oper):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.opper = oper
        self.result = False
        
    def display(self,value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0,value)
    
    def clear(self):
        self.result = False
        if len(self.current)> 0:
            if len(self.current) == 1:
                self.display(0)
                self.input_value = True
            else:
                self.current = self.current[0:len(self.current) - 1]
                self.display(self.current)
        else:
            self.display(0)
            self.input_value = True
            
    def clearAll(self):
        self.display(0)
        self.input_value = True
    
    def pm(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)
        
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)
  
    def twopi(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)          
        
    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)  
        
    def cos(self):
        self.result = False
        self.current = math.cos(float(txtDisplay.get()))
        self.display(self.current)
        
    def cosh(self):
        self.result = False
        self.current = math.cosh(float(txtDisplay.get()))
        self.display(self.current)
        
    def sin(self):
        self.result = False
        self.current = math.sin(float(txtDisplay.get()))
        self.display(self.current)
        
    def sinh(self):
        self.result = False
        self.current = math.sinh(float(txtDisplay.get()))
        self.display(self.current)
        
    def tan(self):
        self.result = False
        self.current = math.tan(float(txtDisplay.get()))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tan(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    def mod(self):
        self.result = False
        self.current = math.modf(float(txtDisplay.get()))
        self.display(self.current)

    def deg(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)
    
    def ln(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)
#initialisation de la class    
added_value = Calculator()
        
    
# -------------------------FIN LOGIQUE----------------------------------

#les buttons
numberStandard = "789456123"
btn = []
i=0
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calculator,width=5,height=3,font=('sans-serif',20,'bold'),bd=4,text=numberStandard[i]))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]["command"] = lambda x = numberStandard[i]: added_value.numberEnter(x)
        i+=1
        
        
btnClear = Button(calculator,text=chr(67),width=5,height=3,font=('sans-serif',20,'bold'),bd=4,bg='powder blue',command=added_value.clear).grid(row=1,column=0,pady=1)
btnAllClear = Button(calculator,text=chr(67)+chr(69),width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.clearAll).grid(row=1,column=1,pady=1)
btnsq = Button(calculator,text=chr(8730),width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue').grid(row=1,column=2,pady=1)

btnAdd = Button(calculator,text="+",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue', command = lambda: added_value.operator("add")).grid(row=1,column=3,pady=1)
btnSub = Button(calculator,text="-",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue', command = lambda: added_value.operator("sub")).grid(row=2,column=3,pady=1)
btnMul = Button(calculator,text="*",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue', command = lambda: added_value.operator("mul")).grid(row=3,column=3,pady=1)
btnDiv = Button(calculator,text=chr(247),width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue', command = lambda: added_value.operator("div")).grid(row=4,column=3,pady=1)


btnZero = Button(calculator,text="0",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue',command= lambda: added_value.numberEnter("0")).grid(row=5,column=0,pady=1)
btnPoint = Button(calculator,text=".",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue',command= lambda: added_value.numberEnter(".")).grid(row=5,column=1,pady=1)
btnPM = Button(calculator,text=chr(177),width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.pm).grid(row=5,column=2,pady=1)
btnEqual = Button(calculator,text="=",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue',command= added_value.sum_of_total).grid(row=5,column=3,pady=1)

#scientifique
btnpi = Button(calculator,text="π",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.pi).grid(row=1,column=4,pady=1)
btnCos = Button(calculator,text="cos",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.cos).grid(row=1,column=5,pady=1)
btnTan = Button(calculator,text="tan",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.tan).grid(row=1,column=6,pady=1)
btnSin = Button(calculator,text="sin",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.sin).grid(row=1,column=7,pady=1)

#..../next row
btn2pi = Button(calculator,text="2π",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.twopi).grid(row=2,column=4,pady=1)
btnConh = Button(calculator,text="cosh",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.cosh).grid(row=2,column=5,pady=1)
btnTanh = Button(calculator,text="tanh",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.tanh).grid(row=2,column=6,pady=1)
btnSinh = Button(calculator,text="sinh",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.sinh).grid(row=2,column=7,pady=1)

#..../next row
btnlog = Button(calculator,text="log",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue').grid(row=3,column=4,pady=1)
btnExp = Button(calculator,text="exp",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue').grid(row=3,column=5,pady=1)
btnMod = Button(calculator,text="mod",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue').grid(row=3,column=6,pady=1)
btnE = Button(calculator,text="e",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.e).grid(row=3,column=7,pady=1)

#..../next row
btnln = Button(calculator,text="ln",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.ln).grid(row=4,column=4,pady=1)
btnDeg = Button(calculator,text="deg",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue',command=added_value.deg).grid(row=4,column=5,pady=1)
btnAcosh = Button(calculator,text="acosh",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue').grid(row=4,column=6,pady=1)
btnAsinh = Button(calculator,text="acosh",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue').grid(row=4,column=7,pady=1)

#..../next row
btnlog10 = Button(calculator,text="log10",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue').grid(row=5,column=4,pady=1)
btnlog1p = Button(calculator,text="log1p",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue').grid(row=5,column=5,pady=1)
btnExpm1 = Button(calculator,text="expm1",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue').grid(row=5,column=6,pady=1)
btnGamma = Button(calculator,text="lgamma",width=5,height=3,font=('arial',20,'bold'),bd=4,bg='powder blue').grid(row=5,column=7,pady=1)

TextextDisplay = Label(calculator,text="Scientific Calculator",font=('arial',30,'bold'),bd=4,bg='powder blue',justify=CENTER)
TextextDisplay.grid(row=0,column=4,columnspan=4)
# -------------------------FIN ZONE DE SAISIR INFOS----------------------------------



# -------------------------DEBUT FONCTIONS----------------------------------
def quitter():
    confirm = tkinter.messagebox.askyesno("Scientific calculator","Voulez-vous vraiment quitter ?")
    if confirm > 0:
        root.destroy()
        return

def scientifique():
    root.resizable(width=True,height=True)
    root.geometry("944x568+0+0")
    
def standard():
    root.resizable(width=True,height=True)
    root.geometry("485x568+0+0")  
    
# -------------------------FIN FONCTIONS----------------------------------

    
menubar = Menu(calculator)

# -------------------------DEBUT MENU----------------------------------
#menu file
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Fichier",menu=filemenu)
filemenu.add_command(label="standard",command=standard)
filemenu.add_command(label="scientific",command=scientifique)
filemenu.add_separator()
filemenu.add_command(label="Quitter",command=quitter)

#menu edit
editmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Editer",menu=editmenu)
editmenu.add_command(label="couper")
editmenu.add_command(label="copier")
editmenu.add_separator()
editmenu.add_command(label="coller")

#menu d'aide
helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Aide",menu=helpmenu)
helpmenu.add_command(label="Obtenir de l'aide")

root.config(menu=menubar)
# -------------------------FIN MENU----------------------------------






root.mainloop()


