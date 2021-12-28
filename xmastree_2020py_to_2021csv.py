import functools;

class Pixels:
    pixelCount = 0
    pixelList = []
    shownCounter = 0

    def __init__(self, pixelCount):
        self.pixelCount = pixelCount
        self.pixelList = [[0, 0, 0]] * pixelCount
        self.shownCounter = 0

    def __getitem__(self, key):
        return self.pixelList[key]
    
    def __setitem__(self, key, value):
        self.pixelList[key] = value
    
    def show(self):
        if self.shownCounter == 0:
            headers = list(map(lambda i: ["R_" + str(i), "G_" + str(i), "B_" + str(i)], list(range(self.pixelCount))))
            headers = ",".join(list(map(lambda colors: ",".join(colors), headers)))
            headers = "FRAME_ID," + headers
            
            print(headers)

        result = list(map(lambda colors: ",".join(list(map(lambda c: str(round(c)), colors))), self.pixelList))
        result = ",".join(result)

        print(",".join([str(self.shownCounter), result]))

        self.shownCounter += 1
