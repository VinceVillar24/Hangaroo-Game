def getAvailableLetters(lettersGuessed):
   
    #Create a variable equal to the list of the English Alphabet 
    Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # A character on the Alphabet will be removed if it is inputted in lettersGuessed
    for char in lettersGuessed:
        Alphabet.remove(char)
    # Returns the refreshed list that the user still haven't guessed
    return ''.join(Alphabet)