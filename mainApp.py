import eel
import test3
import appUtils as au
# expose python functions to javascript
# these functions can be called from JS in index.html
@eel.expose
def initApp():
    pass

@eel.expose
def closeApp():
    print("Init Terminate Process")
    import newdata
    newdata.get_result()
    import sys
    eel.terminate()
    sys.exit()

@eel.expose
def addPoint():
    uResponse = au.sysListen()
    # print(uResponse)
    eel.opEnd(uResponse)
    test3.fn(uResponse)

try:
    eel.init('web', allowed_extensions=['.js','.html', ".jpg", ".py"])
    eel.start('index.html', size=(1024,720))
except (SystemExit, MemoryError, KeyboardInterrupt):
    pass
print("Application Terminated")