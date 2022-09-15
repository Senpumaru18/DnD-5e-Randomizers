from string import ascii_lowercase as asc
from string import ascii_uppercase as ASC

alphabet = asc + "!@#$%" + ASC + "^&* "

def CeaserCipher():
    message = str(input("Enter your message: "))
    shift = int(input("Enter the amount to shift: "))
    shifted = alphabet[shift:] + alphabet[:shift]
    coded = ""
    for x in range(len(message)):
        letter = message[x]
        letteridx = alphabet.index(letter)
        newLetter = shifted[letteridx]
        coded += newLetter
    print(coded)



CeaserCipher()
