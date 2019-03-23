"""
Kevin and Stuart want to play the 'The Minion Game'.

**Game Rules**

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

**Scoring**
A player gets +1 point for each occurrence of the substring in the string .

**For Example:**
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

**Sample Input**

    >>> BANANA
    
**Sample Output**

    >>> Stuart 12

"""
import string
vowels = "AEIOU".lower()
stuart_score = 0
kevin_score = 0

def minion_game(string):
    string = string.lower()
    print(string)
    for word_length in range(len(string)):
        list_of_specific_word_length = [string[i:i+1+word_length] for i in range(len(string)) if i+1+word_length <= len(string)]
        for item in list_of_specific_word_length:
            print(item)
        for item_in_each_list in list_of_specific_word_length:
            if item_in_each_list[0] in vowels:
                stuart_score += 1
            else:
                kevin_score += 1
    print("Stuart score = {} and Kevin's Score = {}".format(stuart_score, kevin_score))

def smart_minion_game(string):
    """
    .. note::
        logic behind this method is when you begin from a specific letter, number of word you can create = length of the string  - position of the letter

    :param string: input string
    :return:
    """
    global kevin_score, stuart_score
    string = string.lower()
    for each_position in range(len(string)):
        if string[each_position] in vowels:
            stuart_score += len(string) - each_position
        else:
            kevin_score += len(string) - each_position
    print("Stuart score = {} and Kevin's Score = {}".format(stuart_score, kevin_score))

#smart_minion_game("BANANA")

if __name__ == '__main__':
    s = raw_input()
    minion_game(s)