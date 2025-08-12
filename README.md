# Word Frequency Analyzer

## Option selected:
3 – Word Frequency Analyzer

---

## How to run the code:

1. Open terminal and run:  
   ```bash
   python word_frequency.py
    ```
2. Enter the path to the test case file (if it's in the same folder, you can use a relative path).
3. Enter the number that represents the word type you want to analyze for frequency.
4. After filtering and calculating word frequencies, enter a number `n` to display the top `n` most frequent words with their counts, or press Enter to use the default value.

---

## Languages, Tools & Libraries used:
### Language: 
 - **Python 3.13.5**

### Tools
- **Visual Studio Code (VSCode)**
- **Git** & **GitHub**

### Libraries:

- **matplotlib**: Generates bar charts to visualize word frequency results.
- **collections.Counter**: Efficiently counts occurrences of each word in the text.
- **re (Regular Expressions)**: Extracts words by filtering out punctuation and splitting text.
- **arabic_reshaper**: Reshapes Arabic text for correct display, fixing letter forms.
- **bidi.algorithm.get_display**: Adjusts bidirectional text (e.g.,  Arabic mixed with English) for proper right-to-left display.
- **pandas**: Used for data manipulation and tabular display.
## Extra Features:
- Includes `generate_testcases.py` to create sample test case files.
- Supports Arabic words, handling correct reshaping and display direction.
- Allows user input to specify how many top frequent words to display.
- Provides an option for the user to choose which types of words to include in the analysis:  
  *(e.g., English words only, Arabic words only, numbers only, or mixed)*.

