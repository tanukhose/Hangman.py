import string
import random

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    word_list=["navgurukul","learning","kindess"]
    return word_list
    # WORDLIST_FILENAME="words.txt"
    # inFile=open(WORDLIST_FILENAME,'r',0)
    # line=inFile.readline()
    # word_list=string.split(line)
    # print(" ",len(word_list),"words loaded.\n")



def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word































































































































# import random
# a=[1,2,3,4,5,6,7]

# c=random.choice(a)
# print(c)