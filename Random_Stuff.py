from string import ascii_lowercase as asc
from string import ascii_uppercase as ASC

alphabet = asc + '{} !"@#$%*,&.^012345678?9' + ASC      # Cengage 4.1
# alphabet = asc + "{}@ !%#$*&',^.9012345678?" + ASC    # Cengage 4.2

def CeaserCipher(message = str(input("Enter your message: ")),shift = int(input("Enter the amount to shift: "))):
    shifted = alphabet[shift:] + alphabet[:shift]
    coded = ""
    for x in range(len(message)):
        letter = message[x]
        letteridx = alphabet.index(letter)
        newLetter = shifted[letteridx]
        coded += newLetter
    print(coded)
def CeaserDecoder(message = str(input("Enter your message: ")),shift = int(input("Enter the amount to shift: "))):
    shifted = alphabet[shift:] + alphabet[:shift]
    coded = ""
    for x in range(len(message)):
        letter = message[x]
        letteridx = shifted.index(letter)
        newLetter = alphabet[letteridx]
        coded += newLetter
    print(coded)

CeaserCipher()
CeaserDecoder()