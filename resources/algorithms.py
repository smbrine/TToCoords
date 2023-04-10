from geocoder import arcgis as geoconv
from typing import Optional
from logging import basicConfig as logger_cfg
from logging import INFO as BASIC
from logging import info as logwriter
import pyautogui

class Coording():
    
    def __init__(self, location: Optional[str]=None, coords: Optional[tuple]=None, logger: Optional[bool]=False, logdir: Optional[str]=None) -> None:
        if location == None and coords == None:
            raise ValueError("At least one argumet should be specified")
        if logger:
            if logdir != None:
                logger_cfg(filename=logdir, level=BASIC)
                logwriter(f"[Coording] Requested logger at {logdir}")
                logwriter(f'[Coording] Recieved {location} and {coords}')
            else:
                raise AttributeError("You have activated logger, but no logdir specified. Please specify logdir. No default logdir is available at the moment")
        
        self.location = location
        self.coords = coords
        
    def toCoords(self) -> tuple:
        lat, long = geoconv(location=self.location).latlng
        logwriter(f"[Coording] Successfully converted {self.location} to {[lat, long]}")
        return [lat, long]
    
    def toStr(self, format: Optional[bool]=True) -> str: 
        locname = geoconv(location=self.coords, method="reverse")
        logwriter(f'[Coording] Successfully converted {self.coords} to {locname}')
        if format:
            locname = str(locname[0]).replace("[", '').replace(']','')
        return locname
    
class ToDict():
    """
    service can take only 2 arguments at the moment: "google", "yandex" and convert to a respective format.
    """
    def __init__(self, places: dict, service: Optional[str] = "google", logger: Optional[bool]=False, logdir: Optional[str]=None) -> None:
        self.places = places
        self.service = service
        
        if logger:
            if logdir != None:
                logger_cfg(filename=logdir, level=BASIC)
                logwriter(f"[ToDict] Initialized logger at {logdir}")
            else:
                raise AttributeError("You have activated logger, but no logdir specified. Please specify logdir. No default logdir is available at the moment")
    def convert(self):
        pass
    
class Unpacker():
    def __init__(self, iterlist: list, logger: Optional[bool]=False, logdir: Optional[str]=None) -> None:
        if iterlist == None:
            raise ValueError("Error: target list is not specified")
        
        if logger:
            if logdir != None:
                logger_cfg(filename=logdir, level=BASIC)
                logwriter(f"[Unpacker] Initialized logger at {logdir}")
            else:
                raise AttributeError("You have activated logger, but no logdir specified. Please specify logdir. No default logdir is available at the moment")
        
        self.packed = iterlist
        
    def unpack(self) -> str:
        unpacked = ", ".join(self.packed)
        logwriter(f'[Unpacker] Successfully unpacked {self.packed} to {unpacked}')
        return str(unpacked)
    
    def unpack_tuples_list(self):
        repacked = []
        for x, y in self.packed:
            repacked.append(f"[{x}, {y}]")
        unpacked = ", ".join(repacked)
        logwriter(f'[Unpacker] Successfully unpacked {self.packed} to {unpacked}')
        return unpacked

class ScreenRes():
    def __init__(self) -> None:
        pass
    
    def get(self):
        width, height = pyautogui.size()
        return width, height
