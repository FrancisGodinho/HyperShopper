from tkinter import *

from gui.add_user import AddUserForm
from user.user import User

class UserComponent:

    def __init__(self, root):
        self.user_comp = LabelFrame(root, height=500, width=320)
        self.user_comp.grid(row=0, column=0, ipadx=2, ipady=2, sticky=W)
         
        self.users = {}
        self.current_user = None

        self._create_user_component()

    def get_current_user(self):
        return self.users[self.current_user]

    def _create_user_component(self):
        self.user_list = Frame(self.user_comp, height=430, width=320)
        self.user_list.grid(row=1, column=0, columnspan=3)
        self.user_list.pack_propagate(False)

        Label(self.user_list, text="Users", font=("Helvetica", 20)).pack(pady=2)
        
        add_user_button = Button(self.user_comp, text="Add User", command= self._add_user).grid(row=6, column=0, ipadx=15, ipady=10, padx=(5, 0), pady=10)
        info_button = Button(self.user_comp, text="Show Info", command=self._show_info).grid(row=6, column=1, ipadx=15, ipady=10, padx=(5, 0), pady=10)
        remove_user_button = Button(self.user_comp, text="Remove User", command=self._remove_user).grid(row=6, column=2, ipadx=15, ipady=10, padx=(5, 5), pady=10)
    
    def _add_user(self):
        form = AddUserForm()
        self.user_comp.wait_window(form.root) # wait for the user to finish filling out the form

        info = form.get_info()
        new_user = User(data=info, shoe_size=info["Shoe Size"], shirt_size=info["Shirt Size"], pant_size=info["Pant Size"])

        user_label = Button(self.user_list, text=info["Name"], relief=FLAT, width=25, height=2)
        user_label.pack(pady=5)
        user_label.configure(command=lambda button=user_label: self._set_curr_user(button), font=("Helvetica", 15))
        
        self.users[user_label] = new_user
        self._set_curr_user(user_label)
        
    def _set_curr_user(self, selection):
        selection.configure(bg="purple")
        self.current_user = selection

        for user in self.users.keys():
            if user != selection:
                user.configure(bg="light grey")
        
    def _show_info(self):
        if len(self.users.keys()) == 0:
            return 

        info_box = Toplevel(padx=35, pady=15)
        info_box.title(self.users[self.current_user].get_data("Name"))
        info_box.resizable(0, 0)

        user_info = self.users[self.current_user].get_all_data()

        for i, data in enumerate(user_info.keys()):
            Label(info_box, text=data + ": ").grid(row=i, column=0, sticky=W)
            Label(info_box, text=user_info[data]).grid(row=i, column=1, sticky=W, ipady=1)
        
        Button(info_box, text="Exit", command=lambda:info_box.destroy()).grid(row=len(user_info.keys()), column=0, columnspan=2, ipadx=40, ipady=4, pady=5)

    def _remove_user(self):
        if len(self.users.keys()) > 0:

            del self.users[self.current_user]
            self.current_user.destroy()

            if len(self.users.keys()) > 0:
                self._set_curr_user(list(self.users.keys())[-1])
                
root = Tk()
root.title("Hyper Shopper")
root.geometry("800x500")
root.resizable(0, 0)

user = UserComponent(root)

root.mainloop()








