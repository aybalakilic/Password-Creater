from tkinter import *
import random

main=Tk()

main.title("Password Creater")
main.resizable(False,False)

canva=Canvas(main,height=500,width=600)
canva.pack()

topFrame = Frame(main,width=580,height=100,bg="black")
topFrame.place(x=10,y=10)

passwordLabel=Label(topFrame,text="Your Password:",font=("Times-20",20),bg="black",fg="green")
passwordLabel.place(x=10,y=10)

middleFrame=Frame(main,width=580,height=300,bg="black")
middleFrame.place(x=10,y=120)

lengthLabel=Label(middleFrame,text="Length:",font=("Times-20",20),bg="black",fg="white")
lengthLabel.place(x=10,y=10)

entry=Entry(middleFrame,font=("Times-20",18,"bold"),bg="white",fg="black")
entry.place(x=10,y=50)


v1=IntVar()
capitalButton=Checkbutton(middleFrame,text="Uppercase",font=("Times-20",15),bg="green",fg="black",variable=v1,onvalue=1,offvalue=0)
capitalButton.place(x=330,y=10)

v2=IntVar()
lowerButton=Checkbutton(middleFrame,text="Lowercase",font=("Times-20",15),bg="green",fg="black",variable=v2,onvalue=1,offvalue=0)
lowerButton.place(x=330,y=60)

v3=IntVar()
numbersButton=Checkbutton(middleFrame,text="Numbers",font=("Times-20",15),bg="green",fg="black",variable=v3,onvalue=1,offvalue=0)
numbersButton.place(x=330,y=110)

v4=IntVar()
symbolButton=Checkbutton(middleFrame,text="Symbols",font=("Times-20",15),bg="green",fg="black",variable=v4,onvalue=1,offvalue=0)
symbolButton.place(x=330,y=160)

def func():
   
    uppercases=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","Y","Z","X","Q","W"]
    lowercases=["a","b","c","d","e","f","g","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z","x","q","w"]
    numbers=["0","1","2","3","4","5","6","7","8","9"]
    symbols=["!","£","#","$","&","?","*","/","@","<",">"]

    length=int(entry.get())


    if v1.get()==1 and v2.get()==0 and v3.get()==0 and v4.get()==0:
        result=random.sample(uppercases,length)
        passwordLabel.config(text=result)
    elif v1.get()==0 and v2.get()==1 and v3.get()==0 and v4.get()==0:
        result=random.sample(lowercases,length)
        passwordLabel.config(text=result)
    elif v1.get()==0 and v2.get()==0 and v3.get()==1 and v4.get()==0:
        result=random.sample(numbers,length)
        passwordLabel.config(text=result)
    elif v1.get()==0 and v2.get()==0 and v3.get()==0 and v4.get()==1:
        result=random.sample(symbols,length)
        passwordLabel.config(text=result)
    elif v1.get()==1 and v2.get()==1 and v3.get()==0 and v4.get()==0:
        uppercases.extend(lowercases)
        result=random.sample(uppercases,length)
        passwordLabel.config(text=result)
    elif v1.get()==1 and v2.get()==0 and v3.get()==1 and v4.get()==0:
        uppercases.extend(numbers)
        result=random.sample(uppercases,length)
        passwordLabel.config(text=result)
    elif v1.get()==1 and v2.get()==0 and v3.get()==0 and v4.get()==1:
        uppercases.extend(symbols)
        result=random.sample(uppercases,length)
        passwordLabel.config(text=result)
    elif v1.get()==0 and v2.get()==1 and v3.get()==1 and v4.get()==0:
        lowercases.extend(numbers)
        result=random.sample(lowercases,length)
        passwordLabel.config(text=result)
    elif v1.get()==0 and v2.get()==1 and v3.get()==0 and v4.get()==1:
        lowercases.extend(symbols)
        result=random.sample(lowercases,length)
        passwordLabel.config(text=result)
    elif v1.get()==0 and v2.get()==0 and v3.get()==1 and v4.get()==1:
        numbers.extend(symbols)
        result=random.sample(numbers,length)
        passwordLabel.config(text=result)
    elif v1.get()==1 and v2.get()==1 and v3.get()==1 and v4.get()==0:
        uppercases.extend(lowercases)
        uppercases.extend(numbers)
        result=random.sample(uppercases,length)
        passwordLabel.config(text=result)
    elif v1.get()==1 and v2.get()==1 and v3.get()==0 and v4.get()==1:
        uppercases.extend(lowercases)
        uppercases.extend(symbols)
        result=random.sample(uppercases,length)
        passwordLabel.config(text=result)
    elif v1.get()==0 and v2.get()==1 and v3.get()==1 and v4.get()==1:
        lowercases.extend(numbers)
        lowercases.extend(symbols)
        result=random.sample(lowercases,length)
        passwordLabel.config(text=result)
    elif v1.get()==1 and v2.get()==0 and v3.get()==1 and v4.get()==1:
        uppercases.extend(numbers)
        uppercases.extend(symbols)
        result=random.sample(uppercases,length)
        passwordLabel.config(text=result)
    elif v1.get()==1 and v2.get()==1 and v3.get()==1 and v4.get()==1:
        uppercases.extend(lowercases)
        uppercases.extend(numbers)
        uppercases.extend(symbols)
        result=random.sample(uppercases,length)
        passwordLabel.config(text=result)


createButton=Button(main,text="CREATE",font=("Times-20",18,"bold"),fg="white",bg="black",command=func)
createButton.place(x=230,y=430)

main.mainloop()