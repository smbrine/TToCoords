from geocoder import arcgis as geoconv
from typing import Optional
from logging import basicConfig as logger_cfg
from logging import INFO as BASIC
from logging import info as logwriter

class Coording():
    
    def __init__(self, location: Optional[str]=None, coords: Optional[tuple]=None, logger: Optional[bool]=False, logdir: Optional[str]=None):
        if location == None and coords == None:
            raise ValueError("At least one argumet should be specified")
        if logger:
            if logdir != None:
                logger_cfg(filename=logdir, level=BASIC)
                logwriter(f"Requested logger at {logdir}")
                logwriter(f'Recieved {location} and {coords}')
            else:
                raise AttributeError("Please specify logdir. No default logdir is available at the moment")
        
        self.location = location
        self.coords = coords
        
    def toCoords(self):
        lat, long = geoconv(location=self.location).latlng
        logwriter(f"Successfully converted {self.location} to {[lat, long]}")
        return [lat, long]
    
    def toStr(self, format: Optional[bool]=True): 
        locname = geoconv(location=self.coords, method="reverse")
        logwriter(f'Successfully converted {self.coords} to {locname}')
        if format:
            locname = str(locname[0]).replace("[", '').replace(']','')
        return locname
    
class ToDict():
    """
    service can take only 2 arguments at the moment: "google", "yandex" and convert to a respective format.
    """
    def __init__(self, places: dict, service: Optional[str] = "google", logger: Optional[bool]=False, logdir: Optional[str]=None):
        self.places = places
        self.service = service
        if logger:
            if logdir != None:
                logger_cfg(filename=logdir, level=BASIC)
                logwriter(f"Initialized logger at {logdir}")
            else:
                raise AttributeError("Please specify logdir. No default logdir is available at the moment")

# print(test := geoconv("Moscow"))
# print(test.latlng)