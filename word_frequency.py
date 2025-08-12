# importing needed libraries
import matplotlib.pyplot as plt
from collections import Counter
import re
import arabic_reshaper as arre
from bidi.algorithm import get_display
import os
import pandas as pd

def handle_read_file(pattern): 
    """
        Reading data from the given file path
        - Getting words will be used by its pattern
        - based on the words pattern make update as follows:
            * English words --> make it all in lower case
            * Arabic words --> fix letters forms for correct display & adjust bidirectional text 
            * Numbers --> Nothing
        - Update words frequencies 
    """             
    with open(file_path,"r",encoding="utf-8") as file:
        data = []
        for i in file:
            for l in re.findall(pattern,i):
                if re.match(r"[a-zA-Z]", l): 
                    data.append(l.lower())
                elif re.match(r"[أ-ي]", l):
                    reshaped = arre.reshape(l)   
                    data.append(get_display(reshaped))
                else:
                    data.append(l)
    counter.update(data)

def display_most_frequent(n):
    """
       - Takes n which represents number of words wants to display
       - Make a table to represent n words with their frequencies
       - Make bar chart to represent the table 
    """        
    top_words = counter.most_common(n)
    word,word_frequency = zip(*top_words)

    print(f"Word  :  Frequency")
    for i in range(len(word)):
        # Calculate number of spaces needed so that the frequencies
        # will be put in the same index for all words displayed
        spaces_number = len("Word  :  Freq") - len(word[i])
        print(f"{word[i]}{' '* spaces_number}{word_frequency[i]}")

    plt.figure(figsize=(12,6))
    plt.bar(word,word_frequency)
    plt.title("Words Frequencies (BOW)")
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.savefig(f"{folder_name}/BOW.png") 
    plt.show()

if __name__ == '__main__':   
    # Getting file path from user
    file_path = input("Enter File Path: ")
    counter = Counter()
   
    # Make a Folder to save results
    folder_name = "Results"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Make user select type of words want to calculate its frequency
    patterns = {
        1:  r"[a-zA-Z]+",
        2:  r"[أ-ي]+",
        3:  r"/d+",
        4:  r"[أ-يa-zA-Z0-9]+"
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
        handle_read_file(ch)        
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