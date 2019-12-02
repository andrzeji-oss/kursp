# napisz funkcje, ktora wygeneruje losowe zdanie zawierajace podaną liczbę wyrazów, domyslnie 5
from random import randint

sentence = "Po 10 latach starań udało się w końcu doprowadzić do rozpoczęcia rozbiórki w warszawskim Czarnym Kocie. Podpisano odpowiednią umowę, a firma rozbiórkowa weszła już na posesję. Informację przekazał wiceprezydent Warszawy."

def sentenceGenerator(sentence, n=5):
    sentence = sentence.replace(".","").replace(",","").replace("-","").replace("[0-9]","")
    words = sentence.split(" ")
    resultSentence = ""
    for i in range(n):
        resultSentence += words[randint(0, len(words)) - 1] + " "
    resultSentence = resultSentence[0: 1].upper() + resultSentence[1: len(resultSentence)-1] + "."
    return  resultSentence

print("Auto-sentence: ", sentenceGenerator(sentence))
