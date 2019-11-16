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
               
