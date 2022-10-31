from pickle import TRUE
import easyocr
from googletrans import Translator

translator = Translator()
arr=[]
f_str=""



reader = easyocr.Reader(['de'],gpu=TRUE) # this needs to run only once to load the model into memory
result=reader.readtext('germantext.jpg', detail = 0)
dock=list()
for f in result:
    dock.append(f)

#print(dock)
translations = translator.translate(dock, dest='en')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)