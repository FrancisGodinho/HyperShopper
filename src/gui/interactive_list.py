from tkinter import *
from tkinter import messagebox

class InteractiveListGUI:

    def __init__(self, title, root, deselected_col="grey", selected_col="red", font="Helvetica", label_font_size=14, title_font_size=20, max_length=4, width=320, height=440):
        
        self.deselected_col = deselected_col
        self.selected_col = selected_col
        self.font = font
        self.label_font_size = label_font_size
        self.title_font_size = title_font_size
        self.max_length = max_length
        
        self.frame = Frame(root, height=height, width=width)
        self.frame.grid(row=1, column=0, columnspan=3)
        self.frame.pack_propagate(False)

        self.elem_list = {}
        self.current_elem = None

        Label(self.frame, text=title, font=(self.font, self.title_font_size)).pack(pady=2)
        
    def add_elem(self, elem, label):
        if len(self.elem_list) == self.max_length:
            messagebox.showerror("Element Limit Reached", "Unable to add more elements")
            return 
        info_label = Button(self.frame, text=label, relief=FLAT, width=18, height=1)
        info_label.pack(pady=5)
        info_label.configure(command=lambda button=info_label: self._set_curr_elem(button), font=(self.label_font_size, self.title_font_size))
        
        self.elem_list[info_label] = elem
        self._set_curr_elem(info_label)

    def _set_curr_elem(self, selection):
        selection.configure(bg=self.selected_col)
        self.current_elem = selection

        for elem in self.elem_list.keys():
            if elem != selection:
                elem.configure(bg=self.deselected_col)

    def remove_elem(self):
        if len(self.elem_list.keys()) > 0:

            del self.elem_list[self.current_elem]
            self.current_elem.destroy()

            if len(self.elem_list.keys()) > 0:
                self._set_curr_elem(list(self.elem_list.keys())[-1])

    def get_selected_key(self):
        return self.current_elem
    
    def get_selected_value(self):
        return self.elem_list[self.current_elem]

    def get_all_items(self):
        return self.elem_list