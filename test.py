import textrazor

textrazor.api_key = "043e170ef41a6d297a508581225bd493943f3a9f831345fb71f86d64"

client = textrazor.TextRazor(extractors=["words", "relations"])
client.set_do_cleanup_HTML(True)

url = "http://www.amazon.com/LG-42LM6200-42-Inch-LED-LCD-Glasses/product-reviews/B006ZH0JW6/ref=cm_cr_dp_see_all_btm?ie=UTF8&showViewpoints=1&sortBy=bySubmissionDateDescending"
response = client.analyze_url(url)
l=[]

for property in response.properties():
    for word in property.predicate_words:
        l.append(word.lemma)
        if word.lemma == "sound":
            for property_word in property.property_words:
                for phrase in property_word.noun_phrases:
                    print (phrase)
            break

for sentence in response.sentences():
    for word in sentence.words:
        if word.lemma=="sound":
            print("yes")

'''for relation in response.relations():
    for word in relation.predicate_words:
        if word.lemma == "sound":
            print()
            break'''