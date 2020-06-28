from tkinter import *

class AddUserForm:

    def __init__(self):
        self.root = Toplevel(padx=20, pady=20)
        self.root.title("Add User")
        self.root.geometry("530x320")
        root.resizable(0,0)

        self.entries = {i : None for i in ["Name", "Email", "Tel", "Address", "Zip", "City", "Province", "Country", 
                                        "Card Number", "Exp Date", "CVV", "Shoe Size", "Shirt Size", "Pant Size"]}
        
        self.create_form()
        submit_form = Button(self.root, text="Submit", padx=200, pady=8, command=self.on_submit).grid(row=4, column=0, columnspan=2, sticky=N, pady=5)
        

    def create_form(self):

        #billing and shipping info
        shipinfo = LabelFrame(self.root, padx=10, pady=10)
        shipinfo.grid(row=0, column=0, rowspan=3)
        title = Label(shipinfo, text="Billing/Shipping Information").grid(row=0, column=0, columnspan=2)

        for i, info in enumerate(list(self.entries.keys())[:8]):
            Label(shipinfo, text=info + ":").grid(row = i + 1, sticky=W)
            entry = Entry(shipinfo)
            entry.grid(row = i + 1, column=1, ipadx="30", ipady=2, pady=1)
            self.entries[info] = entry

        #credit card info
        cardinfo = LabelFrame(self.root, padx=10, pady=10)
        cardinfo.grid(row=0, column=1, sticky=N)
        title = Label(cardinfo, text="Credit Card Information").grid(row=0, column=0, columnspan=4)

        for i, info in enumerate(list(self.entries.keys())[8:11]):
            Label(cardinfo, text=info + ":").grid(row = i + 1, sticky=W)
            entry = Entry(cardinfo)
            entry.grid(row = i + 1,column=1, ipady=2, pady=1)
            self.entries[info] = entry

        #user size info
        sizeinfo = LabelFrame(self.root, padx=21, pady=12)
        sizeinfo.grid(row=1, column=1, sticky=NW)
        Label(sizeinfo, text="Size").grid(row=0, column=0, columnspan=2)

        for i, info in enumerate(list(self.entries.keys())[11:]):
            Label(sizeinfo, text=info + ":").grid(row = i + 1, column=0)
            entry = Entry(sizeinfo)
            entry.grid(row=i + 1,column=1, ipady=2, pady=1)
            self.entries[info] = entry

    def on_submit(self):
        self.info = {info : entry.get() for info, entry in zip(self.entries.keys(), self.entries.values())}
        self.root.destroy()
         
    def get_info(self):
        return self.info

        



def add_user():
    global form
    form = AddUserForm()

def info():
    global form
    print(form.get_info())


form = None
root = Tk()
button = Button(root, text="Add User", command=add_user).pack()
button = Button(root, text="print info", command=info).pack()




root.mainloop()


