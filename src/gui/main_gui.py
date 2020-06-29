from tkinter import *
from tkinter import ttk
import datetime
import time
import _thread

from gui.user_component import UserComponent
from gui.progress_component import ProgressComponent
from user.user import User
from browser.browser import Browser
from browser.supreme_browser import SupremeBrowser

class MainGUI:

    def __init__(self):
        self.root = Tk()
        self.root.title("Hyper Shopper")
        self.root.geometry("1024x500")
        self.root.resizable(0, 0)

        self.user = UserComponent(self.root)
        self.progress = ProgressComponent(self.root)
        
        center_frame = Frame(self.root, height=500, width=373)
        center_frame.grid(row=0, column=1)
        center_frame.grid_propagate(False)

        Label(center_frame, text="Hyper Shopper", font=("Open Sans", 40)).grid(row=0, column=0)
        Button(center_frame, text="COP", padx=120, pady=15, font=("Open Sans", 20), command=self._create_request).grid(row=2, column=0, sticky=S)


        self._create_info(center_frame)

    
    def _create_info(self, parent):
        info_frame = Frame(parent, height=300, width=373)
        info_frame.grid(row=1, column=0, pady=10, sticky=N)
        info_frame.grid_propagate(False)

        # website link
        Label(info_frame, text="Link:", font=("Comic Sans", 13)).grid(row=0, column=0, sticky=W, pady=(20, 15))
        self.link = Entry(info_frame, font=("Comic Sans", 12))
        self.link.grid(row=0, column=1, ipady=3, ipadx=68, pady=(20, 15), columnspan=3, sticky=W)

        # time
        Label(info_frame, text="Time:", font=("Comic Sans", 13)).grid(row=1, column=0, sticky=W)
        self.hour = ttk.Combobox(info_frame, values=[i for i in range(0, 24)], width=6, font=("Comic Sans", 12))
        self.hour.grid(row=1, column=1)
        self.minute = ttk.Combobox(info_frame, values=[f"0{i}" if i < 10 else i for i in range(0, 60)], width=6, font=("Comic Sans", 12))
        self.minute.grid(row=1, column=3)
        Label(info_frame, text=":", font=("Comic Sans", 16)).grid(row=1, column=2)

    def _create_request(self):
        
        _thread.start_new_thread( self._shop, ())
    
    def _shop(self):
        user = self.user.get_selected_value()
        link = self.link.get()
        minute = self.minute.get()
        hour = self.hour.get()

        value = {"time":(hour, minute), "user": user, "link":link, "valid":True}
        self.progress.add_elem(label=f"{hour}:{minute}\n" + (f"{link}" if len(link) < 30 else f"{link[0:30]}"), elem=value)

        self.link.delete(0, 'end')
        self.minute.delete(0, 'end')
        self.hour.delete(0, 'end')

        browser = SupremeBrowser(user) if 'supreme' in link else None
        browser.launch()

        while int(datetime.datetime.now().minute) < int(minute) or int(datetime.datetime.now().hour) < int(hour):
            if value["valid"] == False:
                browser.close()
                self.progress.remove(value=value)
                _thread.exit()

        browser.add_to_cart_bylink(link)
        browser.checkout()
        browser.close()

        self.progress.remove(value=value)

    
    def main(self):
        self.root.mainloop()




        




