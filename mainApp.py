import eel

import test3

# expose python functions to javascript
# these functions can be called from JS in index.html
@eel.expose
def initApp():
    import appUtils as au
    uResponse = au.sysListen()
    test3.fn(uResponse)

eel.init('web', allowed_extensions=['.js','.html'])
eel.start('index.html', size=(1024,720))