# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        # Sort the letters of the word we are checking against
        sorted_word = sorted(self.word)
        
        # List to store anagrams
        anagrams = []
        
        for candidate in possible_anagrams:
            # Check if the sorted version of the candidate matches the sorted_word
            if sorted(candidate) == sorted_word:
                anagrams.append(candidate)
        
        return anagrams
