from resources.algorithms import Coording

while (text := input("Type in your geographical name: ")) != "quit":
    coordinates = Coording(location=text, logger=True, logdir="./logger.log").toCoords()
    print(coordinates)