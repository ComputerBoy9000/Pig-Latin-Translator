import numpy as np
import pandas as pd 
import csv


vowels = ["a","e","i","o","u"]

##create a list of words in which 'y' is the only vowel
sometimes_y = pd.read_csv("sometimesy.csv")
sometimes_y["Word"] = sometimes_y["Word"].astype(str)

y_is_vowel = sometimes_y["Word"].values.tolist()

##create a list of words in which there are no vowels
no_vowels_here = pd.read_csv("novowels.csv")
no_vowels_here["Word"] = no_vowels_here["Word"].astype(str)

no_vowels = no_vowels_here["Word"].values.tolist()

w_is_vowel = ["cwm","cwms", "crwth", "crwths", "cwtch", "cwtchs"]

## a function which translates English words into Pig Latin
def Pig_Latin(word):
    
    if word[0].lower() in vowels:
        word = word + "way"
        return word
      
    elif word.lower() in y_is_vowel:
        while word[0].lower() != "y":
            word = word[1:] + word[0]
        
        word = word + "ay"
        return word    
    
    elif word in w_is_vowel:
        while word[0].lower() != "w":
            word = word[1:] + word[0]
            
        word = word + "ay"
        return word
    
    elif word in no_vowels:
        if word[1] in ["s","r","h","f"]:
            word = word[1:] + word[0]
            word = word + "ay"
            return word
        else:
            word = word + "way"
            return word
    
    else:
        while word[0].lower() not in vowels:
            word = word[1:] + word[0]
            
    
        word = word + "ay"
        return word
    
    print(word)
    
#a function which translates English sentences into Pig Latin
def Pig_Latin_Translator(sentence):
    words = sentence.split()
    new_words = []
    for word in words:
        if "," in word:
            word = word[0:len(word)-1]
            word = Pig_Latin(word) + ","
            new_words.append(word)
            
        elif "." in word:
            word = word[0:len(word)-1]
            word = Pig_Latin(word) + "."
            new_words.append(word)
            
        elif "?" in word:
            word = word[0:len(word)-1]
            word = Pig_Latin(word) + "?"
            new_words.append(word)
        
        elif "!" in word:
            word = word[0:len(word)-1]
            word = Pig_Latin(word) + "!"
            new_words.append(word)
        
        elif ";" in word:
            word = word[0:len(word)-1]
            word = Pig_Latin(word) + ";"
            new_words.append(word)
            
        elif "-" in word:
            word = word[0:len(word)-1]
            word = Pig_Latin(word) + "-"
            new_words.append(word)
        
        else:
            word = Pig_Latin(word)
            new_words.append(word)
            
    new_sentence = ""   
    for word in new_words:
        new_sentence = new_sentence + " " + word
        
    print(new_sentence)
        
            
