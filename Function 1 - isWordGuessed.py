"Funtion #1"
def isWordGuessed(secretWord, lettersGuessed):
    for n in secretWord:
        if n not in lettersGuessed:
            return False
    return True
