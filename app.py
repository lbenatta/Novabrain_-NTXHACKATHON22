import eel
import os
import time
import sys

sys.path.append("../../../lib")
import nova

eel.init("www")




num = 0


@eel.expose
def getTrigger():
    global num
    f = open("lol")
    rep = int(f.read())
    f.close()
    #rep = rep.split("%")[0].split("[")[-1]

    
    if (int(rep) != num):
        print("up")
        eel.js_trigger()
    num = int(rep)


@eel.expose
def getAct():
    return False

@eel.expose
def sendAction(txt):
    print("python3 tst.py " + txt)
    os.system("python3 tst.py " + txt)

eel.start("index.html", mode="google-chrome")

