#Function 1 
def isWordGuessed(secretWord, lettersGuessed):
# Use "for" statement for the variable  and "secretWord"
    for x in secretWord:
# Use "if" statement & "return" for the conditions
        if x not in lettersGuessed:
            return False
    return True

#Function 2
def getGuessedWord(secretWord, lettersGuessed):
#Set ctr=0
   ctr=0
#Set a variable "x" as blank string
   x = ' '
#Use "for" & "if" statements for the conditions
   for _ in secretWord:
           if(_ in lettersGuessed):              
              ctr+=1
              x = x + _
           else:
              x = x + '_' + ' '
   return x
               
#Function 3
def getAvailableLetters(lettersGuessed):
   
    #Create a variable equal to the list of the English Alphabet 
    Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # A character on the Alphabet will be removed if it is inputted in lettersGuessed
    for char in lettersGuessed:
        Alphabet.remove(char)
    # Returns the refreshed list that the user still haven't guessed
    return ''.join(Alphabet)

#Hangaroo Game 
def hangaroo(secretWord):
#Output Welcoming statement
    print ("__________________________________________________")
    print ("Welcome to Hangaroo!")
    print ("No Kangaroos were harmed in the making of this game")
#Output after inputting a secret word in hangaroo function
    print ("__________________________________________________")
    print ("The word has " + str(len(secretWord)) + " letters.")
    lettersGuessed = ''
#Hangaroo only allows you to have 4 guesses
    guessesRemaining = 4
    mistakesMade = 0
#Use while steatement to loop and proceed 
#Use "getAvailableLetters" function to output remaining unused letters
    while True:
        print ("You have " + str(guessesRemaining) + " guesses left.")
        print ("Available letters: " + getAvailableLetters(lettersGuessed))
        print ("__________________________________________________")
#Input guessing process repeats
        guess = input("Guess a letter: ")
        guess = str(guess)
#Allows user to input capitalized letter
        guess = guess.lower() 
#Use Conditional Statements to process if the guess is correct or wrong 
#Use "getGuessedWord" function to output the progress of the player 
        if guess in secretWord and guess not in lettersGuessed:
#the guess input will be stored on lettersGuessed   
            lettersGuessed += guess        
            print ("Nice Guess!:" + getGuessedWord(secretWord, lettersGuessed))
            print ("__________________________________________________")
        elif guess in lettersGuessed:
            print ("__________________________________________________")
            print ("Letter already guessed: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += guess
            mistakesMade += 1
            print ("Wrong Guess!:" + getGuessedWord(secretWord, lettersGuessed))
            print ("Mistakes Made:" + str(mistakesMade))
            print ("__________________________________________________")
            guessesRemaining -= 1
#Use break and if statement to conclude if the player wins or lose
#Use "isWordGuessed" function to output if the player wins 
        if guessesRemaining <= 0:
            print ("The kangaroo died. The word was " + secretWord + ".")
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print ("Congratulations! You've guessed the word!")
            break