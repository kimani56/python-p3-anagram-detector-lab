# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        anagrams = []

        for word in words:
            is_anagram  = True
            for c in word:
                if not (c in self.word):
                    is_anagram = False
                    break
                    

            if is_anagram:
                anagrams.append(word)

        return anagrams