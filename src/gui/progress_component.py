from tkinter import *

from gui.interactive_list import InteractiveListGUI
from user.user import User

class ProgressComponent(InteractiveListGUI):
    
    def __init__(self, root, bg="#121212", fg="#e6e6e6", button_bg="#2e2e2e", activebackground="#505050", activeforeground="#e6e6e6"):
        self.bg = bg
        self.fg = fg
        self.button_bg = button_bg
        self.activebackground = activebackground
        self.activeforeground = activeforeground

        self.progress_frame = LabelFrame(root, height=400, width=320, bg=bg)
        self.progress_frame.grid(row=0, column=3, ipadx=2, ipady=2, sticky=NE)
        self.progress_frame.grid_propagate(False)

        super().__init__(root=self.progress_frame, title="In Progress", deselected_col="#017167", selected_col="#00ae9e", font="Helvetica", 
                        label_font_size=14, title_font_size=20, max_length=4, columnspan=2, row=0, column=0, label_highlight="#00c0af", height=343)

        Button(self.progress_frame, text="Cancel", font=("Comic Sans", 9), width=20, height=2, command=self._cancel_request, bg=button_bg, fg=fg, 
                activebackground=activebackground, activeforeground=activeforeground).grid(row=3, column=0, sticky=S, pady=(9, 0))
        Button(self.progress_frame, text="Show Details", font=("Comic Sans", 9), width=20, height=2, command=self._show_details, bg=button_bg, fg=fg, 
                activebackground=activebackground, activeforeground=activeforeground).grid(row=3, column=1, sticky=S, pady=(9, 0))

    """
    Cancels the selected request
    """
    def _cancel_request(self):

        if self.get_selected_value() is None:
            return 

        value = self.elem_list[self.get_selected_key()]
        value["valid"] = False

        self.remove_elem()
    
    """
    Remove a request from the list by the value

    value: A {time, user, link} dictionary which represents the value of a request
            which is to be removed
    """
    def remove(self, value):
        for key in self.elem_list.keys():
            elem_value = self.elem_list[key]
            if  value["user"].get_all_data() == elem_value["user"].get_all_data() and value["link"] == elem_value["link"] and value["time"] == elem_value["time"]:
                self.remove_elem_by_key(key)
                return 

    """
    Show details about the request to the user
    """
    def _show_details(self):
        value = self.get_selected_value()

        if value is None:
            return

        info_box = Toplevel(padx=35, pady=15, bg=self.bg)
        info_box.title("Request Information")
        info_box.iconbitmap("images/hypershopper_favicon.ico")
        info_box.resizable(0, 0)

        labels =  ["Time", "User", "Link"]

        for i, data in enumerate(list(value.values())[:len(value.values()) - 1]):
            Label(info_box, text=labels[i] + ": ", bg=self.bg, fg=self.fg).grid(row=i, column=0, sticky=W)
            Label(info_box, text=data.get_data("Name") if isinstance(data, User) else f"{data[0]}:{data[1]}" if isinstance(data, tuple) else data, 
                bg=self.bg, fg=self.fg).grid(row=i, column=1, sticky=W, ipady=1)

        Button(info_box, text="Exit", command=lambda:info_box.destroy(), bg=self.button_bg, fg=self.fg, activebackground=self.activebackground, 
                activeforeground=self.activeforeground).grid(row=len(value.keys()), column=0, columnspan=2, ipadx=40, ipady=4, pady=5)






        

    


    

        