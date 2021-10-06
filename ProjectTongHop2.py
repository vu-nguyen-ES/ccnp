from tkinter import *
from XuLyFile2 import *

def ThemAction():
    line = stringMa.get()+";"+stringTen.get()+";"+stringNam.get()
    LuuFile(line)
    ShowSach()
def ShowSach():
    arr = DocFile()
    listbox.delete(0,END)
    for item in arr:
        listbox.insert(END,item)
def TimAction():
    arr = DocFile()
    ma = stringMa.get()
    found = False
    i=0

    for sach in arr:
        if sach[0]==ma:
            found=True
            i = sach
            break

    if found:
        listbox.delete(0,END)
        listbox.insert(END,i)
    else:
        listbox.delete(0,END)
        listbox.insert(END,"Ma Khong Dung")

def SapXepAction():
    arr= DocFile()
    for i in range(len(arr)):
        for j in range(len(arr)):
            a= arr[i]
            b = arr[j]
            if a[2]>b[2]:
                arr[i]=b
                arr[j]=a
    listbox.delete(0,END)
    for item in arr:
        listbox.insert(END,item)
root = Tk()

stringMa = StringVar()
stringTen = StringVar()
stringNam = StringVar()

root.title("Quan Ly Sach")
root.resizable(height=True,width=True)
root.minsize(height=300,width=310)
#Listbox
listbox = Listbox(root,width=50)
listbox.grid(row=1,columnspan=2)
ShowSach()
#Label
Label(root,text="Quan Ly Sach",font=("tohoma",16),fg="red").grid(row=0,columnspan=2)
#Button
framebutton = Frame()
Button(framebutton,text="Them",command=ThemAction).pack(side=LEFT)
Button(framebutton,text="Tim",command=TimAction).pack(side=LEFT)
Button(framebutton,text="Sap Xep",command=SapXepAction).pack(side=LEFT)
Button(framebutton,text="Thoat",command=quit).pack(side=LEFT)
framebutton.grid(row=5,column=1)
#Entry
Label(root,text="Ma Sach:").grid(row=2,column=0)
Entry(root,width=30,textvariable = stringMa).grid(row=2,column=1)
Label(root,text="Ten Sach:").grid(row=3,column=0)
Entry(root,width=30,textvariable=stringTen).grid(row=3,column=1)
Label(root,text="Nam Xuat Ban:").grid(row=4,column=0)
Entry(root,width=30,textvariable=stringNam).grid(row=4,column=1)
root.mainloop()