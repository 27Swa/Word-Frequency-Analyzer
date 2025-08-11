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

3. After filtering and calculating word frequencies, you can enter a number n to display the top n most frequent words with their counts, or press Enter to use the default value.

---

## Languages, Tools & Libraries used:
### Language: 
 - **Python 3.13.5**

### Tools
- **VSCode** 
- **Git & GitHub**

### Libraries:

- **matplotlib**: Used to generate bar charts to visualize the word frequency results.
- **collections.Counter**: Efficiently counts occurrences of each word in the text.
- **re (Regular Expressions)**: For extracting words by filtering out punctuation and splitting text.
- **arabic_reshaper**: Reshapes Arabic text for correct display, fixing letter forms.
- **bidi.algorithm.get_display**: Adjusts bidirectional text (like Arabic mixed with English) for proper right-to-left display.

## Extra Features:
- Created generate_testcases.py to generate sample test case files.
- Supports Arabic words, handling correct reshaping and display direction.
- Allows user input to specify how many top frequent words to display.س