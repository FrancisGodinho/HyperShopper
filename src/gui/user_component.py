from tkinter import *
from tkinter import messagebox

from gui.add_user import AddUserForm
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

                








