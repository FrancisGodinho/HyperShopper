from tkinter import *

from gui.interactive_list import InteractiveListGUI
from user.user import User

class ProgressComponent(InteractiveListGUI):
    
    def __init__(self, root):
        self.progress_frame = LabelFrame(root, height=500, width=320)
        self.progress_frame.grid(row=0, column=3, ipadx=2, ipady=2, sticky=NE)
        self.progress_frame.grid_propagate(False)

        super().__init__(root=self.progress_frame, title="In Progress", deselected_col="grey", selected_col="purple", font="Helvetica", 
                        label_font_size=14, title_font_size=20, max_length=6, columnspan=2, row=0, column=0)

        Button(self.progress_frame, text="Cancel", width=20, height=2, command=self._cancel_request).grid(row=3, column=0, sticky=S, pady=(9, 0))
        Button(self.progress_frame, text="Show Details", width=20, height=2, command=self._show_details).grid(row=3, column=1, sticky=S, pady=(9, 0))

    def _cancel_request(self):

        if self.get_selected_value() is None:
            return 

        value = self.elem_list[self.get_selected_key()]
        value["valid"] = False

        self.remove_elem()
    
    def remove(self, value):
        for key in self.elem_list.keys():
            elem_value = self.elem_list[key]
            if  value["user"].get_all_data() == elem_value["user"].get_all_data() and value["link"] == elem_value["link"] and value["time"] == elem_value["time"]:
                self.remove_elem_by_key(key)
                return 

    def _show_details(self):
        value = self.get_selected_value()

        if value is None:
            return

        info_box = Toplevel(padx=35, pady=15)
        info_box.title("Request Information")
        info_box.resizable(0, 0)

        labels =  ["Time", "User", "Link"]

        for i, data in enumerate(list(value.values())[:len(value.values()) - 1]):
            Label(info_box, text=labels[i] + ": ").grid(row=i, column=0, sticky=W)
            Label(info_box, text=data.get_data("Name") if isinstance(data, User) else data).grid(row=i, column=1, sticky=W, ipady=1)

        Button(info_box, text="Exit", command=lambda:info_box.destroy()).grid(row=len(value.keys()), column=0, columnspan=2, ipadx=40, ipady=4, pady=5)






        

    


    

        