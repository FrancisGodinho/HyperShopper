from tkinter import *
from tkinter import messagebox

class InteractiveListGUI:

    def __init__(self, title, root, deselected_col="#2e2e2e", selected_col="#bd88ff", selected_fg="black", font="Helvetica", label_font_size=14, 
                title_font_size=20, max_length=4, width=320, height=440, row=1, column=0, columnspan=3, bg="#121212", fg="#e6e6e6", label_highlight="#ceb2f1"):
        
        self.deselected_col = deselected_col
        self.selected_col = selected_col
        self.font = font
        self.label_font_size = label_font_size
        self.title_font_size = title_font_size
        self.max_length = max_length
        self.fg = fg
        self.selected_fg = selected_fg
        self.label_highlight = label_highlight
        
        self.frame = Frame(root, height=height, width=width, bg=bg)
        self.frame.grid(row=row, column=column, columnspan=columnspan)
        self.frame.pack_propagate(False)

        self.elem_list = {}
        self.current_elem = None

        Label(self.frame, text=title, font=(self.font, self.title_font_size), bg=bg, fg=fg).pack(pady=2)
    
    """
    Add an element to the interative list
    
    elem: The element to add to the list
    label: The gui label that will be displayed. Must be a string.
    """
    def add_elem(self, elem, label):
        if len(self.elem_list) == self.max_length:
            messagebox.showerror("Element Limit Reached", "Unable to add more elements")
            return 
        info_label = Button(self.frame, text=label, relief=FLAT, width=26, height=1, fg=self.fg, activebackground=self.label_highlight)
        info_label.pack(pady=5, ipady=8)
        info_label.configure(command=lambda button=info_label: self._set_curr_elem(button), font=(self.font, self.label_font_size))
        
        self.elem_list[info_label] = elem
        self._set_curr_elem(info_label)

    """
    Private method to set a selection

    selection: The button to highlight 
    """
    def _set_curr_elem(self, selection):
        selection.configure(bg=self.selected_col, fg=self.selected_fg)
        self.current_elem = selection

        for elem in self.elem_list.keys():
            if elem != selection:
                elem.configure(bg=self.deselected_col, fg=self.fg)

    """
    Remove the selected element from the list
    """
    def remove_elem(self):
        self.remove_elem_by_key(self.current_elem)

    """
    Remove an element from the list

    key: The button which we want to remove
    """
    def remove_elem_by_key(self, key):
        if len(self.elem_list.keys()) > 0:

            del self.elem_list[key]
            key.destroy()

            if len(self.elem_list.keys()) > 0:
                self._set_curr_elem(list(self.elem_list.keys())[-1])

    """
    Get the selected button 

    Returns: The selected button
    """
    def get_selected_key(self):
        return self.current_elem
    
    """
    Get the selected button's value 

    Returns: The selected value
    """
    def get_selected_value(self):
        if self.current_elem is None:
            return None

        return self.elem_list[self.current_elem]

    """
    Get all the items in this interative list

    Returns: A {button, value} dictionary of all items in this list
    """
    def get_all_items(self):
        return self.elem_list