def isWordGuessed(secretWord, lettersGuessed):
# Use "for" statement for the variable  and "secretWord"
    for x in secretWord:
# Use "if" statement & "return" for the conditions
        if x not in lettersGuessed:
            return False
    return True
               
