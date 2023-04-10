from customtkinter import *

from customtkinter import END as konets
# Appending root folder
import sys
sys.path.append('./')
from resources.CTkMessagebox import CTkMessagebox
from resources.algorithms import Unpacker, Coording, ScreenRes, ToDict

# Main prefs
set_appearance_mode("system")
set_default_color_theme("green")

class MainApp(CTk):
    def __init__(self, width, height) -> None:
        super().__init__()
        self.width = width
        self.height = height
        
        self.grid_propagate(True)
        # App title and geometry
        self.title("Interactive interface v0.1b1")
        self.geometry(f"{self.width}x{self.height}")
        
        # App grid
        self.grid_columnconfigure((1,2,3,4,5), weight=1)
        self.grid_rowconfigure((1,2,3,4,5,6), weight=1)
        
        # Theme changer
        theme = CTkComboBox(self, values=['system', 'dark', 'light'], justify="center", command=self.color_event)
        theme.place(x=int(self.width/20), y=int(self.height/20))
        
        # Meme
        self.main_menu()
        self.loc_dict = []
        self.coord_dict = []
    
    def main_menu(self): 
        
        self.strtypein = CTkEntry(self, width=int(self.width*0.8), placeholder_text="Type in required location...")
        self.coordtypein_lat = CTkEntry(self, width=int(self.width*0.35), placeholder_text="Type in latitude...")
        self.coordtypein_long = CTkEntry(self, width=int(self.width*0.35), placeholder_text="Type in longtitude...", )
        
        self.strtypein.grid(column=2, row=2, columnspan=3, padx=20, pady=20)
        self.coordtypein_lat.grid(column=2, row=3, columnspan=1, padx=20, pady=20)
        self.coordtypein_long.grid(column=4, row=3, columnspan=1, padx=20, pady=20)
        
        self.buttonappend = CTkButton(self, text="Append!", command=self.append_event)
        self.buttonappend.grid(row=4, column=3)
    
    def append_event(self):
        
        # Handler of "empty everything"
        if self.strtypein.get()+self.coordtypein_lat.get()+self.coordtypein_long.get() == "":
            error_pop = CTkMessagebox(self, title="Error!", message="You haven't specified anything")
            return error_pop
        
        # Checks if the placename is filled
        if (text := self.strtypein.get()) != "":
            if text not in self.loc_dict:
                self.loc_dict.append(text)
                self.update_datainfo()
                self.strtypein.delete(0, konets)
        
        # Checks if coords are filled
        elif (lat := self.coordtypein_lat.get()) != "":
            if (long := self.coordtypein_long.get()) != "":
                
                # Checks if coords are typed in correctly
                try:
                    lat = float(lat)
                    long = float(long)
                except:
                    error_message = "Invalid coordinates: Please enter a valid numerical value for both latitude and longitude."
                    error_pop = CTkMessagebox(self, title="Error!", message=error_message)
                
                # Checks if values are real
                if lat > 90 or lat < -90:
                    error_pop = CTkMessagebox(self, title="Error!", message="Latitude is always between 90 and -90")
                elif long > 90 or long < -90:
                    error_pop = CTkMessagebox(self, title="Error!", message="Longtitude is always between 90 and -90")
                
                # Appends dictionary with float tuple
                else:
                    if [lat, long] not in self.coord_dict:
                        self.coord_dict.append([lat, long])
                        self.update_datainfo()
                        self.coordtypein_long.delete(0, konets)
                        self.coordtypein_lat.delete(0, konets)
                    else:
                        pass
            
            else:
                error_pop = CTkMessagebox(self, title="Error!", message="You specified latitude, but not longtitude")
                return error_pop
        
        # Checks if both coordinates are filled correctly
        elif (long := self.coordtypein_long.get()) != "":
            
            if (lat := self.coordtypein_lat.get()) == "":
                error_pop = CTkMessagebox(self, title="Error!", message="You specified longtitude, but not latitude")
                return error_pop      
    
    def update_datainfo(self):
        self.button_calculate = CTkButton(self, text='Convert everything!', command=self.convert_event)
        if self.loc_dict != []:
            self.locations_infolabel = CTkLabel(self, text=f'Current locations are: {Unpacker(self.loc_dict).unpack()}')
            self.locations_infolabel.grid(row=6, column=2)
            self.buttonappend.grid(row=4, column=2)
            self.button_calculate.grid(row=4, column=4)
        if self.coord_dict != []:
            self.coords_infolabel = CTkLabel(self, text=f'Current coordinates are: {Unpacker(self.coord_dict).unpack_tuples_list()}')
            self.coords_infolabel.grid(row=6, column=4)
            self.buttonappend.grid(row=4, column=2)
            self.button_calculate.grid(row=4, column=4)

    def convert_event(self):
        coords = self.coord_dict
        locs = self.loc_dict
        loc_coords = []
        r_coords = []
        
        if locs != []:
            for loc in locs:
                loc_coords.append(Coording(loc).toCoords())
        if coords != []:
            loc_coords.append(coords[0])
        
        for i, *_ in enumerate(loc_coords):
            r_coords.append([round(loc_coords[i][0], ndigits=6), round(loc_coords[i][1], ndigits=6)])
        
        self.infolabel = CTkLabel(self, text=f'{r_coords}')
        self.infolabel.place(x=20, y=500)
        
        # out_data = ToDict(r_coords, logger=True, logdir="logger.log")
        
        # with open('Output Locations.csv', 'w+', "utf-8") as of:
        #     of.write(r_coords)
        
    def color_event(self, new_color: str):
        set_appearance_mode(new_color)
        
# if __name__ == "__main__":
#     width, height = ScreenRes().get()
#     app = MainApp(int(width*0.8), int(height*0.8))
#     app.mainloop()
