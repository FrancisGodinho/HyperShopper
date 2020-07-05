from tkinter import *
from tkinter import ttk
import datetime
import time
import _thread
from PIL import ImageTk, Image
from tkinter import messagebox

from gui.user_component import UserComponent
from gui.progress_component import ProgressComponent
from user.user import User
from browser.browser import Browser
from browser.supreme_browser import SupremeBrowser
from browser.nike_browser import NikeBrowser

class MainGUI:

    def __init__(self):
        self.bg = "#121212"
        self.fg = "#e6e6e6"
        self.button_bg = "#2e2e2e"
        self.entry_bg = '#1c1c1c'
        self.activebackground = "#505050"
        self.activeforeground = "#e6e6e6"

        self.root = Tk()
        self.root.title("Hyper Shopper")
        self.root.iconbitmap("images/hypershopper_favicon.ico")
        self.root.geometry("1027x400")
        self.root.resizable(0, 0)
        self.root.configure(bg=self.bg)

        self.user = UserComponent(self.root, bg=self.bg, fg=self.fg, button_bg=self.button_bg, 
                    activebackground=self.activebackground, activeforeground=self.activeforeground, entry_bg=self.entry_bg)
        self.progress = ProgressComponent(self.root, bg=self.bg, fg=self.fg, button_bg=self.button_bg, 
                    activebackground=self.activebackground, activeforeground=self.activeforeground)
        
        center_frame = Frame(self.root, height=400, width=373, bg=self.bg)
        center_frame.grid(row=0, column=1)
        center_frame.grid_propagate(False)

        image = Image.open("images/hypershopper_logo.JPG")
        image = image.resize((360, 180), Image.ANTIALIAS)
        image.save("images/logo.ppm", "ppm")
        self.logo = ImageTk.PhotoImage(file="images/logo.ppm") 
        
        Label(center_frame, image=self.logo, bg=self.bg).grid(row=0, column=0)
        Button(center_frame, text="BUY", padx=120, pady=0, font=("Comic Sans", 20), command=self._create_request, bg=self.button_bg, fg=self.fg, 
                activebackground=self.activebackground, activeforeground=self.activeforeground).grid(row=2, column=0, sticky=S, padx=(0, 15))

        self._create_info(center_frame)

    """
    Create the center link/time gui

    parent: The parent frame which the gui will be added to
    """
    def _create_info(self, parent):

        info_frame = Frame(parent, height=120, width=373, bg=self.bg)
        info_frame.grid(row=1, column=0, pady=10, sticky=N, padx=10)
        info_frame.grid_propagate(False)

        # website link
        Label(info_frame, text="Link:", font=("Comic Sans", 13), bg=self.bg, fg=self.fg).grid(row=0, column=0, sticky=W, pady=(30, 20))
        self.link = Entry(info_frame, font=("Comic Sans", 12), width=18, bg=self.entry_bg, fg=self.fg, insertbackground=self.fg)
        self.link.grid(row=0, column=1, ipady=3, ipadx=68, pady=(30, 20), columnspan=3, sticky=W)

        # time
        Label(info_frame, text="Time:", font=("Comic Sans", 13), bg=self.bg, fg=self.fg).grid(row=1, column=0, sticky=W)
        self.hour = ttk.Combobox(info_frame, values=[i for i in range(0, 24)], width=6, font=("Comic Sans", 12), state="readonly")
        self.hour.grid(row=1, column=1)
        self.minute = ttk.Combobox(info_frame, values=[f"0{i}" if i < 10 else i for i in range(0, 60)], width=6, font=("Comic Sans", 12), state="readonly")
        self.minute.grid(row=1, column=3)
        Label(info_frame, text=":", font=("Comic Sans", 16), bg=self.bg, fg=self.fg).grid(row=1, column=2)

        combostyle = ttk.Style() #adding color to combobox
        combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': self.button_bg,'fieldbackground': self.button_bg,'background': self.button_bg, 
                                        "selectforeground":self.fg, "arrowcolor":self.fg, "foreground":self.fg}
                                       }})
        combostyle.theme_use('combostyle') 

    """
    Creates a new request and starts a thread if the request was valid
    """
    def _create_request(self):
        if self.user.get_selected_value() is None:
            messagebox.showerror("Error", "User has not been created correctly")
            return
        elif self.link.get() == "":
            messagebox.showerror("Error", "Link has not been entered correctly")
            return
        elif self.minute.get() == "" or self.hour.get() == "":
            messagebox.showerror("Error", "Time has not been set correctly")
            return
        
        _thread.start_new_thread( self._shop, ())
    
    """
    Execute the request
    """
    def _shop(self):
        user = self.user.get_selected_value()
        link = self.link.get()
        minute = self.minute.get()
        hour = self.hour.get()

        if "supreme" not in link and "nike" not in link:
            messagebox.showerror("Error", "Link has not been entered correctly. Enter a link from either supreme.com or nike.com")
            return

        request = {"time":(hour, minute), "user": user, "link":link, "valid":True}
        self.progress.add_elem(label=f"{hour}:{minute}\n Link: " + (link if len(link) < 24 else f"{link[0:24]}..."), elem=request)

        self.link.delete(0, 'end')

        self.minute.configure(state="normal")
        self.hour.configure(state="normal")
        self.minute.delete(0, 'end')
        self.hour.delete(0, 'end')
        self.minute.configure(state="readonly")
        self.hour.configure(state="readonly")

        browser = SupremeBrowser(user) if 'supreme' in link else NikeBrowser(user)
        browser.launch()

        while int(datetime.datetime.now().minute) != int(minute) or int(datetime.datetime.now().hour) != int(hour):
            if request["valid"] == False:
                browser.close()
                self.progress.remove(value=request)
                _thread.exit()

        success = browser.add_to_cart_bylink(link)
        if success == False:
            messagebox.showerror("Error", "Unable to add item to cart")
            browser.close()
            
        browser.checkout()
        browser.close()

        self.progress.remove(value=request)

    """
    Main function: displays GUI
    """
    def run(self):
        self.root.mainloop()




        




