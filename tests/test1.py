import speech_recognition as sr
import textrazor


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))





textrazor.api_key = "043e170ef41a6d297a508581225bd493943f3a9f831345fb71f86d64"

client = textrazor.TextRazor(extractors=["words", "relations"])
#client.set_do_cleanup_HTML(True)

response = client.analyze(r.recognize_google(audio))
l=[]

for property in response.properties():
    for word in property.predicate_words:
        l.append(word.lemma)
        if word.lemma == "sound":
            for property_word in property.property_words:
                for phrase in property_word.noun_phrases:
                    print (phrase)
            break
l=[]

for sentence in response.sentences():
    print(sentence.words)
    for word in sentence.words:
        if word.lemma=="image":
            print("yes") 
        l.append(word.lemma)

s=l.index("image")
m=l[s:]
#print(word.lemma)

t=""
for i in m:
    t+=i+" "



print(t)
response1=client.analyze(t)

for noun in response1.noun_phrases():
    print(noun.words)
    for word in noun.words:
        print(word.lemma)


