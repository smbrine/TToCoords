from customtkinter import *
# Appending root folder
import sys
sys.path.append('./')
from resources.CTkMessagebox import CTkMessagebox

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
        
        # Meme
        self.initbutton = CTkButton(self, text="Initialize!", command=self.main_menu)
        self.initbutton.grid(row=2, column=2, rowspan=3, columnspan=3, sticky='nsew')
        self.loc_dict = []
        self.coord_dict = []
    
    def main_menu(self): 
        self.initbutton.grid_forget()
        
        self.strtypein = CTkEntry(self, width=int(self.width*0.8), placeholder_text="Type in required location...")
        self.coordtypein_lat = CTkEntry(self, width=int(self.width*0.35), placeholder_text="Type in latitude...")
        self.coordtypein_long = CTkEntry(self, width=int(self.width*0.35), placeholder_text="Type in longtitude...")
        
        self.strtypein.grid(column=2, row=2, columnspan=3)
        self.coordtypein_lat.grid(column=2, row=3, columnspan=1)
        self.coordtypein_long.grid(column=4, row=3, columnspan=1)
        
        self.buttonappend = CTkButton(self, text="Append!", command=self.append_event)
        self.buttonappend.grid(row=4, column=3)
    
    def append_event(self):
        print(type(self.strtypein.get()))
        if [self.strtypein.get(), self.coordtypein_lat.get(), self.coordtypein_long.get()] == [None, None, None]:
            error_pop = CTkMessagebox(self, title="Error!", message="You haven't specified anything")
            return error_pop
        if (text := self.strtypein.get()) != None:
            self.loc_dict.append(text)
        if (lat := self.coordtypein_lat.get()) != None:
            if (long := self.coordtypein_long.get()) != None:
                self.coord_dict.append([lat, long])
            else:
                error_pop = CTkMessagebox(self, title="Error!", message="You specified latitude, but not longtitude")
                return error_pop
        elif (long := self.coordtypein_long.get()) != None:
            if (lat := self.coordtypein_lat.get()) == None:
                error_pop = CTkMessagebox(self, title="Error!", message="You specified longtitude, but not latitude")
                return error_pop      
    
    def color_event(self, new_color: str):
        set_appearance_mode(new_color)
        
if __name__ == "__main__":
    app = MainApp(1280, 800)
    app.mainloop()