from tkinter import *

from gui.interactive_list import InteractiveListGUI

class ProgressComponent(InteractiveListGUI):
    
    def __init__(self, root):
        self.frame = LabelFrame(root, height=500, width=320)
        self.frame.grid(row=0, column=3, ipadx=2, ipady=2, sticky=NE)
        self.frame.grid_propagate(False)

        super().__init__(root=self.frame, title="In Progress", deselected_col="grey", selected_col="purple", font="Helvetica", label_font_size=14, title_font_size=20, max_length=6)


    

        