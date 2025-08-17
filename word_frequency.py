# importing needed libraries
import matplotlib.pyplot as plt
from collections import Counter
import re
import arabic_reshaper as arre
from bidi.algorithm import get_display
import os
import pandas as pd
from abc import ABC, abstractmethod
from enum import Enum

class RegexPattern(Enum):
    ENGLISH = r"[a-zA-Z]+"
    ARABIC = r"[إةآأ-ي]+"
    NUMBERS = r"[0-9]+"
    ALL = r"[أإةآأ-يa-zA-Z0-9]+"

class HandlingFileData(): 
    file_path = None
    pattern = None   
    pattern_map = {
            1: RegexPattern.ENGLISH.value,
            2: RegexPattern.ARABIC.value,
            3: RegexPattern.NUMBERS.value,
            4: RegexPattern.ALL.value
        }
    def __init__(self,file_path = r"Test cases\6.txt", pattern = RegexPattern.ALL.value):
        self.file_path = file_path
        self.pattern = pattern     
    def getpattern(self):
        if self.pattern == None:
            print("Pattern isn't initalized yet")
            return
        return self.pattern
    def setpattern(self,bow):
        # Make user select type of words want to calculate its frequency
        try:
            self.pattern = self.pattern_map.get(bow, RegexPattern.ALL.value)
            if bow not in self.pattern_map:
                print("Invalid input use all type of words")
        except ValueError:
            print("Invalid input use all type of words")
            self.pattern = RegexPattern.ALL.value
    def getfile_path(self):
        if self.file_path == None:
            print("File Path isn't initalized yet")
            return
        return self.pattern
    def setfile_path(self,value):
        try: 
            if not value.endswith(".txt"):    
                print("File must ends with .txt, Default value used")

            elif os.path.getsize(value) == 0:
                    print("Empty file entered, Default path used")
            else:
                    self.file_path = value    
        except FileNotFoundError:
                print("Wrong File Path Entered!!!")
        except Exception as e:
            print(f"Error raised: {e}, Using Default value")
    def handle_word(self,w):
        """
            based on the words pattern make update as follows:
                * English words --> make it all in lower case
                * Arabic words, Numbers --> Nothing
        """
        if re.match(RegexPattern.ENGLISH.value, w): 
            return w.lower()
        elif any(re.match(p, w) for p in (RegexPattern.ARABIC.value,RegexPattern.NUMBERS.value)):
            return w
    def handle_read_file(self): 
        """
            Reading data from the given file path
            Filter from  some arabic special characters
            Getting words will be used by its pattern
        """             
        try:
            with open(self.file_path,"r",encoding="utf-8") as file:
                for i in file:
                    for l in re.findall(self.pattern,re.sub(r'[\u0640\u064B-\u0652]', '', i)):
                        yield self.handle_word(l)
        except  re.error:
            print("Error in Regular expression")
        except:
            print("A Problem Occured, Please check data entered")
            
class Plotting(ABC):
    x=None
    y=None
    x_label = None
    y_label = None

    @abstractmethod
    def plot(self):
        pass

    @staticmethod
    def prepare_data(i):
        # Taking number of words wants display
        op = input("Enter # words you want to display, Enter to use default number: ")
        n = int(op) if op.isdigit() else 10
  
        if n > i:
            print(f"In this data there are {i} words")

        # Update words to be plot in its right way
        Plotting.x = [get_display(arre.reshape(w)) if re.match(RegexPattern.ARABIC.value, w) else w for w in words_[:n]]
        Plotting.y =  words_counter[:n]
        Plotting.x_label = get_display(arre.reshape("الكلمة")) if handle_data_obj.getpattern() == RegexPattern.ARABIC.value else "Word"  
        Plotting.y_label = get_display(arre.reshape("التكرار")) if handle_data_obj.getpattern() == RegexPattern.ARABIC.value else "Frequency"
     
class TablePlot(Plotting):
    """
        This class extends from Plotting abstract class
        it has variables as follows:
            table_width: the width of the table when displayed
            col_width: the width of each column
            word_col: the word column width
            frequency_col: the frequency column width 
        it display the data as table
    """
    table_width = None
    col_width = None
    word_col = None
    frequency_col = None
    def __init__(self):
        # Displaying data in table in terminal
        self.table_width = len(f"|     {self.x_label}     | {self.y_label} |")
        self.col_width = 18
        self.word_col = self.col_width - len(f" {self.x_label} ")
        self.frequency_col = self.col_width - len(f"{self.y_label}")
     
    def plot(self):
        print(f"{'-'*self.table_width}")   
        # This operation ^ to make the words put in the center of its index 
        print("| {:^{}} | {:^{}} |".format(f"{self.x_label}",self.word_col,f"{self.y_label}",self.frequency_col))
        print(f"{'-'*self.table_width}")
        for i in range(len(self.x)):
            print("| {:<{}} | {:>{}} |".format(self.x[i],self.word_col, self.y[i],self.frequency_col))
            print(f"{'-'*self.table_width}")   

class GrapPlot(Plotting):
    """
        This class extends from Plotting abstract class
        it has variables as follows:
            x_label : represents xlabel to be represented in the plot 
            y_label :  represents ylabel to be represented in the plot
            img_path : represents the graph image path to save the image in 
        it display the data as bar plot
    """
    img_path = "Results/BOW.png"
    def plot(self): 
        try:
            # Ploting data in bar chart
            plt.figure(figsize=(12,6))
            plt.bar(self.x,self.y)
            plt.xlabel(self.x_label)
            plt.ylabel(self.y_label)
            plt.xticks(rotation=90)
            plt.savefig(self.img_path) 
            plt.show()
        except ValueError:
            print("There is nothing to display")
        except:
            print("A Problem Occured, Please check data entered")

if __name__ == '__main__':   
      
    # Make a Folder to save results
    folder_name = "Results"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    handle_data_obj = HandlingFileData()

    # Getting file path from user
    file_path_used = input("Enter File Path: ")
    handle_data_obj.setfile_path(file_path_used)

    # Make user select type of words want to calculate its frequency
    bow = int(input("Select type of words you want to calculate its frequency: \n [1] English words\n [2] Arabic Words\n [3] Numbers\n [4] All\n Selected Choice: "))
    handle_data_obj.setpattern(bow)

    # Apply Word Analyzer
    counter = Counter(handle_data_obj.handle_read_file())  

    items_number = len(counter.items())
    # Getting all data sorted
    words_,words_counter = zip(*counter.most_common(items_number))  
    Plotting.prepare_data(items_number)
    
    graph =  GrapPlot()
    table = TablePlot()
    table.plot()
    graph.plot()
    x1 = "الكلمة" if handle_data_obj.getpattern() == RegexPattern.ARABIC.value else "Word"  
    x2 = "التكرار" if handle_data_obj.getpattern() == RegexPattern.ARABIC.value else "Frequency"
    
    try:        
        # save data (all words with their frequencies) in csv file        
        df = pd.DataFrame({f'{x1}':words_,f'{x2}':words_counter})
        df.to_csv('Results/data.csv',index= False)
    except:
        print("Error in reading data")
