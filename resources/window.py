from customtkinter import *

# Main prefs
set_appearance_mode("system")
set_default_color_theme("green")


class MainApp(CTk):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        
        # Enable overlapping        
        self.grid_propagate(False)
        
        # App title and geometry
        self.title("Interactive interface v0.1b1")
        self.geometry(f"{self.width}x{self.height}")
        
        # App grid
        self.grid_columnconfigure((1,2,3,4,5), weight=1)
        self.grid_rowconfigure((1,2,3,4,5), weight=1)
        
        # Theme changer
        theme = CTkComboBox(self, values=['dark', 'light'], justify="center", command=self.color_event)
        theme.place(x=int(self.width*0.05), y=int(self.height*0.9))
        
        self.initbutton = CTkButton(self, text="Initialize!", command=self.main_menu)
        self.initbutton.grid(row=2, column=2, rowspan=3, columnspan=3, sticky='nsew')
    
    def main_menu(self): 
        self.initbutton.grid_forget()
        
        self.strtypein = CTkEntry(self, width=int(self.width*0.8), placeholder_text="Type in required location...")
        self.coordtypein_lat = CTkEntry(self, width=int(self.width*0.35), placeholder_text="Type in latitude...")
        self.coordtypein_long = CTkEntry(self, width=int(self.width*0.35), placeholder_text="Type in longtitude...")
        
        self.strtypein.grid(column=2, row=2, columnspan=3)
        self.coordtypein_lat.grid(column=2, row=3, columnspan=1)
        self.coordtypein_long.grid(column=4, row=3, columnspan=1)
        
        self.buttonappend = CTkButton(self)
    
    def color_event(self, new_color: str):
        set_appearance_mode(new_color)
        
if __name__ == "__main__":
    app = MainApp(1280, 800)
    app.mainloop()