# importing needed libraries
import matplotlib.pyplot as plt
from collections import Counter
import re
import arabic_reshaper as arre
from bidi.algorithm import get_display

def handle_read_file():       
        with open(fpath,"r",encoding="utf-8") as file:
            for i in file:
                x = []
                for l in re.findall(r"[أ-يa-zA-Z]+",i):
                    if re.search(r"[a-zA-Z]", l): 
                        x.append(l.lower())
                    else:
                        # Handling in case having arabic words
                        reshaped = arre.reshape(l)   
                        x.append(get_display(reshaped))
                cnt.update(x)
def display_most_frequent():
        top_words = cnt.most_common(10)
        word,cnts = zip(*top_words)

        print(f"Word  :  Frequency")
        for i in range(len(word)):
            sp_n = 12 - len(word[i])
            print(f"{word[i]}{' '* sp_n}{cnts[i]}")

        plt.figure(figsize=(12,6))
        plt.bar(word,cnts)
        plt.xlabel("Word")
        plt.ylabel("Frequency")
        plt.show()
if __name__ == '__main__':   
    # Apply word analyzer
    fpath = input("Enter File Path: ")
    cnt = Counter()

    try:
        handle_read_file()
        display_most_frequent()
    except FileNotFoundError:
        print("Wrong File Path Entered!!!")
    except re.error:
        print("Error in Regular expression")
    except:
        print("There is nothing to display")