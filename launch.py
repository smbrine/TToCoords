from resources.window import MainApp
from resources.algorithms import ScreenRes

if __name__ == "__main__":
    width, height = ScreenRes().get()
    app = MainApp(int(width*0.8), int(height*0.8))
    app.mainloop()