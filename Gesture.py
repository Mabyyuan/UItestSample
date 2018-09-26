from time import sleep
# Get Screen size

def getSize(self):
    x = self.driver.get_window_size()['width']
    y = self.driver.get_window_size()['height']
    print(x,y)
    return (x, y)

    # Slide from right to the left

def swipeLeft(self, t):
    l = getSize(self)
    x1 = int(l[0] * 0.75)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.25)
    self.driver.swipe(x1, y1, x2, y1, t)

def SetGaolWHswipeLeft(self, repeat, t):
    l = getSize(self)
    x1 = int(l[0] * 0.75)
    y1 = int(l[1] * 0.30)
    x2 = int(l[0] * 0.25)
    i = 0
    while i <= repeat:
        self.driver.swipe(x1, y1, x2, y1, t)
        sleep(0.3)
        i += 1

    # Slide from let to the right

def swipeRight(self, t):
    l = getSize(self)
    x1 = int(l[0] * 0.25)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.75)
    self.driver.swipe(x1, y1, x2, y1, t)

def SetGaolWHswipeRight(self, repeat, t):
    l = getSize(self)
    x1 = int(l[0] * 0.25)
    y1 = int(l[1] * 0.30)
    x2 = int(l[0] * 0.75)
    i = 0
    while i <= repeat:
        self.driver.swipe(x1, y1, x2, y1, t)
        sleep(0.3)
        i += 1

    # Slide from down to the top

def swipeUp(self, t):
    l = getSize(self)
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.75)
    y2 = int(l[1] * 0.25)
    self.driver.swipe(x1, y1, x1, y2, t)

    # Slide from top to the down

def swipeDown(self, t):
    l = getSize(self)
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.25)
    y2 = int(l[1] * 0.75)
    self.driver.swipe(x1, y1, x1, y2, t)