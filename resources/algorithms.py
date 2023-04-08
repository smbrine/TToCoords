from geocoder import osm as geoconv
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
                logwriter(f"Initialized logger at {logdir}")
            else:
                raise AttributeError("Please specify logdir. No default logdir is available at the moment")
        
        self.location = location
        self.coords = coords
        
    def toCoords(self):
        lat, long = geoconv(self.location).latlng
        logwriter(f"Successfully converted {self.location} to {[lat, long]}")
        return [lat, long]
    
    def toStr(self): 
        locname = geoconv(self.coords, method="reverse")
        logwriter(f'Successfully converted {self.coords} to {locname}')
        return str(locname[0]).replace("[", '').replace(']','')
    
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
