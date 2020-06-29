from tkinter import *
from tkinter import messagebox

from user.user import User
from gui.interactive_list import InteractiveListGUI

class UserComponent(InteractiveListGUI):

    def __init__(self, root):
        self.user_comp = LabelFrame(root, height=500, width=320)
        self.user_comp.grid(row=0, column=0, ipadx=2, ipady=2, sticky=NW)
        self.max_length = 6

        super().__init__(root=self.user_comp, title="Users", deselected_col="grey", selected_col="purple", font="Helvetica", label_font_size=14, title_font_size=20, max_length=self.max_length)

        add_user_button = Button(self.user_comp, text="Add User", command= self._add_user).grid(row=6, column=0, ipadx=15, ipady=8, padx=(5, 0), pady=5)
        info_button = Button(self.user_comp, text="Show Info", command=self._show_info).grid(row=6, column=1, ipadx=15, ipady=8, padx=(5, 0), pady=5)
        remove_user_button = Button(self.user_comp, text="Remove User", command=self.remove_elem).grid(row=6, column=2, ipadx=15, ipady=8, padx=(5, 5), pady=10)
    
    """
    Adds a user to the interactive list
    """
    def _add_user(self):
        if len(self.get_all_items()) == self.max_length:
            messagebox.showerror("User Limit Reached", "Unable to add more users")
            return

        form = AddUserForm()
        self.user_comp.wait_window(form.root) # wait for the user to finish filling out the form

        info = form.get_info()
        if len(info.keys()) == 0:
            return 

        new_user = User(data=info, shoe_size=info["Shoe Size"], shirt_size=info["Shirt Size"], pant_size=info["Pant Size"])
        self.add_elem(new_user, info["Name"])
    
    """
    Show info about the selected user
    """
    def _show_info(self):
        users = self.get_all_items()
        if len(users.keys()) == 0:
            return 

        info_box = Toplevel(padx=35, pady=15)
        info_box.title(self.get_selected_value().get_data("Name"))
        info_box.resizable(0, 0)

        user_info = self.get_selected_value().get_all_data()

        for i, data in enumerate(user_info.keys()):
            Label(info_box, text=data + ": ").grid(row=i, column=0, sticky=W)
            Label(info_box, text=user_info[data]).grid(row=i, column=1, sticky=W, ipady=1)
        
        Button(info_box, text="Exit", command=lambda:info_box.destroy()).grid(row=len(user_info.keys()), column=0, columnspan=2, ipadx=40, ipady=4, pady=5)

                
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

        Label(sizeinfo, text= "Shoe Size:").grid(row = 1, column=0)
        entry = Entry(sizeinfo)
        entry.grid(row=1, column=1, ipady=2, pady=1, columnspan=5)
        self.entries["Shoe Size"] = entry
        
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
    Returns info from the submitted form
    """
    def get_info(self):
        return self.info









