from tkinter import *

class AddUserForm:

    def __init__(self):
        self.root = Toplevel(padx=20, pady=20)
        self.root.title("Add User")
        self.root.geometry("530x360")
        self.root.resizable(0,0)

        self.entries = {i : None for i in ["Name", "Email", "Tel", "Address", "Zip", "City", "Province", "Country", 
                                        "Card Number", "Exp Date", "CVV", "Shoe Size", "Shirt Size", "Pant Size"]}
        self.info = {}
        self._create_form()
        submit_form = Button(self.root, text="Add", padx=200, pady=8, command=self._on_submit).grid(row=4, column=0, columnspan=2, sticky=N, pady=5)
        

    """
    Create a new form
    """
    def _create_form(self):

        #billing and shipping info
        shipinfo = LabelFrame(self.root, padx=10, pady=10)
        shipinfo.grid(row=0, column=0, rowspan=3, sticky=N)
        title = Label(shipinfo, text="Billing/Shipping Information").grid(row=0, column=0, columnspan=2, pady=(0, 3))

        for i, info in enumerate(list(self.entries.keys())[:8]):
            entry = Entry(shipinfo)
            if i == 7: 
                Label(shipinfo, text=info + ":").grid(row = i + 1, sticky=W, pady=(1, 38))
                entry.grid(row = i + 1, column=1, ipadx="30", ipady=2, pady=(1, 38))
            else:
                Label(shipinfo, text=info + ":").grid(row = i + 1, sticky=W)
                entry.grid(row = i + 1, column=1, ipadx="30", ipady=2, pady=1)
            self.entries[info] = entry

        #credit card info
        cardinfo = LabelFrame(self.root, padx=10, pady=10)
        cardinfo.grid(row=0, column=1, sticky=N)
        title = Label(cardinfo, text="Credit Card Information").grid(row=0, column=0, columnspan=2, pady=(0, 3))

        for i, info in enumerate(list(self.entries.keys())[8:11]):
            Label(cardinfo, text=info + ":").grid(row = i + 1, sticky=W)
            entry = Entry(cardinfo)
            entry.grid(row = i + 1,column=1, ipady=2, pady=1)
            self.entries[info] = entry

        #user size info
        sizeinfo = LabelFrame(self.root, padx=14, pady=10)
        sizeinfo.grid(row=1, column=1, sticky=NW)
        Label(sizeinfo, text="Size").grid(row=0, column=0, columnspan=6)

        for i, info in enumerate(list(self.entries.keys())[11:12]):
            Label(sizeinfo, text=info + ":").grid(row = i + 1, column=0)
            entry = Entry(sizeinfo)
            entry.grid(row=i + 1, column=1, ipady=2, pady=1, columnspan=5)
            self.entries[info] = entry
        
        sizes = { "XS":"XSmall", "S":"Small", "M":"Medium","L":"Large", "XL":"XLarge"}

        self.entries["Shirt Size"] = StringVar()
        self.entries["Pant Size"] = StringVar()
        self.entries["Shirt Size"].set("Large")
        self.entries["Pant Size"].set("Large")

        Label(sizeinfo, text="Shirt Size:").grid(row = 3, column=0)
        Label(sizeinfo, text="Pant Size:").grid(row = 5, column=0)

        for i, size in enumerate(sizes.keys()):
            Label(sizeinfo, text=size).grid(row=2, column=i + 1)
            Radiobutton(sizeinfo, variable=self.entries["Shirt Size"], value=sizes[size]).grid(row=3, column=i + 1)
            Label(sizeinfo, text=size).grid(row=4, column=i + 1)
            Radiobutton(sizeinfo, variable=self.entries["Pant Size"], value=sizes[size]).grid(row=5, column=i + 1)
    
    """
    Extract info from the form and make sure all info is valid
    """
    def _on_submit(self):
        
        self.info = {info : entry.get() for info, entry in zip(self.entries.keys(), self.entries.values())}
        self.root.destroy()
    
    """
    Returns info from the form
    """
    def get_info(self):
        return self.info

    def done(self):
        return  len(self.info.keys()) != 0


"""
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

"""
