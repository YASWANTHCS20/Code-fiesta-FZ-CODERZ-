from googletrans import Translator

translater=Translator()

string=input()

out=translater.translate(string , dest="en")

print(out) 
