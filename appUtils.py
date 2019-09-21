import speech_recognition as sr
recog = sr.Recognizer()
mic = sr.Microphone()

def sysListen():
    with mic as source:
        recog.adjust_for_ambient_noise(source)
        audio = recog.listen(source)
    
    # setup response
    response = {
        "success" : True,
        "error" : None,
        "transcription" : None
    }

    # use Google API
    try:
        response["transcription"] = recog.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response["transcription"]

