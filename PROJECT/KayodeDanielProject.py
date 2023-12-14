# ------------NAME:          KAYODE DANIEL------------------
# ------------PROJECT TOPIC: CONTACT BOOK-------------------
# ------------DEPARTMENT:    NCAIR--------------------------
# ------------DATE:          8TH DECEMBER, 2023.------------


# To create a contact book project(python) using the Graphical user Interface(GUI)
# Contact book is a GUI-based project built using Python Tkinter module and message module
# A contact book is used to store some person’s contacts like name, phone number etc.
# In this project we have some functionality like add, edit, delete, view, and reset contacts.

# Step 1- Importing Modules

#PythonGeeks - import library
from tkinter import *
from tkinter import messagebox

#Step 2- Initializing the window

root = Tk()
root.geometry('600x480')
root.config(bg = '#2f4f4f')
root.title('Cayodeys Contact Book')
root.resizable(0,0)
contactlist = [
    ['Mansur Usman','08135400000'],
    ['Agenyi Abel', '08153240000'],
    ['Stephen Kuku', '08091060000'],
    ['Ejike Alphonsus', '07039300000'],
    ['Khalid Aliyu', '07010050000'],
    ['Ruth Bishio', '09046460000'],
    ['Kayode Daniel', '08060000000'],
    ['Aisha Ismail', '07051280000'],
    ['Queen Oge','09112380000'],
    ['Marshal Andy', '09024550000'],
    ['Rayan Bello', '07026440000'],
    ['Sylvia Baby', '080333250000'],
    ['Favour Nnana', '08036540000'],
    ['Tim Monejo', '07095840000'],
    ['Madaaki Abdulahhi', '08047150000'],
    ['Lady Vivian', '07125840000'],
    ['Austin Harrison', '09055410000'],
    ['Muhammad R Shehu', '090354210000'],
    ['Al-amin J. Bashir', '070653210000'],
    ['Godspower Asokoro', '070363510000'],
    ['Samuel K.O.', '080959630000'],
    ['Joshua Bashorun', '090475810000'],
    ['Oluwaseun Adeniji', '08032140000'],
    ]
 
Name = StringVar()
Number = StringVar()

#Step 3- Create frame

frame = Frame(root)
frame.pack(side = RIGHT)
 
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman' ,16), bg="#f0fffc", width=20, height=20, borderwidth=3, relief= "groove")
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)

# Step 4- Function to get select value
 
def Selected():
    print("hello",len(select.curselection()))
    if len(select.curselection())==0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])
    
# step 5-function to add new contact
def AddContact():
    if Name.get()!="" and Number.get()!="":
        contactlist.append([Name.get() ,Number.get()])
        print(contactlist)
        Select_set()
        # EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Add New Contact")
 
    else:
        messagebox.showerror("Error","Please fill the information")
 
def UpdateDetail():
    if Name.get() and Number.get():
        contactlist[Selected()] = [Name.get(), Number.get()]
   
        messagebox.showinfo("Confirmation", "Successfully Update Contact")
        # EntryReset()
        Select_set()
 
    elif not(Name.get()) and not(Number.get()) and not(len(select.curselection())==0):
        messagebox.showerror("Error", "Please fill the information")
 
    else:
        if len(select.curselection())==0:
            messagebox.showerror("Error", "Please Select the Name and \n press Load button")
        else:
            message1 = """To Load the all information of \n
                          selected row press Load button\n.
                          """
            messagebox.showerror("Error", message1)
def Delete_Entry():
    if len(select.curselection())!=0:
        result=messagebox.askyesno('Confirmation','You Want to Delete Contact\n Which you selected')
        if result==True:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')
 
def VIEW():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)

#to exit game window  

def EXIT():
    root.destroy() 
 
def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone in contactlist :
        select.insert (END, name)
Select_set()

#to define buttons labels and entry widget

Label(root, text = 'Name', font=("Times new roman",20,"bold"), bg = 'SpringGreen1').place(x= 27, y=17)
Entry(root, textvariable = Name, width=20).place(x= 200, y=30)
Label(root, text = 'Contact No.', font=("Times new roman",18,"bold"),bg = 'SpringGreen1').place(x= 30, y=70)
Entry(root, textvariable = Number, width=20).place(x= 200, y=80)
 
Button(root,text=" ADD", font='Times 18 bold',bg='#836fff', command = AddContact, padx=20). place(x= 50, y=140)
Button(root,text="EDIT", font='Times 18 bold',bg='#836fff',command = UpdateDetail, padx=20).place(x= 50, y=200)
Button(root,text="DELETE", font='Times 18 bold',bg='#836fff',command = Delete_Entry, padx=20).place(x= 50, y=260)
Button(root,text="VIEW", font='Times 18 bold',bg='#836fff', command = VIEW).place(x= 50, y=325)
# Button(root,text="RESET", font='Helvetica 18 bold',bg='#e8c1c7', command = EntryReset).place(x= 50, y=390)
Button(root,text="EXIT", font='Times 20 bold',bg='tomato', command = EXIT).place(x= 200, y=420)
 
root.mainloop()
