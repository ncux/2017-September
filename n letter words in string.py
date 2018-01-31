# find the number of n letter words in the input string

def numberofnWords(string):
    wordList = string.split()
    nLetterWords = 0
    for word in wordList:
        if len(word) == 4:
            nLetterWords = nLetterWords + 1
    print(nLetterWords)


numberofnWords("Japan flies 72 people 7000 miles to aid in rescue efforts, not because they're obligated to, but simply because it's the right thing to do. As much as the Mexican people must appreciate the help, I feel like they must appreciate the symbolism behind this gesture far more. In the end we're all human, and we're part of the same community.")
