import os

device = [ "10.1.21.92:5555"]
Port = ["4725"]

def FolderCheckOnPC():
    if not os.path.exists('screenshots'):
        os.mkdir('screenshots')
    return

def FolderCheckOnAndorid():
    i = 0
    while i < len(device):
        os.system("adb -s " + device[i] + " shell mkdir /sdcard/screenshots")
        i += 1
    return 0
a
def AndroidScreenshot(ScreenshotName):
    i = 0
    while i < len(device):
        os.system("adb -s " + device[i] + " shell screencap -p /sdcard/screenshots/" + ScreenshotName + ".png")
        i += 1
    return 0
