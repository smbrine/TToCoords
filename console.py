from resources.algorithms import Coording

while (text := input("Type in your geographical name: ")) != "quit":
    coordinates = Coording(location=text, logger=True, logdir="./logger.log").toCoords()
    if coordinates[1] == None:
        print(coordinates[0])
    else:
        print(coordinates)