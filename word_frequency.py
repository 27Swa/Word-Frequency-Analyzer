# importing needed libraries
import matplotlib.pyplot as plt
from collections import Counter
import re
import arabic_reshaper as arre
from bidi.algorithm import get_display
import os
import pandas as pd

def handle_word(w):
    """
        based on the words pattern make update as follows:
            * English words --> make it all in lower case
            * Arabic words --> fix letters forms for correct display & adjust bidirectional text 
            * Numbers --> Nothing
    """
    if re.match(patterns[1], w): 
         return w.lower()
    elif re.match(patterns[2], w):
        reshaped = arre.reshape(w)  
        return get_display(reshaped)
    elif re.match(patterns[3],w):
        return w

def handle_read_file(pattern): 
    """
        Reading data from the given file path
        Filter from  some arabic special characters
        Getting words will be used by its pattern
    """             
    with open(file_path,"r",encoding="utf-8") as file:
        for i in file:
            for l in re.findall(pattern,re.sub(r'[\u0640\u064B-\u0652]', '', i)):
                yield handle_word(l)
def display_most_frequent(n):
    """
       - Takes n which represents number of words wants to display
       - Make a table to represent n words with their frequencies
       - Make bar chart to represent the table 
    """   
    # Making the architecture for the table and present its data     
    top_words = counter.most_common(n)
    if n > len(top_words):
        print(f"In this data there are {len(top_words)} words")
    word,word_frequency = zip(*top_words)
    table_width = len("|     Word     | Frequency |")
    print(f"{'-'*table_width}")
    print(f"|     Word     | Frequency |")
    print(f"{'-'*table_width}")

    for i in range(len(word)):
        # Calculate number of spaces needed so that the frequencies
        # will be put in the same index for all words displayed
        line = len("|     Word   ") - len(word[i]) + 1
        end_table = len("uency ") - len(str(word_frequency[i])) 
        print(f"|{word[i]}{' '* line}|{' '* len(" Freq")}{word_frequency[i]}{' '*end_table}|")
    print(f"{'-'*table_width}")

    plt.figure(figsize=(12,6))
    plt.bar(word,word_frequency)
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.savefig(f"{folder_name}/BOW.png") 
    plt.show()

if __name__ == '__main__':   
    # Getting file path from user
    file_path = input("Enter File Path: ")
   
    # Make a Folder to save results
    folder_name = "Results"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Make user select type of words want to calculate its frequency
    patterns = {
        1:  r"[a-zA-Z]+",
        2:  r"[إةآأ-ي]+",
        3:  r"[0-9]+",
        4:  r"[أإةآأ-يa-zA-Z0-9]+"
    }
    try:
        bow = int(input("Select type of words you want to calculate its frequency: \n [1] English words\n [2] Arabic Words\n [3] Numbers\n [4] All\n Selected Choice: "))
        ch = patterns.get(bow, patterns[4])
        if bow not in patterns:
            print("Invalid input use all type of words")
    except ValueError:
        print("Invalid input use all type of words")
        ch = patterns[4]
    
    # Apply Word Analyzer
    try:
        counter = Counter(handle_read_file(ch))  
        # Taking number of words wants display
        op = input("Enter # words you want to display, Enter to use default number: ")
        n = int(op) if op.isdigit() else 10
        display_most_frequent(n)        
        # save data (all words with their frequencies) in csv file
        words_,words_counter = zip(*counter.items())
        df = pd.DataFrame({'Word':words_,'Frequency':words_counter})
        df.to_csv('Results/data.csv',index= False)
    except FileNotFoundError:
        print("Wrong File Path Entered!!!")
    except re.error:
        print("Error in Regular expression")
    except ValueError:
        print("There is nothing to display")
    except:
        print("A Problem Occured, Please check data entered")