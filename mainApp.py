import eel

import appUtils as au
# expose python functions to javascript
# these functions can be called from JS in index.html
@eel.expose
def initApp():
    pass

@eel.expose
def closeApp():
    pass

@eel.expose
def addPoint():
    uResponse = au.sysListen()
    eel.opEnd(uResponse)

eel.init('web', allowed_extensions=['.js','.html', ".jpg"])
eel.start('index.html', size=(1024,720))